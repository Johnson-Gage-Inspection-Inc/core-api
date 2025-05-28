import pytest
import jwt
from unittest.mock import patch
from app import validate_token, REQUIRED_SCOPE, app

@pytest.fixture
def fake_jwks():
    return {
        "keys": [
            {
                "kid": "testkid",
                "kty": "RSA",
                "alg": "RS256",
                "use": "sig",
                "n": "testn",
                "e": "AQAB"
            }
        ]
    }

@pytest.fixture
def fake_token():
    return "fake.jwt.token"

@pytest.fixture
def fake_payload():
    return {
        "scp": f"other_scope {REQUIRED_SCOPE}",
        "sub": "user1"
    }

@patch("app.jwt.get_unverified_header")
@patch("app.jwks", {"keys": [{"kid": "testkid", "kty": "RSA", "alg": "RS256", "use": "sig", "n": "testn", "e": "AQAB"}]})
@patch("app.jwt.algorithms.RSAAlgorithm.from_jwk")
@patch("app.jwt.decode")
def test_validate_token_success(mock_decode, mock_from_jwk, mock_get_unverified_header, fake_token, fake_payload):
    mock_get_unverified_header.return_value = {"kid": "testkid"}
    mock_from_jwk.return_value = "public_key"
    mock_decode.return_value = fake_payload

    result = validate_token(fake_token)
    assert result == fake_payload
    mock_decode.assert_called_once()

@patch("app.jwt.get_unverified_header")
@patch("app.jwks", {"keys": [{"kid": "testkid", "kty": "RSA", "alg": "RS256", "use": "sig", "n": "testn", "e": "AQAB"}]})
@patch("app.jwt.algorithms.RSAAlgorithm.from_jwk")
@patch("app.jwt.decode")
def test_validate_token_missing_scope_raises(mock_decode, mock_from_jwk, mock_get_unverified_header, fake_token):
    mock_get_unverified_header.return_value = {"kid": "testkid"}
    mock_from_jwk.return_value = "public_key"
    mock_decode.return_value = {"scp": "other_scope"}

    with pytest.raises(jwt.InvalidTokenError):
        validate_token(fake_token)

@patch("app.jwt.get_unverified_header")
@patch("app.jwks", {"keys": [{"kid": "testkid", "kty": "RSA", "alg": "RS256", "use": "sig", "n": "testn", "e": "AQAB"}]})
@patch("app.jwt.algorithms.RSAAlgorithm.from_jwk")
@patch("app.jwt.decode")
def test_validate_token_no_scp_field_raises(mock_decode, mock_from_jwk, mock_get_unverified_header, fake_token):
    mock_get_unverified_header.return_value = {"kid": "testkid"}
    mock_from_jwk.return_value = "public_key"
    mock_decode.return_value = {}

    with pytest.raises(jwt.InvalidTokenError):
        validate_token(fake_token)

@patch("app.jwt.get_unverified_header")
@patch("app.jwks", {"keys": [{"kid": "testkid", "kty": "RSA", "alg": "RS256", "use": "sig", "n": "testn", "e": "AQAB"}]})
@patch("app.jwt.algorithms.RSAAlgorithm.from_jwk")
@patch("app.jwt.decode")
def test_validate_token_kid_not_found(mock_decode, mock_from_jwk, mock_get_unverified_header, fake_token):
    mock_get_unverified_header.return_value = {"kid": "unknown_kid"}
    mock_from_jwk.return_value = "public_key"
    mock_decode.return_value = {"scp": f"{REQUIRED_SCOPE}"}

    with pytest.raises(StopIteration):
        validate_token(fake_token)

def test_index_route_returns_204():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 204
        assert response.data == b""

def test_index_route_options_returns_204():
    with app.test_client() as client:
        response = client.options("/")
        assert response.status_code == 204
        assert response.data == b""
