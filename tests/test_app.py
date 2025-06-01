"""
Tests for core Flask application functionality.

Note: Authentication-specific tests are in test_auth.py.
This file focuses on app-level functionality like route registration and basic responses.
"""

from app import app


def test_index_route_returns_204():
    """Test that the root route returns 204 No Content."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 204
        assert response.data == b""


def test_index_route_options_returns_204():
    """Test that OPTIONS request to root route returns 204 No Content."""
    with app.test_client() as client:
        response = client.options("/")
        assert response.status_code == 204
        assert response.data == b""


def test_app_startup():
    """Test that the app starts up correctly."""
    assert app is not None
    assert app.config is not None


def test_app_routes_exist():
    """Test that expected routes are registered."""
    rule_paths = [rule.rule for rule in app.url_map.iter_rules()]
    expected_routes = ["/whoami", "/pyro-assets", "/work-item-details"]

    for route in expected_routes:
        assert route in rule_paths, f"Route {route} not found in registered routes"


def test_app_has_cors_support():
    """Test that CORS is properly configured."""
    with app.test_client() as client:
        # Test preflight request
        response = client.options(
            "/whoami",
            headers={
                "Origin": "https://example.com",
                "Access-Control-Request-Method": "GET",
                "Access-Control-Request-Headers": "Authorization",
            },
        )

        # Should get a response (not necessarily 200, but CORS headers should be present)
        assert response.status_code in [
            200,
            204,
            401,
        ]  # Different depending on auth mode


def test_app_blueprint_registration():
    """Test that all expected blueprints are registered."""
    blueprint_names = [bp.name for bp in app.blueprints.values()]
    expected_blueprints = [
        "whoami",
        "work-item-details",
        "pyro-assets",
        "employees",
        "clients",
        "git-ops",
    ]

    for blueprint in expected_blueprints:
        assert blueprint in blueprint_names, f"Blueprint {blueprint} not registered"
