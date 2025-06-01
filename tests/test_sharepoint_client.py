# tests/test_sharepoint_client.py
"""Tests for SharePoint client integration."""

import os
import pytest
from unittest.mock import patch, MagicMock

from utils.sharepoint_client import (
    SharePointClient,
    get_pyro_file_reference,
    get_pyro_standards_file_reference,
    search_pyro_files,
    get_wiresetcerts_file_reference,
    get_wiresetcerts_content,
    list_pyro_folder_contents,
)


class TestSharePointClient:
    """Test SharePoint client functionality."""

    def test_sharepoint_client_init_with_token(self):
        """Test SharePoint client initialization with access token."""
        client = SharePointClient("test-token")
        assert client.access_token == "test-token"
        assert client.base_url == "https://graph.microsoft.com/v1.0"

    @patch("utils.sharepoint_client.get_app_only_token")
    def test_sharepoint_client_init_without_token_uses_app_auth(self, mock_get_token):
        """Test SharePoint client initialization without token uses app-only auth."""
        mock_get_token.return_value = "app-only-token"

        client = SharePointClient()
        assert client.access_token == "app-only-token"
        mock_get_token.assert_called_once()

    @patch("utils.sharepoint_client.get_app_only_token")
    def test_sharepoint_client_init_app_auth_fails_raises_error(self, mock_get_token):
        """Test SharePoint client initialization when app auth fails."""
        mock_get_token.side_effect = ValueError("Token acquisition failed")

        with pytest.raises(ValueError, match="Failed to get app token"):
            SharePointClient()

    def test_explicit_token_overrides_app_auth(self):
        """Test that explicit token takes precedence over app auth."""
        client = SharePointClient("explicit-token")
        # Should use explicit token, not app auth
        assert client.access_token == "explicit-token"

    @patch("utils.sharepoint_client.requests.request")
    def test_make_request_success(self, mock_request):
        """Test successful API request."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"test": "data"}
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        response = client._make_request("GET", "test/endpoint")

        assert response == mock_response
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        assert args[0] == "GET"
        assert args[1] == "https://graph.microsoft.com/v1.0/test/endpoint"
        assert kwargs["headers"]["Authorization"] == "Bearer test-token"

    @patch("utils.sharepoint_client.requests.request")
    def test_get_site_info_with_site_id(self, mock_request):
        """Test getting site info using site ID."""
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "test-site", "name": "Test Site"}
        mock_request.return_value = mock_response

        with patch.dict(os.environ, {"SHAREPOINT_SITE_ID": "test-site-id"}):
            client = SharePointClient("test-token")
            result = client.get_site_info()

            assert result == {"id": "test-site", "name": "Test Site"}
            mock_request.assert_called_once()
            args = mock_request.call_args[0]
            assert "sites/test-site-id" in args[1]

    @patch("utils.sharepoint_client.requests.request")
    def test_get_drive_items(self, mock_request):
        """Test getting drive items."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "value": [{"name": "file1.txt"}, {"name": "file2.txt"}]
        }
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.get_drive_items("test-drive-id", "test/folder")

        assert len(result) == 2
        assert result[0]["name"] == "file1.txt"
        mock_request.assert_called_once()

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_by_path(self, mock_request):
        """Test getting file by path."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": "file-id",
            "name": "test.txt",
            "size": 1024,
            "webUrl": "https://sharepoint.com/test.txt",
        }
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.get_file_by_path("documents/test.txt", "test-drive-id")

        assert result["id"] == "file-id"
        assert result["name"] == "test.txt"
        mock_request.assert_called_once()

    @patch("utils.sharepoint_client.requests.request")
    def test_search_files(self, mock_request):
        """Test searching files."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "value": [
                {"name": "document1.pdf", "id": "doc1-id"},
                {"name": "document2.pdf", "id": "doc2-id"},
            ]
        }
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.search_files("document", "test-drive-id")

        assert len(result) == 2
        assert result[0]["name"] == "document1.pdf"
        mock_request.assert_called_once()

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_reference(self, mock_request):
        """Test getting comprehensive file reference."""
        # Mock the file info request
        file_info_response = MagicMock()
        file_info_response.json.return_value = {
            "id": "file-123",
            "name": "test-document.pdf",
            "size": 2048,
            "webUrl": "https://sharepoint.com/test-document.pdf",
            "lastModifiedDateTime": "2025-06-01T10:00:00Z",
            "file": {"mimeType": "application/pdf"},
        }

        # Mock the download URL request
        download_response = MagicMock()
        download_response.headers.get.return_value = (
            "https://download.sharepoint.com/temp-url"
        )

        mock_request.side_effect = [file_info_response, download_response]

        client = SharePointClient("test-token")
        result = client.get_file_reference(
            "documents/test-document.pdf", "test-drive-id", by_path=True
        )

        assert result["id"] == "file-123"
        assert result["name"] == "test-document.pdf"
        assert result["downloadUrl"] == "https://download.sharepoint.com/temp-url"
        assert result["mimeType"] == "application/pdf"
        assert result["driveId"] == "test-drive-id"
        assert result["path"] == "documents/test-document.pdf"

    @patch("utils.sharepoint_client.requests.request")
    def test_get_wiresetcerts_file_internal_method(self, mock_request):
        """Test the internal get_wiresetcerts_file method."""
        # Mock file info response
        file_info_response = MagicMock()
        file_info_response.json.return_value = {
            "id": "wiresetcerts-123",
            "name": "WireSetCerts.xlsx",
            "size": 4096,
            "webUrl": "https://sharepoint.com/WireSetCerts.xlsx",
            "lastModifiedDateTime": "2025-06-01T10:00:00Z",
            "file": {
                "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            },
        }

        # Mock download URL response
        download_response = MagicMock()
        download_response.headers.get.return_value = (
            "https://download.sharepoint.com/wiresetcerts-temp"
        )

        mock_request.side_effect = [file_info_response, download_response]

        with patch.dict(os.environ, {"SHAREPOINT_DRIVE_ID": "pyro-drive-123"}):
            client = SharePointClient("test-token")
            result = client.get_wiresetcerts_file()

            assert result["id"] == "wiresetcerts-123"
            assert result["name"] == "WireSetCerts.xlsx"
            assert (
                result["downloadUrl"]
                == "https://download.sharepoint.com/wiresetcerts-temp"
            )
            assert (
                result["mimeType"]
                == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    def test_get_wiresetcerts_file_missing_drive_id(self):
        """Test get_wiresetcerts_file with missing drive ID."""
        # Set environment variable to None/empty to test the error case
        with patch.dict(os.environ, {"SHAREPOINT_DRIVE_ID": ""}, clear=False):
            with patch("utils.sharepoint_client.os.getenv") as mock_getenv:
                # Make getenv return None for the drive_id specifically
                def side_effect(key, default=None):
                    if key == "SHAREPOINT_DRIVE_ID":
                        return None
                    return default

                mock_getenv.side_effect = side_effect

                client = SharePointClient("test-token")
                with pytest.raises(
                    ValueError, match="SHAREPOINT_DRIVE_ID not configured"
                ):
                    client.get_wiresetcerts_file()

    @patch("utils.sharepoint_client.SharePointClient")
    def test_get_pyro_file_reference(self, mock_client_class):
        """Test getting Pyro file reference."""
        mock_client = MagicMock()
        mock_client.drive_id = "pyro-drive-123"
        mock_client.get_file_reference.return_value = {"name": "pyro-file.xlsx"}
        mock_client_class.return_value = mock_client

        result = get_pyro_file_reference("data/pyro-file.xlsx", "test-token")

        assert result["name"] == "pyro-file.xlsx"
        mock_client.get_file_reference.assert_called_once_with(
            "data/pyro-file.xlsx", "pyro-drive-123", by_path=True
        )

    @patch("utils.sharepoint_client.SharePointClient")
    def test_get_pyro_file_reference_missing_drive_id(self, mock_client_class):
        """Test getting Pyro file reference with missing drive ID."""
        mock_client = MagicMock()
        mock_client.drive_id = None
        mock_client_class.return_value = mock_client

        with pytest.raises(ValueError, match="SHAREPOINT_DRIVE_ID not configured"):
            get_pyro_file_reference("data/pyro-file.xlsx", "test-token")

    @patch("utils.sharepoint_client.SharePointClient")
    def test_get_pyro_standards_file_reference(self, mock_client_class):
        """Test getting Pyro Standards file reference."""
        mock_client = MagicMock()
        mock_client.pyro_standards_drive_id = "standards-drive-456"
        mock_client.get_file_reference.return_value = {"name": "standard.pdf"}
        mock_client_class.return_value = mock_client

        result = get_pyro_standards_file_reference(
            "standards/standard.pdf", "test-token"
        )

        assert result["name"] == "standard.pdf"
        mock_client.get_file_reference.assert_called_once_with(
            "standards/standard.pdf", "standards-drive-456", by_path=True
        )

    @patch("utils.sharepoint_client.SharePointClient")
    def test_search_pyro_files(self, mock_client_class):
        """Test searching Pyro files."""
        mock_client = MagicMock()
        mock_client.drive_id = "pyro-drive-123"
        mock_client.search_files.return_value = [{"name": "found-file.xlsx"}]
        mock_client_class.return_value = mock_client

        result = search_pyro_files("calibration", "test-token")

        assert len(result) == 1
        assert result[0]["name"] == "found-file.xlsx"
        mock_client.search_files.assert_called_once_with(
            "calibration", "pyro-drive-123"
        )

    @patch("utils.sharepoint_client.SharePointClient")
    def test_list_pyro_folder_contents(self, mock_client_class):
        """Test listing Pyro folder contents."""
        mock_client = MagicMock()
        mock_client.drive_id = "pyro-drive-123"
        mock_client.get_drive_items.return_value = [
            {"name": "file1.xlsx", "type": "file"},
            {"name": "subfolder", "type": "folder"},
        ]
        mock_client_class.return_value = mock_client

        result = list_pyro_folder_contents("data", "test-token")

        assert len(result) == 2
        assert result[0]["name"] == "file1.xlsx"
        mock_client.get_drive_items.assert_called_once_with("pyro-drive-123", "data")

    @patch("utils.sharepoint_client.SharePointClient")
    def test_get_wiresetcerts_file_reference(self, mock_client_class):
        """Test getting WireSetCerts.xlsx file reference."""
        mock_client = MagicMock()
        mock_client.get_wiresetcerts_file.return_value = {
            "name": "WireSetCerts.xlsx",
            "id": "wiresetcerts-file-id",
            "downloadUrl": "https://sharepoint.com/download/wiresetcerts.xlsx",
        }
        mock_client_class.return_value = mock_client

        result = get_wiresetcerts_file_reference("test-token")

        assert result["name"] == "WireSetCerts.xlsx"
        assert result["id"] == "wiresetcerts-file-id"
        mock_client.get_wiresetcerts_file.assert_called_once()

    def test_SharePointClient(self):
        """Test SharePoint client factory function."""
        client = SharePointClient("test-token")

        assert isinstance(client, SharePointClient)
        assert client.access_token == "test-token"


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Skipped when SKIP_AUTH=true",
)
class TestSharePointClientIntegration:
    """Integration tests for SharePoint client (requires real auth)."""

    def test_sharepoint_client_with_real_config(self):
        """Test SharePoint client with real configuration."""
        # This test only runs when SKIP_AUTH=false
        # and would require real SharePoint configuration
        client = SharePointClient("test-token")
        assert client.drive_id is not None or client.pyro_standards_drive_id is not None
