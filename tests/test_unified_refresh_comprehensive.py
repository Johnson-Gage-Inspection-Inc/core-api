# tests/test_unified_refresh_comprehensive.py
"""
Comprehensive tests for the unified refresh system.
"""

from datetime import datetime, timedelta
from unittest.mock import MagicMock, patch

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
            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": old_datetime.isoformat(),
                "id": "test-id",
            }

            # Mock empty Pyro_Standards folder
            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates()

            assert not result["wiresetcerts"]["has_updates"]
            assert not result["wireoffsets"]["has_updates"]
            assert not result["daqbookoffsets"]["has_updates"]
            assert len(result["wiresetcerts"]["files"]) == 0
            assert len(result["wireoffsets"]["files"]) == 0
            assert len(result["daqbookoffsets"]["files"]) == 0

    def test_wiresetcerts_has_updates(self):
        """Test when WireSetCerts.xlsx has been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock WireSetCerts.xlsx as recently updated
            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": recent_datetime.isoformat(),
                "id": "test-id",
            }

            # Mock empty Pyro_Standards folder
            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates()

            assert result["wiresetcerts"]["has_updates"]
            assert len(result["wiresetcerts"]["files"]) == 1
            assert result["wiresetcerts"]["files"][0]["name"] == "WireSetCerts.xlsx"

    def test_daqbook_file_updates(self):
        """Test when DAQbook files have been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock old WireSetCerts.xlsx
            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": (
                    datetime.now() - timedelta(days=2)
                ).isoformat(),
                "id": "test-id",
            }

            # Mock DAQbook files in Pyro_Standards
            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                {
                    "name": "J1_0124.xlsm",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "daqbook-id-1",
                },
                {
                    "name": "K5_0224.xlsm",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "daqbook-id-2",
                },
            ]

            result = get_file_categories_with_updates()

            assert result["daqbookoffsets"]["has_updates"]
            assert len(result["daqbookoffsets"]["files"]) == 2
            assert result["daqbookoffsets"]["files"][0]["name"] == "J1_0124.xlsm"

    def test_wire_certificate_file_updates(self):
        """Test when wire certificate files have been updated."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock old WireSetCerts.xlsx
            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": (
                    datetime.now() - timedelta(days=2)
                ).isoformat(),
                "id": "test-id",
            }

            # Mock wire certificate files in Pyro_Standards
            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                {
                    "name": "123456A.xls",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "wire-id-1",
                },
                {
                    "name": "789012B.xls",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "wire-id-2",
                },
            ]

            result = get_file_categories_with_updates()

            assert result["wireoffsets"]["has_updates"]
            assert len(result["wireoffsets"]["files"]) == 2
            assert result["wireoffsets"]["files"][0]["name"] == "123456A.xls"

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
            assert not result["wiresetcerts"]["has_updates"]
            assert not result["wireoffsets"]["has_updates"]
            assert not result["daqbookoffsets"]["has_updates"]

    def test_custom_last_checked_datetime(self):
        """Test using a custom last_checked datetime."""
        custom_datetime = datetime.now() - timedelta(hours=6)
        file_datetime = datetime.now() - timedelta(hours=3)  # After custom datetime

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": file_datetime.isoformat(),
                "id": "test-id",
            }

            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates(last_checked=custom_datetime)

            assert result["wiresetcerts"]["has_updates"]
            assert result["last_checked"] == custom_datetime.isoformat()

    def test_datetime_parsing_with_z_suffix(self):
        """Test datetime parsing when SharePoint returns Z suffix."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            # Mock datetime with Z suffix (common SharePoint format)
            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": recent_datetime.isoformat() + "Z",
                "id": "test-id",
            }

            mock_instance.list_files_in_pyro_standards_folder.return_value = []

            result = get_file_categories_with_updates()

            # Should successfully parse the datetime
            assert result["wiresetcerts"]["has_updates"]

    def test_invalid_filename_patterns_ignored(self):
        """Test that files not matching patterns are ignored."""
        recent_datetime = datetime.now() - timedelta(hours=1)

        with patch("utils.unified_refresh.SharePointClient") as mock_client:
            mock_instance = MagicMock()
            mock_client.return_value = mock_instance

            mock_instance.get_wiresetcerts_file.return_value = {
                "name": "WireSetCerts.xlsx",
                "lastModifiedDateTime": (
                    datetime.now() - timedelta(days=2)
                ).isoformat(),
                "id": "test-id",
            }

            # Mock files that don't match expected patterns
            mock_instance.list_files_in_pyro_standards_folder.return_value = [
                {
                    "name": "random_file.txt",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "random-id",
                },
                {
                    "name": "invalid.xlsx",
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "invalid-id",
                },
                {
                    "name": "J99_0124.xlsm",  # Invalid DAQbook pattern (J99 not valid)
                    "lastModifiedDateTime": recent_datetime.isoformat(),
                    "id": "invalid-daqbook-id",
                },
            ]

            result = get_file_categories_with_updates()

            # Should not detect any updates for invalid patterns
            assert not result["wireoffsets"]["has_updates"]
            assert not result["daqbookoffsets"]["has_updates"]


