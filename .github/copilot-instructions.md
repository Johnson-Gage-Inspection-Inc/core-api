# 🤖 GitHub Copilot Instructions for JGI Flask API

---

## 🔍 Quick Reference

- **Main Docs**: [`README.md`](../README.md)
- **Testing Guide**: [`docs/TESTING.md`](../docs/TESTING.md)
- 📖 Full onboarding guide: [`DEVELOPER_GUIDE.md`](../docs/DEVELOPER_GUIDE.md)
- **API Spec**: [Qualer SDK OpenAPI](https://raw.githubusercontent.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/refs/heads/master/spec.json)

---

## 🧠 Copilot Strategy Summary

### ✅ Golden Rules

- **TDD First**: Every new route or function must have a test written first or alongside it.
- **Micro-Commits**: Each commit must be atomic, isolated, and meaningfully named.
- **PR Required**: All changes must go through Pull Requests to `main`.
- **Test Placement**: Tests must be in `/tests/`, named `test_*.py`.
- **CI Enforced**: PRs will fail if coverage is below 80%.

### ✅ Copilot Prompt Examples

| Task        | Prompt |
|-------------|--------|
| Add route   | `Add a GET /wire_offsets route that returns cached DB results for a given wirelot.` |
| Add test    | `Write pytest for /wire_offsets that returns 200 and mocked JSON response.` |
| Refactor    | `Refactor this function to split DB query and transformation into separate steps.` |
| Fix         | `Fix AttributeError in test_get_token.py when SKIP_AUTH=true` |

---

## 🧪 Development & Testing Strategy

### ✅ TDD & Coverage Rules

- CI pipeline (`ci.yml`) runs all tests on push/PR to `main`.
- Use:
  ```bash
  pytest --cov=app --cov=routes --cov=utils --cov-report=html:htmlcov
````

* Thresholds:

  * 80% minimum coverage
  * All HTML coverage artifacts uploaded

### ✅ Commit Rules

| ✅ Good Examples                              | ❌ Avoid         |
| -------------------------------------------- | --------------- |
| `test: add test for /daqbook_offsets`        | `fix stuff`     |
| `feat: add pivot logic to route`             | `working on it` |
| `refactor: split schema into its own module` | `mixed updates` |

---

## 📁 Project Structure Overview

### 🔧 Core App

* `app.py`, `config.py`, `schemas.py`, `requirements.txt`

### 📦 Routes

* Flask-Smorest blueprints: `work_item_details.py`, `whoami.py`, etc.

### 🧰 Utilities

* Auth: `utils/auth.py`
* Qualer client: `utils/qualer_client.py`
* Token dev tools: `get_token.py`

---

## 🧪 Test Architecture Expectations

* Use `mock_view_bindings.py` with `SKIP_AUTH=true`
* `conftest.py` provides reusable fixtures
* Use `@pytest.mark.skipif` for dual-mode (mocked/real) testing

| Test Type   | Notes                                       |
| ----------- | ------------------------------------------- |
| Unit        | Patch external dependencies                 |
| Integration | Use Flask test client                       |
| Auth        | Check scope, token logic                    |
| Error       | Restore view bindings for full-stack errors |

---

## ⚠️ Copilot Edit Behavior

| Action             | Tool                                    |
| ------------------ | --------------------------------------- |
| Check file state   | `read_file`                             |
| Detect syntax bugs | `get_errors`                            |
| Update code safely | `replace_string_in_file` (with context) |
| Confirm changes    | `run_tests`                             |

---

## 🧪 Useful Commands

```bash
# Full suite
python -m pytest --cov=. --cov-report=term-missing

# Auth modes
$env:SKIP_AUTH="true"; python -m pytest
$env:SKIP_AUTH="false"; python -m pytest
```

---

## 🔐 Auth Expectations

* JWT via Azure AD
* Required scope: `access_as_user`
* Header: `Authorization: Bearer <token>`
* Verified against Azure’s public JWKS keys
* All protected routes use `@require_auth`

---

## 🔁 Deployment Flow

* Deployed at `https://api.jgiquality.com`
* Secured with NGINX + SSL
* CI/CD: GitHub Actions on PRs to `main`

---

## 🧰 Common Copilot Tasks

| Scenario      | Prompt                                                                       |
| ------------- | ---------------------------------------------------------------------------- |
| New route     | `Create GET /daqbook_offsets that reads from PostgreSQL and pivots results`  |
| Add test      | `Add pytest that mocks DB call for /daqbook_offsets and verifies JSON shape` |
| Define schema | `Create Marshmallow schema for DaqbookOffsetPivotRow`                        |
| Add migration | `Write Alembic migration to create daqbook_offsets table`                    |

---

## 📌 Summary

| Policy                  | Enforced   |
| ----------------------- | ---------- |
| PRs required            | ✅ Yes      |
| CI coverage threshold   | ✅ 80%      |
| TDD for all features    | ✅ Yes      |
| Tests only in `/tests/` | ✅ Yes      |
| Micro-commits           | ✅ Yes      |
| Copilot prompt guidance | ✅ Provided |

---

Copilot, help us build with confidence.
