import os
import pytest
from unittest import mock

import utils.get_token as get_token_mod

@mock.patch.dict(os.environ, {"SKIP_AUTH": "true"})
def test_get_access_token_skip_auth(monkeypatch, capsys):
    token = get_token_mod.get_access_token()
    assert token == "fake-token"
    captured = capsys.readouterr()
    assert "Skipping get_access_token()" in captured.out

@mock.patch("msal.PublicClientApplication")
@mock.patch("dotenv.load_dotenv")
def test_get_access_token_success(mock_load_dotenv, mock_pca, monkeypatch):
    # Set required env vars
    monkeypatch.setenv("SKIP_AUTH", "false")
    monkeypatch.setenv("AZURE_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("AZURE_TENANT_ID", "test-tenant-id")

    # Mock msal app and its method
    mock_app = mock.Mock()
    mock_app.acquire_token_interactive.return_value = {"access_token": "real-token"}
    mock_pca.return_value = mock_app

    token = get_token_mod.get_access_token()
    assert token == "real-token"
    mock_app.acquire_token_interactive.assert_called_once()

@mock.patch("msal.PublicClientApplication")
@mock.patch("dotenv.load_dotenv")
def test_get_access_token_error(mock_load_dotenv, mock_pca, monkeypatch, capsys):
    monkeypatch.setenv("SKIP_AUTH", "false")
    monkeypatch.setenv("AZURE_CLIENT_ID", "test-client-id")
    monkeypatch.setenv("AZURE_TENANT_ID", "test-tenant-id")

    mock_app = mock.Mock()
    mock_app.acquire_token_interactive.return_value = {
        "error": "invalid_grant",
        "error_description": "Some error"
    }
    mock_pca.return_value = mock_app

    with pytest.raises(KeyError):
        # Should raise because "access_token" is missing
        get_token_mod.get_access_token()
    captured = capsys.readouterr()
    assert "Error acquiring token:" in captured.out