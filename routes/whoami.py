# routes/whoami.py
from flask import Blueprint, jsonify, request
from utils.auth import require_auth

bp = Blueprint("whoami", __name__)

@bp.route("/whoami", methods=["GET"])
@require_auth
def whoami():
    return jsonify({
        "user": request.claims.get("preferred_username"),
        "sub": request.claims.get("sub")
    })
