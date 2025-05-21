# app.py
from flask import Flask, request, jsonify
import jwt
import requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()

app = Flask(__name__)

TENANT_ID = getenv("AZURE_TENANT_ID")
AUDIENCE = getenv("AZURE_CLIENT_ID")
REQUIRED_SCOPE = "access_as_user"

# OpenID discovery to get signing keys
def get_openid_config():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0/.well-known/openid-configuration"
    return requests.get(url).json()

openid_config = get_openid_config()
jwks_uri = openid_config["jwks_uri"]
issuer = openid_config["issuer"]
jwks = requests.get(jwks_uri).json()

# Token validator
def validate_token(token):
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header["kid"]
    key = next(k for k in jwks["keys"] if k["kid"] == kid)

    public_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)

    payload = jwt.decode(
        token,
        key=public_key,
        algorithms=["RS256"],
        audience=AUDIENCE,
        issuer=issuer
    )

    scopes = payload.get("scp", "").split()
    if REQUIRED_SCOPE not in scopes:
        raise jwt.InvalidTokenError("Required scope missing")

    return payload

# Auth decorator
from functools import wraps

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid Authorization header"}), 401
        token = auth_header[len("Bearer "):]

        try:
            claims = validate_token(token)
            request.claims = claims  # optionally store for use in route
        except Exception as e:
            return jsonify({"error": str(e)}), 401

        return f(*args, **kwargs)
    return wrapper

def get_openid_config():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/v2.0/.well-known/openid-configuration"
    print(f"Fetching OpenID config from: {url}")
    response = requests.get(url)
    print("Response JSON:", response.json())
    return response.json()


# Example protected route
@app.route("/whoami")
@require_auth
def whoami():
    return jsonify({"user": request.claims["preferred_username"]})

if __name__ == "__main__":
    get_openid_config()
    app.run(debug=True)
