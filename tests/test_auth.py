import pytest
from unittest.mock import patch, MagicMock
from flask import Flask, g, jsonify
import jwt

import utils.auth as auth

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route("/protected")
    @auth.require_auth
    def protected():
        return jsonify({"claims": g.claims})

    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_require_auth_no_auth_header(client):
    resp = client.get("/protected")
    assert resp.status_code == 401
    assert "WWW-Authenticate" in resp.headers

def test_require_auth_invalid_auth_header(client):
    resp = client.get("/protected", headers={"Authorization": "InvalidToken"})
    assert resp.status_code == 401
    assert "WWW-Authenticate" in resp.headers

@patch("utils.auth.validate_token")
def test_require_auth_valid_token(mock_validate_token, client):
    mock_validate_token.return_value = {"sub": "user1", "scp": "access_as_user"}
    resp = client.get("/protected", headers={"Authorization": "Bearer validtoken"})
    assert resp.status_code == 200
    assert resp.json["claims"]["sub"] == "user1"

@patch("utils.auth.validate_token")
def test_require_auth_invalid_token(mock_validate_token, client):
    mock_validate_token.side_effect = Exception("Invalid token")
    resp = client.get("/protected", headers={"Authorization": "Bearer badtoken"})
    assert resp.status_code == 401
    assert resp.json["error"] == "Invalid token"

@patch("utils.auth.requests.get")
def test_load_openid_config_caches(mock_get, monkeypatch):
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    mock_openid = {"jwks_uri": "https://example.com/jwks", "issuer": "issuer"}
    mock_jwks = {"keys": [{"kid": "abc"}]}
    mock_get.side_effect = [
        MagicMock(json=lambda: mock_openid),
        MagicMock(json=lambda: mock_jwks)
    ]
    config, jwks = auth.load_openid_config()
    assert config == mock_openid
    assert jwks == mock_jwks

    # Should not call requests.get again
    mock_get.reset_mock()
    config2, jwks2 = auth.load_openid_config()
    assert config2 == mock_openid
    assert jwks2 == mock_jwks
    mock_get.assert_not_called()

@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.RSAAlgorithm.from_jwk")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_success(mock_load_config, mock_decode, mock_from_jwk, mock_get_header):
    mock_load_config.return_value = (
        {"issuer": "issuer"},
        {"keys": [{"kid": "abc"}]}
    )
    mock_get_header.return_value = {"kid": "abc"}
    mock_from_jwk.return_value = "publickey"
    mock_decode.return_value = {"scp": "access_as_user", "sub": "user1"}

    token = "sometoken"
    result = auth.validate_token(token)
    assert result["sub"] == "user1"
    mock_decode.assert_called_once()

@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.load_openid_config")
def test_validate_token_missing_kid(mock_load_config, mock_get_header):
    mock_load_config.return_value = (
        {"issuer": "issuer"},
        {"keys": [{"kid": "other"}]}
    )
    mock_get_header.return_value = {"kid": "abc"}
    with pytest.raises(StopIteration):
        auth.validate_token("token")

@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.RSAAlgorithm.from_jwk")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_missing_scope(mock_load_config, mock_decode, mock_from_jwk, mock_get_header):
    mock_load_config.return_value = (
        {"issuer": "issuer"},
        {"keys": [{"kid": "abc"}]}
    )
    mock_get_header.return_value = {"kid": "abc"}
    mock_from_jwk.return_value = "publickey"
    mock_decode.return_value = {"scp": "other_scope"}

    with pytest.raises(jwt.InvalidTokenError):
        auth.validate_token("token")