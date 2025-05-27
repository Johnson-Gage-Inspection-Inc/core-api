# app.py
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_smorest import Api
from os import getenv
from routes.pyro_assets import blp as pyro_assets_blp
from routes.whoami import blp as whoami_blp
from routes.work_item_details import blp as main_blp
from werkzeug.middleware.proxy_fix import ProxyFix
import jwt
import requests

load_dotenv()

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app,
    x_for=1,
    x_proto=1,
    x_host=1,
    x_port=1,
    x_prefix=1,
)
CORS(app)
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
api.register_blueprint(pyro_assets_blp)

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

# Guard against missing keys
if "jwks_uri" not in openid_config:
    import logging
    logging.error("Missing 'jwks_uri' in OpenID config: %s", openid_config)
    raise KeyError("'jwks_uri' not found in OpenID configuration.")

jwks_uri = openid_config["jwks_uri"]
issuer = openid_config.get("issuer", "unknown")
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

@app.before_request
def log_client_ip():
    app.logger.debug(f"Incoming request from {request.remote_addr} → {request.method} {request.path}")

@app.route("/", methods=["GET", "OPTIONS"])
def index():
    """Root endpoint to check if the server is running."""
    return ("", 204)


if __name__ == "__main__":
    get_openid_config()
    app.run(debug=True)
