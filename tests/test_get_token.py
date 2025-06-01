import logging
import os
from unittest import mock

import pytest

import utils.get_token as get_token_mod


@mock.patch.dict(os.environ, {"SKIP_AUTH": "true"})
def test_get_access_token_skip_auth(monkeypatch, caplog):
    # Set logging level to capture INFO messages
    caplog.set_level(logging.INFO)
    token = get_token_mod.get_access_token()
    assert token == "fake-token"
    assert "Skipping get_access_token() because SKIP_AUTH is true" in caplog.text


@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch("msal.SerializableTokenCache")
@mock.patch("msal.PublicClientApplication")
@mock.patch("dotenv.load_dotenv")
@mock.patch("os.path.exists")
def test_get_access_token_success(
    mock_exists, mock_load_dotenv, mock_pca, mock_cache_class, mock_file, monkeypatch
):
    # Set required env vars
    monkeypatch.setenv("SKIP_AUTH", "false")
    monkeypatch.setenv("AZURE_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("AZURE_TENANT_ID", "test-tenant-id")
    monkeypatch.setenv("AZURE_API_AUDIENCE", "https://api.example.com")
    monkeypatch.setenv("AZURE_REQUIRED_SCOPE", "access_as_user")

    # Mock cache file doesn't exist (fresh start)
    mock_exists.return_value = False

    # Mock cache
    mock_cache = mock.Mock()
    mock_cache.has_state_changed = True
    mock_cache.serialize.return_value = '{"valid": "json"}'
    mock_cache_class.return_value = mock_cache

    # Mock msal app and its methods
    mock_app = mock.Mock()
    mock_app.get_accounts.return_value = []  # No cached accounts
    mock_app.acquire_token_interactive.return_value = {"access_token": "real-token"}
    mock_pca.return_value = mock_app

    token = get_token_mod.get_access_token()
    assert token == "real-token"
    mock_app.acquire_token_interactive.assert_called_once()
    mock_app.acquire_token_silent.assert_not_called()  # Should not try silent first since no accounts


@mock.patch("builtins.open", new_callable=mock.mock_open)
@mock.patch("msal.SerializableTokenCache")
@mock.patch("msal.PublicClientApplication")
@mock.patch("dotenv.load_dotenv")
@mock.patch("os.path.exists")
def test_get_access_token_error(
    mock_exists, mock_load_dotenv, mock_pca, mock_cache_class, mock_file, monkeypatch
):
    monkeypatch.setenv("SKIP_AUTH", "false")
    monkeypatch.setenv("AZURE_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("AZURE_TENANT_ID", "test-tenant-id")
    monkeypatch.setenv("AZURE_API_AUDIENCE", "https://api.example.com")
    monkeypatch.setenv("AZURE_REQUIRED_SCOPE", "access_as_user")

    # Mock cache file doesn't exist
    mock_exists.return_value = False

    # Mock cache
    mock_cache = mock.Mock()
    mock_cache.has_state_changed = False
    mock_cache_class.return_value = mock_cache

    mock_app = mock.Mock()
    mock_app.get_accounts.return_value = []  # No cached accounts
    mock_app.acquire_token_interactive.return_value = {
        "error": "invalid_grant",
        "error_description": "Some error",
    }
    mock_pca.return_value = mock_app

    with pytest.raises(Exception, match="Failed to acquire token"):
        get_token_mod.get_access_token()
