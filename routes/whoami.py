from flask_smorest import Blueprint
from flask.views import MethodView
from utils.auth import require_auth
from flask import g
from schemas import WhoamiResponse

blp = Blueprint("whoami", __name__, url_prefix="/")


@blp.route("/whoami")
class Whoami(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, WhoamiResponse)
    def get(self):
        return {
            "user": g.claims.get("preferred_username"),
            "sub": g.claims.get("sub")
        }
