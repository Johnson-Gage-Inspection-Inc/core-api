# tests/test_pyro_standards.py
"""Tests for Pyro Standards Excel file API endpoint."""

import os
import pytest
from unittest.mock import patch, MagicMock

from utils.sharepoint_client import get_pyro_standards_excel_file


class TestPyroStandardsSharePointClient:
    """Test Pyro Standards SharePoint client functionality."""

    def test_get_pyro_standards_excel_file_search_fallback(self):
        """Test fallback to search when direct path fails."""
        result = get_pyro_standards_excel_file("K6_0824.xlsm")
        assert result

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
