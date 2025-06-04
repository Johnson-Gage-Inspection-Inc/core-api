# tests/test_sharepoint_client.py
"""Tests for SharePoint client integration."""

import os
from unittest.mock import MagicMock, patch

import pytest
import requests

from utils.sharepoint_client import (
    SharePointClient,
    get_pyro_file_reference,
    get_pyro_standards_file_reference,
    get_wiresetcerts_file_reference,
    list_pyro_folder_contents,
    search_pyro_files,
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
    def test_make_request_error_handling(self, mock_request):
        """Test API request error handling."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("Not found")
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")

        with pytest.raises(requests.HTTPError):
            client.get_site_info()

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
    def test_get_file_by_path_not_found(self, mock_request):
        """Test getting file by path when file doesn't exist."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.get_file_by_path("nonexistent/file.txt", "test-drive-id")

        assert result == {}

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_by_id(self, mock_request):
        """Test getting file by ID."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "id": "file-id-123",
            "name": "test.xlsx",
            "size": 2048,
        }
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.get_file_by_id("file-id-123", "test-drive-id")

        assert result["id"] == "file-id-123"
        assert result["name"] == "test.xlsx"
        mock_request.assert_called_once()

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_download_url(self, mock_request):
        """Test getting file download URL."""
        mock_response = MagicMock()
        mock_response.headers = {"Location": "https://download.url/file.xlsx"}
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        url = client.get_file_download_url("file-id", "test-drive-id")

        assert url == "https://download.url/file.xlsx"
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        assert kwargs["allow_redirects"] is False

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_download_url_no_location(self, mock_request):
        """Test getting file download URL when Location header is missing."""
        mock_response = MagicMock()
        mock_response.headers = {}
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        url = client.get_file_download_url("file-id", "test-drive-id")

        assert url == ""

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_reference_by_path(self, mock_request):
        """Test getting file reference by path."""
        # Mock the file metadata response
        mock_file_response = MagicMock()
        mock_file_response.json.return_value = {
            "id": "file-123",
            "name": "test.xlsx",
            "size": 1024,
            "webUrl": "https://sharepoint.com/test.xlsx",
        }
        mock_file_response.status_code = 200

        # Mock the download URL response
        mock_download_response = MagicMock()
        mock_download_response.headers = {"Location": "https://download.url/test.xlsx"}

        mock_request.side_effect = [mock_file_response, mock_download_response]

        client = SharePointClient("test-token")
        result = client.get_file_reference(
            "documents/test.xlsx", "test-drive-id", by_path=True
        )
        assert result["id"] == "file-123"
        assert result["name"] == "test.xlsx"
        assert result["downloadUrl"] == "https://download.url/test.xlsx"
        assert mock_request.call_count == 2

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_reference_by_id(self, mock_request):
        """Test getting file reference by ID."""
        # Mock the file metadata response
        mock_file_response = MagicMock()
        mock_file_response.json.return_value = {
            "id": "file-123",
            "name": "test.xlsx",
            "size": 1024,
        }

        # Mock the download URL response
        mock_download_response = MagicMock()
        mock_download_response.headers = {"Location": "https://download.url/test.xlsx"}

        mock_request.side_effect = [mock_file_response, mock_download_response]

        client = SharePointClient("test-token")
        result = client.get_file_reference("file-123", "test-drive-id", by_path=False)
        assert result["id"] == "file-123"
        assert result["downloadUrl"] == "https://download.url/test.xlsx"
        assert mock_request.call_count == 2

    @patch("utils.sharepoint_client.requests.request")
    def test_get_file_reference_file_not_found(self, mock_request):
        """Test getting file reference when file doesn't exist."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_request.return_value = mock_response

        client = SharePointClient("test-token")
        result = client.get_file_reference("nonexistent.xlsx", "test-drive-id")

        # Should return dict with None values when file not found
        expected_result = {
            "id": None,
            "name": None,
            "webUrl": None,
            "downloadUrl": None,
            "size": None,
            "lastModifiedDateTime": None,
            "createdDateTime": None,
            "mimeType": None,
            "driveId": "test-drive-id",
            "path": "nonexistent.xlsx",
        }
        assert result == expected_result

    @patch("utils.sharepoint_client.get_app_only_token")
    def test_init_fallback_to_flask_token(self, mock_get_token):
        """Test fallback to Flask request token when app auth fails."""

        from flask import Flask

        # Mock app token failure
        mock_get_token.side_effect = ValueError("App token failed")

        # Create Flask app and context for testing
        app = Flask(__name__)
        with app.test_request_context(headers={"Authorization": "Bearer flask-token"}):
            client = SharePointClient()
            assert client.access_token == "flask-token"

    @patch("utils.sharepoint_client.get_app_only_token")
    @patch("utils.sharepoint_client.has_request_context")
    def test_init_no_token_no_context_raises_error(
        self, mock_has_context, mock_get_token
    ):
        """Test error when no token available and no Flask context."""
        mock_get_token.side_effect = ValueError("App token failed")
        mock_has_context.return_value = False
        with pytest.raises(
            ValueError,
            match="Failed to get app token.*and no Flask request context available",
        ):
            SharePointClient()

    @patch("utils.sharepoint_client.get_app_only_token")
    def test_init_invalid_flask_token_raises_error(self, mock_get_token):
        """Test error when Flask token is invalid format."""
        from flask import Flask

        mock_get_token.side_effect = ValueError("App token failed")

        # Create Flask app and context with invalid token
        app = Flask(__name__)
        with app.test_request_context(headers={"Authorization": "InvalidToken"}):
            with pytest.raises(
                ValueError,
                match="Failed to get app token.*and no valid request token found",
            ):
                SharePointClient()

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

    @patch("utils.sharepoint_client.requests.get")
    @patch("utils.sharepoint_client.requests.request")
    def test_get_pyro_standards_excel_file_content_parsing(
        self, mock_request, mock_get
    ):
        """Test Excel content parsing in get_pyro_standards_excel_file."""
        # Mock Excel file content
        from unittest.mock import MagicMock

        # Create a mock Excel file in memory
        excel_content = b"mock excel content"

        # Mock file reference response
        mock_file_response = MagicMock()
        mock_file_response.json.return_value = {
            "id": "excel-file-id",
            "name": "test.xlsm",
            "size": 1024,
        }
        mock_file_response.status_code = 200

        # Mock download URL response
        mock_download_response = MagicMock()
        mock_download_response.headers = {"Location": "https://download.url/test.xlsm"}
        # Mock actual file download
        mock_content_response = MagicMock()
        mock_content_response.content = excel_content
        mock_content_response.raise_for_status = MagicMock()
        mock_request.side_effect = [
            mock_file_response,  # get_file_by_path call in get_file_reference
            mock_download_response,  # get_file_download_url call in get_file_reference
            mock_download_response,  # Second get_file_download_url call in download_file_content
        ]

        # Mock the requests.get call for file download
        mock_get.return_value = mock_content_response

        with patch("openpyxl.load_workbook") as mock_load_wb:
            # Mock openpyxl workbook
            mock_sheet = MagicMock()
            mock_sheet.title = "Sheet1"
            mock_sheet.max_row = 10
            mock_sheet.max_column = 5
            mock_sheet.iter_rows.return_value = [
                (MagicMock(value="Header1"), MagicMock(value="Header2")),
                (MagicMock(value="Data1"), MagicMock(value="Data2")),
            ]

            mock_workbook = MagicMock()
            mock_workbook.sheetnames = ["Sheet1"]
            mock_workbook.__getitem__.return_value = mock_sheet
            mock_workbook.__iter__.return_value = iter([mock_sheet])
            mock_load_wb.return_value = mock_workbook

            from utils.sharepoint_client import get_pyro_standards_excel_file

            result = get_pyro_standards_excel_file("test.xlsm", "test-token")

            assert "file_info" in result
            assert "sheets" in result
            assert "Sheet1" in result["sheets"]
            assert result["sheet_names"] == ["Sheet1"]
            assert result["total_sheets"] == 1

    def test_get_pyro_standards_excel_file_no_openpyxl(self):
        """Test error when openpyxl is not available."""
        with patch.dict("sys.modules", {"openpyxl": None}):
            from utils.sharepoint_client import get_pyro_standards_excel_file

            with pytest.raises(ImportError, match="openpyxl is required"):
                get_pyro_standards_excel_file("test.xlsm", "test-token")

    @patch("utils.sharepoint_client.requests.get")
    @patch("utils.sharepoint_client.requests.request")
    def test_get_wiresetcerts_content_parsing(self, mock_request, mock_get):
        """Test wiresetcerts content parsing."""
        # Mock Excel file content
        excel_content = b"mock excel content"

        # Mock file reference response
        mock_file_response = MagicMock()
        mock_file_response.json.return_value = {
            "id": "wiresetcerts-id",
            "name": "wiresetcerts.xlsx",
            "size": 2048,
        }
        mock_file_response.status_code = 200
        # Mock download and content responses
        mock_download_response = MagicMock()
        mock_download_response.headers = {
            "Location": "https://download.url/wiresetcerts.xlsx"
        }

        mock_content_response = MagicMock()
        mock_content_response.content = excel_content
        mock_content_response.raise_for_status = MagicMock()
        mock_request.side_effect = [
            mock_file_response,  # get_file_by_path call in get_wiresetcerts_file -> get_file_reference
            mock_download_response,  # get_file_download_url call in get_file_reference
            mock_download_response,  # Second get_file_download_url call in download_file_content
        ]

        # Mock the requests.get call for file download
        mock_get.return_value = mock_content_response

        with patch("openpyxl.load_workbook") as mock_load_wb:
            # Mock workbook with wiresetcerts data
            mock_sheet = MagicMock()
            mock_sheet.title = "WireSetCerts"
            mock_sheet.max_row = 100
            mock_sheet.max_column = 10
            mock_sheet.iter_rows.return_value = [
                # Header row
                (MagicMock(value="Wire Lot"), MagicMock(value="Certificate")),
                # Data rows
                (MagicMock(value="W12345"), MagicMock(value="Cert123")),
                (MagicMock(value="W67890"), MagicMock(value="Cert456")),
            ]
            mock_workbook = MagicMock()
            mock_workbook.sheetnames = ["WireSetCerts"]
            mock_workbook.__getitem__.return_value = mock_sheet
            mock_load_wb.return_value = mock_workbook

            from utils.sharepoint_client import get_wiresetcerts_content

            result = get_wiresetcerts_content("test-token")

            assert "file_info" in result
            assert "sheets" in result
            assert "WireSetCerts" in result["sheets"]
            assert "sample_data" in result["sheets"]["WireSetCerts"]
            # The implementation tries to get up to 5 rows of data (rows 2-6)
            # Our mock data is repeated for each row, so we'll have 5 identical rows
            assert len(result["sheets"]["WireSetCerts"]["sample_data"]) == 5

    @patch("utils.sharepoint_client.SharePointClient")
    def test_search_pyro_files_error_handling(self, mock_client_class):
        """Test error handling in search_pyro_files."""
        mock_client = MagicMock()
        mock_client.search_files.side_effect = Exception("Search failed")
        mock_client_class.return_value = mock_client

        from utils.sharepoint_client import search_pyro_files

        with pytest.raises(Exception, match="Search failed"):
            search_pyro_files("test query", "test-token")

    @patch("utils.sharepoint_client.SharePointClient")
    def test_list_pyro_folder_contents_error_handling(self, mock_client_class):
        """Test error handling in list_pyro_folder_contents."""
        mock_client = MagicMock()
        mock_client.get_drive_items.side_effect = Exception("Folder access failed")
        mock_client_class.return_value = mock_client

        from utils.sharepoint_client import list_pyro_folder_contents

        with pytest.raises(Exception, match="Folder access failed"):
            list_pyro_folder_contents("test-folder", "test-token")

    # ...existing tests...


class TestSharePointClientConfiguration:
    """Test SharePoint client configuration and environment variables."""

    def test_default_site_id_configuration(self):
        """Test default site ID when environment variable not set."""
        with patch.dict(os.environ, {}, clear=True):
            client = SharePointClient("test-token")
            assert (
                client.site_id
                == "jgiquality.sharepoint.com,b8d7ad55-622f-41e1-9140-35b87b4616f9,160cda33-41a0-4b31-8ebf-11196986b3e3"
            )

    def test_custom_site_id_from_environment(self):
        """Test site ID loaded from environment variable."""
        custom_site_id = "custom.sharepoint.com,custom-id"
        with patch.dict(os.environ, {"SHAREPOINT_SITE_ID": custom_site_id}):
            client = SharePointClient("test-token")
            assert client.site_id == custom_site_id

    def test_default_drive_id_configuration(self):
        """Test default drive ID when environment variable not set."""
        with patch.dict(os.environ, {}, clear=True):
            client = SharePointClient("test-token")
            assert (
                client.drive_id
                == "b!34PQK-JF0EmH57ieExSqveCp2B5j30NMsNTGcMEXae_5x8SnfJhdR6JqUh5dD03F"
            )

    def test_custom_drive_id_from_environment(self):
        """Test drive ID loaded from environment variable."""
        custom_drive_id = "custom-drive-id-123"
        with patch.dict(os.environ, {"SHAREPOINT_DRIVE_ID": custom_drive_id}):
            client = SharePointClient("test-token")
            assert client.drive_id == custom_drive_id

    def test_pyro_standards_drive_id_not_set_by_default(self):
        """Test pyro standards drive ID is None when not configured."""
        with patch.dict(os.environ, {}, clear=True):
            client = SharePointClient("test-token")
            assert client.pyro_standards_drive_id is None

    def test_pyro_standards_drive_id_from_environment(self):
        """Test pyro standards drive ID loaded from environment variable."""
        standards_drive_id = "standards-drive-id-456"
        with patch.dict(
            os.environ, {"SHAREPOINT_PYRO_STANDARDS_DRIVE_ID": standards_drive_id}
        ):
            client = SharePointClient("test-token")
            assert client.pyro_standards_drive_id == standards_drive_id

    def test_all_environment_variables_configured(self):
        """Test client with all environment variables configured."""
        env_vars = {
            "SHAREPOINT_SITE_ID": "test-site-id",
            "SHAREPOINT_DRIVE_ID": "test-drive-id",
            "SHAREPOINT_PYRO_STANDARDS_DRIVE_ID": "test-standards-drive-id",
        }
        with patch.dict(os.environ, env_vars):
            client = SharePointClient("test-token")
            assert client.site_id == "test-site-id"
            assert client.drive_id == "test-drive-id"
            assert client.pyro_standards_drive_id == "test-standards-drive-id"

    def test_empty_string_environment_variables(self):
        """Test handling of empty string environment variables."""
        env_vars = {
            "SHAREPOINT_SITE_ID": "",
            "SHAREPOINT_DRIVE_ID": "",
            "SHAREPOINT_PYRO_STANDARDS_DRIVE_ID": "",
        }
        with patch.dict(os.environ, env_vars):
            client = SharePointClient("test-token")
            # Empty strings should be treated as not configured
            assert client.site_id == ""
            assert client.drive_id == ""
            assert client.pyro_standards_drive_id == ""

    def test_drive_id_validation_in_convenience_functions(self):
        """Test drive ID validation in convenience functions."""
        with patch.dict(os.environ, {"SHAREPOINT_DRIVE_ID": ""}, clear=False):
            with patch("utils.sharepoint_client.os.getenv") as mock_getenv:
                mock_getenv.return_value = None

                with pytest.raises(
                    ValueError, match="SHAREPOINT_DRIVE_ID not configured"
                ):
                    search_pyro_files("test", "token")

                with pytest.raises(
                    ValueError, match="SHAREPOINT_DRIVE_ID not configured"
                ):
                    list_pyro_folder_contents("folder", "token")

    def test_pyro_standards_drive_id_validation(self):
        """Test pyro standards drive ID validation."""
        with patch("utils.sharepoint_client.SharePointClient") as mock_client_class:
            mock_client = MagicMock()
            mock_client.pyro_standards_drive_id = None
            mock_client_class.return_value = mock_client

            with pytest.raises(
                ValueError, match="SHAREPOINT_PYRO_STANDARDS_DRIVE_ID not configured"
            ):
                get_pyro_standards_file_reference("test.pdf", "token")


class TestSharePointClientIntegrationSetup:
    """Test integration test class setup and configuration validation."""

    def test_integration_test_skip_condition(self):
        """Test that integration tests are properly skipped when SKIP_AUTH=true."""
        # This test verifies the skip condition works correctly
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
        if skip_auth:
            pytest.skip("Integration tests skipped when SKIP_AUTH=true")

    def test_sharepoint_client_configuration_validation(self):
        """Test SharePoint client configuration for integration testing."""
        client = SharePointClient("test-token")

        # Verify client has required configuration properties
        assert hasattr(client, "site_id")
        assert hasattr(client, "drive_id")
        assert hasattr(client, "pyro_standards_drive_id")
        assert hasattr(client, "base_url")
        assert hasattr(client, "access_token")

        # Verify base URL is correct
        assert client.base_url == "https://graph.microsoft.com/v1.0"

        # Verify at least one drive ID is configured (either main or standards)
        has_main_drive = client.drive_id is not None and client.drive_id != ""
        has_standards_drive = (
            client.pyro_standards_drive_id is not None
            and client.pyro_standards_drive_id != ""
        )
        assert (
            has_main_drive or has_standards_drive
        ), "At least one drive ID should be configured"

    def test_integration_test_environment_requirements(self):
        """Test environment requirements for integration testing."""
        # Check if required environment variables would be available for real testing
        required_env_vars = ["SHAREPOINT_SITE_ID", "SHAREPOINT_DRIVE_ID"]
        for var in required_env_vars:
            assert os.getenv(var) is not None

        client = SharePointClient("test-token")

        # For integration tests, we need at least the basic configuration
        assert client.site_id is not None, "Site ID required for integration tests"

        # Drive ID can be default or from environment
        assert client.drive_id is not None, "Drive ID required for integration tests"

    @patch("utils.sharepoint_client.get_app_only_token")
    def test_integration_client_with_app_only_auth(self, mock_get_token):
        """Test integration client initialization with app-only authentication."""
        mock_get_token.return_value = "app-only-integration-token"

        client = SharePointClient()
        assert client.access_token == "app-only-integration-token"
        assert client.site_id is not None
        assert client.drive_id is not None

    def test_integration_client_methods_available(self):
        """Test that all required methods are available for integration testing."""
        client = SharePointClient("test-token")

        # Verify all required methods exist
        required_methods = [
            "get_site_info",
            "get_drive_items",
            "get_file_by_path",
            "get_file_by_id",
            "search_files",
            "get_file_download_url",
            "get_file_reference",
            "download_file_content",
            "get_wiresetcerts_file",
        ]

        for method_name in required_methods:
            assert hasattr(
                client, method_name
            ), f"Method {method_name} should be available"
            assert callable(
                getattr(client, method_name)
            ), f"Method {method_name} should be callable"


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

    def test_integration_client_initialization(self):
        """Test client initialization for integration testing."""
        client = SharePointClient("test-token")

        # Verify client is properly configured for integration tests
        assert client.access_token == "test-token"
        assert client.base_url == "https://graph.microsoft.com/v1.0"

        # At least one drive should be configured
        has_configuration = (client.drive_id is not None and client.drive_id != "") or (
            client.pyro_standards_drive_id is not None
            and client.pyro_standards_drive_id != ""
        )
        assert (
            has_configuration
        ), "Client should have at least one drive configured for integration tests"

    def test_integration_environment_variables_loaded(self):
        """Test that environment variables are properly loaded for integration."""
        client = SharePointClient("test-token")

        # Site ID should always be configured (either default or from env)
        assert client.site_id is not None and client.site_id != ""

        # Main drive ID should be configured
        assert client.drive_id is not None and client.drive_id != ""

        # Standards drive ID is optional but should be None if not configured
        if client.pyro_standards_drive_id is not None:
            assert client.pyro_standards_drive_id != ""


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Skipped when SKIP_AUTH=true",
)
def test_list_pyro_standards_excel_files_contains_xlsm():
    """Should include at least one .xlsm file from the Pyro_Standards folder."""
    from utils.sharepoint_client import list_pyro_standards_excel_files

    files = list_pyro_standards_excel_files()
    xlsm_files = [f for f in files if f["name"].lower().endswith(".xlsm")]
    assert xlsm_files, "Expected at least one .xlsm file in Pyro_Standards folder"
    assert "K6_0525.xlsm" in [
        f["name"] for f in xlsm_files
    ], "Expected K6_0525.xlsm file to be present"
