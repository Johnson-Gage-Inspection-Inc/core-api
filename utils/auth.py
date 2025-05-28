from flask import request, jsonify, g, Response
from functools import wraps
from jwt.algorithms import RSAAlgorithm
from os import getenv
import jwt
import requests
import logging

TENANT_ID = getenv("AZURE_TENANT_ID")
AUDIENCE = getenv("AZURE_CLIENT_ID")  # Use client ID as audience for Azure AD tokens
REQUIRED_SCOPE = getenv("AZURE_REQUIRED_SCOPE", "access_as_user")

_openid_config = None
_jwks = None


def require_auth(f):
    """Decorator to require authentication for a route."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Skip authentication if SKIP_AUTH is true
        if getenv("SKIP_AUTH", "false").lower() == "true":
            # Set fake claims for consistency with authenticated flow
            g.claims = {
                "preferred_username": "testuser@example.com",
                "sub": "fake-subject"
            }
            return f(*args, **kwargs)
        
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return Response(
                "Unauthorized",
                401,
                {
                    "WWW-Authenticate": (
                        f'Bearer authorization_uri="https://login.microsoftonline.com/{TENANT_ID}"'
                    )
                }
            )
        
        token = auth_header[len("Bearer "):]
        
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
        url = (
            f"https://login.microsoftonline.com/"
            f"{TENANT_ID}/v2.0/.well-known/openid-configuration"
        )
        try:
            _openid_config = requests.get(url).json()
            _jwks = requests.get(_openid_config["jwks_uri"]).json()
        except Exception as e:
            print(f"DEBUG: Failed to load OpenID config: {e}")
            raise
    return _openid_config, _jwks


def validate_token(token):
    config, jwks = load_openid_config()
    unverified_header = jwt.get_unverified_header(token)
    key = next((k for k in jwks["keys"] if k["kid"] == unverified_header["kid"]), None)
    
    if key is None:
        raise jwt.InvalidTokenError(f"Key ID {unverified_header['kid']} not found in JWKS")
    
    public_key = RSAAlgorithm.from_jwk(key)

    payload = jwt.decode(
        token,
        public_key,
        algorithms=["RS256"],
        audience=AUDIENCE,
        issuer=config["issuer"]
    )

    scopes = payload.get("scp", "").split()
    if REQUIRED_SCOPE not in scopes:
        raise jwt.InvalidTokenError("Missing required scope")
    return payload
