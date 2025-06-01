import os
import subprocess

from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import Blueprint, abort


def is_authorized():
    expected = os.getenv("DEPLOY_TOKEN")
    auth_header = request.headers.get("Authorization", "")
    return auth_header == f"Bearer {expected}"


blp = Blueprint("git-ops", __name__, url_prefix="/")


@blp.route("/git-pull")
class GitPull(MethodView):
    @blp.doc(tags=["System"])
    def post(self):
        """
        Update the server by pulling the latest changes from the main branch.

        This endpoint performs a git pull operation to update the server with the
        latest code changes from the main branch. It requires a special deployment
        token for authorization rather than the standard JWT authentication.

        ### Authentication:
          - Requires a deployment token passed as Bearer token in Authorization header. This token should match the DEPLOY_TOKEN environment variable.

        ### Returns:
        - **dict**: Success response with git pull output, or error details
          - status: "success" if git pull succeeded, error message if failed
          - output: Git command output (on success)
          - error: Error message from git command (on failure)

        ###  Raises:
        - **401**: If deployment token is invalid or missing
        - **500**: If git pull command fails or times out

        **Example**: POST /git-pull with Authorization: Bearer <deploy-token>

        ### Success Response:
        ```
        {
            "status": "success",
            "output": "Already up to date."
        }
        ```

        ### Error Response:
        ```
        {
            "status": "git pull failed",
            "error": "fatal: not a git repository"
        }
        ```
        """
        if not is_authorized():
            abort(401, message="Unauthorized")

        try:
            result = subprocess.run(
                ["git", "pull", "origin", "main"],
                cwd=os.getcwd(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:

                return (
                    jsonify({"error": result.stderr, "status": "git pull failed"}),
                    500,
                )

            return {"status": "success", "output": result.stdout}

        except Exception as e:
            abort(500, message=str(e))
