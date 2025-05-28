from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
import os
import subprocess

def is_authorized():
    expected = os.getenv("DEPLOY_TOKEN")
    auth_header = request.headers.get("Authorization", "")
    return auth_header == f"Bearer {expected}"

blp = Blueprint("git-ops", __name__, url_prefix="/")

@blp.route("/git-pull")
class GitPull(MethodView):
    def post(self):
        if not is_authorized():
            abort(401, message="Unauthorized")

        try:
            result = subprocess.run(
                ["git", "pull", "origin", "main"],
                cwd=os.getcwd(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10
            )

            if result.returncode != 0:

                return jsonify({
                    "error": result.stderr,
                    "status": "git pull failed"
                }), 500


            return {"status": "success", "output": result.stdout}

        except Exception as e:
            abort(500, message=str(e))
