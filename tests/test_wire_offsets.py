# tests/test_wire_offsets.py
import os
from datetime import datetime
from unittest.mock import MagicMock, patch

import pytest

from db.models import WireOffset, WireSetCert
from utils.database import SessionLocal


class TestWireOffsetModel:
    """Test WireOffset model functionality."""

    def test_wire_offset_model_creation(self):
        """Test creating a WireOffset model instance."""
        # TODO: Update test for append-only model with timestamp
        wire_offset = WireOffset(
            wirelot="123456A",
            block="Top",
            col1=1.1,
            col2=2.2,
            col3=3.3,
            col4=4.4,
            col5=5.5,
            created_at=datetime.now(),
        )

        assert wire_offset.wirelot == "123456A"
        assert wire_offset.block == "Top"
        assert wire_offset.col1 == 1.1
        assert wire_offset.col2 == 2.2
        assert wire_offset.col3 == 3.3
        assert wire_offset.col4 == 4.4
        assert wire_offset.col5 == 5.5
        assert wire_offset.created_at is not None

    def test_wire_offset_repr(self):
        """Test WireOffset string representation."""
        # TODO: Update expected repr for new model structure
        created_at = datetime(2025, 6, 4, 12, 0, 0)
        wire_offset = WireOffset(
            id=1,
            wirelot="123456A",
            block="Top",
            col1=1.1,
            col2=2.2,
            col3=3.3,
            col4=4.4,
            col5=5.5,
            created_at=created_at,
        )

        expected = f"<WireOffset(id=1, wirelot='123456A', block='Top', created_at={created_at})>"
        assert repr(wire_offset) == expected


