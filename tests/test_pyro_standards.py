# tests/test_pyro_standards.py
"""Tests for Pyro Standards Excel file API endpoint."""

import hashlib
import os
from unittest.mock import MagicMock, patch

import pytest

from utils.sharepoint_client import get_pyro_standards_excel_file


class TestPyroStandardsSharePointClient:
    """Test Pyro Standards SharePoint client functionality."""

    @pytest.mark.parametrize(
        "filename, expected_hash",
        [
            ("J1_0325.xlsm", "dd25e82ad2a1135786fd2695ce9e8b3d"),
            ("K6_0525.xlsm", "089ba1223980c29c76543ba669dff0ab"),
            ("K6_0225.xlsm", "8f37d6fd46d1429aef03a2f19b127795"),
        ],
        ids=[
            "J1_0325.xlsm",
            "K6_0525.xlsm",
            "K6_0225.xlsm",
        ],
    )
    @pytest.mark.skipif(
        os.getenv("SKIP_AUTH", "false").lower() == "true",
        reason="Skipping tests when SKIP_AUTH is set (CI environment)",
    )
    def test_get_pyro_standards_excel_file_search_fallback(
        self, filename, expected_hash
    ):
        """Test fallback to search when direct path fails."""
        result = get_pyro_standards_excel_file(filename)
        assert list(result.keys()) == [
            "sheet_names",
            "total_sheets",
            "sheets",
            "file_info",
        ]
        result_hash = hashlib.md5(result["file_info"]["name"].encode()).hexdigest()
        assert (
            result_hash == expected_hash
        ), "File name hash does not match expected value."

    @patch("utils.sharepoint_client.SharePointClient")
    def test_get_pyro_standards_excel_file_not_found(self, mock_client_class):
        """Test error when file is not found."""
        mock_client = MagicMock()
        mock_client.drive_id = "test-drive-id"
        mock_client_class.return_value = mock_client

        # Make direct path fail
        mock_client.get_file_reference.side_effect = Exception("Path not found")

        # Make search return empty results
        mock_client.search_files.return_value = []

        with pytest.raises(ValueError, match="file not found"):
            get_pyro_standards_excel_file("NonExistent.xlsx")
