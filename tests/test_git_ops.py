from unittest.mock import MagicMock, patch

import pytest
from flask import Flask
from flask_smorest import Api

from routes.git_ops import blp

# Import the Blueprint from the code to test


@pytest.fixture(autouse=True)
def set_deploy_token(monkeypatch):
    monkeypatch.setenv("DEPLOY_TOKEN", "testtoken")


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.config["API_TITLE"] = "Test"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["ERROR_404_HELP"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    api = Api(app)
    api.register_blueprint(blp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_git_pull_unauthorized(client):
    response = client.post("/git-pull")
    assert response.status_code == 401
    assert b"Unauthorized" in response.data


@patch("routes.git_ops.subprocess.run")
def test_git_pull_success(mock_run, client):
    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = "Already up to date."
    mock_run.return_value = mock_result

    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/git-pull", headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "Already up to date." in data["output"]


@patch("routes.git_ops.subprocess.run")
def test_git_pull_git_error(mock_run, client):
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stderr = "Some git error"
    mock_run.return_value = mock_result

    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/git-pull", headers=headers)

    assert response.status_code == 500
    data = response.get_json()
    assert "Some git error" in data["error"]
    assert data["status"] == "git pull failed"


@patch("routes.git_ops.subprocess.run", side_effect=Exception("Unexpected error"))
def test_git_pull_exception(mock_run, client):
    headers = {"Authorization": "Bearer testtoken"}
    response = client.post("/git-pull", headers=headers)
    assert response.status_code == 500
    assert b"Unexpected error" in response.data
