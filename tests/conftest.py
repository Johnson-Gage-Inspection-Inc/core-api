from app import app as flask_app
from flask import Flask
from routes.main import bp as main_bp
import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client