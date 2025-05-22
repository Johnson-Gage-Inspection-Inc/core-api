# app.py
from dotenv import load_dotenv
from flask import Flask
from flask import Flask, request, jsonify
from flask_smorest import Api
from os import getenv
from routes.work_item_details import blp as main_blp
from routes.whoami import blp as whoami_blp
from utils.auth import require_auth
import jwt
import requests

load_dotenv()

app = Flask(__name__)
app.config["API_TITLE"] = "JGI Quality API"
app.config["API_VERSION"] = "1.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.11.0/"
app.config["API_SPEC_OPTIONS"] = {
  "components": {
    "securitySchemes": {
      "BearerAuth": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT"
      }
    }
  },
  "security": [{"BearerAuth": []}]
}

api = Api(app)

# Register all your blueprints with this, not `app`
api.register_blueprint(main_blp)
api.register_blueprint(whoami_blp)

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


if __name__ == "__main__":
    get_openid_config()
    app.run(host="0.0.0.0",
            port=8080,
            debug=False)
