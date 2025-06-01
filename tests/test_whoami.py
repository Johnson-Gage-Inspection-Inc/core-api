def test_whoami_with_auth(client, auth_token):
    response = client.get("/whoami", headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == 200
    data = response.get_json()
    assert "user" in data
    assert "@" in data["user"]  # basic check for email structure


def test_whoami_without_auth(client):
    response = client.get("/whoami")
    assert response.status_code == 401
    assert response.text == "Unauthorized"
