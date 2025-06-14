import io
from datetime import datetime
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
from marshmallow import ValidationError

from db.models import WireSetCert
from utils.schemas import WireSetCertResult
from utils.wire_set_cert_refresher import WireSetCertRefresher, refresh_wire_set_certs


@pytest.fixture
def mock_session():
    """Create a mock database session."""
    session = MagicMock()
    session.query.return_value.filter_by.return_value.first.return_value = None
    return session


@pytest.fixture
def mock_sharepoint_client():
    """Create a mock for the native SDK SharePoint client."""
    with patch(
        "utils.wire_set_cert_refresher.download_wiresetcerts_content"
    ) as mock_download:
        mock_download.return_value = b"mock excel data"
        yield mock_download


@pytest.fixture
def sample_excel_data():
    """Create a sample Excel file in memory for testing."""
    # Create a sample DataFrame that matches the expected structure
    data = {
        "asset_id": [1001, 1002, None],
        "serial_number": ["SN001", "SN002", None],
        "asset_tag": ["AT001", "AT002", "AT003"],
        "custom_order_number": ["CO001", "CO002", "CO003"],
        "service_date": [datetime(2023, 1, 1), "2023-02-01", None],
        "next_service_date": [datetime(2024, 1, 1), "2024-02-01", None],
        "certificate_number": ["CERT001", "CERT002", "CERT003"],
        "wire_roll_cert_number": ["WIRE001", "WIRE002", "WIRE003"],
        "type": ["Group A", "Group B", "Group C"],
    }
    df = pd.DataFrame(data)

    # Convert to Excel bytes
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, engine="openpyxl", index=False)
    excel_buffer.seek(0)
    return excel_buffer.getvalue()


@pytest.fixture
def mock_schema():
    """Create a mock schema that simulates validation."""
    with patch("utils.wire_set_cert_refresher.WireSetCertSchema") as mock_schema_class:
        schema_instance = mock_schema_class.return_value

        # Default behavior: successful validation
        def mock_load(data):
            # Ensure serial_number exists to avoid validation errors
            if not data.get("serial_number"):
                raise ValidationError(
                    {"serial_number": ["Missing data for required field."]}
                )
            # Return the data with wire_set_group (mapped from type if needed)
            result = dict(data)
            if "wire_set_group" not in result and "type" in result:
                result["wire_set_group"] = result.pop("type")
            return result

        schema_instance.load.side_effect = mock_load
        yield schema_instance


