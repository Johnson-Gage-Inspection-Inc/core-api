# tests/test_employees.py
import pytest


def test_employees_endpoint_basic(client, auth_token):
    """Basic test to call the employees endpoint - useful for debugging with breakpoints."""
    response = client.get(
        "/employees",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    
    # For debugging: set a breakpoint in routes/employees.py line 24 to inspect employee_pool
    assert response.status_code == 200
    
    # Basic validation that we get a list back
    data = response.get_json()
    assert isinstance(data, list)
    
    # Print some basic info for debugging
    print(f"Received {len(data)} employees from Qualer")
    if data:
        print(f"First employee keys: {list(data[0].keys()) if isinstance(data[0], dict) else 'Not a dict'}")