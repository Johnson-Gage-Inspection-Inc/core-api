import os
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder

from integrations.sharepoint.client import Office365SharePointClient


class TestOffice365SharePointClient:
    def test_init(self):
        """Test client initialization with default values."""
        client = Office365SharePointClient()
        assert client.site_url == "https://jgiquality.sharepoint.com/sites/JGI"
        assert client.auth_method == "app_only"
        assert client._context is None

    def test_init_custom_values(self):
        """Test client initialization with custom values."""
        client = Office365SharePointClient(
            site_url="https://custom.sharepoint.com/sites/Custom",
            auth_method="user_credential",
        )
        assert client.site_url == "https://custom.sharepoint.com/sites/Custom"
        assert client.auth_method == "user_credential"
        assert client._context is None

    @patch.dict(
        os.environ, {"AZURE_CLIENT_ID": "test_id", "AZURE_CLIENT_SECRET": "test_secret"}
    )
    @patch("integrations.sharepoint.client.ClientCredential")
    @patch("integrations.sharepoint.client.ClientContext")
    def test_get_app_context(self, mock_client_context, mock_client_credential):
        """Test getting app context with valid credentials."""
        mock_context = MagicMock()
        mock_client_context.return_value.with_credentials.return_value = mock_context

        client = Office365SharePointClient()
        context = client._get_app_context()

        mock_client_credential.assert_called_once_with("test_id", "test_secret")
        mock_client_context.assert_called_once_with(client.site_url)
        mock_client_context.return_value.with_credentials.assert_called_once()
        assert context == mock_context

    @patch.dict(os.environ, {"AZURE_CLIENT_ID": "", "AZURE_CLIENT_SECRET": ""})
    def test_get_app_context_missing_credentials(self):
        """Test getting app context with missing credentials."""
        client = Office365SharePointClient()
        with pytest.raises(ValueError, match="Missing Azure app credentials"):
            client._get_app_context()

    def test_get_context_not_implemented(self):
        """Test getting context with unsupported auth method."""
        client = Office365SharePointClient(auth_method="user_credential")
        with pytest.raises(
            NotImplementedError, match="User credential auth not implemented yet"
        ):
            client._get_context()

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_app_context")
    def test_get_context_caching(self, mock_get_app_context):
        """Test context caching behavior."""
        mock_context = MagicMock()
        mock_get_app_context.return_value = mock_context

        client = Office365SharePointClient()
        context1 = client._get_context()
        context2 = client._get_context()

        assert context1 == mock_context
        assert context2 == mock_context
        mock_get_app_context.assert_called_once()  # Should only be called once due to caching

    def test_execute_query_with_error_handling_success(self):
        """Test successful query execution."""
        mock_context = MagicMock()

        client = Office365SharePointClient()
        client._execute_query_with_error_handling(mock_context)

        mock_context.execute_query.assert_called_once()

    def test_execute_query_with_error_handling_404(self):
        """Test error handling for 404 errors."""
        mock_context = MagicMock()
        mock_context.execute_query.side_effect = Exception("404 Not Found")

        client = Office365SharePointClient()
        with pytest.raises(FileNotFoundError, match="SharePoint resource not found"):
            client._execute_query_with_error_handling(mock_context)

    def test_execute_query_with_error_handling_403(self):
        """Test error handling for 403 errors."""
        mock_context = MagicMock()
        mock_context.execute_query.side_effect = Exception("403 Forbidden")

        client = Office365SharePointClient()
        with pytest.raises(
            PermissionError, match="Access denied to SharePoint resource"
        ):
            client._execute_query_with_error_handling(mock_context)

    def test_execute_query_with_error_handling_other(self):
        """Test error handling for other errors."""
        mock_context = MagicMock()
        mock_context.execute_query.side_effect = Exception("Some other error")

        client = Office365SharePointClient()
        with pytest.raises(RuntimeError, match="SharePoint operation failed"):
            client._execute_query_with_error_handling(mock_context)

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_get_file_by_url_success(self, mock_execute_query, mock_get_context):
        """Test getting a file by URL successfully."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_file = MagicMock(spec=File)
        mock_file.exists = True
        mock_context.web.get_file_by_server_relative_url.return_value = mock_file

        client = Office365SharePointClient()
        result = client.get_file_by_url("/test/path/file.txt")

        mock_get_context.assert_called_once()
        mock_context.web.get_file_by_server_relative_url.assert_called_once_with(
            "/test/path/file.txt"
        )
        mock_context.load.assert_called_once_with(mock_file)
        mock_execute_query.assert_called_once_with(mock_context)
        assert result == mock_file

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_get_file_by_url_not_exists(self, mock_execute_query, mock_get_context):
        """Test getting a file by URL that doesn't exist."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_file = MagicMock(spec=File)
        mock_file.exists = False
        mock_context.web.get_file_by_server_relative_url.return_value = mock_file

        client = Office365SharePointClient()
        with pytest.raises(FileNotFoundError, match="File not found"):
            client.get_file_by_url("/test/path/file.txt")

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_search_files_with_folder_path(self, mock_execute_query, mock_get_context):
        """Test searching files with a folder path."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_folder = MagicMock()
        mock_context.web.get_folder_by_server_relative_url.return_value = mock_folder

        mock_file1 = MagicMock(spec=File)
        mock_file1.name = "test_file.txt"
        mock_file2 = MagicMock(spec=File)
        mock_file2.name = "other_file.txt"
        mock_folder.files = [mock_file1, mock_file2]

        client = Office365SharePointClient()
        results = client.search_files("test", Path("/test/folder"))

        mock_get_context.assert_called_once()
        mock_context.web.get_folder_by_server_relative_url.assert_called_once_with(
            Path("/test/folder")
        )
        mock_context.load.assert_any_call(mock_folder)
        mock_context.load.assert_any_call(mock_folder.files)
        assert (
            mock_execute_query.call_count >= 2
        )  # At least twice: once for folder, once for file
        assert len(results) == 1
        assert results[0] == mock_file1

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_search_files_without_folder_path(
        self, mock_execute_query, mock_get_context
    ):
        """Test searching files without a folder path."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_list = MagicMock()
        mock_context.web.lists.get_by_title.return_value = mock_list

        mock_file1 = MagicMock(spec=File)
        mock_file1.name = "test_file.txt"
        mock_file2 = MagicMock(spec=File)
        mock_file2.name = "other_file.txt"
        mock_list.root_folder.files = [mock_file1, mock_file2]

        client = Office365SharePointClient()
        results = client.search_files("test")

        mock_get_context.assert_called_once()
        mock_context.web.lists.get_by_title.assert_called_once_with("Documents")
        mock_context.load.assert_any_call(mock_list.root_folder.files)
        assert (
            mock_execute_query.call_count >= 2
        )  # At least twice: once for list, once for file
        assert len(results) == 1
        assert results[0] == mock_file1

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_get_folder_contents(self, mock_execute_query, mock_get_context):
        """Test getting folder contents."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_folder = MagicMock()
        mock_context.web.get_folder_by_server_relative_url.return_value = mock_folder

        mock_file = MagicMock(spec=File)
        mock_subfolder = MagicMock(spec=Folder)
        mock_folder.files = [mock_file]
        mock_folder.folders = [mock_subfolder]

        client = Office365SharePointClient()
        files, folders = client.get_folder_contents(Path("/test/folder"))

        mock_get_context.assert_called_once()
        mock_context.web.get_folder_by_server_relative_url.assert_called_once_with(
            Path("/test/folder")
        )
        mock_context.load.assert_any_call(mock_folder)
        mock_context.load.assert_any_call(mock_folder.files)
        mock_context.load.assert_any_call(mock_folder.folders)
        assert (
            mock_execute_query.call_count >= 3
        )  # At least 3 times: folder, file, subfolder
        assert len(files) == 1
        assert len(folders) == 1
        assert files[0] == mock_file
        assert folders[0] == mock_subfolder

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    def test_download_file_content(self, mock_execute_query, mock_get_context):
        """Test downloading file content."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_file = MagicMock()
        mock_context.web.get_file_by_server_relative_url.return_value = mock_file

        mock_content_result = MagicMock()
        mock_content_result.value = b"test content"
        mock_file.get_content.return_value = mock_content_result

        client = Office365SharePointClient()
        content = client.download_file_content("/test/path/file.txt")

        mock_get_context.assert_called_once()
        mock_context.web.get_file_by_server_relative_url.assert_called_once_with(
            "/test/path/file.txt"
        )
        mock_file.get_content.assert_called_once()
        mock_execute_query.assert_called_once_with(mock_context)
        assert content == b"test content"

    @patch(
        "integrations.sharepoint.client.Office365SharePointClient.download_file_content"
    )
    @patch("builtins.open", new_callable=mock_open)
    def test_download_file_to_path(self, mock_file_open, mock_download_content):
        """Test downloading file to a local path."""
        mock_download_content.return_value = b"test content"

        client = Office365SharePointClient()
        client.download_file_to_path(
            "/test/path/file.txt", Path("/local/path/file.txt")
        )

        mock_download_content.assert_called_once_with("/test/path/file.txt")
        mock_file_open.assert_called_once_with(Path("/local/path/file.txt"), "wb")
        mock_file_open().write.assert_called_once_with(b"test content")

    @patch("integrations.sharepoint.client.Office365SharePointClient._get_context")
    @patch(
        "integrations.sharepoint.client.Office365SharePointClient._execute_query_with_error_handling"
    )
    @patch("builtins.open", new_callable=mock_open, read_data=b"test content")
    def test_upload_file(self, mock_file_open, mock_execute_query, mock_get_context):
        """Test uploading a file."""
        mock_context = MagicMock()
        mock_get_context.return_value = mock_context

        mock_folder = MagicMock()
        mock_context.web.get_folder_by_server_relative_url.return_value = mock_folder

        mock_uploaded_file = MagicMock(spec=File)
        mock_folder.files.upload.return_value = mock_uploaded_file

        client = Office365SharePointClient()
        result = client.upload_file(
            Path("/local/path/file.txt"), "/target/folder", "custom_name.txt"
        )
        assert result == mock_uploaded_file

        mock_get_context.assert_called_once()
        mock_context.web.get_folder_by_server_relative_url.assert_called_once_with(
            "/target/folder"
        )
        mock_file_open.assert_called_once_with(Path("/local/path/file.txt"), "rb")
        mock_folder.files.upload.assert_called_once()
        assert mock_execute_query.call_count
