import pytest
from get_token import get_access_token

def test_whoami_with_auth(client):
    token = get_access_token()
    assert token, "Access token is missing — check .env and get_token.py config"

    response = client.get(
        "/whoami",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "user" in data
    assert "@" in data["user"]  # basic check for email structure

def test_whoami_without_auth(client):
    response = client.get("/whoami")
    assert response.status_code == 401
    data = response.get_json()
    assert "error" in data
