# tests/test_unified_refresh_comprehensive.py
"""
Comprehensive tests for the unified refresh system.
"""

from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

from utils.schemas import (
    FileCategory,
    FileCategoryUpdateResultSet,
    RefreshSummary,
    SharePointFileInfo,
    UnifiedRefreshResult,
)
from utils.unified_refresh import (
    get_file_categories_with_updates,
    log_refresh_result,
    refresh_all_updated_categories,
)


class TestGetFileCategoriesWithUpdates:
    """Test the file categorization and update detection logic."""

    def test_no_updates_within_timeframe(self):
        """Test when no files have been updated recently."""
        old_datetime = datetime.now() - timedelta(days=2)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock WireSetCerts.xlsx as old
            mock_instance.get_wiresetcerts_file.return_value = SharePointFileInfo(
                name="WireSetCerts.xlsx",
                lastModifiedDateTime=old_datetime.isoformat(),
                id="test-id",
                webUrl="https://example.com/wiresetcerts.xlsx",
                size=12345,
                downloadUrl="https://example.com/download",
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                driveId="test-drive-id",
                path="/Pyro_Standards/WireSetCerts.xlsx",
            )

            # Mock empty Pyro_Standards folder
            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result: FileCategoryUpdateResultSet = get_file_categories_with_updates()

            assert not result.wiresetcerts.has_updates
            assert not result.wireoffsets.has_updates
            assert not result.daqbookoffsets.has_updates
            assert len(result.wiresetcerts.files) == 0
            assert len(result.wireoffsets.files) == 0
            assert len(result.daqbookoffsets.files) == 0

    def test_wiresetcerts_has_updates(self):
        """Test when WireSetCerts.xlsx has been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock WireSetCerts.xlsx as recently updated
            mock_instance.get_wiresetcerts_file.return_value = SharePointFileInfo(
                name="WireSetCerts.xlsx",
                lastModifiedDateTime=recent_datetime.isoformat(),
                id="test-id",
                webUrl="https://example.com/wiresetcerts.xlsx",
                size=12345,
                downloadUrl="https://example.com/download",
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                driveId="test-drive-id",
                path="/Pyro_Standards/WireSetCerts.xlsx",
            )

            # Mock empty Pyro_Standards folder
            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates()

            assert result.wiresetcerts.has_updates
            assert len(result.wiresetcerts.files) == 1
            assert result.wiresetcerts.files[0].name == "WireSetCerts.xlsx"

    def test_daqbook_file_updates(self):
        """Test when DAQbook files have been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance  # Mock old WireSetCerts.xlsx
            mock_wiresetcerts_file = MagicMock()
            mock_wiresetcerts_file.name = "WireSetCerts.xlsx"
            mock_wiresetcerts_file.lastModifiedDateTime = (
                datetime.now() - timedelta(days=2)
            ).isoformat()
            mock_wiresetcerts_file.id = "test-id"
            mock_instance.get_wiresetcerts_file.return_value = (
                mock_wiresetcerts_file  # Mock DAQbook files in Pyro_Standards
            )
            mock_daqbook_file1 = SharePointFileInfo(
                id="daqbook-id-1",
                name="J1_0124.xlsm",
                webUrl="https://example.com/file1",
                size=12345,
                lastModifiedDateTime=recent_datetime.isoformat(),
                downloadUrl="https://example.com/download1",
                mimeType="application/vnd.ms-excel.sheet.macroEnabled.12",
                driveId="test-drive",
                path="/Pyro_Standards/J1_0124.xlsm",
            )

            mock_daqbook_file2 = SharePointFileInfo(
                id="daqbook-id-2",
                name="K5_0224.xlsm",
                webUrl="https://example.com/file2",
                size=54321,
                lastModifiedDateTime=recent_datetime.isoformat(),
                downloadUrl="https://example.com/download2",
                mimeType="application/vnd.ms-excel.sheet.macroEnabled.12",
                driveId="test-drive",
                path="/Pyro_Standards/K5_0224.xlsm",
            )

            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                mock_daqbook_file1,
                mock_daqbook_file2,
            ]

            result: FileCategoryUpdateResultSet = get_file_categories_with_updates()

            assert result.daqbookoffsets.has_updates
            assert len(result.daqbookoffsets.files) == 2
            assert (file := result.daqbookoffsets.files[0])
            assert isinstance(file, SharePointFileInfo)
            assert file.name == "J1_0124.xlsm"

    def test_wire_certificate_file_updates(self):
        """Test when wire certificate files have been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance
            # Mock old WireSetCerts.xlsx
            mock_wiresetcerts_file = MagicMock()
            mock_wiresetcerts_file.name = "WireSetCerts.xlsx"
            mock_wiresetcerts_file.lastModifiedDateTime = (
                datetime.now() - timedelta(days=2)
            ).isoformat()
            mock_wiresetcerts_file.id = "test-id"
            mock_instance.get_wiresetcerts_file.return_value = mock_wiresetcerts_file

            # Mock wire certificate files in Pyro_Standards
            mock_wire_file1 = MagicMock()
            mock_wire_file1.name = "123456A.xls"
            mock_wire_file1.lastModifiedDateTime = recent_datetime.isoformat()
            mock_wire_file1.id = "wire-id-1"

            mock_wire_file2 = MagicMock()
            mock_wire_file2.name = "789012B.xls"
            mock_wire_file2.lastModifiedDateTime = recent_datetime.isoformat()
            mock_wire_file2.id = "wire-id-2"
            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                mock_wire_file1,
                mock_wire_file2,
            ]

            result = get_file_categories_with_updates()

            assert result.wireoffsets.has_updates
            assert len(result.wireoffsets.files) == 2
            assert result.wireoffsets.files[0].name == "123456A.xls"

    def test_error_handling_sharepoint_failure(self):
        """Test error handling when SharePoint client fails."""
        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock SharePoint failure
            mock_instance.get_wiresetcerts_file.side_effect = Exception(
                "SharePoint connection failed"
            )
            mock_instance.list_files_in_pyro_standards_folder.side_effect = Exception(
                "SharePoint connection failed"
            )

            result = get_file_categories_with_updates()

            # Should return empty results but not crash
            assert not result.wiresetcerts.has_updates
            assert not result.wireoffsets.has_updates
            assert not result.daqbookoffsets.has_updates

    def test_custom_last_checked_datetime(self):
        """Test using a custom last_checked datetime."""
        custom_datetime = datetime.now() - timedelta(hours=6)
        file_datetime = datetime.now() - timedelta(hours=3)  # After custom datetime

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            mock_instance.get_wiresetcerts_file.return_value = SharePointFileInfo(
                name="WireSetCerts.xlsx",
                lastModifiedDateTime=file_datetime.isoformat(),
                id="test-id",
                webUrl="https://example.com/wiresetcerts.xlsx",
                size=12345,
                downloadUrl="https://example.com/download",
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                driveId="test-drive-id",
                path="/Pyro_Standards/WireSetCerts.xlsx",
            )

            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates(last_checked=custom_datetime)

            assert result.wiresetcerts.has_updates
            assert result.last_checked == custom_datetime

    def test_datetime_parsing_with_z_suffix(self):
        """Test datetime parsing when SharePoint returns Z suffix."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock datetime with Z suffix (common SharePoint format)
            mock_instance.get_wiresetcerts_file.return_value = SharePointFileInfo(
                name="WireSetCerts.xlsx",
                lastModifiedDateTime=recent_datetime.isoformat() + "Z",
                id="test-id",
                webUrl="https://example.com/wiresetcerts.xlsx",
                size=12345,
                downloadUrl="https://example.com/download",
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                driveId="test-drive-id",
                path="/Pyro_Standards/WireSetCerts.xlsx",
            )

            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates()

            # Should successfully parse the datetime
            assert result.wiresetcerts.has_updates

    def test_invalid_filename_patterns_ignored(self):
        """Test that files not matching patterns are ignored."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            mock_instance.get_wiresetcerts_file.return_value = SharePointFileInfo(
                name="WireSetCerts.xlsx",
                lastModifiedDateTime=recent_datetime.isoformat(),
                id="test-id",
                webUrl="https://example.com/wiresetcerts.xlsx",
                size=12345,
                downloadUrl="https://example.com/download",
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                driveId="test-drive-id",
                path="/Pyro_Standards/WireSetCerts.xlsx",
            )

            # Mock files that don't match expected patterns
            # TODO: Create at least one SharePointFileInfo fixture for testing, to DRY this up
            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                SharePointFileInfo(
                    name="random_file.txt",
                    lastModifiedDateTime=recent_datetime.isoformat(),
                    id="random-id",
                    webUrl="https://example.com/random_file.txt",
                    size=12345,
                    downloadUrl="https://example.com/download",
                    mimeType="text/plain",
                    driveId="test-drive-id",
                    path="/Pyro_Standards/random_file.txt",
                ),
                SharePointFileInfo(
                    name="invalid.xlsx",
                    lastModifiedDateTime=recent_datetime.isoformat(),
                    id="invalid-id",
                    webUrl="https://example.com/invalid.xlsx",
                    size=12345,
                    downloadUrl="https://example.com/download",
                    mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    driveId="test-drive-id",
                    path="/Pyro_Standards/invalid.xlsx",
                ),
                SharePointFileInfo(
                    name="J99_0124.xlsm",  # Invalid DAQbook pattern (J99 not valid)
                    lastModifiedDateTime=recent_datetime.isoformat(),
                    id="invalid-daqbook-id",
                    webUrl="https://example.com/J99_0124.xlsm",
                    size=12345,
                    downloadUrl="https://example.com/download",
                    mimeType="application/vnd.ms-excel.sheet.macroEnabled.12",
                    driveId="test-drive-id",
                    path="/Pyro_Standards/J99_0124.xlsm",
                ),
            ]

            result = get_file_categories_with_updates()

            # Should not detect any updates for invalid patterns
            assert not result.wireoffsets.has_updates
            assert not result.daqbookoffsets.has_updates


class TestRefreshAllUpdatedCategories:
    """Test the unified refresh orchestration logic."""

    def test_no_categories_need_updates(self):
        """Test when no categories have file updates."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(has_updates=False, files=[]),
                wireoffsets=FileCategory(has_updates=False, files=[]),
                daqbookoffsets=FileCategory(has_updates=False, files=[]),
                last_checked=datetime.now(),
            )

            with patch("utils.unified_refresh.log_refresh_result") as mock_log:
                result = refresh_all_updated_categories()

                assert result.categories_updated == []
                assert result.summary.categories_with_updates == 0
                assert result.summary.total_files_processed == 0
                assert result.summary_line == "No categories needed updates"
                mock_log.assert_called_once()

    def test_wiresetcerts_refresh_success(self):
        """Test successful WireSetCerts refresh."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="WireSetCerts.xlsx",
                            id="test-id",
                            webUrl="https://example.com/WireSetCerts.xlsx",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/WireSetCerts.xlsx",
                        )
                    ],
                ),
                wireoffsets=FileCategory(has_updates=False, files=[]),
                daqbookoffsets=FileCategory(has_updates=False, files=[]),
                last_checked=datetime.now(),
            )

            with patch("utils.unified_refresh.refresh_wire_set_certs") as mock_refresh:
                # Create a mock WireSetCertResult with records_processed attribute
                mock_result = MagicMock()
                mock_result.records_processed = 1
                mock_refresh.return_value = mock_result

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wiresetcerts" in result.categories_updated
                    assert result.summary.categories_with_updates == 1
                    assert result.summary.total_files_processed == 1
                    assert "wiresetcerts" in result.summary_line
                    mock_refresh.assert_called_once()

    def test_wiresetcerts_refresh_failure(self):
        """Test WireSetCerts refresh failure handling."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="WireSetCerts.xlsx",
                            id="test-id",
                            webUrl="https://example.com/WireSetCerts.xlsx",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/WireSetCerts.xlsx",
                        )
                    ],
                ),
                wireoffsets=FileCategory(has_updates=False, files=[]),
                daqbookoffsets=FileCategory(has_updates=False, files=[]),
                last_checked=datetime.now(),
            )

            with patch("utils.unified_refresh.refresh_wire_set_certs") as mock_refresh:
                mock_refresh.side_effect = Exception("Database connection failed")

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wiresetcerts" not in result.categories_updated
                    assert result.results["wiresetcerts"]["status"] == "error"
                    assert (
                        "Database connection failed"
                        in result.results["wiresetcerts"]["message"]
                    )

    def test_daqbook_refresh_success(self):
        """Test successful DAQbook refresh."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(has_updates=False, files=[]),
                wireoffsets=FileCategory(has_updates=False, files=[]),
                daqbookoffsets=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="J1_0124.xlsm",
                            id="test-id",
                            webUrl="https://example.com/J1_0124.xlsm",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.ms-excel.sheet.macroEnabled.12",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/J1_0124.xlsm",
                        )
                    ],
                ),
                last_checked=datetime.now(),
            )

            with patch("utils.unified_refresh.refresh_daqbook_offsets") as mock_refresh:
                mock_refresh.return_value = {
                    "success": True,
                    "files_processed": 1,
                    "message": "Successfully refreshed DAQbook offsets",
                }

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "daqbookoffsets" in result.categories_updated
                    # DAQbook refresher doesn't take updated_files parameter - it discovers files internally
                    mock_refresh.assert_called_once_with()

    def test_wire_offsets_refresh_success(self):
        """Test successful wire offsets refresh."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(has_updates=False, files=[]),
                wireoffsets=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="123456A.xls",
                            id="test-id",
                            webUrl="https://example.com/123456A.xls",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.ms-excel",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/123456A.xls",
                        )
                    ],
                ),
                daqbookoffsets=FileCategory(has_updates=False, files=[]),
                last_checked=datetime.now(),
            )

            with patch("utils.unified_refresh.refresh_wire_offsets") as mock_refresh:
                mock_refresh.return_value = {
                    "success": True,
                    "files_processed": 1,
                    "message": "Successfully refreshed wire offsets",
                }

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wireoffsets" in result.categories_updated
                    # Check that the function was called with the correct files
                    mock_refresh.assert_called_once()
                    called_args = mock_refresh.call_args
                    assert "updated_files" in called_args.kwargs
                    assert len(called_args.kwargs["updated_files"]) == 1
                    assert called_args.kwargs["updated_files"][0].name == "123456A.xls"

    def test_multiple_categories_refresh(self):
        """Test refreshing multiple categories simultaneously."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="WireSetCerts.xlsx",
                            id="test-id",
                            webUrl="https://example.com/WireSetCerts.xlsx",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/WireSetCerts.xlsx",
                        )
                    ],
                ),
                wireoffsets=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="123456A.xls",
                            id="test-id",
                            webUrl="https://example.com/123456A.xls",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.ms-excel",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/123456A.xls",
                        )
                    ],
                ),
                daqbookoffsets=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="J1_0124.xlsm",
                            id="test-id",
                            webUrl="https://example.com/J1_0124.xlsm",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.ms-excel.sheet.macroEnabled.12",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/J1_0124.xlsm",
                        )
                    ],
                ),
                last_checked=datetime.now(),
            )

            with patch(
                "utils.unified_refresh.refresh_wire_set_certs"
            ) as mock_refresh_wire_set:
                mock_result = MagicMock()
                mock_result.records_processed = 1
                mock_refresh_wire_set.return_value = mock_result

                with patch(
                    "utils.unified_refresh.refresh_wire_offsets"
                ) as mock_refresh_wire:
                    mock_refresh_wire.return_value = {
                        "success": True,
                        "files_processed": 1,
                    }

                    with patch(
                        "utils.unified_refresh.refresh_daqbook_offsets"
                    ) as mock_refresh_daqbook:
                        mock_refresh_daqbook.return_value = {
                            "success": True,
                            "files_processed": 1,
                        }

                        with patch("utils.unified_refresh.log_refresh_result"):
                            result = refresh_all_updated_categories()

                            assert len(result.categories_updated) == 3
                            assert "wiresetcerts" in result.categories_updated
                            assert "wireoffsets" in result.categories_updated
                            assert "daqbookoffsets" in result.categories_updated
                            assert result.summary.total_files_processed == 3

    def test_partial_refresh_failures(self):
        """Test when some categories succeed and others fail."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = FileCategoryUpdateResultSet(
                wiresetcerts=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="WireSetCerts.xlsx",
                            id="test-id",
                            webUrl="https://example.com/WireSetCerts.xlsx",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/WireSetCerts.xlsx",
                        )
                    ],
                ),
                wireoffsets=FileCategory(
                    has_updates=True,
                    files=[
                        SharePointFileInfo(
                            name="123456A.xls",
                            id="test-id",
                            webUrl="https://example.com/123456A.xls",
                            size=12345,
                            lastModifiedDateTime=datetime.now().isoformat(),
                            downloadUrl="https://example.com/download",
                            mimeType="application/vnd.ms-excel",
                            driveId="test-drive-id",
                            path="/Pyro_Standards/123456A.xls",
                        )
                    ],
                ),
                daqbookoffsets=FileCategory(has_updates=False, files=[]),
                last_checked=datetime.now(),
            )

            with patch(
                "utils.unified_refresh.refresh_wire_set_certs"
            ) as mock_refresh_wire_set:
                mock_result = MagicMock()
                mock_result.records_processed = 1
                mock_refresh_wire_set.return_value = mock_result

                with patch(
                    "utils.unified_refresh.refresh_wire_offsets"
                ) as mock_refresh_wire:
                    mock_refresh_wire.side_effect = Exception("Wire refresh failed")

                    with patch("utils.unified_refresh.log_refresh_result"):
                        result = refresh_all_updated_categories()

                        # Should have one success and one failure
                        assert "wiresetcerts" in result.categories_updated
                        assert "wireoffsets" not in result.categories_updated
                        assert result.results["wireoffsets"]["status"] == "error"
                        assert (
                            "Wire refresh failed"
                            in result.results["wireoffsets"]["message"]
                        )
                        assert result.summary.total_files_processed == 1


