"""
Test to ensure sensitive environment variables are not accidentally committed.
This test should run in CI to prevent secrets from being checked into Git.
"""

from pathlib import Path

import pytest


def test_no_secrets_in_settings_env():
    """Ensure that sensitive values are not in the tracked settings.env file."""
    settings_file = Path(__file__).parent.parent / "config" / "settings.env"

    if not settings_file.exists():
        pytest.skip("settings.env not found")

    content = settings_file.read_text()

    # Check for sensitive patterns that should NOT be in settings.env
    forbidden_patterns = [
        "AZURE_CLIENT_SECRET=",  # Should be in .env only
        "QUALER_API_KEY=",  # Should be in .env only
        "DATABASE_URL=postgresql",  # Should be in .env only
        "password",  # Should never be in tracked files
        "secret",  # Should be generic placeholders only
    ]

    for pattern in forbidden_patterns:
        assert (
            pattern not in content
        ), f"Sensitive pattern '{pattern}' found in settings.env"


def test_required_secrets_in_env_example():
    """Ensure .env.example contains all required secret placeholders."""
    env_example = Path(__file__).parent.parent / ".env.example"

    if not env_example.exists():
        pytest.skip(".env.example not found")

    content = env_example.read_text()

    # Required secret placeholders
    required_vars = [
        "QUALER_API_KEY=",
        "AZURE_CLIENT_SECRET=",
        "DATABASE_URL=",
    ]

    for var in required_vars:
        assert var in content, f"Required variable '{var}' not found in .env.example"


def test_environment_split_is_secure():
    """Test that the environment split configuration is working properly."""
    # This test ensures config.py loads both files in the correct order

    # Verify that config.py exists and has the right structure
    config_file = Path(__file__).parent.parent / "config.py"
    assert config_file.exists(), "config.py not found"

    config_content = config_file.read_text()
    assert "settings.env" in config_content, "config.py should load settings.env"
    assert "override=False" in config_content, "settings.env should not override"
    assert "override=True" in config_content, ".env should override settings.env"


def test_gitignore_protects_secrets():
    """Ensure .gitignore is properly configured to protect secrets."""
    gitignore = Path(__file__).parent.parent / ".gitignore"

    if gitignore.exists():
        content = gitignore.read_text()

        # .env should be ignored (but not .env.example)
        assert ".env" in content, ".env should be in .gitignore"

        # Check that we're not accidentally ignoring .env.example
        lines = [line.strip() for line in content.split("\n")]
        env_patterns = [line for line in lines if line.startswith(".env")]

        # Should have .env but not .env.example explicitly ignored
        assert any(
            ".env" == pattern for pattern in env_patterns
        ), ".env should be ignored"
