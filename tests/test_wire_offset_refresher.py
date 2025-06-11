# utils/test_wire_offset_refresher.py
"""
Tests for wire_offset_refresher module.
"""

from unittest.mock import Mock, patch

import pytest
from sqlalchemy.orm import Session

from utils.wire_offset_refresher import refresh_wire_offsets


class TestRefreshWireOffsets:
    """Test cases for refresh_wire_offsets function."""

    def test_refresh_with_no_files_provided_and_none_found(self):
        """Test refresh when no files are provided and none are found on SharePoint."""
        mock_session = Mock(spec=Session)

        with patch("utils.wire_offset_refresher.SharePointClient") as mock_sp_client:
            # Mock SharePoint client to return no files
            mock_sp_instance = mock_sp_client.return_value
            mock_sp_instance.list_files_in_pyro_standards_folder.return_value = []

            result = refresh_wire_offsets(session=mock_session)

            assert result["status"] == "success"
            assert result["files_found"] == 0
            assert result["files_processed"] == 0
            assert result["message"] == "No wire certificate files found to process"
            assert not result["errors"]

    def test_refresh_with_provided_files_empty_list(self):
        """Test refresh when empty list of files is provided."""
        mock_session = Mock(spec=Session)

        result = refresh_wire_offsets(updated_files=[], session=mock_session)

        assert result["status"] == "success"
        assert result["files_found"] == 0
        assert result["files_processed"] == 0
        assert result["message"] == "No wire certificate files found to process"

    @patch("utils.wire_offset_refresher.wirecert_filename_pattern")
    def test_refresh_filters_wire_certificate_files(self, mock_pattern):
        """Test that only wire certificate files are processed."""
        mock_session = Mock(spec=Session)
        mock_pattern.match.side_effect = lambda x: x.endswith(".xls")

        with patch("utils.wire_offset_refresher.SharePointClient") as mock_sp_client:
            # Create mock objects with .name attribute instead of dictionaries
            mock_file_1 = Mock()
            mock_file_1.name = "072513A.xls"
            mock_file_2 = Mock()
            mock_file_2.name = "other_file.pdf"
            mock_file_3 = Mock()
            mock_file_3.name = "072513B.xls"

            mock_sp_instance = mock_sp_client.return_value
            mock_sp_instance.list_files_in_pyro_standards_folder.return_value = [
                mock_file_1,
                mock_file_2,
                mock_file_3,
            ]

            result = refresh_wire_offsets(session=mock_session)

            assert result["files_found"] == 2  # Only .xls files should be counted

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.os.remove")
    def test_successful_file_processing(
        self, mock_remove, mock_parse, mock_sp_client, mock_exists
    ):
        """Test successful processing of a wire certificate file."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Mock SharePoint download
        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"

        # Mock parser to return test data
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001},
            {"TraceabilityNo": "124", "NominalTemp": 25.0, "CorrectionFactor": 1.002},
        ]

        file_info = {"name": "072513A.xls"}

        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        assert result["status"] == "success"
        assert result["files_processed"] == 1
        assert result["records_processed"] == 2
        assert result["records_added"] == 2
        assert len(result["errors"]) == 0

        # Verify session operations
        assert mock_session.add.call_count == 2
        mock_session.commit.assert_called_once()

        # Verify cleanup
        mock_remove.assert_called_once_with("/tmp/072513A.xls")

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    def test_download_failure(self, mock_sp_client, mock_exists):
        """Test handling of file download failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = False

        # Mock SharePoint download to fail
        mock_sp_client.download_file_from_sharepoint.return_value = None

        file_info = {"name": "072513A.xls"}
        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        assert result["status"] == "partial_success"
        # Has errors so gets partial_success
        assert result["files_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Failed to download file: 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_parse_excel_failure(self, mock_parse, mock_sp_client, mock_exists):
        """Test handling of Excel parsing failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.side_effect = Exception("Excel parsing failed")

        file_info = {"name": "072513A.xls"}

        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        assert result["status"] == "partial_success"
        assert result["files_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Error parsing Excel file 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.WireOffset")
    def test_database_record_creation_failure(
        self, mock_wire_offset, mock_parse, mock_sp_client, mock_exists
    ):
        """Test handling of database record creation failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001}
        ]

        # Mock WireOffset constructor to raise exception
        mock_wire_offset.side_effect = Exception("Database error")

        file_info = {"name": "072513A.xls"}
        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        assert result["status"] == "partial_success"
        assert result["files_processed"] == 1
        assert result["records_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Error processing offset record in 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.os.remove")
    def test_file_cleanup_failure(
        self, mock_remove, mock_parse, mock_sp_client, mock_exists
    ):
        """Test that file cleanup failure doesn't affect overall result."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": 25.0, "CorrectionFactor": 1.001}
        ]
        mock_remove.side_effect = OSError("Permission denied")

        file_info = {"name": "072513A.xls"}

        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        # Should still succeed despite cleanup failure
        assert result["status"] == "success"
        assert result["files_processed"] == 1

    @patch("utils.wire_offset_refresher.SessionLocal")
    def test_session_management_with_provided_session(self, mock_session_local):
        """Test that provided session is used and not closed."""
        mock_session = Mock(spec=Session)

        refresh_wire_offsets(updated_files=[], session=mock_session)

        # Should not create new session
        mock_session_local.assert_not_called()
        # Should not close provided session
        mock_session.close.assert_not_called()

    @patch("utils.wire_offset_refresher.SessionLocal")
    def test_session_management_without_provided_session(self, mock_session_local):
        """Test that new session is created and closed when none provided."""
        mock_session = Mock(spec=Session)
        mock_session_local.return_value = mock_session

        refresh_wire_offsets(updated_files=[])

        # Should create new session
        mock_session_local.assert_called_once()
        # Should close created session
        mock_session.close.assert_called_once()

    @patch("utils.wire_offset_refresher.SessionLocal")
    def test_major_exception_handling(self, mock_session_local):
        """Test handling of major exceptions with rollback."""
        mock_session = Mock(spec=Session)
        mock_session_local.return_value = mock_session

        with patch("utils.wire_offset_refresher.SharePointClient") as mock_sp_client:
            mock_sp_client.side_effect = Exception("Major failure")

            result = refresh_wire_offsets()

            assert result["status"] == "error"
            assert "Wire offset refresh failed" in result["message"]
            assert len(result["errors"]) == 1
            mock_session.rollback.assert_called_once()
            mock_session.close.assert_called_once()

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_temperature_mapping_to_columns(
        self, mock_parse, mock_sp_client, mock_exists
    ):
        """Test that temperature values are correctly stored in the new schema."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001},
            {"TraceabilityNo": "124", "NominalTemp": 0.0, "CorrectionFactor": 1.002},
            {"TraceabilityNo": "125", "NominalTemp": 25.0, "CorrectionFactor": 1.003},
            {"TraceabilityNo": "126", "NominalTemp": 50.0, "CorrectionFactor": 1.004},
            {"TraceabilityNo": "127", "NominalTemp": 100.0, "CorrectionFactor": 1.005},
        ]

        file_info = {"name": "072513A.xls"}

        with patch("utils.wire_offset_refresher.WireOffset") as mock_wire_offset:
            refresh_wire_offsets(updated_files=[file_info], session=mock_session)

            # Verify WireOffset was called with correct new schema fields
            calls = mock_wire_offset.call_args_list
            assert len(calls) == 5

            # Check first record (traceability_no=123, nominal_temp=-40.0)
            call_kwargs = calls[0][1]
            assert call_kwargs["traceability_no"] == "123"
            assert call_kwargs["nominal_temp"] == -40.0
            assert call_kwargs["correction_factor"] == 1.001

            # Check second record (traceability_no=124, nominal_temp=0.0)
            call_kwargs = calls[1][1]
            assert call_kwargs["traceability_no"] == "124"
            assert call_kwargs["nominal_temp"] == 0.0
            assert call_kwargs["correction_factor"] == 1.002

            # Check third record (traceability_no=125, nominal_temp=25.0)
            call_kwargs = calls[2][1]
            assert call_kwargs["traceability_no"] == "125"
            assert call_kwargs["nominal_temp"] == 25.0
            assert call_kwargs["correction_factor"] == 1.003

            # Check fourth record (traceability_no=126, nominal_temp=50.0)
            call_kwargs = calls[3][1]
            assert call_kwargs["traceability_no"] == "126"
            assert call_kwargs["nominal_temp"] == 50.0
            assert call_kwargs["correction_factor"] == 1.004

            # Check fifth record (traceability_no=127, nominal_temp=100.0)
            call_kwargs = calls[4][1]
            assert call_kwargs["traceability_no"] == "127"
            assert call_kwargs["nominal_temp"] == 100.0
            assert call_kwargs["correction_factor"] == 1.005

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_wirelot_extraction_from_filename(
        self, mock_parse, mock_sp_client, mock_exists
    ):
        """Test that traceability_no is correctly stored in the new schema."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": 25.0, "CorrectionFactor": 1.001}
        ]

        file_info = {"name": "072513A.xls"}

        with patch("utils.wire_offset_refresher.WireOffset") as mock_wire_offset:
            refresh_wire_offsets(updated_files=[file_info], session=mock_session)

            # Verify traceability_no was stored correctly
            call_kwargs = mock_wire_offset.call_args[1]
            assert call_kwargs["traceability_no"] == "123"
            assert call_kwargs["nominal_temp"] == 25.0
            assert call_kwargs["correction_factor"] == 1.001

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_empty_offset_data_handling(self, mock_parse, mock_sp_client, mock_exists):
        """Test handling when parser returns empty offset data."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        mock_sp_client.download_file_from_sharepoint.return_value = "/tmp/072513A.xls"
        mock_parse.return_value = []  # Empty data

        file_info = {"name": "072513A.xls"}

        result = refresh_wire_offsets(updated_files=[file_info], session=mock_session)

        assert result["status"] == "success"
        assert result["files_processed"] == 0  # No records processed
        assert result["records_processed"] == 0
        assert len(result["errors"]) == 0

    def test_result_structure(self):
        """Test that result dictionary has expected structure."""
        mock_session = Mock(spec=Session)

        result = refresh_wire_offsets(updated_files=[], session=mock_session)

        # Verify all expected keys are present
        expected_keys = {
            "status",
            "message",
            "files_processed",
            "files_found",
            "records_processed",
            "records_added",
            "records_updated",
            "errors",
        }
        assert set(result.keys()) == expected_keys

        # Verify types
        assert isinstance(result["status"], str)
        assert isinstance(result["message"], str)
        assert isinstance(result["files_processed"], int)
        assert isinstance(result["files_found"], int)
        assert isinstance(result["records_processed"], int)
        assert isinstance(result["records_added"], int)
        assert isinstance(result["records_updated"], int)
        assert isinstance(result["errors"], list)
        assert isinstance(result["records_updated"], int)
        assert isinstance(result["errors"], list)

    @pytest.mark.skip(reason="Integration test requires real database setup")
    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.SharePointClient")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_database_population_after_successful_refresh(
        self, mock_parse, mock_sp_client, mock_exists
    ):
        """Test that database is populated with records after successful refresh."""
        from sqlalchemy import text

        from db.models import WireOffset
        from utils.database import SessionLocal

        # Use real database session for this integration test
        session = SessionLocal()

        try:
            # Clean up any existing test data
            session.query(WireOffset).delete()
            session.commit()

            # Verify table is empty before test
            count_before = session.execute(
                text("SELECT COUNT(*) FROM public.wire_offsets")
            ).scalar()
            assert count_before == 0, "Database should be empty before test"

            # Mock external dependencies
            mock_exists.return_value = True
            mock_sp_instance = mock_sp_client.return_value
            mock_sp_instance.list_files_in_pyro_standards_folder.return_value = [
                {"name": "072513A.xls", "modified_by": "test_user"}
            ]
            mock_sp_instance.download_file_from_sharepoint.return_value = (
                "/tmp/072513A.xls"
            )

            # Mock parsed wire offset data
            mock_parse.return_value = [
                {
                    "TraceabilityNo": "072513A-001",
                    "NominalTemp": -40.0,
                    "CorrectionFactor": 1.001,
                },
                {
                    "TraceabilityNo": "072513A-002",
                    "NominalTemp": 0.0,
                    "CorrectionFactor": 1.002,
                },
                {
                    "TraceabilityNo": "072513A-003",
                    "NominalTemp": 25.0,
                    "CorrectionFactor": 1.003,
                },
                {
                    "TraceabilityNo": "072513A-004",
                    "NominalTemp": 50.0,
                    "CorrectionFactor": 1.004,
                },
                {
                    "TraceabilityNo": "072513A-005",
                    "NominalTemp": 100.0,
                    "CorrectionFactor": 1.005,
                },
            ]

            # Run the refresh with real database session
            result = refresh_wire_offsets(session=session)

            # Verify successful refresh
            assert result["status"] == "success"
            assert result["files_processed"] == 1
            assert result["records_processed"] == 5
            assert result["records_added"] == 5
            assert not result["errors"]

            # Verify database population
            count_after = session.execute(
                text("SELECT COUNT(*) FROM public.wire_offsets")
            ).scalar()
            assert (
                count_after > 0
            ), "Database should contain records after successful refresh"
            assert (
                count_after == 5
            ), f"Expected 5 records, found {count_after}"  # Verify specific record content
            sample_record = session.execute(
                text(
                    "SELECT traceability_no, nominal_temp, correction_factor FROM public.wire_offsets WHERE traceability_no = '072513A-001'"
                )
            ).fetchone()

            assert sample_record is not None, "Sample record should exist in database"
            assert sample_record[0] == "072513A-001"  # traceability_no
            assert (
                float(sample_record[1]) == -40.0
            )  # nominal_temp (convert from Decimal)
            assert (
                float(sample_record[2]) == 1.001
            )  # correction_factor (convert from Decimal)

        finally:
            # Clean up test data
            session.query(WireOffset).delete()
            session.commit()
            session.close()
            session.close()
            session.close()
            session.close()
