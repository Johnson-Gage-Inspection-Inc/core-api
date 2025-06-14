# app.py
import os

from flask import Flask, request
from flask_cors import CORS
from flask_smorest import Api
from werkzeug.middleware.proxy_fix import ProxyFix

# Import config to load environment variables BEFORE importing routes
import config  # noqa: F401
from routes import (
    asset_service_records,
    clients,
    daqbook_offsets,
    employees,
    git_ops,
    pyro_assets,
    refresh_excel_data,
    whoami,
    wire_offsets,
    work_item_details,
)

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
app.config["OPENAPI_URL_PREFIX"] = ""
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_URL"] = (
    "https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.11.0/"
)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["ERROR_404_HELP"] = False
app.config["API_SPEC_OPTIONS"] = {
    "components": {
        "securitySchemes": {
            "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
        }
    },
    "security": [{"BearerAuth": []}],
    "tags": [
        {
            "name": "Qualer",
            "description": "Simple wrapper endpoints for Qualer API endpoints.",
        },
        {
            "name": "Pyro",
            "description": "Data retrieval endpoints for use in the Pyro TUS workbook.",
        },
        {
            "name": "System",
            "description": "Administrative and system management endpoints for operational tasks such as git operations, deployment management, and system monitoring.",
        },
    ],
}

api = Api(app)

# Register all your blueprints with this, not `app`
api.register_blueprint(asset_service_records.blp)
api.register_blueprint(clients.blp)
api.register_blueprint(daqbook_offsets.blp)
api.register_blueprint(employees.blp)
api.register_blueprint(git_ops.blp)
api.register_blueprint(pyro_assets.blp)
api.register_blueprint(refresh_excel_data.blp)
api.register_blueprint(whoami.blp)
api.register_blueprint(wire_offsets.blp)
api.register_blueprint(work_item_details.blp)


@app.before_request
def log_client_ip():
    app.logger.debug(
        f"Incoming request from {request.remote_addr} → {request.method} {request.path}"
    )


@app.route("/", methods=["GET", "OPTIONS"])
def index():
    """Root endpoint to check if the server is running."""
    return ("", 204)


if __name__ == "__main__":
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode)
