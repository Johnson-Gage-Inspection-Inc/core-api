from app import app as flask_app
from flask import Flask
from routes.work_item_details import bp as work_item_details_bp
from routes.whoami import bp as whoami_bp
import pytest
from get_token import get_access_token


@pytest.fixture(scope="session")
def auth_token():
    return get_access_token()


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True

    app.register_blueprint(work_item_details_bp)
    app.register_blueprint(whoami_bp)

    with app.test_client() as client:
        yield client
