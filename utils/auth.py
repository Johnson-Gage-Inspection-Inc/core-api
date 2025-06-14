import logging
import os

# ----------------------------
# Dataclass for Azure settings
# ----------------------------
from dataclasses import dataclass
from functools import lru_cache, wraps
from typing import Any, Callable, Dict, Tuple

import jwt
import requests
from flask import Response, g, jsonify, request
from jwt import InvalidTokenError


@dataclass(frozen=True)
class AzureConfig:
    tenant_id: str
    audience: str
    required_scope: str

    @classmethod
    def from_env(cls) -> "AzureConfig":
        tenant_id = os.getenv("AZURE_TENANT_ID", "9def3ae4-854a-4465-952c-5693835965d9")
        audience = os.getenv("AZURE_CLIENT_ID", "43a01068-983b-41b9-bb61-7ed191bd0e29")
        required_scope = os.getenv("AZURE_REQUIRED_SCOPE", "access_as_user")
        return cls(
            tenant_id=tenant_id, audience=audience, required_scope=required_scope
        )


# ----------------------------
# OpenID / JWKS caching
# ----------------------------
# We cache the OpenID configuration and JWKS in-memory. In production, keys rotate infrequently,
# but you may want a TTL-based refresh. Here we simply cache once per process lifetime.


@lru_cache(maxsize=1)
def load_openid_config_and_jwks() -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Load the OpenID Connect configuration and JWKS for Azure AD.
    Cached for process lifetime. Raises on errors.
    """
    cfg = AzureConfig.from_env()
    well_known = f"https://login.microsoftonline.com/{cfg.tenant_id}/v2.0/.well-known/openid-configuration"
    try:
        resp = requests.get(well_known, timeout=5)
        resp.raise_for_status()
        openid_cfg = resp.json()
    except Exception as e:
        logging.error(f"Failed to fetch OpenID configuration from {well_known}: {e}")
        raise RuntimeError(f"Failed to load OpenID configuration: {e}")

    jwks_uri = openid_cfg.get("jwks_uri")
    if not jwks_uri:
        logging.error("openid-configuration did not include 'jwks_uri'")
        raise RuntimeError("Invalid OpenID configuration: missing jwks_uri")

    try:
        resp2 = requests.get(jwks_uri, timeout=5)
        resp2.raise_for_status()
        jwks = resp2.json()
    except Exception as e:
        logging.error(f"Failed to fetch JWKS from {jwks_uri}: {e}")
        raise RuntimeError(f"Failed to load JWKS: {e}")

    return openid_cfg, jwks


# ----------------------------
# Token validation
# ----------------------------
def validate_token(token: str) -> Dict[str, Any]:
    """
    Validate the JWT access token using Azure AD JWKS.
    Returns the decoded payload (claims) if valid.
    Raises an exception (InvalidTokenError or RuntimeError) on failure.
    """
    openid_cfg, jwks = load_openid_config_and_jwks()
    cfg = AzureConfig.from_env()

    # Get unverified header to find the 'kid'
    try:
        unverified_header = jwt.get_unverified_header(token)
    except jwt.PyJWTError as e:
        raise InvalidTokenError(f"Failed to parse JWT header: {e}")

    kid = unverified_header.get("kid")
    if not kid:
        raise InvalidTokenError("JWT header missing 'kid'")

    # Find matching key in JWKS
    jwk_key = next((k for k in jwks.get("keys", []) if k.get("kid") == kid), None)
    if jwk_key is None:
        raise InvalidTokenError(f"Key ID {kid} not found in JWKS")

    # PyJWT's PyJWK can convert JWK dict to a key object
    try:
        public_key = jwt.PyJWK(jwk_key).key
    except Exception as e:
        raise InvalidTokenError(f"Failed to construct public key from JWK: {e}")

    # Decode & verify signature and standard claims
    issuer = openid_cfg.get("issuer")
    if not issuer:
        raise RuntimeError("OpenID configuration missing 'issuer'")

    try:
        # audience is typically the client ID (or App ID URI).
        # This checks signature, expiration, issuer, audience.
        payload = jwt.decode(
            token,
            public_key,
            algorithms=["RS256"],
            audience=cfg.audience,
            issuer=issuer,
        )
    except InvalidTokenError as e:
        raise InvalidTokenError(f"JWT validation error: {e}")

    # Scope (scp) check
    scp = payload.get("scp", "")
    scopes = scp.split() if isinstance(scp, str) else []
    if cfg.required_scope not in scopes:
        raise InvalidTokenError(f"Missing required scope: {cfg.required_scope}")

    return payload


# ----------------------------
# Decorator
# ----------------------------
def require_auth(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to require Azure AD JWT authentication for a Flask route.
    If SKIP_AUTH=true in env, sets fake claims.
    On failure, returns 401 JSON error.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        # Skip authentication (for local/dev/testing)
        if os.getenv("SKIP_AUTH", "false").lower() == "true":
            # Fake claims for consistency
            g.claims = {
                "preferred_username": "testuser@example.com",
                "sub": "fake-subject",
            }
            return f(*args, **kwargs)

        # Retrieve and check Authorization header
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            # Challenge header to prompt clients
            cfg = AzureConfig.from_env()
            auth_uri = f"https://login.microsoftonline.com/{cfg.tenant_id}"
            return Response(
                "Unauthorized",
                401,
                {"WWW-Authenticate": f'Bearer authorization_uri="{auth_uri}"'},
            )

        token = auth_header[len("Bearer ") :].strip()
        if not token:
            return jsonify({"error": "Empty Bearer token"}), 401

        # Validate token
        try:
            claims = validate_token(token)
            # Attach to Flask global context
            g.claims = claims
        except Exception as e:
            # Log error details at debug level
            logging.error(f"Token validation failed: {e}")
            logging.debug(f"Exception type: {type(e)}")
            # Do not leak sensitive info in production; here return generic message
            return jsonify({"error": "Invalid or expired token"}), 401

        # Proceed to the actual route
        return f(*args, **kwargs)

    return wrapper


# ----------------------------
# Example usage in Flask routes
# ----------------------------
# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/my-protected-endpoint")
# @require_auth
# def protected():
#     claims = g.claims  # type: Dict[str, Any]
#     user = claims.get("preferred_username", "<unknown>")
#     return jsonify({"message": f"Hello, {user}!"})
