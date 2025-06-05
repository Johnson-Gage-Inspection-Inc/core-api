import os
from unittest.mock import Mock, patch

import pytest

from utils.graph_auth import get_app_only_token

"""Tests for Microsoft Graph authentication utilities."""


class TestGetAppOnlyToken:
    """Test cases for get_app_only_token function."""

    def test_successful_token_acquisition(self):
        """Test successful token acquisition with valid credentials."""
        mock_result = {
            "access_token": "test_access_token_123",
            "token_type": "Bearer",
            "expires_in": 3600,
        }

        with patch.dict(
            os.environ,
            {
                "AZURE_TENANT_ID": "test-tenant-id",
                "AZURE_CLIENT_ID": "test-client-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
        ):
            with patch(
                "utils.graph_auth.msal.ConfidentialClientApplication"
            ) as mock_app_class:
                mock_app = Mock()
                mock_app.acquire_token_for_client.return_value = mock_result
                mock_app_class.return_value = mock_app

                token = get_app_only_token()

                assert token == "test_access_token_123"
                mock_app_class.assert_called_once_with(
                    client_id="test-client-id",
                    authority="https://login.microsoftonline.com/test-tenant-id",
                    client_credential="test-client-secret",
                )
                mock_app.acquire_token_for_client.assert_called_once_with(
                    scopes=["https://graph.microsoft.com/.default"]
                )

    def test_missing_tenant_id(self):
        """Test ValueError when AZURE_TENANT_ID is missing."""
        with patch.dict(
            os.environ,
            {
                "AZURE_CLIENT_ID": "test-client-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
            clear=True,
        ):
            with pytest.raises(ValueError) as exc_info:
                get_app_only_token()

            assert "Missing required environment variables: AZURE_TENANT_ID" in str(
                exc_info.value
            )

    def test_missing_client_id(self):
        """Test ValueError when AZURE_CLIENT_ID is missing."""
        with patch.dict(
            os.environ,
            {
                "AZURE_TENANT_ID": "test-tenant-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
            clear=True,
        ):
            with pytest.raises(ValueError) as exc_info:
                get_app_only_token()

            assert "Missing required environment variables: AZURE_CLIENT_ID" in str(
                exc_info.value
            )

    def test_missing_client_secret(self):
        """Test ValueError when AZURE_CLIENT_SECRET is missing."""
        with patch.dict(
            os.environ,
            {"AZURE_TENANT_ID": "test-tenant-id", "AZURE_CLIENT_ID": "test-client-id"},
            clear=True,
        ):
            with pytest.raises(ValueError) as exc_info:
                get_app_only_token()

            assert "Missing required environment variables: AZURE_CLIENT_SECRET" in str(
                exc_info.value
            )

    def test_missing_multiple_env_vars(self):
        """Test ValueError when multiple environment variables are missing."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError) as exc_info:
                get_app_only_token()

            error_message = str(exc_info.value)
            assert "Missing required environment variables:" in error_message
            assert "AZURE_TENANT_ID" in error_message
            assert "AZURE_CLIENT_ID" in error_message
            assert "AZURE_CLIENT_SECRET" in error_message

    def test_token_acquisition_failure_with_error_details(self):
        """Test RuntimeError when token acquisition fails with error details."""
        mock_result = {
            "error": "invalid_client",
            "error_description": "AADSTS70002: The request body must contain the following parameter: 'client_secret'",
        }

        with patch.dict(
            os.environ,
            {
                "AZURE_TENANT_ID": "test-tenant-id",
                "AZURE_CLIENT_ID": "test-client-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
        ):
            with patch(
                "utils.graph_auth.msal.ConfidentialClientApplication"
            ) as mock_app_class:
                mock_app = Mock()
                mock_app.acquire_token_for_client.return_value = mock_result
                mock_app_class.return_value = mock_app

                with pytest.raises(RuntimeError) as exc_info:
                    get_app_only_token()

                error_message = str(exc_info.value)
                assert "Token acquisition failed [invalid_client]:" in error_message
                assert "AADSTS70002" in error_message

    def test_token_acquisition_failure_without_error_details(self):
        """Test RuntimeError when token acquisition fails without detailed error info."""
        mock_result = {}  # No error details provided

        with patch.dict(
            os.environ,
            {
                "AZURE_TENANT_ID": "test-tenant-id",
                "AZURE_CLIENT_ID": "test-client-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
        ):
            with patch(
                "utils.graph_auth.msal.ConfidentialClientApplication"
            ) as mock_app_class:
                mock_app = Mock()
                mock_app.acquire_token_for_client.return_value = mock_result
                mock_app_class.return_value = mock_app

                with pytest.raises(RuntimeError) as exc_info:
                    get_app_only_token()

                error_message = str(exc_info.value)
                assert (
                    "Token acquisition failed [unknown_error]: Unknown error"
                    in error_message
                )

    def test_token_acquisition_partial_error_info(self):
        """Test RuntimeError when token acquisition fails with partial error info."""
        mock_result = {
            "error": "invalid_request"
            # Missing error_description
        }

        with patch.dict(
            os.environ,
            {
                "AZURE_TENANT_ID": "test-tenant-id",
                "AZURE_CLIENT_ID": "test-client-id",
                "AZURE_CLIENT_SECRET": "test-client-secret",
            },
        ):
            with patch(
                "utils.graph_auth.msal.ConfidentialClientApplication"
            ) as mock_app_class:
                mock_app = Mock()
                mock_app.acquire_token_for_client.return_value = mock_result
                mock_app_class.return_value = mock_app

                with pytest.raises(RuntimeError) as exc_info:
                    get_app_only_token()

                error_message = str(exc_info.value)
                assert (
                    "Token acquisition failed [invalid_request]: Unknown error"
                    in error_message
                )
                error_message = str(exc_info.value)
                assert (
                    "Token acquisition failed [invalid_request]: Unknown error"
                    in error_message
                )
