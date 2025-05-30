# JGI Flask API - Developer Guide

This guide provides in-depth architecture, testing strategy, and contribution practices for developers working on the Johnson Gage and Inspection (JGI) Flask-based API. For a Copilot-friendly summary, see `.github/copilot-instructions.md`.

---

## Quick Reference

* **Main Documentation**: [`README.md`](../README.md)
* **Testing Guide**: [`docs/TESTING.md`](../docs/TESTING.md)
* **Copilot Policy**: [`.github/copilot-instructions.md`](../.github/copilot-instructions.md)
* **API Specification**: [Qualer SDK OpenAPI](https://raw.githubusercontent.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/refs/heads/master/spec.json)

---

## Project Overview

The JGI Flask API is a secure internal REST interface that exposes quality and calibration-related data from Qualer and SharePoint, protected by Microsoft Entra ID (Azure AD). Excel and Power Query are common clients.

---

## Project Structure

### Core Application Files

* `app.py` – Entry point and blueprint registration
* `config.py` – `.env` loader
* `schemas.py` – Marshmallow schemas
* `requirements.txt` – Dependencies

### Routes (`/routes/`)

All routes are Flask-Smorest blueprints:

* `whoami.py`
* `work_item_details.py`
* `pyro_assets.py`
* `employees.py`
* `clients.py`
* `git_ops.py`

### Utilities (`/utils/`)

* `auth.py` – JWT validation, auth decorators
* `qualer_client.py` – SDK client config
* `get_token.py` – Dev tool for token acquisition

---

## Authentication Architecture

* Auth handled via `@require_auth` using `utils.auth`
* JWT tokens are validated against Azure's JWKS URL
* Required scope: `access_as_user`
* Token passed via `Authorization: Bearer <token>`
* When `SKIP_AUTH=true`, mock bindings from `mock_view_bindings.py` are used

---

## Testing Framework

### Test Layout

* Tests live in `/tests/`
* Filenames: `test_*.py`
* All test files mirror core structure

### Fixtures

* `conftest.py`: provides `client`, `auth_token`, resets state
* `mock_view_bindings.py`: swaps real endpoints for mocks

### Test Categories

* **Unit Tests**: use `unittest.mock` to isolate behavior
* **Integration Tests**: real routes with mocked services
* **Auth Tests**: token validation, error responses
* **Error Tests**: verify proper use of `abort()`

### Testing Modes

* `SKIP_AUTH=true`: mock auth enabled
* `SKIP_AUTH=false`: real token needed

### Commands

```bash
python -m pytest --cov=. --cov-report=term-missing
$env:SKIP_AUTH="true"; python -m pytest
```

### Coverage

* CI threshold: **80%+**
* Coverage report saved to `htmlcov/`
* PRs fail if below threshold

---

## Code Style Guidelines

* Use docstrings for logic-heavy functions
* Use Marshmallow for schemas
* Use `abort()` for error handling (not `raise`)
* Validate inputs strictly
* Follow standard import order

---

## Deployment

* Public URL: `https://api.jgiquality.com`
* NGINX reverse proxy with TLS
* CORS enabled for Power Query and Excel
* Uses `ProxyFix` for correct header parsing
* GitOps endpoint: `/git-pull`

---

## External Systems

### Qualer SDK

* Python client via `qualer_sdk`
* Token-based auth using `Api-Token <KEY>`
* Swagger UI: [https://jgiquality.qualer.com/swagger/](https://jgiquality.qualer.com/swagger/)

### Azure AD

* Enforces authentication
* Validates user identity and scopes

---

## Common Tasks

### Add a New Route

1. Create file in `routes/`
2. Define Flask-Smorest `Blueprint`
3. Add `@require_auth` to protected routes
4. Define request/response schema in `schemas.py`
5. Register blueprint in `app.py`
6. Write tests in `tests/test_<route>.py`
7. Optionally mock in `mock_view_bindings.py`

### Write a Test

1. Add to `tests/`, named `test_*.py`
2. Use `conftest.py` fixtures
3. Mock external APIs
4. Use `SKIP_AUTH` toggles
5. Run full test suite + coverage

---

## Tips for Debugging

* Run `pytest` directly after each commit
* Use `read_file`, `get_errors`, `replace_string_in_file` if editing with Copilot CLI
* Restore view bindings manually if testing auth error cases

---

For all contributions, follow TDD, write focused commits, and ensure full test coverage. See the Copilot Instructions for specific rules enforced by GitHub CI.
