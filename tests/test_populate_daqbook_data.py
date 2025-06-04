#!/usr/bin/env python3
"""
Tests for utils.populate_daqbook_data module.

Tests the DAQbook data population functionality that extracts offset data
from SharePoint calibration files and saves to the database.
"""

import io
import os
import sys
from unittest.mock import Mock, patch

import pandas as pd
import pytest
from sqlalchemy.exc import SQLAlchemyError

from utils.populate_daqbook_data import DaqbookDataPopulator, main

# Add the parent directory to sys.path to import the module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class TestDaqbookDataPopulator:
    """Test cases for DaqbookDataPopulator class."""

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_init_success(self, mock_sharepoint, mock_sessionmaker, mock_create_engine):
        """Test successful initialization."""
        mock_session = Mock()
        mock_sessionmaker.return_value = Mock(return_value=mock_session)

        populator = DaqbookDataPopulator()

        assert populator.database_url == "sqlite:///:memory:"
        mock_create_engine.assert_called_once_with("sqlite:///:memory:")
        mock_sessionmaker.assert_called_once()
        mock_sharepoint.assert_called_once()
        assert len(populator.daqbook_patterns) == 7

    @patch("utils.populate_daqbook_data.SharePointClient")
    def test_init_no_database_url(self, mock_sharepoint):
        """Test initialization fails without DATABASE_URL."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(
                ValueError, match="DATABASE_URL environment variable not set"
            ):
                DaqbookDataPopulator()

    def test_extract_tn_from_filename_success(self):
        """Test successful TN extraction from various filename patterns."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker"),
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            populator = DaqbookDataPopulator()

            test_cases = [
                ("J1_0325.xlsm", "J10325"),
                ("J2_1234.xlsm", "J21234"),
                ("K4_0001.xlsm", "K40001"),
                ("N2_9999.xlsm", "N29999"),
            ]

            for filename, expected in test_cases:
                result = populator.extract_tn_from_filename(filename)
                assert result == expected

    def test_extract_tn_from_filename_invalid(self):
        """Test TN extraction with invalid filenames."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker"),
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            populator = DaqbookDataPopulator()

            invalid_cases = [
                "invalid_file.xlsm",
                "J1_0325.xlsx",  # Wrong extension
                "Z1_0325.xlsm",  # Invalid prefix
                "J1-0325.xlsm",  # Wrong separator
                "J1_abc.xlsm",  # Non-numeric
            ]

            for filename in invalid_cases:
                result = populator.extract_tn_from_filename(filename)
                assert result is None

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_search_daqbook_files_success(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test successful file search."""
        mock_sharepoint = Mock()
        mock_sharepoint_class.return_value = mock_sharepoint

        # Mock search results
        mock_sharepoint.search_files.return_value = [
            {"name": "J1_0325.xlsm", "id": "file1"},
            {"name": "J2_0326.xlsm", "id": "file2"},
        ]

        populator = DaqbookDataPopulator()

        with patch("builtins.print"):  # Suppress print output
            files = populator.search_daqbook_files()

        assert len(files) >= 2
        assert any(f["name"] == "J1_0325.xlsm" for f in files)
        assert any(f["name"] == "J2_0326.xlsm" for f in files)

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_search_daqbook_files_with_errors(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test file search with some patterns failing."""
        mock_sharepoint = Mock()
        mock_sharepoint_class.return_value = mock_sharepoint

        # Mock search to fail for some patterns
        def search_side_effect(pattern):
            if "J1_" in pattern:
                return [{"name": "J1_0325.xlsm", "id": "file1"}]
            else:
                raise Exception("SharePoint error")

        mock_sharepoint.search_files.side_effect = search_side_effect

        populator = DaqbookDataPopulator()

        with patch("builtins.print"):  # Suppress print output
            files = populator.search_daqbook_files()

        assert len(files) >= 1
        assert files[0]["name"] == "J1_0325.xlsm"

    def test_parse_daqbook_excel_success(self):
        """Test successful Excel parsing."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker"),
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            populator = DaqbookDataPopulator()

            # Create mock Excel data
            df = pd.DataFrame(
                {
                    "Point": [1, 2, 3],
                    -40.0: [1.1, 1.2, 1.3],
                    0.0: [2.1, 2.2, 2.3],
                    100.0: [3.1, 3.2, 3.3],
                }
            )

            # Create mock Excel file content
            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False, engine="openpyxl")
            excel_content = excel_buffer.getvalue()

            with patch("builtins.print"):  # Suppress print output
                result = populator.parse_daqbook_excel(excel_content, "J10325")

            assert len(result) == 9  # 3 rows × 3 temp columns
            assert result[0]["tn"] == "J10325"
            assert result[0]["temp"] == -40.0
            assert result[0]["point"] == 1
            assert result[0]["reading"] == 1.1

    def test_parse_daqbook_excel_error(self):
        """Test Excel parsing with invalid content."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker"),
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            populator = DaqbookDataPopulator()

            invalid_content = b"not an excel file"

            with patch("builtins.print"):  # Suppress print output
                result = populator.parse_daqbook_excel(invalid_content, "J10325")

            assert result == []

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch("utils.populate_daqbook_data.DaqbookOffset")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_save_offset_data_new_records(
        self, mock_offset_model, mock_sharepoint, mock_sessionmaker, mock_create_engine
    ):
        """Test saving new offset data records."""
        mock_session = Mock()
        mock_sessionmaker.return_value = Mock(return_value=mock_session)

        # Mock query to return no existing records
        mock_session.query.return_value.filter_by.return_value.first.return_value = None

        populator = DaqbookDataPopulator()

        offset_data = [
            {"tn": "J10325", "temp": -40.0, "point": 1, "reading": 1.1},
            {"tn": "J10325", "temp": 0.0, "point": 1, "reading": 2.1},
        ]

        with patch("builtins.print"):  # Suppress print output
            result = populator.save_offset_data(offset_data)

        assert result == 2
        assert mock_session.add.call_count == 2
        mock_session.commit.assert_called_once()

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_save_offset_data_update_existing(
        self, mock_sharepoint, mock_sessionmaker, mock_create_engine
    ):
        """Test updating existing offset data records."""
        mock_session = Mock()
        mock_sessionmaker.return_value = Mock(return_value=mock_session)

        # Mock existing record
        existing_record = Mock()
        existing_record.reading = 1.0
        mock_session.query.return_value.filter_by.return_value.first.return_value = (
            existing_record
        )

        populator = DaqbookDataPopulator()

        offset_data = [
            {"tn": "J10325", "temp": -40.0, "point": 1, "reading": 1.5},
        ]

        with patch("builtins.print"):  # Suppress print output
            result = populator.save_offset_data(offset_data)

        assert result == 1
        assert existing_record.reading == 1.5
        mock_session.commit.assert_called_once()

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_save_offset_data_commit_error(
        self, mock_sharepoint, mock_sessionmaker, mock_create_engine
    ):
        """Test handling database commit errors."""
        mock_session = Mock()
        mock_sessionmaker.return_value = Mock(return_value=mock_session)
        mock_session.query.return_value.filter_by.return_value.first.return_value = None
        mock_session.commit.side_effect = SQLAlchemyError("Database error")

        populator = DaqbookDataPopulator()

        offset_data = [
            {"tn": "J10325", "temp": -40.0, "point": 1, "reading": 1.1},
        ]

        with patch("builtins.print"):  # Suppress print output
            result = populator.save_offset_data(offset_data)

        assert result == 0
        mock_session.rollback.assert_called_once()

    def test_save_offset_data_empty_list(self):
        """Test saving empty offset data list."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker"),
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            populator = DaqbookDataPopulator()
            result = populator.save_offset_data([])
            assert result == 0

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_process_daqbook_file_success(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test successful file processing."""
        mock_sharepoint = Mock()
        mock_sharepoint_class.return_value = mock_sharepoint
        mock_sharepoint.download_file_content.return_value = b"mock excel content"

        populator = DaqbookDataPopulator()

        # Mock the parse and save methods
        with (
            patch.object(populator, "parse_daqbook_excel") as mock_parse,
            patch.object(populator, "save_offset_data") as mock_save,
            patch("builtins.print"),
        ):

            mock_parse.return_value = [
                {"tn": "J10325", "temp": -40.0, "point": 1, "reading": 1.1}
            ]
            mock_save.return_value = 1

            file_info = {"name": "J1_0325.xlsm", "id": "file123"}
            result = populator.process_daqbook_file(file_info)

            assert result == 1
            mock_sharepoint.download_file_content.assert_called_once_with("file123")
            mock_parse.assert_called_once_with(b"mock excel content", "J10325")
            mock_save.assert_called_once()

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_process_daqbook_file_invalid_filename(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test processing file with invalid filename."""
        populator = DaqbookDataPopulator()

        file_info = {"name": "invalid_file.xlsm", "id": "file123"}

        with patch("builtins.print"):  # Suppress print output
            result = populator.process_daqbook_file(file_info)

        assert result == 0

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_process_daqbook_file_download_error(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test processing file with download error."""
        mock_sharepoint = Mock()
        mock_sharepoint_class.return_value = mock_sharepoint
        mock_sharepoint.download_file_content.side_effect = Exception("Download failed")

        populator = DaqbookDataPopulator()

        file_info = {"name": "J1_0325.xlsm", "id": "file123"}

        with patch("builtins.print"):  # Suppress print output
            result = populator.process_daqbook_file(file_info)

        assert result == 0

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_populate_all_daqbook_data_success(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test complete data population process."""
        populator = DaqbookDataPopulator()

        with (
            patch.object(populator, "search_daqbook_files") as mock_search,
            patch.object(populator, "process_daqbook_file") as mock_process,
            patch("builtins.print"),
        ):

            mock_search.return_value = [
                {"name": "J1_0325.xlsm", "id": "file1"},
                {"name": "J2_0326.xlsm", "id": "file2"},
            ]
            mock_process.side_effect = [5, 3]  # Return different record counts

            result = populator.populate_all_daqbook_data()

            expected = {"files_found": 2, "files_processed": 2, "total_records": 8}
            assert result == expected

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_populate_all_daqbook_data_no_files(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test data population with no files found."""
        populator = DaqbookDataPopulator()

        with (
            patch.object(populator, "search_daqbook_files") as mock_search,
            patch("builtins.print"),
        ):

            mock_search.return_value = []

            result = populator.populate_all_daqbook_data()

            expected = {"files_found": 0, "files_processed": 0, "total_records": 0}
            assert result == expected

    @patch("utils.populate_daqbook_data.create_engine")
    @patch("utils.populate_daqbook_data.sessionmaker")
    @patch("utils.populate_daqbook_data.SharePointClient")
    @patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"})
    def test_populate_all_daqbook_data_processing_errors(
        self, mock_sharepoint_class, mock_sessionmaker, mock_create_engine
    ):
        """Test data population with some processing errors."""
        populator = DaqbookDataPopulator()

        with (
            patch.object(populator, "search_daqbook_files") as mock_search,
            patch.object(populator, "process_daqbook_file") as mock_process,
            patch("builtins.print"),
        ):

            mock_search.return_value = [
                {"name": "J1_0325.xlsm", "id": "file1"},
                {"name": "J2_0326.xlsm", "id": "file2"},
            ]
            mock_process.side_effect = [5, Exception("Processing error")]

            result = populator.populate_all_daqbook_data()

            expected = {"files_found": 2, "files_processed": 1, "total_records": 5}
            assert result == expected

    def test_close(self):
        """Test closing database connection."""
        with (
            patch("utils.populate_daqbook_data.create_engine"),
            patch("utils.populate_daqbook_data.sessionmaker") as mock_sessionmaker,
            patch("utils.populate_daqbook_data.SharePointClient"),
            patch.dict(os.environ, {"DATABASE_URL": "sqlite:///:memory:"}),
        ):

            mock_session = Mock()
            mock_sessionmaker.return_value = Mock(return_value=mock_session)

            populator = DaqbookDataPopulator()
            populator.close()

            mock_session.close.assert_called_once()


class TestMainFunction:
    """Test cases for the main function."""

    @patch("utils.populate_daqbook_data.DaqbookDataPopulator")
    def test_main_success(self, mock_populator_class):
        """Test successful main execution."""
        mock_populator = Mock()
        mock_populator_class.return_value = mock_populator
        mock_populator.populate_all_daqbook_data.return_value = {
            "files_found": 2,
            "files_processed": 2,
            "total_records": 10,
        }

        with patch("builtins.print"), patch("sys.exit") as mock_exit:

            main()

            mock_populator.populate_all_daqbook_data.assert_called_once()
            mock_populator.close.assert_called_once()
            mock_exit.assert_called_once_with(0)

    @patch("utils.populate_daqbook_data.DaqbookDataPopulator")
    def test_main_no_files_processed(self, mock_populator_class):
        """Test main execution with no files processed."""
        mock_populator = Mock()
        mock_populator_class.return_value = mock_populator
        mock_populator.populate_all_daqbook_data.return_value = {
            "files_found": 2,
            "files_processed": 0,
            "total_records": 0,
        }

        with patch("builtins.print"), patch("sys.exit") as mock_exit:

            main()

            mock_populator.close.assert_called_once()
            mock_exit.assert_called_once_with(1)

    @patch("utils.populate_daqbook_data.DaqbookDataPopulator")
    def test_main_exception(self, mock_populator_class):
        """Test main execution with exception."""
        mock_populator_class.side_effect = Exception("Fatal error")

        with patch("builtins.print"), patch("sys.exit") as mock_exit:

            main()

            mock_exit.assert_called_once_with(1)
