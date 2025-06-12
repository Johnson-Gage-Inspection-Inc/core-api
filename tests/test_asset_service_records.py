# tests/test_asset_service_records.py
import os
from datetime import datetime as dt
from unittest.mock import MagicMock, patch

import pytest
from qualer_sdk.rest import ApiException


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Skipping asset service records test when SKIP_AUTH=true (CI environment)",
)
def test_asset_service_record_endpoint_basic(client, auth_token):
    """Basic test to call the asset service records endpoint - useful for debugging with breakpoints."""
    response = client.get(
        "/asset-service-records/1235426",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    # This will likely fail in a real environment without valid data, but useful for debugging
    print(f"Response status: {response.status_code}")
    print(f"Response data: {response.get_json()}")


def test_asset_service_record_endpoint_without_auth(client):
    """Test that unauthenticated requests are rejected"""
    resp = client.get("/asset-service-records/12345")
    assert resp.status_code == 401
    # In SKIP_AUTH mode, we get JSON error response from Flask-Smorest abort()
    if resp.content_type and "application/json" in resp.content_type:
        data = resp.get_json()
        assert "message" in data
        assert "Unauthorized" in data["message"]
    else:
        assert resp.text == "Unauthorized"


@patch("routes.asset_service_records.get_asset_service_records")
@patch("utils.qualer_client.make_qualer_client")
def test_asset_service_record_endpoint_mocked(
    mock_qualer_client, mock_get_asset_service_records, client, auth_token
):
    """Test asset service records endpoint with mocked Qualer client for CI environments."""
    # Create a list of mock asset service records that behave like SDK objects
    mock_asset_service_record1 = MagicMock()
    mock_asset_service_record1.to_dict.return_value = {
        "AssetServiceRecordId": 1001,
        "AssetId": 12345,
        "ServiceDate": dt.fromisoformat("2023-01-01T00:00:00Z"),
        "ResultStatus": "Pass",
        "SerialNumber": "SN123456",
        "AssetName": "Test Asset",
        "ServiceType": "Calibration",
        "TechnicianName": "John Doe",
        "CreatedDateUtc": dt.fromisoformat("2023-01-01T00:00:00Z"),
        "ModifiedDateUtc": dt.fromisoformat("2023-01-01T00:00:00Z"),
    }
    # Add model_dump method for compatibility with new schema serialization
    mock_asset_service_record1.model_dump.return_value = (
        mock_asset_service_record1.to_dict.return_value
    )

    mock_asset_service_record2 = MagicMock()
    mock_asset_service_record2.to_dict.return_value = {
        "AssetServiceRecordId": 1002,
        "AssetId": 12345,
        "ServiceDate": "2023-06-15T09:30:00Z",
        "ResultStatus": "Pass",
        "SerialNumber": "SN123456",
        "AssetName": "Test Asset",
        "ServiceType": "Inspection",
        "TechnicianName": "Jane Smith",
        "CreatedDateUtc": "2023-06-15T09:30:00Z",
        "ModifiedDateUtc": "2023-06-15T09:30:00Z",
    }
    # Add model_dump method for compatibility with new schema serialization
    mock_asset_service_record2.model_dump.return_value = (
        mock_asset_service_record2.to_dict.return_value
    )

    mock_asset_service_records = [
        mock_asset_service_record1,
        mock_asset_service_record2,
    ]

    # Mock the get_asset_service_records function directly
    mock_get_asset_service_records.return_value = mock_asset_service_records

    mock_client = MagicMock()
    mock_qualer_client.return_value = mock_client

    response = client.get(
        "/asset-service-records/12345",
        headers={"Authorization": f"Bearer {auth_token}"},
    )

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
    # We only need to check that we get a list with the right structure
    # The exact fields may vary based on the Qualer SDK object structure

    # Check first record
    assert data[0]["AssetServiceRecordId"] == 1001
    assert data[0]["AssetId"] == 12345

    # Check second record
    assert data[1]["AssetServiceRecordId"] == 1002
    assert data[1]["AssetId"] == 12345


@patch("routes.asset_service_records.asset_service_records")
@patch("utils.qualer_client.make_qualer_client")
def test_asset_service_record_endpoint_not_found(
    mock_qualer_client, mock_asset_service_records_api, client, auth_token
):
    """Test asset service records endpoint when record is not found"""
    # Check if SKIP_AUTH is enabled - in this mode, the mock bindings handle the response
    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        # Test with an ID that triggers 404 in mock bindings (999999 is configured to return 404)
        response = client.get(
            "/asset-service-records/999999",
            headers={"Authorization": f"Bearer {auth_token}"},
        )

        assert response.status_code == 404
        assert "Asset service records not found" in response.get_data(as_text=True)
    else:
        # Normal testing mode with SDK mocks

        # Create a mock API object
        mock_api = MagicMock()
        mock_api.get_asset_service_records_by_asset.side_effect = ApiException(
            status=404, reason="Not Found"
        )
        mock_asset_service_records_api.return_value = mock_api

        mock_client = MagicMock()
        mock_qualer_client.return_value = mock_client

        response = client.get(
            "/asset-service-records/999999",
            headers={"Authorization": f"Bearer {auth_token}"},
        )

        assert response.status_code == 404
        data = response.get_json()
        assert "message" in data
        assert "999999" in data["message"]


@patch("routes.asset_service_records.get_asset_service_records")
@patch("utils.qualer_client.make_qualer_client")
def test_asset_service_record_endpoint_api_error(
    mock_qualer_client, mock_get_asset_service_records, client, auth_token
):
    """Test asset service records endpoint when the Qualer API throws an error"""
    # Check if SKIP_AUTH is enabled
    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        # In SKIP_AUTH mode, we need to temporarily restore the real view function to test error handling
        from app import app
        from routes.asset_service_records import AssetServiceRecord

        # Store the mock function
        mock_function = app.view_functions.get(
            "asset-service-records.AssetServiceRecord"
        )

        try:
            # Restore real view function for this test
            asset_service_record_view = AssetServiceRecord()
            app.view_functions["asset-service-records.AssetServiceRecord"] = (
                asset_service_record_view.get
            )

            # Mock the get_asset_service_records function to raise an exception
            mock_get_asset_service_records.side_effect = Exception("Qualer API Error")

            mock_client = MagicMock()
            mock_client = MagicMock()
            mock_qualer_client.return_value = mock_client

            response = client.get(
                "/asset-service-records/12345",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "message" in data
            assert "error fetching asset service records" in data["message"].lower()

        finally:
            # Restore the mock function
            if mock_function:
                app.view_functions["asset-service-records.AssetServiceRecord"] = (
                    mock_function
                )
            else:
                # Normal testing mode with SDK mocks
                # Mock the get_asset_service_records function to raise an exception
                mock_get_asset_service_records.side_effect = Exception(
                    "Qualer API Error"
                )

                mock_client = MagicMock()
                mock_qualer_client.return_value = mock_client

                response = client.get(
                    "/asset-service-records/12345",
                    headers={"Authorization": f"Bearer {auth_token}"},
                )

                assert response.status_code == 500
                data = response.get_json()
                assert "message" in data
                assert "Error fetching asset service records" in data["message"]
            if mock_function:
                app.view_functions["asset-service-records.AssetServiceRecord"] = (
                    mock_function
                )
    else:  # Normal testing mode
        mock_api = MagicMock()
        mock_api.get_asset_service_records_by_asset.side_effect = ApiException(
            status=500, reason="Internal Server Error"
        )

        mock_client = MagicMock()
        mock_qualer_client.return_value = mock_client

        response = client.get(
            "/asset-service-records/12345",
            headers={"Authorization": f"Bearer {auth_token}"},
        )

        assert response.status_code == 500
        data = response.get_json()
        assert "message" in data
        assert "Error fetching asset service records" in data["message"]


def test_asset_service_record_endpoint_with_auth_skip_mode(client):
    """Test that authenticated requests work in SKIP_AUTH mode"""
    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        # In SKIP_AUTH mode, mock bindings should still enforce Bearer token format
        response = client.get(
            "/asset-service-records/12345",
            headers={"Authorization": "Bearer fake-token"},
        )
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, list)
        assert len(data) == 2  # Verify first record
        assert data[0]["AssetServiceRecordId"] == 1001
        assert data[0]["AssetId"] == 12345

        # Verify second record
        assert data[1]["AssetServiceRecordId"] == 1002
    else:
        # In normal mode, this would require a real auth token, so skip
        pytest.skip("Test only runs in SKIP_AUTH mode")
