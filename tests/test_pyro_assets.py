import os

import pytest


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "false",
    reason="Skipping pyro-assets test when SKIP_AUTH=false due to external API validation issues",
)
def test_pyro_assets_with_auth(client, auth_token):
    response = client.get(
        "/pyro-assets", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert isinstance(data[0], dict)


def test_pyro_assets_without_auth(client):
    response = client.get("/pyro-assets")
    assert response.status_code == 401
    assert response.text == "Unauthorized"
    assert response.text == "Unauthorized"
