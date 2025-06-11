# tests/test_unified_refresh.py
"""
Tests for the unified refresh system.
"""

from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

from utils.schemas import FileCategory, FileCategoryUpdateResultSet
from utils.unified_refresh import (
    get_file_categories_with_updates,
    refresh_all_updated_categories,
)


class TestUnifiedRefreshPipeline:
    @patch("utils.unified_refresh.get_wiresetcerts_file")
    @patch("utils.unified_refresh.get_pyro_standards_files")
    def test_get_file_categories_with_updates_detects_all_categories(
        self, mock_get_pyro_files, mock_get_wiresetcerts
    ):
        # Use timezone-naive datetime to match unified_refresh behavior
        now = datetime.now()
        last_checked = now - timedelta(days=1)

        # Mock WireSetCerts file
        mock_wiresetcerts_file = MagicMock()
        mock_wiresetcerts_file.time_last_modified = now
        mock_get_wiresetcerts.return_value = mock_wiresetcerts_file

        # Create mock files with .name and .time_last_modified attributes (timezone-naive)
        mock_wire_file = MagicMock()
        mock_wire_file.name = "072513A.xls"
        mock_wire_file.time_last_modified = now

        mock_daqbook_file = MagicMock()
        mock_daqbook_file.name = "J1_0625.xlsm"
        mock_daqbook_file.time_last_modified = now

        mock_get_pyro_files.return_value = [
            mock_wire_file,  # wire cert
            mock_daqbook_file,  # daqbook
        ]

        result = get_file_categories_with_updates(last_checked=last_checked)

        assert result.wiresetcerts.has_updates is True
        assert result.wireoffsets.has_updates is True
        assert result.daqbookoffsets.has_updates is True
        assert len(result.wireoffsets.files) == 1
        assert len(result.daqbookoffsets.files) == 1

    @patch("utils.unified_refresh.refresh_wire_set_certs")
    @patch("utils.unified_refresh.refresh_wire_offsets")
    @patch("utils.unified_refresh.refresh_daqbook_offsets")
    @patch("utils.unified_refresh.get_file_categories_with_updates")
    def test_refresh_all_updated_categories_executes_only_for_updates(
        self, mock_get_updates, mock_daqbook, mock_wire_offsets, mock_wiresetcerts
    ):
        now = datetime.now(timezone.utc)

        # Create mock File objects
        mock_wiresetcerts_file = MagicMock()
        mock_wiresetcerts_file.name = "WireSetCerts.xlsx"

        mock_daqbook_file = MagicMock()
        mock_daqbook_file.name = "J1_0625.xlsm"

        # Mock the return value as a proper FileCategoryUpdateResultSet object
        mock_update_result = FileCategoryUpdateResultSet(
            wiresetcerts=FileCategory(has_updates=True, files=[mock_wiresetcerts_file]),
            wireoffsets=FileCategory(has_updates=False, files=[]),
            daqbookoffsets=FileCategory(has_updates=True, files=[mock_daqbook_file]),
            last_checked=now,
        )
        mock_get_updates.return_value = mock_update_result

        # Create mock objects with attributes instead of dictionaries
        mock_wiresetcerts_result = MagicMock()
        mock_wiresetcerts_result.records_processed = 1
        mock_wiresetcerts.return_value = mock_wiresetcerts_result

        mock_daqbook_result = MagicMock()
        mock_daqbook_result.files_processed = 1
        mock_daqbook.return_value = mock_daqbook_result

        result = refresh_all_updated_categories()

        assert "wiresetcerts" in result.categories_updated
        assert "daqbookoffsets" in result.categories_updated
        assert "wireoffsets" not in result.categories_updated
        assert result.summary.total_files_processed == 2