class TestRefreshAllUpdatedCategories:
    """Test the unified refresh orchestration logic."""

    def test_no_categories_need_updates(self):
        """Test when no categories have file updates."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {"has_updates": False, "files": []},
                "wireoffsets": {"has_updates": False, "files": []},
                "daqbookoffsets": {"has_updates": False, "files": []},
                "last_checked": datetime.now().isoformat(),
            }

            with patch("utils.unified_refresh.log_refresh_result") as mock_log:
                result = refresh_all_updated_categories()

                assert result["categories_updated"] == []
                assert result["summary"]["categories_with_updates"] == 0
                assert result["summary"]["total_files_processed"] == 0
                assert result["summary_line"] == "No categories needed updates"
                mock_log.assert_called_once()

    def test_wiresetcerts_refresh_success(self):
        """Test successful WireSetCerts refresh."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {
                    "has_updates": True,
                    "files": [{"name": "WireSetCerts.xlsx"}],
                },
                "wireoffsets": {"has_updates": False, "files": []},
                "daqbookoffsets": {"has_updates": False, "files": []},
                "last_checked": datetime.now().isoformat(),
            }

            with patch("utils.unified_refresh.refresh_wire_set_certs") as mock_refresh:
                mock_refresh.return_value = {
                    "success": True,
                    "files_processed": 1,
                    "message": "Successfully refreshed wire set certificates",
                }

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wiresetcerts" in result["categories_updated"]
                    assert result["summary"]["categories_with_updates"] == 1
                    assert result["summary"]["total_files_processed"] == 1
                    assert "wiresetcerts" in result["summary_line"]
                    mock_refresh.assert_called_once()

    def test_wiresetcerts_refresh_failure(self):
        """Test WireSetCerts refresh failure handling."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {
                    "has_updates": True,
                    "files": [{"name": "WireSetCerts.xlsx"}],
                },
                "wireoffsets": {"has_updates": False, "files": []},
                "daqbookoffsets": {"has_updates": False, "files": []},
                "last_checked": datetime.now().isoformat(),
            }

            with patch("utils.unified_refresh.refresh_wire_set_certs") as mock_refresh:
                mock_refresh.side_effect = Exception("Database connection failed")

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wiresetcerts" not in result["categories_updated"]
                    assert result["results"]["wiresetcerts"]["status"] == "error"
                    assert (
                        "Database connection failed"
                        in result["results"]["wiresetcerts"]["message"]
                    )

    def test_daqbook_refresh_success(self):
        """Test successful DAQbook refresh."""
        mock_files = [{"name": "J1_0124.xlsm", "id": "test-id"}]

        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {"has_updates": False, "files": []},
                "wireoffsets": {"has_updates": False, "files": []},
                "daqbookoffsets": {"has_updates": True, "files": mock_files},
                "last_checked": datetime.now().isoformat(),
            }
            with patch("utils.unified_refresh.refresh_daqbook_offsets") as mock_refresh:
                mock_refresh.return_value = {
                    "success": True,
                    "files_processed": 1,
                    "message": "Successfully refreshed DAQbook offsets",
                }

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "daqbookoffsets" in result["categories_updated"]
                    # DAQbook refresher doesn't take updated_files parameter - it discovers files internally
                    mock_refresh.assert_called_once_with()

    def test_wire_offsets_refresh_success(self):
        """Test successful wire offsets refresh."""
        mock_files = [{"name": "123456A.xls", "id": "test-id"}]

        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {"has_updates": False, "files": []},
                "wireoffsets": {"has_updates": True, "files": mock_files},
                "daqbookoffsets": {"has_updates": False, "files": []},
                "last_checked": datetime.now().isoformat(),
            }

            with patch("utils.unified_refresh.refresh_wire_offsets") as mock_refresh:
                mock_refresh.return_value = {
                    "success": True,
                    "files_processed": 1,
                    "message": "Successfully refreshed wire offsets",
                }

                with patch("utils.unified_refresh.log_refresh_result"):
                    result = refresh_all_updated_categories()

                    assert "wireoffsets" in result["categories_updated"]
                    mock_refresh.assert_called_once_with(updated_files=mock_files)

    def test_multiple_categories_refresh(self):
        """Test refreshing multiple categories simultaneously."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {
                    "has_updates": True,
                    "files": [{"name": "WireSetCerts.xlsx"}],
                },
                "wireoffsets": {
                    "has_updates": True,
                    "files": [{"name": "123456A.xls"}],
                },
                "daqbookoffsets": {
                    "has_updates": True,
                    "files": [{"name": "J1_0124.xlsm"}],
                },
                "last_checked": datetime.now().isoformat(),
            }

            with patch(
                "utils.unified_refresh.refresh_wire_set_certs"
            ) as mock_refresh_wire_set:
                mock_refresh_wire_set.return_value = {
                    "success": True,
                    "files_processed": 1,
                }

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

                            assert len(result["categories_updated"]) == 3
                            assert "wiresetcerts" in result["categories_updated"]
                            assert "wireoffsets" in result["categories_updated"]
                            assert "daqbookoffsets" in result["categories_updated"]
                            assert result["summary"]["total_files_processed"] == 3

    def test_partial_refresh_failures(self):
        """Test when some categories succeed and others fail."""
        with patch(
            "utils.unified_refresh.get_file_categories_with_updates"
        ) as mock_updates:
            mock_updates.return_value = {
                "wiresetcerts": {
                    "has_updates": True,
                    "files": [{"name": "WireSetCerts.xlsx"}],
                },
                "wireoffsets": {
                    "has_updates": True,
                    "files": [{"name": "123456A.xls"}],
                },
                "daqbookoffsets": {"has_updates": False, "files": []},
                "last_checked": datetime.now().isoformat(),
            }

            with patch(
                "utils.unified_refresh.refresh_wire_set_certs"
            ) as mock_refresh_wire_set:
                mock_refresh_wire_set.return_value = {
                    "success": True,
                    "files_processed": 1,
                }

                with patch(
                    "utils.unified_refresh.refresh_wire_offsets"
                ) as mock_refresh_wire:
                    mock_refresh_wire.side_effect = Exception("Wire refresh failed")

                    with patch("utils.unified_refresh.log_refresh_result"):
                        result = (
                            refresh_all_updated_categories()
                        )  # Should have one success and one failure
                        assert "wiresetcerts" in result["categories_updated"]
                        assert "wireoffsets" not in result["categories_updated"]
                        assert result["results"]["wireoffsets"]["status"] == "error"
                        assert (
                            "Wire refresh failed"
                            in result["results"]["wireoffsets"]["message"]
                        )
                        assert result["summary"]["total_files_processed"] == 1


class TestLogRefreshResult:
    """Test the database logging functionality."""

    def test_log_refresh_result_success(self, db_session):
        """Test successful logging of refresh results."""
        result = {
            "categories_updated": ["wiresetcerts", "daqbookoffsets"],
            "summary": {"total_files_processed": 5},
            "results": {
                "wiresetcerts": {"success": True, "files_processed": 1},
                "daqbookoffsets": {"success": True, "files_processed": 4},
            },
        }
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
        result = {
            "categories_updated": ["wiresetcerts"],
            "summary": {"total_files_processed": 1},
            "results": {"wiresetcerts": {"success": True}},
        }

        with patch("utils.database.SessionLocal") as mock_session_local:
            mock_db = MagicMock()
            mock_session_local.return_value = mock_db
            mock_db.add.side_effect = Exception("Database connection failed")

            # Should not raise an exception
            log_refresh_result(result)

    def test_log_refresh_result_missing_fields(self):
        """Test logging when result dictionary has missing fields."""
        result = {}  # Empty result

        with patch("utils.database.SessionLocal") as mock_session_local:
            mock_db = MagicMock()
            mock_session_local.return_value = mock_db

            log_refresh_result(result)

            # Should handle missing fields gracefully
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
