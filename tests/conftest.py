import tests.mock_view_bindings
from app import app as flask_app
import pytest
from utils.get_token import get_access_token
import utils.auth


@pytest.fixture(autouse=True)
def reset_auth_cache():
    """Reset auth cache before each test to prevent test interference."""
    utils.auth._openid_config = None
    utils.auth._jwks = None
    yield
    # Clean up after test
    utils.auth._openid_config = None
    utils.auth._jwks = None


@pytest.fixture(scope="session")
def auth_token():
    return get_access_token()


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
