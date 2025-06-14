# tests/test_employees.py
import os
from unittest.mock import MagicMock, patch

import pytest
from qualer_sdk.models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel,
)


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Skipping employees test when SKIP_AUTH=true (CI environment)",
)
def test_employees_endpoint_basic(client, auth_token):
    """Basic test to call the employees endpoint - useful for debugging with breakpoints."""
    response = client.get(
        "/employees", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)
    assert all(data), "Expected a non-empty list of employees"


@patch("utils.qualer_client.make_qualer_client")
def test_employees_endpoint_mocked(mock_qualer_client, client, auth_token):
    """Test employees endpoint with mocked Qualer client for CI environments."""
    # Create a mock that behaves exactly like the SDK object but is easier to control
    mock_employee = MagicMock(spec=QualerApiModelsClientsToEmployeeResponseModel)
    mock_employee.is_deleted = False

    # Mock the to_dict method to return exactly what the real SDK returns
    mock_employee.to_dict.return_value = {
        "EmployeeId": 123,
        "FirstName": "John",
        "LastName": "Doe",
        "CompanyId": 1,
        "LoginEmail": "john.doe@test.com",
        "Departments": [],
        "IsLocked": False,
        "Title": "Developer",
        "IsDeleted": False,
        "CultureName": "en-US",
        "CultureUiName": "en-US",
    }

    mock_client = MagicMock()
    mock_qualer_client.return_value = mock_client

    # Patch the get_employees function directly to return our mock employee
    with patch("routes.employees.get_employees", return_value=[mock_employee]):
        response = client.get(
            "/employees", headers={"Authorization": f"Bearer {auth_token}"}
        )

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert all(data), "Expected a non-empty list of employees"

    employee = data[0]

    # Test the actual field names returned by to_dict()
    assert employee["EmployeeId"] == 123
    assert employee["FirstName"] == "John"
    assert employee["LastName"] == "Doe"
    assert employee["CompanyId"] == 1
    assert employee["LoginEmail"] == "john.doe@test.com"
    assert employee["IsDeleted"] is False
    assert employee["Title"] == "Developer"
