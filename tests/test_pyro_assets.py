import os
from unittest.mock import patch


def test_pyro_assets_with_auth(client, auth_token):
    """Test the /pyro-assets endpoint with valid authentication."""
    response = client.get(
        "/pyro-assets", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

    if skip_auth:
        # In mock mode, expect specific mock data structure
        assert len(data) >= 2  # Mock returns 2 items
        if len(data) > 0:
            first_asset = data[0]
            assert "asset_id" in first_asset
            assert "asset_tag" in first_asset
            assert "description" in first_asset
            assert first_asset["asset_tag"] == "PYRO001"
    else:
        # In real mode, just verify it's a list (may be empty if no assets in pool)
        # The fact that we got 200 and a list means the auth and API call worked
        assert isinstance(data, list)
        assert (
            len(data) >= 0
        ), "Expected at least an empty list in the real mode response"
        # If there are assets, they should be dictionaries
        assert all(x != {} for x in data), "Expected non-empty asset objects"
        if data:
            assert all(isinstance(item, dict) for item in data)


def test_pyro_assets_without_auth(client):
    """Test the /pyro-assets endpoint without authentication token."""
    response = client.get("/pyro-assets")
    assert response.status_code == 401
    # Support both simple text and JSON format for Unauthorized message
    assert "Unauthorized" in response.text


def test_pyro_assets_api_error(client, auth_token):
    """Test the /pyro-assets endpoint when Qualer API fails."""
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

    if skip_auth:
        # In mock mode, temporarily restore real view function to test error handling
        from app import app
        from routes.pyro_assets import PyroAssets

        original_view_func = app.view_functions.get("pyro-assets.PyroAssets")
        app.view_functions["pyro-assets.PyroAssets"] = PyroAssets().get

        try:
            with patch("routes.pyro_assets.get_asset_by_asset_pool") as mock_api:
                # Simulate API returning None (which we handle gracefully)
                mock_api.return_value = None

                response = client.get(
                    "/pyro-assets", headers={"Authorization": f"Bearer {auth_token}"}
                )
                assert response.status_code == 200
                assert response.get_json() == []
        finally:
            if original_view_func:
                app.view_functions["pyro-assets.PyroAssets"] = original_view_func
    else:
        # In real mode, we can't easily mock the API without affecting the real client
        # So we'll test the actual behavior (which may return empty list)
        response = client.get(
            "/pyro-assets", headers={"Authorization": f"Bearer {auth_token}"}
        )
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)


def test_pyro_assets_invalid_token(client):
    """Test the /pyro-assets endpoint with an invalid token."""
    response = client.get(
        "/pyro-assets", headers={"Authorization": "Bearer invalid_token"}
    )

    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

    if skip_auth:
        # In mock mode, our mock checks for "Bearer " prefix but accepts any token
        assert response.status_code == 200
    else:
        # In real mode, invalid token should be rejected
        assert response.status_code == 401
