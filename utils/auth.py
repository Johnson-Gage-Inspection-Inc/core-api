import logging
from functools import wraps
from os import getenv

import jwt
import requests
from flask import Response, g, jsonify, request

_openid_config = None
_jwks = None


def get_azure_config():
    """Get Azure configuration from environment variables."""
    return {
        "tenant_id": getenv("AZURE_TENANT_ID"),
        "audience": getenv(
            "AZURE_CLIENT_ID"
        ),  # Use client ID as audience for Azure AD tokens
        "required_scope": getenv("AZURE_REQUIRED_SCOPE", "access_as_user"),
    }


def require_auth(f):
    """Decorator to require authentication for a route."""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # Skip authentication if SKIP_AUTH is true
        if getenv("SKIP_AUTH", "false").lower() == "true":
            # Set fake claims for consistency with authenticated flow
            g.claims = {
                "preferred_username": "testuser@example.com",
                "sub": "fake-subject",
            }
            return f(*args, **kwargs)

        config = get_azure_config()
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return Response(
                "Unauthorized",
                401,
                {
                    "WWW-Authenticate": (
                        f'Bearer authorization_uri="https://login.microsoftonline.com/{config["tenant_id"]}"'
                    )
                },
            )

        token = auth_header[len("Bearer ") :]

        try:
            g.claims = validate_token(token)
        except Exception as e:
            logging.error(f"Token validation failed: {e}")
            logging.debug(f"Exception type: {type(e)}")
            logging.debug(f"Token length: {len(token)}")
            logging.debug(f"DEBUG: Token starts with: {token[:10]}...")
            return jsonify({"error": str(e)}), 401

        return f(*args, **kwargs)

    return wrapper


def load_openid_config():
    global _openid_config, _jwks
    if _openid_config is None:
        config = get_azure_config()
        url = (
            f"https://login.microsoftonline.com/"
            f"{config['tenant_id']}/v2.0/.well-known/openid-configuration"
        )
        try:
            _openid_config = requests.get(url).json()
            _jwks = requests.get(_openid_config["jwks_uri"]).json()
        except (requests.RequestException, KeyError, ValueError) as e:
            logging.error(f"Failed to load OpenID config: {e}")
            raise
    return _openid_config, _jwks


def validate_token(token):
    config, jwks = load_openid_config()
    azure_config = get_azure_config()
    unverified_header = jwt.get_unverified_header(token)
    key = next((k for k in jwks["keys"] if k["kid"] == unverified_header["kid"]), None)

    if key is None:
        raise jwt.InvalidTokenError(
            f"Key ID {unverified_header['kid']} not found in JWKS"
        )

    # Use PyJWT's built-in JWK handling
    public_key = jwt.PyJWK(key).key

    payload = jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        audience=azure_config["audience"],
        issuer=config["issuer"],
    )

    scopes = payload.get("scp", "").split()
    if azure_config["required_scope"] not in scopes:
        raise jwt.InvalidTokenError("Missing required scope")
    return payload
