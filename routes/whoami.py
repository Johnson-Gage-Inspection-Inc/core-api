from flask import g
from flask.views import MethodView
from flask_smorest import Blueprint

from utils.auth import require_auth
from utils.schemas import WhoamiResponse

blp = Blueprint("whoami", __name__, url_prefix="/")


@blp.route("/whoami")
class Whoami(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, WhoamiResponse)
    def get(self):
        """
        Get the current authenticated user's information.

        This endpoint returns information about the currently authenticated user
        based on the JWT token provided. It extracts user details from the
        token claims and returns them in a structured format.

        **Returns**:
        - **dict**: User information containing:
          - user: The user's preferred username from the JWT token
          - sub: The subject identifier (user ID) from the JWT token

        **Raises**:
        - **401**: If authentication token is invalid or missing

        **Example**: GET /whoami with Authorization: Bearer <token>

        **Response**: {"user": "john.doe@company.com", "sub": "12345678-1234-1234-1234-123456789012"}
        """
        return {"user": g.claims.get("preferred_username"), "sub": g.claims.get("sub")}
