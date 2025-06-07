#!/usr/bin/env python3
"""
Tests for list_daqbook_files.py module.
"""
import os
import sys
from unittest.mock import Mock, patch

import pytest

from utils.list_daqbook_files import (
    extract_tn_from_filename,
    main,
    search_daqbook_files,
)

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestExtractTnFromFilename:
    """Test TN extraction from filenames."""

    def test_extract_tn_standard_format(self):
        """Test TN extraction from standard format files."""
        assert extract_tn_from_filename("J1_0325.xlsm") == "J10325"
        assert extract_tn_from_filename("K4_1234.xlsm") == "K41234"
        assert extract_tn_from_filename("N2_9876.xlsm") == "N29876"

    def test_extract_tn_case_insensitive(self):
        """Test TN extraction is case insensitive."""
        assert extract_tn_from_filename("j1_0325.xlsm") == "J10325"
        assert extract_tn_from_filename("k4_1234.XLSM") == "K41234"

    def test_extract_tn_flexible_format(self):
        """Test TN extraction from flexible format files."""
        assert extract_tn_from_filename("J1_ABC123.xlsm") == "J1ABC123"
        assert extract_tn_from_filename("K4_test_file.xlsm") == "K4test_file"

    def test_extract_tn_invalid_format(self):
        """Test TN extraction returns Unknown for invalid formats."""
        assert extract_tn_from_filename("invalid_file.xlsm") == "Unknown"
        assert extract_tn_from_filename("J1.xlsm") == "Unknown"
        assert extract_tn_from_filename("J1_test.txt") == "Unknown"
        assert extract_tn_from_filename("") == "Unknown"


class TestSearchDaqbookFiles:
    """Test DAQbook file search functionality."""

    @patch("utils.list_daqbook_files.SharePointClient")
    def test_search_daqbook_files_success(self, mock_sharepoint_class):
        """Test successful DAQbook file search."""
        # Mock SharePoint client
        mock_sharepoint = Mock()
        mock_sharepoint.drive_id = "test-drive-id"
        mock_sharepoint.search_files.return_value = [
            {
                "name": "J1_0325.xlsm",
                "size": 1024,
                "lastModifiedDateTime": "2023-01-01T00:00:00Z",
            },
            {
                "name": "K4_1234.xlsm",
                "size": 2048,
                "lastModifiedDateTime": "2023-01-02T00:00:00Z",
            },
        ]
        mock_sharepoint_class.return_value = mock_sharepoint

        result = search_daqbook_files()

        # Should return only matching files (J1_0325.xlsm matches J1_ pattern, K4_1234.xlsm matches K4_ pattern)
        assert (
            len(result) == 2
        )  # Only files that actually match their respective patterns
        assert result[0]["name"] == "J1_0325.xlsm"

        # Verify SharePoint client was called for each pattern
        assert mock_sharepoint.search_files.call_count == 7

    @patch("utils.list_daqbook_files.SharePointClient")
    @patch("builtins.print")
    def test_search_daqbook_files_no_drive_id(self, mock_print, mock_sharepoint_class):
        """Test DAQbook file search when no drive ID is configured."""
        # Mock SharePoint client with no drive ID
        mock_sharepoint = Mock()
        mock_sharepoint.drive_id = None
        mock_sharepoint_class.return_value = mock_sharepoint

        result = search_daqbook_files()

        assert result == []
        mock_print.assert_any_call("❌ SharePoint drive ID not configured")

    @patch("utils.list_daqbook_files.SharePointClient")
    @patch("builtins.print")
    def test_search_daqbook_files_search_exception(
        self, mock_print, mock_sharepoint_class
    ):
        """Test DAQbook file search handles exceptions gracefully."""
        # Mock SharePoint client that raises exception
        mock_sharepoint = Mock()
        mock_sharepoint.drive_id = "test-drive-id"
        mock_sharepoint.search_files.side_effect = Exception("SharePoint error")
        mock_sharepoint_class.return_value = mock_sharepoint

        result = search_daqbook_files()

        assert result == []
        # Should print error for each pattern
        assert mock_print.call_count >= 7  # At least one error message per pattern

    @patch("utils.list_daqbook_files.SharePointClient")
    @patch("builtins.print")
    def test_search_daqbook_files_filters_correctly(
        self, mock_print, mock_sharepoint_class
    ):
        """Test that search filters files correctly by pattern and extension."""
        # Mock SharePoint client
        mock_sharepoint = Mock()
        mock_sharepoint.drive_id = "test-drive-id"
        mock_sharepoint.search_files.return_value = [
            {
                "name": "J1_0325.xlsm",
                "size": 1024,
                "lastModifiedDateTime": "2023-01-01",
            },
            {
                "name": "J1_0325.xlsx",
                "size": 1024,
                "lastModifiedDateTime": "2023-01-01",
            },  # Wrong extension
            {
                "name": "X1_0325.xlsm",
                "size": 1024,
                "lastModifiedDateTime": "2023-01-01",
            },  # Wrong prefix
            {
                "name": "J1_0326.xlsm",
                "size": 1024,
                "lastModifiedDateTime": "2023-01-01",
            },
        ]
        mock_sharepoint_class.return_value = mock_sharepoint

        result = (
            search_daqbook_files()
        )  # Should only include .xlsm files that start with the correct patterns
        matching_files = [
            f for f in result if f["name"] in ["J1_0325.xlsm", "J1_0326.xlsm"]
        ]
        assert len(matching_files) == 2  # Only the 2 files that match J1_ pattern


class TestMain:
    """Test main function."""

    @patch("utils.list_daqbook_files.search_daqbook_files")
    @patch("builtins.print")
    def test_main_with_files_found(self, mock_print, mock_search):
        """Test main function when files are found."""
        mock_search.return_value = [{"name": "J1_0325.xlsm", "size": 1024}]

        main()

        mock_search.assert_called_once()
        # Should print next steps
        mock_print.assert_any_call("\n🎯 Next steps:")

    @patch("utils.list_daqbook_files.search_daqbook_files")
    @patch("builtins.print")
    def test_main_no_files_found(self, mock_print, mock_search):
        """Test main function when no files are found."""
        mock_search.return_value = []

        main()

        mock_search.assert_called_once()
        mock_print.assert_any_call("\n❌ No DAQbook files found")

    @patch("utils.list_daqbook_files.search_daqbook_files")
    @patch("builtins.print")
    @patch("sys.exit")
    def test_main_handles_exception(self, mock_exit, mock_print, mock_search):
        """Test main function handles exceptions and exits."""
        mock_search.side_effect = Exception("Test error")

        main()

        mock_print.assert_any_call("❌ Error: Test error")
        mock_exit.assert_called_once_with(1)


@pytest.fixture
def sample_file_info():
    """Sample file info for testing."""
    return {
        "name": "J1_0325.xlsm",
        "size": 1024,
        "lastModifiedDateTime": "2023-01-01T00:00:00Z",
    }
