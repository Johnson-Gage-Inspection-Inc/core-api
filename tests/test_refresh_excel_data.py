import os
from unittest.mock import patch

import pytest

from app import app
from routes.refresh_excel_data import ExcelRefresh

# tests/test_refresh_excel_data.py
"""
Tests for the refresh Excel data endpoint.
"""


class TestRefreshExcelData:
    """Test suite for the refresh Excel data endpoint."""

    def test_refresh_excel_data_success(self, client, auth_token):
        """Test successful refresh of Excel data."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # Mock the refresh function for integration test
            with patch(
                "routes.refresh_excel_data.refresh_all_updated_categories"
            ) as mock_refresh:
                mock_refresh.return_value = {
                    "summary": "Refreshed 3 categories successfully",
                    "categories_updated": [
                        "WireSetCerts",
                        "WireOffsets",
                        "DaqbookOffsets",
                    ],
                    "files_processed": 15,
                    "status": "success",
                    "details": {
                        "WireSetCerts": {"status": "success", "files": 1},
                        "WireOffsets": {"status": "success", "files": 8},
                        "DaqbookOffsets": {"status": "success", "files": 6},
                    },
                }

                response = client.post(
                    "/refresh-excel-data/",
                    headers={"Authorization": f"Bearer {auth_token}"},
                )

                assert response.status_code == 200
                data = response.get_json()
                assert data["status"] == "success"
                assert "summary" in data
                assert "categories_updated" in data
                mock_refresh.assert_called_once()
        else:
            # In mock mode, just verify the endpoint exists and returns data
            response = client.post(
                "/refresh-excel-data/",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 200
            data = response.get_json()
            assert "summary" in data or "status" in data

    def test_refresh_excel_data_partial_failure(self, client, auth_token):
        """Test partial failure during refresh operation."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # Temporarily restore real view function to test error handling
            original_view_func = None

            try:
                original_view_func = app.view_functions.get(
                    "refresh_excel_data.ExcelRefresh"
                )
                app.view_functions["refresh_excel_data.ExcelRefresh"] = (
                    ExcelRefresh().post
                )

                with patch(
                    "routes.refresh_excel_data.refresh_all_updated_categories"
                ) as mock_refresh:
                    mock_refresh.return_value = {
                        "summary": "Partial refresh: 2 of 3 categories updated",
                        "categories_updated": ["WireSetCerts", "WireOffsets"],
                        "files_processed": 9,
                        "status": "partial",
                        "details": {
                            "WireSetCerts": {"status": "success", "files": 1},
                            "WireOffsets": {"status": "success", "files": 8},
                            "DaqbookOffsets": {
                                "status": "error",
                                "error": "Access denied",
                            },
                        },
                    }

                    response = client.post(
                        "/refresh-excel-data/",
                        headers={"Authorization": f"Bearer {auth_token}"},
                    )

                    assert response.status_code == 200
                    data = response.get_json()
                    assert data["status"] == "partial"
                    assert len(data["categories_updated"]) == 2

            finally:
                if original_view_func:
                    app.view_functions["refresh_excel_data.ExcelRefresh"] = (
                        original_view_func
                    )

    def test_refresh_excel_data_complete_failure(self, client, auth_token):
        """Test complete failure during refresh operation."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # Temporarily restore real view function to test error handling
            original_view_func = None

            try:
                original_view_func = app.view_functions.get(
                    "refresh_excel_data.ExcelRefresh"
                )
                app.view_functions["refresh_excel_data.ExcelRefresh"] = (
                    ExcelRefresh().post
                )

                with patch(
                    "routes.refresh_excel_data.refresh_all_updated_categories"
                ) as mock_refresh:
                    mock_refresh.side_effect = Exception("SharePoint connection failed")

                    response = client.post(
                        "/refresh-excel-data/",
                        headers={"Authorization": f"Bearer {auth_token}"},
                    )

                    # Should return 500 for unhandled exception
                    assert response.status_code == 500

            finally:
                if original_view_func:
                    app.view_functions["refresh_excel_data.ExcelRefresh"] = (
                        original_view_func
                    )

    def test_refresh_excel_data_unauthorized(self, client):
        """Test unauthorized access to refresh endpoint."""
        response = client.post("/refresh-excel-data/")

        assert response.status_code == 401

    def test_refresh_excel_data_invalid_token(self, client):
        """Test access with invalid token."""
        response = client.post(
            "/refresh-excel-data/", headers={"Authorization": "Bearer invalid_token"}
        )

        assert response.status_code == 401

    def test_refresh_excel_data_wrong_method(self, client, auth_token):
        """Test that GET method is not allowed."""
        response = client.get(
            "/refresh-excel-data/", headers={"Authorization": f"Bearer {auth_token}"}
        )

        assert response.status_code == 405

    @pytest.mark.skipif(
        os.getenv("SKIP_AUTH", "false").lower() == "true",
        reason="Skipped when SKIP_AUTH=true - mock doesn't test real refresh logic",
    )
    def test_refresh_excel_data_no_updates_needed(self, client, auth_token):
        """Test when no files need updating (all files are current)."""
        with patch(
            "routes.refresh_excel_data.refresh_all_updated_categories"
        ) as mock_refresh:
            mock_refresh.return_value = {
                "summary": "No updates needed - all files are current",
                "categories_updated": [],
                "files_processed": 0,
                "status": "success",
                "details": {
                    "WireSetCerts": {"status": "current", "files": 0},
                    "WireOffsets": {"status": "current", "files": 0},
                    "DaqbookOffsets": {"status": "current", "files": 0},
                },
            }

            response = client.post(
                "/refresh-excel-data/",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 200
            data = response.get_json()
            assert data["status"] == "success"
            assert data["files_processed"] == 0
            assert len(data["categories_updated"]) == 0

    @pytest.mark.skipif(
        os.getenv("SKIP_AUTH", "false").lower() == "false",
        reason="Only run in mock mode to verify endpoint structure",
    )
    def test_refresh_excel_data_mock_mode(self, client, auth_token):
        """Test that the endpoint works correctly in mock mode."""
        response = client.post(
            "/refresh-excel-data/", headers={"Authorization": f"Bearer {auth_token}"}
        )

        assert response.status_code == 200
        data = response.get_json()

        # Verify mock response structure
        assert isinstance(data, dict)
        # Mock should return some form of status or summary
        assert any(key in data for key in ["status", "summary", "message"])
