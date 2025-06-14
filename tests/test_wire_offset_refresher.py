# utils/test_wire_offset_refresher.py
"""
Tests for wire_offset_refresher module.
Updated to work with new SharePoint integration using Office365 File objects.
"""

from unittest.mock import Mock, patch

from sqlalchemy.orm import Session

from utils.wire_offset_refresher import refresh_wire_offsets


class TestRefreshWireOffsets:
    """Test cases for refresh_wire_offsets function."""

    def test_refresh_with_no_files_provided_and_none_found(self):
        """Test refresh when no files are provided and none are found on SharePoint."""
        mock_session = Mock(spec=Session)

        with patch(
            "utils.wire_offset_refresher.get_pyro_standards_files"
        ) as mock_get_files:
            # Mock the new SharePoint integration to return no files
            mock_get_files.return_value = []

            result = refresh_wire_offsets(session=mock_session)

            assert result["status"] == "success"
            assert result["files_found"] == 0
            assert result["files_processed"] == 0
            assert result["message"] == "No wire certificate files found to process"
            assert not result["errors"]

    def test_refresh_with_provided_files_empty_list(self):
        """Test refresh when empty list of files is provided."""
        mock_session = Mock(spec=Session)

        with patch(
            "utils.wire_offset_refresher.get_pyro_standards_files"
        ) as mock_get_files:
            # Mock the new SharePoint integration to return no files
            mock_get_files.return_value = []

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

        with patch(
            "utils.wire_offset_refresher.get_pyro_standards_files"
        ) as mock_get_files:
            # Create mock File objects with .name attribute
            mock_file_1 = Mock()
            mock_file_1.name = "072513A.xls"
            mock_file_1.unique_id = "id1"
            mock_file_2 = Mock()
            mock_file_2.name = "other_file.pdf"
            mock_file_2.unique_id = "id2"
            mock_file_3 = Mock()
            mock_file_3.name = "072513B.xls"
            mock_file_3.unique_id = "id3"

            mock_get_files.return_value = [
                mock_file_1,
                mock_file_2,
                mock_file_3,
            ]

            result = refresh_wire_offsets(session=mock_session)

            assert result["files_found"] == 2  # Only .xls files should be counted

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.os.remove")
    def test_successful_file_processing(self, mock_remove, mock_parse, mock_exists):
        """Test successful processing of a wire certificate file."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with get_content method
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.modified_by = "test_user"
        mock_file.get_content.return_value.value = b"mock excel content"

        # Mock parser to return test data
        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001},
            {"TraceabilityNo": "124", "NominalTemp": 25.0, "CorrectionFactor": 1.002},
        ]

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        assert result["status"] == "success"
        assert result["files_processed"] == 1
        assert result["records_processed"] == 2
        assert result["records_added"] == 2
        assert len(result["errors"]) == 0

        # Verify session operations
        assert mock_session.add.call_count == 2
        mock_session.commit.assert_called_once()

        # Verify file download was called
        mock_file.get_content.assert_called_once()

    @patch("utils.wire_offset_refresher.os.path.exists")
    def test_download_failure(self, mock_exists):
        """Test handling of file download failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = False

        # Create mock File object that raises exception on get_content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.get_content.side_effect = Exception("Download failed")

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        assert result["status"] == "partial_success"
        # Has errors so gets partial_success
        assert result["files_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Failed to download file 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_parse_excel_failure(self, mock_parse, mock_exists):
        """Test handling of Excel parsing failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.side_effect = Exception("Excel parsing failed")

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        assert result["status"] == "partial_success"
        assert result["files_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Error parsing Excel file 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.WireOffset")
    def test_database_record_creation_failure(
        self, mock_wire_offset, mock_parse, mock_exists
    ):
        """Test handling of database record creation failure."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001}
        ]

        # Mock WireOffset constructor to raise exception
        mock_wire_offset.side_effect = Exception("Database error")

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        assert result["status"] == "partial_success"
        assert result["files_processed"] == 1
        assert result["records_processed"] == 0
        assert len(result["errors"]) == 1
        assert "Error processing offset record in 072513A.xls" in result["errors"][0]

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    @patch("utils.wire_offset_refresher.os.remove")
    def test_file_cleanup_failure(self, mock_remove, mock_parse, mock_exists):
        """Test that file cleanup failure doesn't affect overall result."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.modified_by = "test_user"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": 25.0, "CorrectionFactor": 1.001}
        ]
        mock_remove.side_effect = OSError("Permission denied")

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        # Should still succeed despite cleanup failure
        assert result["status"] == "success"
        assert result["files_processed"] == 1

    def test_missing_file_object(self):
        """Test handling of file with None get_content result."""
        mock_session = Mock(spec=Session)

        # Create a File object that returns None for get_content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.get_content.return_value.value = None

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

        assert result["status"] == "partial_success"
        assert result["files_processed"] == 0
        assert len(result["errors"]) == 1

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

        with patch(
            "utils.wire_offset_refresher.get_pyro_standards_files"
        ) as mock_get_files:
            mock_get_files.side_effect = Exception("Major failure")

            result = refresh_wire_offsets()

            assert result["status"] == "error"
            assert "Wire offset refresh failed" in result["message"]
            assert len(result["errors"]) == 1
            mock_session.rollback.assert_called_once()
            mock_session.close.assert_called_once()

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_temperature_mapping_to_columns(self, mock_parse, mock_exists):
        """Test that temperature values are correctly stored in the new schema."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.modified_by = "test_user"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": -40.0, "CorrectionFactor": 1.001},
            {"TraceabilityNo": "124", "NominalTemp": 0.0, "CorrectionFactor": 1.002},
            {"TraceabilityNo": "125", "NominalTemp": 25.0, "CorrectionFactor": 1.003},
            {"TraceabilityNo": "126", "NominalTemp": 50.0, "CorrectionFactor": 1.004},
            {"TraceabilityNo": "127", "NominalTemp": 100.0, "CorrectionFactor": 1.005},
        ]

        with patch("utils.wire_offset_refresher.WireOffset") as mock_wire_offset:
            refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

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
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_wirelot_extraction_from_filename(self, mock_parse, mock_exists):
        """Test that traceability_no is correctly stored in the new schema."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.modified_by = "test_user"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.return_value = [
            {"TraceabilityNo": "123", "NominalTemp": 25.0, "CorrectionFactor": 1.001}
        ]

        with patch("utils.wire_offset_refresher.WireOffset") as mock_wire_offset:
            refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

            # Verify traceability_no was stored correctly
            call_kwargs = mock_wire_offset.call_args[1]
            assert call_kwargs["traceability_no"] == "123"
            assert call_kwargs["nominal_temp"] == 25.0
            assert call_kwargs["correction_factor"] == 1.001

    @patch("utils.wire_offset_refresher.os.path.exists")
    @patch("utils.wire_offset_refresher.parse_wire_offsets_from_excel")
    def test_empty_offset_data_handling(self, mock_parse, mock_exists):
        """Test handling when parser returns empty offset data."""
        mock_session = Mock(spec=Session)
        mock_exists.return_value = True

        # Create mock File object with content
        mock_file = Mock()
        mock_file.name = "072513A.xls"
        mock_file.get_content.return_value.value = b"mock excel content"

        mock_parse.return_value = []  # Empty data

        result = refresh_wire_offsets(updated_files=[mock_file], session=mock_session)

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
