# tests/test_unified_refresh.py
"""
Tests for the unified refresh system.
"""

from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

from utils.unified_refresh import (
    get_file_categories_with_updates,
    refresh_all_updated_categories,
)


class TestUnifiedRefreshPipeline:

    @patch("utils.unified_refresh.SharePointClient")
    def test_get_file_categories_with_updates_detects_all_categories(
        self, mock_client_cls
    ):
        mock_client = MagicMock()
        now = datetime.utcnow()
        iso_now = now.isoformat()

        mock_client.get_wiresetcerts_file.return_value = {
            "name": "WireSetCerts.xlsx",
            "lastModifiedDateTime": iso_now,
            "id": "abc123",
        }

        # Create mock objects with .name and .lastModifiedDateTime attributes
        mock_wire_file = MagicMock()
        mock_wire_file.name = "072513A.xls"
        mock_wire_file.lastModifiedDateTime = iso_now

        mock_daqbook_file = MagicMock()
        mock_daqbook_file.name = "J1_0625.xlsm"
        mock_daqbook_file.lastModifiedDateTime = iso_now

        mock_client.list_files_in_pyro_standards_folder.return_value = [
            mock_wire_file,  # wire cert
            mock_daqbook_file,  # daqbook
        ]
        mock_client_cls.return_value = mock_client

        result = get_file_categories_with_updates(last_checked=now - timedelta(days=1))

        assert result["wiresetcerts"]["has_updates"] is True
        assert result["wireoffsets"]["has_updates"] is True
        assert result["daqbookoffsets"]["has_updates"] is True
        assert len(result["wireoffsets"]["files"]) == 1
        assert len(result["daqbookoffsets"]["files"]) == 1

    @patch("utils.unified_refresh.refresh_wire_set_certs")
    @patch("utils.unified_refresh.refresh_wire_offsets")
    @patch("utils.unified_refresh.refresh_daqbook_offsets")
    @patch("utils.unified_refresh.get_file_categories_with_updates")
    def test_refresh_all_updated_categories_executes_only_for_updates(
        self, mock_get_updates, mock_daqbook, mock_wire_offsets, mock_wiresetcerts
    ):
        now = datetime.utcnow()
        mock_get_updates.return_value = {
            "wiresetcerts": {
                "has_updates": True,
                "files": [{"name": "WireSetCerts.xlsx"}],
            },
            "wireoffsets": {"has_updates": False, "files": []},
            "daqbookoffsets": {
                "has_updates": True,
                "files": [{"name": "J1_0625.xlsm"}],
            },
            "last_checked": now.isoformat(),
        }
        # Create mock objects with attributes instead of dictionaries
        mock_wiresetcerts_result = MagicMock()
        mock_wiresetcerts_result.records_processed = 1
        mock_wiresetcerts.return_value = mock_wiresetcerts_result

        mock_daqbook_result = MagicMock()
        mock_daqbook_result.files_processed = 1
        mock_daqbook.return_value = mock_daqbook_result

        result = refresh_all_updated_categories()

        assert "wiresetcerts" in result["categories_updated"]
        assert "daqbookoffsets" in result["categories_updated"]
        assert "wireoffsets" not in result["categories_updated"]
        assert result["summary"]["total_files_processed"] == 2
