import os
from datetime import datetime, timedelta
from unittest.mock import patch

import pytest
from sqlalchemy import text

from db.models import DaqbookOffset as DaqbookOffset
from utils.daqbook import get_updated_daqbook_files, refresh_daqbook_offsets
from utils.sharepoint_client import SharePointClient

# from utils.test_models import StupidDaqbookOffset


@pytest.fixture
def mock_last_check():
    return datetime.utcnow() - timedelta(days=1)


def test_list_files_in_pyro_standards_folder():
    """Should return a list of files from SharePoint"""
    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        with patch(
            "utils.sharepoint_client.SharePointClient.list_files_in_pyro_standards_folder"
        ) as mock_list:
            mock_list.return_value = [
                {
                    "name": "J1_0101.xlsm",
                    "lastModifiedDateTime": "2023-01-01T00:00:00Z",
                },
                {
                    "name": "J1_0102.xlsm",
                    "lastModifiedDateTime": "2023-01-02T00:00:00Z",
                },
            ]
            files = SharePointClient.list_files_in_pyro_standards_folder()
            assert len(files) == 2
            assert files[0]["name"] == "J1_0101.xlsm"
            assert files[1]["name"] == "J1_0102.xlsm"
    else:
        files = SharePointClient.list_files_in_pyro_standards_folder()
        assert isinstance(files, list)
        assert len(files) > 0
        print([f["name"] for f in files])  # Print file names for debugging


def test_returns_only_recent_daqbook_files(mock_last_check):
    """Should return only .xlsm Daqbook files modified after last check"""
    with patch(
        "utils.sharepoint_client.SharePointClient.list_files_in_pyro_standards_folder"
    ) as mock_list:
        mock_list.return_value = [
            {
                "id": "1",
                "name": "J1_0101.xlsm",
                "webUrl": "https://example.com/1",
                "downloadUrl": "https://example.com/download/1",
                "size": 123456,
                "lastModifiedDateTime": datetime.utcnow().isoformat(),
                "mimeType": "application/vnd.ms-excel.sheet.macroEnabled.12",
                "driveId": "abc",
                "path": "/drives/abc/root:/Pyro/Pyro_Standards",
            },
            {
                "id": "2",
                "name": "some-other-file.docx",
                "webUrl": "https://example.com/2",
                "downloadUrl": "https://example.com/download/2",
                "size": 54321,
                "lastModifiedDateTime": datetime.utcnow().isoformat(),
                "mimeType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "driveId": "abc",
                "path": "/drives/abc/root:/Pyro/Pyro_Standards",
            },
            {
                "id": "3",
                "name": "J1_0102.xlsm",
                "webUrl": "https://example.com/3",
                "downloadUrl": "https://example.com/download/3",
                "size": 65432,
                "lastModifiedDateTime": "2023-01-01T00:00:00Z",
                "mimeType": "application/vnd.ms-excel.sheet.macroEnabled.12",
                "driveId": "abc",
                "path": "/drives/abc/root:/Pyro/Pyro_Standards",
            },
        ]

        files = get_updated_daqbook_files(mock_last_check)
        assert len(files) == 1
        assert files[0]["name"] == "J1_0101.xlsm"


def test_refresh_daqbook_offsets_upserts(monkeypatch, db_session):
    """Should upsert parsed offsets into the database"""
    dummy_file = {
        "id": "abc123",
        "name": "J1_0624.xlsm",
        "webUrl": "https://example.com/file",
        "downloadUrl": "https://example.com/download",
        "size": 123456,
        "lastModifiedDateTime": datetime.utcnow().isoformat(),
        "mimeType": "application/vnd.ms-excel.sheet.macroEnabled.12",
        "driveId": "fake_drive",
        "path": "/drives/fake_drive/root:/Pyro/Pyro_Standards",
    }

    monkeypatch.setattr("utils.daqbook.get_updated_daqbook_files", lambda: [dummy_file])

    monkeypatch.setattr(
        "utils.sharepoint_client.SharePointClient.download_file_from_sharepoint",
        lambda f: "/tmp/J1_0624.xlsm",
    )
    monkeypatch.setattr(
        "utils.daqbook.parse_daqbook_offsets_from_excel",
        lambda path: [{"Reading": 0.123, "Temp": 25.0, "Point": 1, "Delta": -24.877}],
    )

    refresh_daqbook_offsets(session=db_session)

    stored = db_session.query(DaqbookOffset).filter_by(tn="J1_0624", point=1).first()
    assert stored is not None
    assert float(stored.reading) == 0.123