class TestWireSetCertRefresher:
    """Tests for the WireSetCertRefresher class."""

    def test_init(self, mock_session):
        """Test initializing the refresher with and without a session."""
        # Test with provided session
        refresher = WireSetCertRefresher(session=mock_session)
        assert refresher.session == mock_session

        # Test with default session (would create a new one)
        with patch("utils.wire_set_cert_refresher.SessionLocal") as mock_session_local:
            mock_session_local.return_value = mock_session
            refresher = WireSetCertRefresher()
            assert refresher.session == mock_session

    @patch("utils.wire_set_cert_refresher.download_wiresetcerts_content")
    def test_download_wiresetcerts_file_success(self, mock_download_wiresetcerts):
        """Test successful download of WireSetCerts.xlsx file."""
        # Mock the download function
        mock_download_wiresetcerts.return_value = b"mock excel data"

        refresher = WireSetCertRefresher(MagicMock())

        # Call the method
        result = refresher._download_wiresetcerts_file()

        # Verify the result
        assert result == b"mock excel data"
        mock_download_wiresetcerts.assert_called_once()

    def test_download_wiresetcerts_file_not_found(self):
        """Test handling when WireSetCerts.xlsx file is not found."""
        refresher = WireSetCertRefresher(MagicMock())

        with patch(
            "utils.wire_set_cert_refresher.download_wiresetcerts_content"
        ) as mock_download:
            # Simulate file not found - raise an exception that would be typical for file not found
            mock_download.side_effect = FileNotFoundError("WireSetCerts.xlsx not found")

            # Call the method
            result = refresher._download_wiresetcerts_file()

            # Verify the result
            assert result is None

    def test_download_wiresetcerts_file_error(self):
        """Test error handling during file download."""
        refresher = WireSetCertRefresher(MagicMock())

        with patch(
            "utils.wire_set_cert_refresher.download_wiresetcerts_content"
        ) as mock_download:
            # Simulate exception during download
            mock_download.side_effect = Exception("Connection error")

            # Call the method
            result = refresher._download_wiresetcerts_file()

            # Verify the result
            assert result is None

    def test_parse_wiresetcerts_excel_success(self, sample_excel_data, mock_schema):
        """Test successful parsing of Excel data."""
        refresher = WireSetCertRefresher(MagicMock())

        # Patch pandas.read_excel to return a controlled DataFrame
        with patch("pandas.read_excel") as mock_read_excel:
            # Create a sample DataFrame that matches the expected structure
            data = {
                "asset_id": [1001, 1002],
                "serial_number": ["SN001", "SN002"],
                "asset_tag": ["AT001", "AT002"],
                "custom_order_number": ["CO001", "CO002"],
                "service_date": [datetime(2023, 1, 1), datetime(2023, 2, 1)],
                "next_service_date": [datetime(2024, 1, 1), datetime(2024, 2, 1)],
                "certificate_number": ["CERT001", "CERT002"],
                "wire_roll_cert_number": ["WIRE001", "WIRE002"],
                "type": ["Group A", "Group B"],
            }
            df = pd.DataFrame(data)
            mock_read_excel.return_value = df

            # Call the method
            result = refresher._parse_wiresetcerts_excel(sample_excel_data)

            # Verify the result
            assert len(result) == 2
            assert result[0]["serial_number"] == "SN001"
            assert result[1]["serial_number"] == "SN002"
            # Check if type was correctly mapped to wire_set_group
            assert "wire_set_group" in result[0]
            assert result[0]["wire_set_group"] == "Group A"

    def test_parse_wiresetcerts_excel_missing_required_columns(self):
        """Test handling when required columns are missing."""
        refresher = WireSetCertRefresher(MagicMock())

        # Patch pandas.read_excel to return a DataFrame missing required columns
        with patch("pandas.read_excel") as mock_read_excel:
            # Create a DataFrame missing serial_number
            data = {
                "asset_id": [1001, 1002],
                "asset_tag": ["AT001", "AT002"],
                "type": ["Group A", "Group B"],
            }
            df = pd.DataFrame(data)
            mock_read_excel.return_value = df

            # Call the method
            result = refresher._parse_wiresetcerts_excel(b"mock excel data")

            # Verify the result
            assert result == []

    def test_parse_wiresetcerts_excel_validation_errors(self):
        """Test handling validation errors during Excel parsing."""
        refresher = WireSetCertRefresher(MagicMock())

        # Patch pandas.read_excel to return a DataFrame with invalid data
        with patch("pandas.read_excel") as mock_read_excel:
            # Create a DataFrame with one valid row and one with missing serial_number
            data = {
                "asset_id": [1001, 1002],
                "serial_number": ["SN001", None],  # Second row has None serial_number
                "asset_tag": ["AT001", "AT002"],
                "type": ["Group A", "Group B"],
            }
            df = pd.DataFrame(data)
            mock_read_excel.return_value = df

            # Call the method
            result = refresher._parse_wiresetcerts_excel(b"mock excel data")

            # Verify the result - should only include the valid row
            assert len(result) == 1
            assert result[0]["serial_number"] == "SN001"

    def test_update_wire_set_certs_table_new_records(self, mock_session):
        """Test adding new records to the database."""
        refresher = WireSetCertRefresher(mock_session)

        # Prepare test data
        mappings = [
            {
                "serial_number": "SN001",
                "wire_set_group": "Group A",
                "asset_id": 1001,
                "asset_tag": "AT001",
            },
            {
                "serial_number": "SN002",
                "wire_set_group": "Group B",
                "asset_id": 1002,
                "asset_tag": "AT002",
            },
        ]

        # Configure the mock session to indicate records don't exist
        mock_session.query.return_value.filter_by.return_value.first.return_value = None

        # Call the method
        result = refresher._update_wire_set_certs_table(mappings)

        # Verify the result
        assert result.status == "success"
        assert result.records_processed == 2
        assert result.records_added == 2
        assert result.records_updated == 0

        # Verify session operations
        assert mock_session.add.call_count == 2
        mock_session.commit.assert_called_once()

    def test_update_wire_set_certs_table_existing_records(self, mock_session):
        """Test updating existing records in the database."""
        refresher = WireSetCertRefresher(mock_session)

        # Prepare test data
        mappings = [
            {
                "serial_number": "SN001",
                "wire_set_group": "Group A",
                "asset_id": 1001,
                "asset_tag": "AT001",
            }
        ]

        # Configure the mock session to return an existing record
        existing_record = MagicMock(spec=WireSetCert)
        existing_record.serial_number = "SN001"
        existing_record.wire_set_group = "Old Group"
        existing_record.asset_id = 999
        mock_session.query.return_value.filter_by.return_value.first.return_value = (
            existing_record
        )

        # Mock the _update_existing_record method to indicate changes
        with patch.object(refresher, "_update_existing_record", return_value=True):
            # Call the method
            result = refresher._update_wire_set_certs_table(mappings)

            # Verify the result
            assert result.status == "success"
            assert result.records_processed == 1
            assert result.records_added == 0
            assert result.records_updated == 1

            # Verify session operations
            mock_session.commit.assert_called_once()

    def test_update_wire_set_certs_table_error(self, mock_session):
        """Test error handling during database update."""
        refresher = WireSetCertRefresher(mock_session)

        # Prepare test data
        mappings = [{"serial_number": "SN001", "wire_set_group": "Group A"}]

        # Configure the mock session to raise an exception
        mock_session.commit.side_effect = Exception("Database error")

        # Call the method
        result = refresher._update_wire_set_certs_table(mappings)

        # Verify the result
        assert result.status == "error"
        assert "Database update failed" in result.message
        assert len(result.errors) == 1

        # Verify session operations
        mock_session.rollback.assert_called_once()

    def test_update_existing_record(self):
        """Test updating an existing record with new values."""
        refresher = WireSetCertRefresher(MagicMock())

        # Create an existing record with some values
        existing = MagicMock(spec=WireSetCert)
        existing.serial_number = "SN001"
        existing.wire_set_group = "Old Group"
        existing.asset_id = 999
        existing.asset_tag = "AT999"

        # Create new data with changes
        new_data = {
            "serial_number": "SN001",
            "wire_set_group": "New Group",
            "asset_id": 1001,
            "asset_tag": "AT999",  # Same as existing
        }

        # Call the method
        updated = refresher._update_existing_record(existing, new_data)

        # Verify the result
        assert updated is True
        assert existing.wire_set_group == "New Group"
        assert existing.asset_id == 1001
        assert existing.asset_tag == "AT999"  # Unchanged

    def test_update_existing_record_no_changes(self):
        """Test when no changes are detected in an existing record."""
        refresher = WireSetCertRefresher(MagicMock())

        # Create an existing record
        existing = MagicMock(spec=WireSetCert)
        existing.serial_number = "SN001"
        existing.wire_set_group = "Group A"
        existing.asset_id = 1001

        # Create new data with identical values
        new_data = {
            "serial_number": "SN001",
            "wire_set_group": "Group A",
            "asset_id": 1001,
        }

        # Call the method
        updated = refresher._update_existing_record(existing, new_data)

        # Verify the result
        assert updated is False

    def test_insert_new_record(self, mock_session):
        """Test inserting a new record into the database."""
        refresher = WireSetCertRefresher(mock_session)

        # Create new data
        new_data = {
            "serial_number": "SN001",
            "wire_set_group": "Group A",
            "asset_id": 1001,
            "asset_tag": "AT001",
            "custom_order_number": "CO001",
            "service_date": datetime(2023, 1, 1),
            "next_service_date": datetime(2024, 1, 1),
            "certificate_number": "CERT001",
            "wire_roll_cert_number": "WIRE001",
        }

        # Call the method
        refresher._insert_new_record(new_data)

        # Verify the session operations
        mock_session.add.assert_called_once()
        # Check that the added object has the correct properties
        added_obj = mock_session.add.call_args[0][0]
        assert isinstance(added_obj, WireSetCert)
        assert added_obj.serial_number == "SN001"
        assert added_obj.wire_set_group == "Group A"
        assert added_obj.asset_id == 1001

    def test_parse_field_value_datetime(self):
        """Test parsing different datetime formats."""
        refresher = WireSetCertRefresher(MagicMock())

        # Test with actual datetime object
        dt = datetime(2023, 1, 1)
        assert refresher._parse_field_value("service_date", dt) == dt

        # Test with ISO format string
        assert refresher._parse_field_value("service_date", "2023-01-01") == datetime(
            2023, 1, 1
        )

        # Test with US format string
        assert refresher._parse_field_value("service_date", "01/01/2023") == datetime(
            2023, 1, 1
        )

        # Test with invalid date string
        assert refresher._parse_field_value("service_date", "invalid-date") is None

        # Test with empty string
        assert refresher._parse_field_value("service_date", "") is None

        # Test with None
        assert refresher._parse_field_value("service_date", None) is None

    def test_parse_field_value_asset_id(self):
        """Test parsing asset_id field values."""
        refresher = WireSetCertRefresher(MagicMock())

        # Test with integer
        assert refresher._parse_field_value("asset_id", 1001) == 1001

        # Test with float
        assert refresher._parse_field_value("asset_id", 1001.0) == 1001

        # Test with string number
        assert refresher._parse_field_value("asset_id", "1001") == 1001

        # Test with invalid string
        assert refresher._parse_field_value("asset_id", "not-a-number") is None

        # Test with empty string
        assert refresher._parse_field_value("asset_id", "") is None

        # Test with None
        assert refresher._parse_field_value("asset_id", None) is None

    def test_parse_field_value_string_fields(self):
        """Test parsing string field values."""
        refresher = WireSetCertRefresher(MagicMock())

        # Test with string
        assert refresher._parse_field_value("serial_number", "SN001") == "SN001"

        # Test with number
        assert refresher._parse_field_value("serial_number", 1001) == "1001"

        # Test with whitespace
        assert refresher._parse_field_value("serial_number", "  SN001  ") == "SN001"

        # Test with empty string
        assert refresher._parse_field_value("serial_number", "") is None

        # Test with None
        assert refresher._parse_field_value("serial_number", None) is None

    def test_refresh_wire_set_certs_success(
        self, mock_session, sample_excel_data, mock_sharepoint_client
    ):
        """Test the full refresh process with successful execution."""
        refresher = WireSetCertRefresher(mock_session)

        # Mock the internal methods to control the flow
        with patch.object(
            refresher, "_download_wiresetcerts_file", return_value=sample_excel_data
        ):
            with patch.object(refresher, "_parse_wiresetcerts_excel") as mock_parse:
                with patch.object(
                    refresher, "_update_wire_set_certs_table"
                ) as mock_update:
                    # Configure the mocks
                    parsed_data = [
                        {"serial_number": "SN001", "wire_set_group": "Group A"},
                        {"serial_number": "SN002", "wire_set_group": "Group B"},
                    ]
                    mock_parse.return_value = parsed_data

                    update_result = WireSetCertResult(
                        status="success",
                        message="",
                        records_processed=2,
                        records_added=1,
                        records_updated=1,
                        errors=[],
                    )
                    mock_update.return_value = update_result

                    # Call the method
                    result = refresher.refresh_wire_set_certs()

                    # Verify the result
                    assert result.status == "success"
                    assert result.records_processed == 2
                    assert result.records_added == 1
                    assert result.records_updated == 1

                    # Verify method calls
                    mock_parse.assert_called_once_with(sample_excel_data)
                    mock_update.assert_called_once_with(parsed_data)

    def test_refresh_wire_set_certs_download_failure(self, mock_session):
        """Test handling when the file download fails."""
        refresher = WireSetCertRefresher(mock_session)

        # Mock the download method to return None (failure)
        with patch.object(refresher, "_download_wiresetcerts_file", return_value=None):
            # Call the method
            result = refresher.refresh_wire_set_certs()

            # Verify the result
            assert result.status == "error"
            assert "Failed to download" in result.message

    def test_refresh_wire_set_certs_no_mappings(self, mock_session, sample_excel_data):
        """Test handling when no valid mappings are found in the Excel file."""
        refresher = WireSetCertRefresher(mock_session)

        # Mock the methods to simulate download success but parsing returns empty list
        with patch.object(
            refresher, "_download_wiresetcerts_file", return_value=sample_excel_data
        ):
            with patch.object(refresher, "_parse_wiresetcerts_excel", return_value=[]):
                # Call the method
                result = refresher.refresh_wire_set_certs()

                # Verify the result
                assert result.status == "warning"
                assert "No wire set mappings found" in result.message

    def test_refresh_wire_set_certs_exception(self, mock_session):
        """Test handling of unexpected exceptions during refresh."""
        refresher = WireSetCertRefresher(mock_session)

        # Mock the download method to raise an exception
        with patch.object(
            refresher,
            "_download_wiresetcerts_file",
            side_effect=Exception("Test error"),
        ):
            # Call the method
            result = refresher.refresh_wire_set_certs()

            # Verify the result
            assert result.status == "error"
            assert "Refresh failed" in result.message
            assert len(result.errors) == 1
            assert "Test error" in result.errors[0]


def test_refresh_wire_set_certs_convenience_function():
    """Test the convenience function that creates and closes the refresher."""
    # Mock the WireSetCertRefresher class
    with patch(
        "utils.wire_set_cert_refresher.WireSetCertRefresher"
    ) as mock_refresher_class:
        # Configure the mock instance
        mock_instance = mock_refresher_class.return_value
        expected_result = WireSetCertResult(
            status="success",
            message="Test result",
            records_processed=5,
            records_added=3,
            records_updated=2,
            errors=[],
        )
        mock_instance.refresh_wire_set_certs.return_value = expected_result

        # Call the convenience function
        result = refresh_wire_set_certs()

        # Verify the result
        assert result == expected_result

        # Verify that the session was closed
        mock_instance.session.close.assert_called_once()
        # Verify that the session was closed
        mock_instance.session.close.assert_called_once()
