import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import utils.auth
from app import app as flask_app
from db.models import Base
from utils.get_token import get_access_token


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

    # Apply mock view bindings if SKIP_AUTH is true
    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        # Import and apply mock bindings after app is fully initialized
        # (This will apply the mocks)
        import tests.mock_view_bindings  # noqa: F401

    with flask_app.test_client() as client:
        yield client


@pytest.fixture
def db_session():
    """Create a test database session."""
    # Use in-memory SQLite for testing
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session

    session.close()
