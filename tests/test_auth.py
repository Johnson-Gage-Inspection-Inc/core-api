import os
from os import getenv
from unittest.mock import MagicMock, patch

import jwt
import pytest
import requests
from flask import Flask, g, jsonify

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


def test_AzureConfig_from_env():
    """Test that AzureConfig.from_env() returns expected structure"""
    config = auth.AzureConfig.from_env()
    assert config.tenant_id is not None
    assert config.audience is not None
    assert config.required_scope is not None


def test_require_auth_no_auth_header(client):
    resp = client.get("/protected")
    if getenv("SKIP_AUTH", "false").lower() == "true":
        # When auth is skipped, no auth header should still work
        assert resp.status_code == 200
        assert resp.json["claims"]["sub"] == "fake-subject"
    else:
        assert resp.status_code == 401
        assert "WWW-Authenticate" in resp.headers


def test_require_auth_invalid_auth_header(client):
    resp = client.get("/protected", headers={"Authorization": "InvalidToken"})
    if getenv("SKIP_AUTH", "false").lower() == "true":
        # When auth is skipped, invalid auth header should still work
        assert resp.status_code == 200
        assert resp.json["claims"]["sub"] == "fake-subject"
    else:
        assert resp.status_code == 401
        assert "WWW-Authenticate" in resp.headers


@patch("utils.auth.validate_token")
def test_require_auth_valid_token(mock_validate_token, client):
    mock_validate_token.return_value = {"sub": "user1", "scp": "access_as_user"}
    resp = client.get("/protected", headers={"Authorization": "Bearer validtoken"})
    assert resp.status_code == 200
    if getenv("SKIP_AUTH", "false").lower() == "true":
        # When auth is skipped, fake claims are used regardless of token
        assert resp.json["claims"]["sub"] == "fake-subject"
    else:
        # When auth is enabled, mocked validate_token should be called
        assert resp.json["claims"]["sub"] == "user1"


@patch("utils.auth.validate_token")
def test_require_auth_invalid_token(mock_validate_token, client):
    mock_validate_token.side_effect = Exception("Invalid token")
    resp = client.get("/protected", headers={"Authorization": "Bearer badtoken"})
    if getenv("SKIP_AUTH", "false").lower() == "true":
        # When auth is skipped, even invalid tokens work
        assert resp.status_code == 200
        assert resp.json["claims"]["sub"] == "fake-subject"
    else:
        assert resp.status_code == 401
        assert resp.json["error"] == "Invalid token"


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="OpenID config not used when SKIP_AUTH=true",
)
@patch("utils.auth.requests.get")
def test_load_openid_config_caches(mock_get, monkeypatch):
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    mock_openid = {"jwks_uri": "https://example.com/jwks", "issuer": "issuer"}
    mock_jwks = {"keys": [{"kid": "abc"}]}
    mock_get.side_effect = [
        MagicMock(json=lambda: mock_openid),
        MagicMock(json=lambda: mock_jwks),
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


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.jwt.PyJWK")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_success(
    mock_load_config, mock_decode, mock_pyjwk, mock_get_header
):
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}
    mock_pyjwk_instance = MagicMock()
    mock_pyjwk_instance.key = "publickey"
    mock_pyjwk.return_value = mock_pyjwk_instance
    mock_decode.return_value = {"scp": "access_as_user", "sub": "user1"}

    token = "sometoken"
    result = auth.validate_token(token)
    assert result["sub"] == "user1"
    mock_decode.assert_called_once()


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.load_openid_config")
def test_validate_token_missing_kid(mock_load_config, mock_get_header):
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "other"}]})
    mock_get_header.return_value = {"kid": "abc"}
    with pytest.raises(jwt.InvalidTokenError):
        auth.validate_token("token")


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.jwt.PyJWK")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_missing_scope(
    mock_load_config, mock_decode, mock_pyjwk, mock_get_header
):
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}
    mock_pyjwk_instance = MagicMock()
    mock_pyjwk_instance.key = "publickey"
    mock_pyjwk.return_value = mock_pyjwk_instance
    mock_decode.return_value = {"scp": "other_scope"}

    with pytest.raises(jwt.InvalidTokenError):
        auth.validate_token("token")


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Auth error handling not tested when SKIP_AUTH=true",
)
def test_load_openid_config_request_error(monkeypatch):
    """Test error handling when requests fail in load_openid_config"""
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    def mock_requests_get_error(url):
        raise Exception("Network error")

    monkeypatch.setattr("utils.auth.requests.get", mock_requests_get_error)

    with pytest.raises(Exception, match="Network error"):
        auth.load_openid_config()


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Auth error handling not tested when SKIP_AUTH=true",
)
@patch("utils.auth.validate_token")
def test_require_auth_exception_handling(mock_validate_token, client):
    """Test that exceptions in validate_token are properly handled"""
    mock_validate_token.side_effect = jwt.DecodeError("Token decode failed")

    resp = client.get("/protected", headers={"Authorization": "Bearer invalidtoken"})
    assert resp.status_code == 401
    assert "Token decode failed" in resp.get_data(as_text=True)


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Auth error handling not tested when SKIP_AUTH=true",
)
@patch("utils.auth.requests.get")
def test_load_openid_config_network_error(mock_get):
    """Test error handling when network request fails"""
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    mock_get.side_effect = requests.RequestException("Network error")

    with pytest.raises(requests.RequestException, match="Network error"):
        auth.load_openid_config()


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Auth error handling not tested when SKIP_AUTH=true",
)
@patch("utils.auth.requests.get")
def test_load_openid_config_json_error(mock_get):
    """Test error handling when JSON parsing fails"""
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    mock_response = MagicMock()
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response

    with pytest.raises(ValueError, match="Invalid JSON"):
        auth.load_openid_config()


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Auth error handling not tested when SKIP_AUTH=true",
)
@patch("utils.auth.requests.get")
def test_load_openid_config_missing_jwks_uri(mock_get):
    """Test error handling when OpenID config is missing jwks_uri"""
    # Reset cache
    auth._openid_config = None
    auth._jwks = None

    # First request returns config without jwks_uri
    mock_openid_response = MagicMock()
    mock_openid_response.json.return_value = {"issuer": "test"}  # Missing jwks_uri
    mock_get.return_value = mock_openid_response

    with pytest.raises(KeyError):
        auth.load_openid_config()


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.jwt.PyJWK")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_jwt_decode_error(
    mock_load_config, mock_decode, mock_pyjwk, mock_get_header
):
    """Test validation when JWT decode fails"""
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}
    mock_pyjwk_instance = MagicMock()
    mock_pyjwk_instance.key = "publickey"
    mock_pyjwk.return_value = mock_pyjwk_instance
    mock_decode.side_effect = jwt.DecodeError("Invalid token format")

    with pytest.raises(jwt.DecodeError):
        auth.validate_token("token")


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.jwt.PyJWK")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_expired_token(
    mock_load_config, mock_decode, mock_pyjwk, mock_get_header
):
    """Test validation when token is expired"""
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}
    mock_pyjwk_instance = MagicMock()
    mock_pyjwk_instance.key = "publickey"
    mock_pyjwk.return_value = mock_pyjwk_instance
    mock_decode.side_effect = jwt.ExpiredSignatureError("Token has expired")

    with pytest.raises(jwt.ExpiredSignatureError):
        auth.validate_token("token")


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.jwt.PyJWK")
@patch("utils.auth.jwt.decode")
@patch("utils.auth.load_openid_config")
def test_validate_token_no_scope_claim(
    mock_load_config, mock_decode, mock_pyjwk, mock_get_header
):
    """Test validation when token has no scope claim"""
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}
    mock_pyjwk_instance = MagicMock()
    mock_pyjwk_instance.key = "publickey"
    mock_pyjwk.return_value = mock_pyjwk_instance
    mock_decode.return_value = {"sub": "user1"}  # No 'scp' claim

    with pytest.raises(jwt.InvalidTokenError, match="Missing required scope"):
        auth.validate_token("token")