class TestLogRefreshResult:
    """Test the database logging functionality."""

    def test_log_refresh_result_success(self, db_session):
        """Test successful logging of refresh results."""
        result = UnifiedRefreshResult(
            categories_checked=["wiresetcerts", "wireoffsets", "daqbookoffsets"],
            categories_updated=["wiresetcerts", "daqbookoffsets"],
            results={
                "wiresetcerts": {"success": True, "files_processed": 1},
                "daqbookoffsets": {"success": True, "files_processed": 4},
            },
            summary=RefreshSummary(
                total_categories=3,
                categories_with_updates=2,
                total_files_processed=5,
            ),
            last_checked=datetime.now(),
            summary_line="Updated wiresetcerts, daqbookoffsets — 5 files total",
        )
        with patch("utils.database.SessionLocal") as mock_session_local:
            mock_db = MagicMock()
            mock_session_local.return_value = mock_db

            log_refresh_result(result)

            mock_db.add.assert_called_once()
            mock_db.commit.assert_called_once()

            # Verify the logged entry structure
            logged_entry = mock_db.add.call_args[0][0]
            assert logged_entry.total_files_processed == 5
            assert logged_entry.get_categories_updated() == [
                "wiresetcerts",
                "daqbookoffsets",
            ]

    def test_log_refresh_result_database_error(self):
        """Test error handling when database logging fails."""
        result = UnifiedRefreshResult(
            categories_checked=["wiresetcerts", "wireoffsets", "daqbookoffsets"],
            categories_updated=["wiresetcerts"],
            results={"wiresetcerts": {"success": True}},
            summary=RefreshSummary(
                total_categories=3,
                categories_with_updates=1,
                total_files_processed=1,
            ),
            last_checked=datetime.now(),
            summary_line="Updated wiresetcerts — 1 files total",
        )

        with patch("utils.database.SessionLocal") as mock_session_local:
            mock_db = MagicMock()
            mock_session_local.return_value = mock_db
            mock_db.add.side_effect = Exception("Database connection failed")

            # Should not raise an exception
            log_refresh_result(result)

    def test_log_refresh_result_missing_fields(self):
        """Test logging when result has minimal data."""
        result = UnifiedRefreshResult(
            categories_checked=["wiresetcerts", "wireoffsets", "daqbookoffsets"],
            categories_updated=[],
            results={},
            summary=RefreshSummary(
                total_categories=3,
                categories_with_updates=0,
                total_files_processed=0,
            ),
            last_checked=datetime.now(),
            summary_line="No categories needed updates",
        )

        with patch("utils.database.SessionLocal") as mock_session_local:
            mock_db = MagicMock()
            mock_session_local.return_value = mock_db

            log_refresh_result(result)

            # Should handle minimal data gracefully
            logged_entry = mock_db.add.call_args[0][0]
            assert logged_entry.total_files_processed == 0
            assert logged_entry.get_categories_updated() == []