class TestWireSetCertModel:
    """Test WireSetCert model functionality."""

    def test_wire_set_cert_model_creation(self):
        """Test creating a WireSetCert model instance."""
        # TODO: Test the new WireSetCert model
        cert = WireSetCert(
            serial_number="J201",
            wire_set_group="J201-J214",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        assert cert.serial_number == "J201"
        assert cert.wire_set_group == "J201-J214"
        assert cert.created_at is not None
        assert cert.updated_at is not None

    def test_wire_set_cert_repr(self):
        """Test WireSetCert string representation."""
        cert = WireSetCert(serial_number="J201", wire_set_group="J201-J214")

        expected = "<WireSetCert(serial_number='J201', wire_set_group='J201-J214')>"
        assert repr(cert) == expected


class TestWireOffsetsAPI:
    """Test wire offsets API endpoints."""

    def test_get_all_wire_offsets_success(self, client, auth_token):
        """Test GET /wire-offsets/ returns current wire offset data."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # TODO: This should test the wire_offsets_current view behavior
            response = client.get(
                "/wire-offsets/", headers={"Authorization": f"Bearer {auth_token}"}
            )
            assert response.status_code == 200
            data = response.get_json()
            assert isinstance(data, list)

            # If we have data, verify structure includes new fields
            if data:
                first_item = data[0]
                assert "id" in first_item
                assert "wirelot" in first_item
                assert "block" in first_item
                assert "col1" in first_item
                assert "col2" in first_item
                assert "col3" in first_item
                assert "col4" in first_item
                assert "col5" in first_item
                assert "created_at" in first_item
                assert isinstance(first_item["col1"], (int, float, type(None)))
                assert isinstance(first_item["col2"], (int, float, type(None)))
                assert isinstance(first_item["col3"], (int, float, type(None)))
                assert isinstance(first_item["col4"], (int, float, type(None)))
                assert isinstance(first_item["col5"], (int, float, type(None)))
        else:
            # Mock mode - test the mock response
            response = client.get(
                "/wire-offsets/", headers={"Authorization": f"Bearer {auth_token}"}
            )
            assert response.status_code == 200
            data = response.get_json()
            assert data == []  # Mock returns empty list

    def test_get_wire_offsets_by_wirelot_success(self, client, auth_token):
        """Test GET /wire-offsets/<wirelot> returns current data for wirelot."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
        test_wirelot = "123456A"

        if not skip_auth:
            # TODO: Should test latest-only behavior for the specified wirelot
            response = client.get(
                f"/wire-offsets/{test_wirelot}",
                headers={"Authorization": f"Bearer {auth_token}"},
            )
            assert response.status_code == 200
            data = response.get_json()
            assert isinstance(data, list)

            # All returned items should have the specified wirelot
            for item in data:
                assert item.get("wirelot") == test_wirelot
        else:
            # Mock mode
            response = client.get(
                f"/wire-offsets/{test_wirelot}",
                headers={"Authorization": f"Bearer {auth_token}"},
            )
            assert response.status_code == 200
            data = response.get_json()
            assert (
                data == []
            )  # Mock returns empty list    def test_get_wire_set_certs_success(self, client, auth_token):
        """Test GET /wire-set-certs/ returns certificate mappings."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # When SKIP_AUTH=false, temporarily restore real view function
            # to bypass mock view bindings that may have been registered
            from app import app
            from routes.wire_offsets import WireSetCerts

            original_view_func = None
            endpoint_name = None

            # Find the correct endpoint name for wire set certs
            for rule in app.url_map.iter_rules():
                if rule.rule == "/wire-set-certs/":
                    endpoint_name = rule.endpoint
                    original_view_func = app.view_functions.get(endpoint_name)
                    break

            if endpoint_name and original_view_func:
                # Temporarily restore the real view function
                real_view = WireSetCerts().get
                app.view_functions[endpoint_name] = real_view

            try:
                response = client.get(
                    "/wire-set-certs/",
                    headers={"Authorization": f"Bearer {auth_token}"},
                )
                assert response.status_code == 200
                data = response.get_json()
                assert isinstance(data, list)

                # If we have data, verify structure
                if data:
                    first_item = data[0]
                    assert "id" in first_item
                    assert "serial_number" in first_item
                    assert "wire_set_group" in first_item
                    assert "created_at" in first_item
                    assert "updated_at" in first_item
            finally:
                # Restore the original view function
                if endpoint_name and original_view_func:
                    app.view_functions[endpoint_name] = original_view_func
        else:
            # Mock mode
            response = client.get(
                "/wire-set-certs/", headers={"Authorization": f"Bearer {auth_token}"}
            )
            assert response.status_code == 200
            data = response.get_json()
            assert data == []

    def test_wire_set_certs_refresh_success(self, client, auth_token):
        """Test POST /wire-set-certs/refresh triggers refresh operation."""
        skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

        if not skip_auth:
            # TODO: Test refresh endpoint (currently returns placeholder)
            response = client.post(
                "/wire-set-certs/refresh",
                headers={"Authorization": f"Bearer {auth_token}"},
            )
            assert response.status_code == 200
            data = response.get_json()
            assert "status" in data
            assert "message" in data
            assert "records_processed" in data
            assert "records_added" in data
            assert "records_updated" in data
            assert "errors" in data
        else:
            # Mock mode
            response = client.post(
                "/wire-set-certs/refresh",
                headers={"Authorization": f"Bearer {auth_token}"},
            )
            assert response.status_code == 200

    # TODO: Add tests for authentication failures
    # TODO: Add tests for database error handling
    # TODO: Add tests for the wire_offsets_current view behavior
    # TODO: Add tests for wire set cert refresh with real SharePoint data
    # TODO: Add tests for append-only behavior (multiple records for same wirelot/block)


class TestWireSetCertsParser:
    """Test WireSetCerts.xlsx parsing functionality."""

    def test_parse_wiresetcerts_excel_success(self):
        """Test that we can successfully parse the WireSetCerts.xlsx file."""
        from utils.wire_set_cert_refresher import WireSetCertRefresher

        # Read the test file
        test_file_path = "tests/data/WireSetCerts.xlsx"
        with open(test_file_path, "rb") as f:
            excel_data = f.read()

        # Parse the Excel data
        refresher = WireSetCertRefresher()
        mappings = refresher._parse_wiresetcerts_excel(excel_data)

        # Assertions
        assert len(mappings) > 0, "Should find wire set mappings in the test file"

        # Check that all mappings have required fields
        for mapping in mappings:
            assert "serial_number" in mapping
            assert "wire_set_group" in mapping
            assert mapping["serial_number"] is not None
            assert mapping["wire_set_group"] is not None

        # Check specific expected mappings from the test file
        serial_numbers = [m["serial_number"] for m in mappings]
        wire_set_groups = [m["wire_set_group"] for m in mappings]

        assert "ENV101" in serial_numbers, "Should find ENV101 serial number"
        assert "J01-J24" in serial_numbers, "Should find J01-J24 serial number"
        assert "ENV" in wire_set_groups, "Should find ENV wire set group"
        assert "J" in wire_set_groups, "Should find J wire set group"

        # Find specific mapping
        env_mapping = next(
            (m for m in mappings if m["serial_number"] == "ENV101"), None
        )
        assert env_mapping is not None, "Should find ENV101 mapping"
        assert env_mapping["wire_set_group"] == "ENV", "ENV101 should map to ENV group"

    def test_parse_wiresetcerts_excel_empty_file(self):
        """Test parsing with empty or invalid Excel data."""
        from utils.wire_set_cert_refresher import WireSetCertRefresher

        refresher = WireSetCertRefresher()

        # Test with empty data
        mappings = refresher._parse_wiresetcerts_excel(b"")
        assert mappings == [], "Empty data should return empty list"

        # Test with invalid data
        mappings = refresher._parse_wiresetcerts_excel(b"invalid excel data")
        assert mappings == [], "Invalid data should return empty list"
        assert mappings == [], "Invalid data should return empty list"
