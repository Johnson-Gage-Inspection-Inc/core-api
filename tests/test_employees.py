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
    for employee in data:
        assert not all(
            v is None for v in employee.values()
        ), "Employee data should not be empty"
        assert isinstance(employee, dict)
        assert employee != {}
        assert "EmployeeId" in employee
        assert employee.get("IsDeleted") is False


@patch("utils.qualer_client.make_qualer_client")
def test_employees_endpoint_mocked(mock_qualer_client, client, auth_token):
    """Test employees endpoint with mocked Qualer client for CI environments."""
    # Create a mock employee that behaves like an SDK object
    mock_employee = MagicMock(spec=QualerApiModelsClientsToEmployeeResponseModel)
    mock_employee.is_deleted = False
    mock_employee.to_dict.return_value = {
        "EmployeeId": 123,
        "FirstName": "John",
        "LastName": "Doe",
        "CompanyId": 1,
        "LoginEmail": "john.doe@test.com",
        "Departments": [],
        "SubscriptionEmail": None,
        "SubscriptionPhone": None,
        "OfficePhone": None,
        "IsLocked": False,
        "ImageUrl": None,
        "Alias": None,
        "Title": "Developer",
        "IsDeleted": False,
        "LastSeenDateUtc": None,
        "CultureName": "en-US",
        "CultureUiName": "en-US",
    }
    # Add model_dump method for compatibility with new schema serialization
    mock_employee.model_dump.return_value = mock_employee.to_dict.return_value

    mock_employees_api = MagicMock()
    mock_employees_api.get_employees_get2.return_value = [mock_employee]

    mock_client = MagicMock()
    mock_qualer_client.return_value = mock_client

    # Patch the EmployeesApi class
    with patch("routes.employees.EmployeesApi", return_value=mock_employees_api):
        response = client.get(
            "/employees", headers={"Authorization": f"Bearer {auth_token}"}
        )

    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    employee = data[0]
    assert employee["EmployeeId"] == 123
    assert employee["FirstName"] == "John"
    assert employee["LastName"] == "Doe"
    assert employee["IsDeleted"] is False
