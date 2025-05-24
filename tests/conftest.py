from app import app as flask_app
import pytest
from get_token import get_access_token


@pytest.fixture(scope="session")
def auth_token():
    return get_access_token()


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