class TestRefreshLogModel:
    """Test the RefreshLog model JSON serialization methods."""

    def test_refresh_log_categories_serialization(self, db_session):
        """Test categories_updated JSON serialization."""
        from db.models import RefreshLog

        log_entry = RefreshLog(total_files_processed=5)
        log_entry.set_categories_updated(["wiresetcerts", "daqbookoffsets"])

        # Test that it was serialized as JSON
        assert log_entry.categories_updated == '["wiresetcerts", "daqbookoffsets"]'

        # Test that it can be deserialized
        assert log_entry.get_categories_updated() == ["wiresetcerts", "daqbookoffsets"]

    def test_refresh_log_details_serialization(self, db_session):
        """Test details JSON serialization."""
        from db.models import RefreshLog

        details = {
            "wiresetcerts": {"success": True, "files_processed": 1},
            "daqbookoffsets": {"success": True, "files_processed": 4},
        }

        log_entry = RefreshLog(total_files_processed=5)
        log_entry.set_details(details)

        # Test that it was serialized as JSON
        assert "wiresetcerts" in log_entry.details
        assert "success" in log_entry.details

        # Test that it can be deserialized
        retrieved_details = log_entry.get_details()
        assert retrieved_details["wiresetcerts"]["success"] is True
        assert retrieved_details["daqbookoffsets"]["files_processed"] == 4

    def test_refresh_log_empty_values(self, db_session):
        """Test handling of empty values."""
        from db.models import RefreshLog

        log_entry = RefreshLog(
            total_files_processed=0, categories_updated="", details=""
        )

        # Should return empty lists/dicts for empty strings
        assert log_entry.get_categories_updated() == []
        assert log_entry.get_details() == {}

    def test_refresh_log_repr(self, db_session):
        """Test the string representation of RefreshLog."""
        from db.models import RefreshLog

        log_entry = RefreshLog(total_files_processed=5)
        log_entry.set_categories_updated(["wiresetcerts"])

        repr_str = repr(log_entry)
        assert "RefreshLog" in repr_str
        assert "wiresetcerts" in repr_str
        assert "wiresetcerts" in repr_str
