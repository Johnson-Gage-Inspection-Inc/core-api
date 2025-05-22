from flask import Flask
from routes.work_item_details import blp as work_item_details_blp
from routes.whoami import blp as whoami_blp
import pytest
from get_token import get_access_token


@pytest.fixture(scope="session")
def auth_token():
    return get_access_token()


@pytest.fixture
def client():
    app = Flask(__name__)
    app.config["TESTING"] = True

    app.register_blueprint(work_item_details_blp)
    app.register_blueprint(whoami_blp)

    with app.test_client() as client:
        yield client
