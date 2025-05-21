import jwt
import requests
from flask import request, jsonify
from functools import wraps
from jwt.algorithms import RSAAlgorithm
from os import getenv

TENANT_ID = getenv("AZURE_TENANT_ID")
AUDIENCE = getenv("AZURE_API_AUDIENCE", "api://jgiquality.com/core-api")
REQUIRED_SCOPE = getenv("AZURE_REQUIRED_SCOPE", "access_as_user")

_openid_config = None
_jwks = None

def load_openid_config():
    global _openid_config, _jwks
    if _openid_config is None:
        url = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0/.well-known/openid-configuration"
        _openid_config = requests.get(url).json()
        _jwks = requests.get(_openid_config["jwks_uri"]).json()
    return _openid_config, _jwks

def validate_token(token):
    config, jwks = load_openid_config()
    unverified_header = jwt.get_unverified_header(token)
    key = next(k for k in jwks["keys"] if k["kid"] == unverified_header["kid"])
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
