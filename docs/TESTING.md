# JGI Flask API - Testing Guide

## Overview

This guide provides comprehensive testing strategies, patterns, and troubleshooting for the JGI Flask API project. The testing framework supports multiple execution environments and authentication modes.

## Testing Architecture

### Test Execution Environments

#### **VS Code Test Runner vs Terminal pytest**

The project supports multiple test execution environments with different behaviors:

**Terminal pytest (`python -m pytest`)**:
- Direct module imports and patches work consistently
- Full control over mock timing and scope
- Imports cached once per session

**VS Code Test Runner**:
- Different import caching behavior
- Module patches may not take effect due to import timing
- Requires special handling for complex mocking scenarios

### Dual Authentication Modes

#### **`SKIP_AUTH=true` (CI/Development Mode)**
- Uses `mock_view_bindings.py` for fast, fake responses
- Some auth tests skipped with `@pytest.mark.skipif`
- Enables testing without Azure AD setup
- Coverage target: 80%+ for GitHub CI
- Mock responses return predefined test data

#### **`SKIP_AUTH=false` (Production Mode)**
- Full authentication required with real Azure AD tokens
- All tests execute real auth paths
- Requires valid Azure AD configuration
- Higher coverage possible: 90%+
- Tests actual business logic end-to-end

## Testing Patterns

### Compatibility Strategies

#### 1. Mock View Function Restoration for Error Testing

When `SKIP_AUTH=true`, `mock_view_bindings.py` intercepts all requests before SDK patches can execute. Use this pattern for testing error conditions:

```python
def test_error_condition(client, auth_token):
    import os
    from app import app
    
    # If SKIP_AUTH=true, temporarily restore real view function
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None
    
    if skip_auth:
        from routes.my_route import MyRouteClass
        original_view_func = app.view_functions.get("blueprint.ViewName")
        app.view_functions["blueprint.ViewName"] = MyRouteClass().get
    
    try:
        # Test with SDK patches that need real code paths
        with patch("routes.my_route.ExternalAPI") as mock_api:
            mock_api.return_value.method.return_value = error_condition
            # Test error handling...
    finally:
        if skip_auth and original_view_func:
            app.view_functions["blueprint.ViewName"] = original_view_func
```

#### 2. SDK-Level Patching

Patch at the SDK/external library level rather than function level for better compatibility:

```python
def test_external_service_error(client, auth_token):
    with patch("routes.my_route.ExternalSDK") as mock_sdk:
        mock_sdk.return_value.get_data.side_effect = Exception("Service unavailable")
        
        response = client.get("/endpoint", headers={"Authorization": f"Bearer {auth_token}"})
        assert response.status_code == 500
```

#### 3. Dual Mode Conditional Testing

Write tests that adapt behavior based on authentication mode:

```python
import os

def test_endpoint_behavior(client, auth_token):
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    
    response = client.get("/endpoint", headers={"Authorization": f"Bearer {auth_token}"})
    
    if skip_auth:
        # Expect mock behavior
        assert response.status_code == 200
        assert response.get_json()["user"] == "testuser@example.com"
    else:
        # Expect real auth behavior
        assert response.status_code == 200
        assert "@" in response.get_json()["user"]  # Real email

@pytest.mark.skipif(os.getenv("SKIP_AUTH", "false").lower() == "true", 
                   reason="Skipped when SKIP_AUTH=true")
def test_auth_specific_feature(client, auth_token):
    # Test only runs in production mode
    pass
```

### Test Isolation

#### Global State Management

Use fixtures to prevent test pollution:

```python
@pytest.fixture(scope="session")
def auth_token():
    """Shared valid auth token for use across tests."""
    return get_access_token()

@pytest.fixture
def client():
    """Flask test client with all blueprints registered."""
    from app import create_app
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_auth_cache():
    """Reset auth cache before each test to prevent test interference."""
    utils.auth._openid_config = None
    utils.auth._jwks = None
    yield
    # Clean up after test
    utils.auth._openid_config = None
    utils.auth._jwks = None
```

## Test Coverage Strategies

### Coverage Targets

- **GitHub CI (SKIP_AUTH=true)**: 80% minimum coverage
- **Local Development (SKIP_AUTH=false)**: 90%+ achievable
- **Critical Files**: Routes and utils should have >95% coverage

### Coverage-Friendly Patterns

1. **Test Both Success and Error Paths**:
```python
def test_endpoint_success(client, auth_token):
    # Test happy path
    pass

def test_endpoint_validation_error(client, auth_token):
    # Test input validation
    pass

def test_endpoint_external_service_error(client, auth_token):
    # Test external dependency failures
    pass
```