@pytest.mark.skipif(
    getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Token validation not used when SKIP_AUTH=true",
)
@patch("utils.auth.jwt.get_unverified_header")
@patch("utils.auth.load_openid_config")
def test_validate_token_pyjwk_error(mock_load_config, mock_get_header):
    """Test validation when PyJWK construction fails"""
    mock_load_config.return_value = ({"issuer": "issuer"}, {"keys": [{"kid": "abc"}]})
    mock_get_header.return_value = {"kid": "abc"}

    with patch("utils.auth.jwt.PyJWK") as mock_pyjwk:
        mock_pyjwk.side_effect = ValueError("Invalid JWK")

        with pytest.raises(ValueError, match="Invalid JWK"):
            auth.validate_token("token")


def test_require_auth_skip_auth_true():
    """Test that SKIP_AUTH=true bypasses all authentication"""
    with patch.dict(os.environ, {"SKIP_AUTH": "true"}):
        app = Flask(__name__)

        @app.route("/test")
        @auth.require_auth
        def test_route():
            return jsonify({"user": g.claims["preferred_username"]})

        with app.test_client() as client:
            # No auth header should work
            resp = client.get("/test")
            assert resp.status_code == 200
            assert resp.json["user"] == "testuser@example.com"

            # Invalid auth header should still work
            resp = client.get("/test", headers={"Authorization": "Invalid"})
            assert resp.status_code == 200
            assert resp.json["user"] == "testuser@example.com"


def test_require_auth_bearer_token_extraction():
    """Test various bearer token formats"""
    with patch.dict(os.environ, {"SKIP_AUTH": "false"}):
        app = Flask(__name__)

        @app.route("/test")
        @auth.require_auth
        def test_route():
            return jsonify({"status": "ok"})

        with app.test_client() as client:
            # Missing Bearer prefix
            resp = client.get("/test", headers={"Authorization": "token123"})
            assert resp.status_code == 401

            # Empty Authorization header
            resp = client.get("/test", headers={"Authorization": ""})
            assert resp.status_code == 401

            # Just "Bearer" without token
            resp = client.get("/test", headers={"Authorization": "Bearer"})
            assert resp.status_code == 401
