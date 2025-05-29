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
    # Import the required model class for proper mocking
    from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel
      # Create a mock employee with proper initialization
    mock_employee = QualerApiModelsClientsToEmployeeResponseModel()
    
    # Set all required attributes - the SDK expects these as internal attributes
    mock_employee._employee_id = 123
    mock_employee._first_name = 'John'
    mock_employee._last_name = 'Doe'
    mock_employee._company_id = 1
    mock_employee._login_email = 'john.doe@test.com'
    mock_employee._departments = []
    mock_employee._subscription_email = None
    mock_employee._subscription_phone = None
    mock_employee._office_phone = None
    mock_employee._is_locked = False
    mock_employee._image_url = None
    mock_employee._alias = None
    mock_employee._title = 'Developer'
    mock_employee._is_deleted = False
    mock_employee._last_seen_date_utc = None
    mock_employee._culture_name = 'en-US'
    mock_employee._culture_ui_name = 'en-US'
    
    mock_employees_api = type('MockEmployeesApi', (), {
        'get_employees': lambda self: [mock_employee]
    })()
    
    mock_client = type('MockClient', (), {})()
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