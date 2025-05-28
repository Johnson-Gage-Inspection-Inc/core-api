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


@patch('utils.qualer_client.make_qualer_client')
def test_employees_endpoint_mocked(mock_qualer_client, client, auth_token):
    """Test employees endpoint with mocked Qualer client for CI environments."""
    # Import the required model class for proper mocking
    from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel
    
    # Create a mock employee that inherits from the expected class
    class MockEmployee(QualerApiModelsClientsToEmployeeResponseModel):
        def __init__(self):
            # Initialize with minimal required attributes
            self.is_deleted = False
            self.employee_id = '123'
            self.name = 'John Doe'
    
    mock_employee = MockEmployee()
    
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