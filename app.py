# app.py
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_smorest import Api
from os import getenv
from routes import (
    asset_service_records,
    clients,
    employees,
    git_ops,
    pyro_assets,
    whoami,
    work_item_details,
)
from werkzeug.middleware.proxy_fix import ProxyFix
import jwt
import logging
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
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["ERROR_404_HELP"] = False
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
  "security": [{"BearerAuth": []}],
  "tags": [
    {
      "name": "Qualer",
      "description": "Simple wrapper endpoints for Qualer API endpoints."
    },
    {
      "name": "Pyro",
      "description": "Data retrieval endpoints for use in the Pyro TUS workbook."
    },
    {
      "name": "System",
      "description": "Administrative and system management endpoints for operational tasks such as git operations, deployment management, and system monitoring."
    }
  ]
}

api = Api(app)

# Register all your blueprints with this, not `app`
api.register_blueprint(asset_service_records.blp)
api.register_blueprint(clients.blp)
api.register_blueprint(employees.blp)
api.register_blueprint(git_ops.blp)
api.register_blueprint(pyro_assets.blp)
api.register_blueprint(whoami.blp)
api.register_blueprint(work_item_details.blp)

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
    logging.error("Missing 'jwks_uri' in OpenID config: %s", openid_config)
    raise KeyError("'jwks_uri' not found in OpenID configuration.")

jwks_uri = openid_config["jwks_uri"]
if "issuer" not in openid_config:
    logging.error("Missing 'issuer' in OpenID config: %s", openid_config)
    raise KeyError("'issuer' not found in OpenID configuration.")
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

@app.before_request
def log_client_ip():
    app.logger.debug(f"Incoming request from {request.remote_addr} → {request.method} {request.path}")

@app.route("/", methods=["GET", "OPTIONS"])
def index():
    """Root endpoint to check if the server is running."""
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)
