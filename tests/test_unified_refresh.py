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
        mock_client.list_files_in_pyro_standards_folder.return_value = [
            {"name": "072513A.xls", "lastModifiedDateTime": iso_now},  # wire cert
            {"name": "J1_0625.xlsm", "lastModifiedDateTime": iso_now},  # daqbook
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
        mock_wiresetcerts.return_value = {"records_processed": 1}
        mock_daqbook.return_value = {}

        result = refresh_all_updated_categories()

        assert "wiresetcerts" in result["categories_updated"]
        assert "daqbookoffsets" in result["categories_updated"]
        assert "wireoffsets" not in result["categories_updated"]
        assert result["summary"]["total_files_processed"] == 2
