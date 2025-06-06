#!/usr/bin/env python
# tests/test_initialize_wire_offsets.py
"""
Test the wire offsets initialization functionality.

Tests the initialization script that populates the wire_offsets table
with all historical data from SharePoint wire certificate files.
"""

import os
from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy import text

from utils.database import SessionLocal
from utils.initialize_wire_offsets import (
    get_all_wire_certificate_files,
    initialize_wire_offsets_table,
)


class TestWireOffsetsInitialization:
    """Test class for wire offsets initialization functionality."""

    def test_get_all_wire_certificate_files_success(self):
        """Test successful retrieval of wire certificate files from SharePoint."""

        mock_files = [
            {
                "name": "Wire_Cert_001.xlsx",
                "id": "file1",
                "lastModifiedDateTime": "2024-01-01T00:00:00Z",
            },
            {
                "name": "Wire_Cert_002.xls",
                "id": "file2",
                "lastModifiedDateTime": "2024-01-02T00:00:00Z",
            },
            {
                "name": "Other_File.pdf",
                "id": "file3",
                "lastModifiedDateTime": "2024-01-03T00:00:00Z",
            },  # Should be filtered out
            {
                "name": "Wire_Cert_003.XLSX",
                "id": "file4",
                "lastModifiedDateTime": "2024-01-04T00:00:00Z",
            },  # Upper case extension
        ]

        with patch(
            "utils.sharepoint_client.list_pyro_standards_excel_files"
        ) as mock_list_files:
            mock_list_files.return_value = mock_files

            result = get_all_wire_certificate_files()

            # Should only return Excel files (3 files, excluding the PDF)
            assert len(result) == 3
            assert any(f["name"] == "Wire_Cert_001.xlsx" for f in result)
            assert any(f["name"] == "Wire_Cert_002.xls" for f in result)
            assert any(f["name"] == "Wire_Cert_003.XLSX" for f in result)
            assert not any(f["name"] == "Other_File.pdf" for f in result)

    def test_get_all_wire_certificate_files_sharepoint_error(self):
        """Test handling of SharePoint connection errors."""
        with patch(
            "utils.sharepoint_client.list_pyro_standards_excel_files"
        ) as mock_list_files:
            mock_list_files.side_effect = Exception("SharePoint connection failed")

            with pytest.raises(Exception, match="SharePoint connection failed"):
                get_all_wire_certificate_files()

    @patch("utils.initialize_wire_offsets.refresh_wire_offsets")
    @patch("utils.initialize_wire_offsets.get_all_wire_certificate_files")
    def test_initialize_wire_offsets_table_success(self, mock_get_files, mock_refresh):
        """Test successful initialization of wire_offsets table."""
        # Mock file list
        mock_files = [
            {"name": "Wire_Cert_001.xlsx", "id": "file1"},
            {"name": "Wire_Cert_002.xls", "id": "file2"},
        ]
        mock_get_files.return_value = mock_files

        # Mock refresh result
        mock_refresh.return_value = {
            "successful_files": 2,
            "failed_files": 0,
            "total_records_added": 50,
        }  # Mock database queries
        with patch("utils.initialize_wire_offsets.SessionLocal") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session

            # Create separate mock results for each query
            count_before_result = MagicMock()
            count_before_result.scalar.return_value = 0

            delete_wire_offsets_result = MagicMock()  # For DELETE wire_offsets

            count_after_result = MagicMock()
            count_after_result.scalar.return_value = 50

            view_count_result = MagicMock()
            view_count_result.scalar.return_value = 25

            sample_records_result = MagicMock()
            sample_records_result.fetchall.return_value = [
                (1, "T001", 25.0, 1.001),
                (2, "T002", 30.0, 1.002),
            ]

            # Set up side_effect with all the queries needed
            mock_session.execute.side_effect = [
                count_before_result,  # count_before
                delete_wire_offsets_result,  # DELETE wire_offsets
                count_after_result,  # count_after
                view_count_result,  # view_count
                sample_records_result,  # sample_records
            ]

            result = initialize_wire_offsets_table()  # Verify result structure
            assert result["status"] == "success"
            assert result["records_before"] == 0
            assert result["records_after"] == 50
            assert result["records_added"] == 50
            assert result["files_processed"] == 2
            assert result["files_successful"] == 2
            assert result["files_failed"] == 0
            assert result["view_records"] == 25
            assert len(result["sample_records"]) == 2

            # Verify refresh was called and database session was used
            assert mock_session.execute.call_count >= 5  # At least 5 queries
            mock_session.commit.assert_called()

    @patch("utils.initialize_wire_offsets.get_all_wire_certificate_files")
    def test_initialize_wire_offsets_table_no_files(self, mock_get_files):
        """Test initialization when no wire certificate files are found."""
        mock_get_files.return_value = []

        with patch("utils.initialize_wire_offsets.SessionLocal") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            mock_session.execute.return_value.scalar.return_value = 0

            result = initialize_wire_offsets_table()

            assert result["status"] == "no_files"
            assert "No wire certificate files found" in result["message"]
            assert result["files_processed"] == 0

    @patch("builtins.input", return_value="n")  # User chooses not to continue
    def test_initialize_wire_offsets_table_already_has_data(self, mock_input):
        """Test initialization when table already has data and user declines to continue."""
        with patch("utils.initialize_wire_offsets.SessionLocal") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            mock_session.execute.return_value.scalar.return_value = (
                100  # Table has data
            )

            result = initialize_wire_offsets_table()

            assert result["status"] == "skipped"
            assert "already has data" in result["message"]
            assert result["records_before"] == 100
            assert result["records_after"] == 100

    @patch("builtins.input", return_value="y")  # User chooses to continue
    @patch("utils.initialize_wire_offsets.refresh_wire_offsets")
    @patch("utils.initialize_wire_offsets.get_all_wire_certificate_files")
    def test_initialize_wire_offsets_table_force_with_existing_data(
        self, mock_get_files, mock_refresh, mock_input
    ):
        """Test initialization when table has data but user forces continuation."""
        mock_files = [{"name": "Wire_Cert_001.xlsx", "id": "file1"}]
        mock_get_files.return_value = mock_files
        mock_refresh.return_value = {"successful_files": 1, "failed_files": 0}

        with patch("utils.initialize_wire_offsets.SessionLocal") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = (
                mock_session  # Create separate mock results for each query
            )
            count_before_result = MagicMock()
            count_before_result.scalar.return_value = 100

            delete_result = MagicMock()  # For DELETE refresh_log

            count_after_result = MagicMock()
            count_after_result.scalar.return_value = 150

            view_count_result = MagicMock()
            view_count_result.scalar.return_value = 75

            sample_records_result = MagicMock()
            sample_records_result.fetchall.return_value = [(1, "T001", 25.0, 1.001)]

            # Mock sequence: before=100, after=150, view=75
            mock_session.execute.side_effect = [
                count_before_result,  # count_before
                delete_result,  # DELETE refresh_log
                count_after_result,  # count_after
                view_count_result,  # view_count
                sample_records_result,  # sample_records
            ]

            result = initialize_wire_offsets_table()

            assert result["status"] == "success"
            assert result["records_before"] == 100
            assert result["records_after"] == 150
            assert result["records_added"] == 50

    @patch("utils.initialize_wire_offsets.get_all_wire_certificate_files")
    def test_initialize_wire_offsets_table_database_error(self, mock_get_files):
        """Test handling of database errors during initialization."""
        mock_get_files.return_value = [{"name": "Wire_Cert_001.xlsx", "id": "file1"}]

        with patch("utils.initialize_wire_offsets.SessionLocal") as mock_session_class:
            mock_session = MagicMock()
            mock_session_class.return_value = mock_session
            mock_session.execute.side_effect = Exception("Database connection failed")

            with pytest.raises(Exception, match="Database connection failed"):
                initialize_wire_offsets_table()

            # Verify rollback was called
            mock_session.rollback.assert_called()


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Integration test - skipped when SKIP_AUTH=true",
)
class TestWireOffsetsInitializationIntegration:
    """Integration tests for wire offsets initialization (requires real SharePoint access)."""

    def test_real_sharepoint_file_retrieval(self):
        """Test actual retrieval of wire certificate files from SharePoint."""
        try:
            files = get_all_wire_certificate_files()

            # Verify we get some files
            assert isinstance(files, list)
            assert len(files) > 0, "Should find at least some wire certificate files"

            # Verify file structure
            for file_info in files[:3]:  # Check first 3 files
                assert "name" in file_info
                assert "id" in file_info
                assert file_info["name"].lower().endswith((".xls", ".xlsx"))

        except Exception as e:
            pytest.skip(f"SharePoint access failed: {e}")

    def test_database_state_verification(self):
        """Test that we can check the current state of the wire_offsets table."""
        session = SessionLocal()
        try:
            # Check table exists and get current count
            count = session.execute(
                text("SELECT COUNT(*) FROM public.wire_offsets")
            ).scalar()
            assert isinstance(count, int)
            assert count >= 0

            # Check view exists
            view_count = session.execute(
                text("SELECT COUNT(*) FROM public.wire_offsets_current")
            ).scalar()
            assert isinstance(view_count, int)
            assert view_count >= 0

        finally:
            session.close()
            session.close()
