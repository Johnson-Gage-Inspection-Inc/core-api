from flask_smorest import Blueprint
from flask.views import MethodView
from utils.auth import require_auth
from flask import request
from schemas import WhoamiResponse

blp = Blueprint("whoami", __name__, url_prefix="/")


@blp.route("/whoami")
class Whoami(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, WhoamiResponse)
    def get(self):
        return {
            "user": request.claims.get("preferred_username"),
            "sub": request.claims.get("sub")
        }
