# tests/test_employees.py
import os
import pytest
from unittest.mock import patch


@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "true",
    reason="Skipping employees test when SKIP_AUTH=true (CI environment)"
)
def test_employees_endpoint_basic(client, auth_token):
    """Basic test to call the employees endpoint - useful for debugging with breakpoints."""
    response = client.get(
        "/employees",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    for employee in data:
        assert isinstance(employee, dict)
        assert employee != {}
        assert 'employee_id' in employee
        assert employee.get('is_deleted') is False


@patch('utils.qualer_client.make_qualer_client')
def test_employees_endpoint_mocked(mock_qualer_client, client, auth_token):
    """Test employees endpoint with mocked Qualer client for CI environments."""
    from unittest.mock import MagicMock
    from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel
    
    # Create a mock employee that behaves like an SDK object
    mock_employee = MagicMock(spec=QualerApiModelsClientsToEmployeeResponseModel)
    mock_employee.is_deleted = False
    mock_employee.to_dict.return_value = {
        'employee_id': 123,
        'first_name': 'John',
        'last_name': 'Doe',
        'company_id': 1,
        'login_email': 'john.doe@test.com',
        'departments': [],
        'subscription_email': None,
        'subscription_phone': None,
        'office_phone': None,
        'is_locked': False,
        'image_url': None,
        'alias': None,
        'title': 'Developer',
        'is_deleted': False,
        'last_seen_date_utc': None,
        'culture_name': 'en-US',
        'culture_ui_name': 'en-US'
    }
    
    mock_employees_api = MagicMock()
    mock_employees_api.get_employees.return_value = [mock_employee]
    
    mock_client = MagicMock()
    mock_qualer_client.return_value = mock_client
    
    # Patch the EmployeesApi class
    with patch('routes.employees.EmployeesApi', return_value=mock_employees_api):
        response = client.get(
            "/employees",
            headers={"Authorization": f"Bearer {auth_token}"}
        )
    
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    
    employee = data[0]
    assert employee['employee_id'] == 123
    assert employee['first_name'] == 'John'
    assert employee['last_name'] == 'Doe'
    assert employee['is_deleted'] is False