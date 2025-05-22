# app.py
from flask import Flask, request, jsonify
import jwt
import requests
from dotenv import load_dotenv
from os import getenv
from routes.work_item_details import bp as main_bp
from utils.auth import require_auth
from flask import Flask

load_dotenv()

app = Flask(__name__)

TENANT_ID = getenv("AZURE_TENANT_ID")
AUDIENCE = getenv("AZURE_CLIENT_ID")
REQUIRED_SCOPE = "access_as_user"


def get_openid_config():
    """Fetch OpenID configuration from Azure AD."""
    url = (
        f"https://login.microsoftonline.com/"
        f"{TENANT_ID}/v2.0/.well-known/openid-configuration"
    )
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


# Example protected route
@app.route("/whoami")
@require_auth
def whoami():
    return jsonify({"user": request.claims["preferred_username"]})

if __name__ == "__main__":
    get_openid_config()
    app.run(debug=True)