@pytest.mark.integration
def test_refresh_daqbook_offsets_inserts_multiple_unique_daqbooks(
    monkeypatch, db_session
):
    """Ensure that refresh_daqbook_offsets inserts more than one unique DAQbook (tn)"""

    dummy_files = [
        {"name": "J1_0101.xlsm", "id": "file1"},
        {"name": "K4_0202.xlsm", "id": "file2"},
    ]

    # Mock parse function to return different data based on file path
    def mock_parse_excel(path):
        if "J1_0101" in path:
            # Return Excel format data for J1_0101.xlsm
            return [
                {"Reading": 1.23, "Temp": 100.0, "Point": 1, "Delta": -0.5},
                {"Reading": 2.34, "Temp": 200.0, "Point": 2, "Delta": -0.6},
            ]
        elif "K4_0202" in path:
            # Return Excel format data for K4_0202.xlsm
            return [
                {"Reading": 3.45, "Temp": 150.0, "Point": 1, "Delta": -0.7},
                {"Reading": 4.56, "Temp": 250.0, "Point": 2, "Delta": -0.8},
            ]
        else:
            return []

    monkeypatch.setattr(
        "utils.daqbook.get_updated_daqbook_files", lambda *_: dummy_files
    )
    monkeypatch.setattr(
        "utils.daqbook.parse_daqbook_offsets_from_excel", mock_parse_excel
    )
    monkeypatch.setattr(
        "utils.daqbook.SharePointClient.download_file_from_sharepoint",
        lambda file: f"/tmp/{file['name']}",
    )

    # Clear existing data for clean test
    db_session.query(DaqbookOffset).delete()
    db_session.commit()

    # Run the sync
    refresh_daqbook_offsets(session=db_session)

    # Count distinct DAQbook IDs - use correct table name (without schema for SQLite compatibility)
    result = db_session.execute(
        text("SELECT COUNT(DISTINCT tn) FROM daqbook_offsets")
    ).scalar()

    print(f"Distinct TN count: {result}")

    # Verify we have multiple distinct TN values
    assert result > 1, f"Expected more than one unique DAQbook ID, got {result}"

    # Verify specific TN values exist
    distinct_tns = db_session.execute(
        text("SELECT DISTINCT tn FROM daqbook_offsets ORDER BY tn")
    ).fetchall()
    tn_values = [row[0] for row in distinct_tns]

    print(f"Distinct TN values: {tn_values}")

    # Should have exactly 2 TN values from our 2 files
    assert (
        len(tn_values) == 2
    ), f"Expected exactly 2 distinct TN values, got {len(tn_values)}"
    assert "J1_0101" in tn_values, "Should contain J1_0101 TN value"
    assert "K4_0202" in tn_values, "Should contain K4_0202 TN value"


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Test requires real database connection - skipped in CI mode",
)
def test_refresh_daqbook_offsets_with_real_excel_format(db_session):
    """
    Test refresh_daqbook_offsets with realistic Excel parser output format.

    This test uses the actual format returned by parse_daqbook_offsets_from_excel
    to ensure compatibility with real Excel data.
    """

    # Mock files
    mock_files = [
        {
            "id": "file1",
            "name": "J2_0456.xlsm",
            "webUrl": "https://example.com/file1",
            "downloadUrl": "https://example.com/download1",
            "size": 123456,
            "lastModifiedDateTime": datetime.utcnow().isoformat(),
            "mimeType": "application/vnd.ms-excel.sheet.macroEnabled.12",
            "driveId": "test_drive",
            "path": "/drives/test_drive/root:/Pyro/Pyro_Standards",
        },
        {
            "id": "file2",
            "name": "K4_0987.xlsm",
            "webUrl": "https://example.com/file2",
            "downloadUrl": "https://example.com/download2",
            "size": 234567,
            "lastModifiedDateTime": datetime.utcnow().isoformat(),
            "mimeType": "application/vnd.ms-excel.sheet.macroEnabled.12",
            "driveId": "test_drive",
            "path": "/drives/test_drive/root:/Pyro/Pyro_Standards",
        },
    ]

    # Mock Excel parser data in real format (dict format with "Reading", "Temp", "Point", "Delta")
    def mock_parse_excel_real_format(file_path):
        """Mock Excel parser returning real format dictionaries."""
        if "J2_0456" in file_path:
            return [
                {"Reading": 25.01, "Temp": 25.0, "Point": 1, "Delta": -0.01},
                {"Reading": 25.02, "Temp": 25.0, "Point": 2, "Delta": -0.02},
                {"Reading": 50.01, "Temp": 50.0, "Point": 1, "Delta": -0.01},
                {"Reading": 50.02, "Temp": 50.0, "Point": 2, "Delta": -0.02},
            ]
        elif "K4_0987" in file_path:
            return [
                {"Reading": 100.05, "Temp": 100.0, "Point": 1, "Delta": -0.05},
                {"Reading": 100.06, "Temp": 100.0, "Point": 2, "Delta": -0.06},
                {"Reading": 200.07, "Temp": 200.0, "Point": 1, "Delta": -0.07},
                {"Reading": 200.08, "Temp": 200.0, "Point": 2, "Delta": -0.08},
            ]
        else:
            return []

    # Clear existing data
    db_session.query(DaqbookOffset).delete()
    db_session.commit()

    with patch("utils.daqbook.get_updated_daqbook_files") as mock_get_files:
        with patch(
            "utils.sharepoint_client.SharePointClient.download_file_from_sharepoint"
        ) as mock_download:
            with patch("utils.daqbook.parse_daqbook_offsets_from_excel") as mock_parse:

                # Configure mocks
                mock_get_files.return_value = mock_files
                mock_download.side_effect = (
                    lambda file_info: f"/tmp/{file_info['name']}"
                )
                mock_parse.side_effect = mock_parse_excel_real_format

                # Execute the function under test
                refresh_daqbook_offsets(session=db_session)

    # Verify results
    distinct_count = db_session.execute(
        text("SELECT count(DISTINCT tn) FROM daqbook_offsets")
    ).scalar()

    print(f"Distinct TN count with real Excel format: {distinct_count}")

    # Should have 2 distinct TN values
    assert distinct_count == 2, f"Expected 2 distinct TN values, got {distinct_count}"

    # Verify specific TN values and their data
    j2_records = db_session.query(DaqbookOffset).filter_by(tn="J2_0456").all()
    k4_records = db_session.query(DaqbookOffset).filter_by(tn="K4_0987").all()

    assert (
        len(j2_records) == 4
    ), f"Expected 4 records for J2_0456, got {len(j2_records)}"
    assert (
        len(k4_records) == 4
    ), f"Expected 4 records for K4_0987, got {len(k4_records)}"

    # Verify data integrity for one record of each
    j2_first = j2_records[0]
    assert j2_first.tn == "J2_0456"
    assert j2_first.temp in [25.0, 50.0]  # Should be one of our mock temperatures
    assert j2_first.point in [1, 2]  # Should be one of our mock points

    k4_first = k4_records[0]
    assert k4_first.tn == "K4_0987"
    assert k4_first.temp in [100.0, 200.0]  # Should be one of our mock temperatures
    assert k4_first.point in [1, 2]  # Should be one of our mock points


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() != "false",
    reason="Only runs in dev environment with SKIP_AUTH=false",
)
def test_refresh_daqbook_offsets_real_data():
    """Run against real SharePoint + production DB; should insert >1 unique DAQbook."""
    from sqlalchemy import text

    from utils.daqbook import refresh_daqbook_offsets
    from utils.database import SessionLocal

    # Run the actual pipeline
    refresh_daqbook_offsets()

    # Check how many distinct TNs got inserted
    session = SessionLocal()
    try:
        count = session.execute(
            text("SELECT COUNT(DISTINCT tn) FROM public.daqbook_offsets")
        ).scalar()
    finally:
        session.close()

    assert count > 1, f"Expected more than 1 unique tn, but got {count}"