2. **Use Parametrized Tests**:
```python
@pytest.mark.parametrize("input_data,expected_status", [
    ({"valid": "data"}, 200),
    ({"invalid": "data"}, 400),
    ({}, 422),
])
def test_endpoint_validation(client, auth_token, input_data, expected_status):
    response = client.post("/endpoint", 
                          json=input_data,
                          headers={"Authorization": f"Bearer {auth_token}"})
    assert response.status_code == expected_status
```

3. **Mock External Dependencies**:
```python
def test_external_api_integration(client, auth_token):
    with patch("utils.external_client.ExternalAPI") as mock_api:
        mock_api.return_value.get_data.return_value = {"test": "data"}
        
        response = client.get("/endpoint", headers={"Authorization": f"Bearer {auth_token}"})
        assert response.status_code == 200
```

## Testing Tools and Commands

### Running Tests

```powershell
# Full test suite with coverage
python -m pytest --cov=. --cov-report=term-missing

# Specific test file
python -m pytest tests/test_specific_file.py

# Test with production auth mode
$env:SKIP_AUTH="false"; python -m pytest

# Test with CI mode (default)
$env:SKIP_AUTH="true"; python -m pytest

# Verbose output with detailed test names
python -m pytest -v

# Stop on first failure for faster debugging
python -m pytest -x

# Run only failed tests from last run
python -m pytest --lf

# Debug with pdb
python -m pytest --pdb
```

### VS Code Integration

Use the Testing panel in VS Code sidebar for:
- Running individual tests
- Debugging with breakpoints
- Viewing test results inline

## Troubleshooting

### Common Issues and Solutions

#### "Tests pass in terminal but fail in VS Code Test Runner"
- **Cause**: Different import caching and module loading behavior
- **Solution**: Use SDK-level patches instead of function-level patches
- **Solution**: Implement view function restoration pattern for error tests
- **Example**: See `test_work_item_details.py` error handling tests

#### "Mocks don't work when SKIP_AUTH=true"
- **Cause**: `mock_view_bindings.py` intercepts requests before patches apply
- **Solution**: Temporarily restore real view functions for error testing
- **Pattern**: Check `skip_auth` flag and swap view functions in test

#### "Different test results between SKIP_AUTH modes"
- **Cause**: Different code paths and response structures
- **Solution**: Use conditional assertions based on auth mode
- **Example**: Status codes may differ (400 vs 422) between modes

#### "Coverage drops significantly with SKIP_AUTH=true"
- **Cause**: Auth-specific code paths are skipped
- **Solution**: Use `@pytest.mark.skipif` for auth-only tests
- **Target**: 80% coverage acceptable for CI mode

#### "Import errors or module not found in tests"
- **Cause**: Incorrect test file location or missing `__init__.py`
- **Solution**: Ensure all test files are in `/tests/` directory
- **Solution**: Check that `/tests/__init__.py` exists

#### "No tests discovered"
- **Cause**: Improper filename or no test prefix
- **Solution**: Ensure file is named `test_*.py` and contains functions prefixed with `test_`
- **Solution**: Check that the `tests/__init__.py` file exists

#### "Global state pollution between tests"
- **Cause**: Module-level caches (e.g., Azure JWKS config)
- **Solution**: Use `reset_auth_cache` fixture (see `conftest.py`)
- **Solution**: Add `autouse=True` fixtures to clean up state

### Debug Techniques

#### Logging in Tests
```python
import logging
logging.basicConfig(level=logging.DEBUG)

def test_with_debug_logging(client, auth_token):
    # Test will show detailed logs
    pass
```

#### Inspecting Responses
```python
def test_response_debugging(client, auth_token):
    response = client.get("/endpoint", headers={"Authorization": f"Bearer {auth_token}"})
    
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Data: {response.get_data(as_text=True)}")
    
    # Add assertions...
```

## Best Practices

### Test Organization
- Place ALL test files in `/tests/` directory with `test_*.py` naming
- Mirror main code structure (e.g., `test_auth.py` for `utils/auth.py`)
- Group related tests in classes when beneficial
- Use descriptive test names that explain the scenario

### Mock Strategy
- Use `mock_view_bindings.py` for endpoint mocking during development
- Use `unittest.mock` for unit testing external dependencies
- Session-scoped `auth_token` fixture for integration tests
- Test client fixture in `conftest.py`

### Authentication Testing
- **Test both authenticated and unauthenticated scenarios**
- **Verify token validation, scope checking, and error handling**
- Use conditional logic for dual-mode compatibility
- Skip auth-specific tests appropriately with decorators

### Error Handling
- **Test all error paths and edge cases**
- **Verify proper HTTP status codes and error messages**
- Test external service failures and timeouts
- Validate input validation and schema errors

### Coverage Configuration

Optional: Use `.coveragerc` to customize coverage reporting:

```ini
[run]
omit = 
    tests/*
    */__init__.py
    */migrations/*
    venv/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

This comprehensive testing guide ensures robust, maintainable tests that work across all environments and authentication modes.
