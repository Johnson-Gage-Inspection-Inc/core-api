# JGI Flask API

A Flask-based REST API for Johnson Gage and Inspection, Inc. (JGI) that serves as an internal API for quality management operations. The API integrates with Microsoft Entra ID for authentication and the Qualer quality management system for data operations.

## 🚀 **Production API**
- **Base URL**: `https://api.jgiquality.com`
- **Documentation**: [`https://api.jgiquality.com/docs`](https://api.jgiquality.com/docs) (Swagger UI)
- **OpenAPI Spec**: [`https://api.jgiquality.com/openapi.json`](https://api.jgiquality.com/openapi.json)

## 📊 **Available Endpoints**

| Endpoint | Description | Purpose |
|----------|-------------|---------|
| `GET /whoami` | User authentication info | Returns current user details from JWT token |
| `GET /work-item-details` | Work item details | Fetches work item data from Qualer system |
| `GET /pyro-assets` | Pyrotechnic assets | Returns assets from specific pyro asset pool |
| `GET /employees` | Employee listing | Gets all employees from Qualer |
| `GET /clients` | Client companies | Returns all client companies from Qualer |
| `POST /git-pull` | Deployment automation | Updates server code (uses separate token auth) |

**📝 See [`https://api.jgiquality.com/docs`](https://api.jgiquality.com/docs) for complete API documentation and interactive testing**

## 🔐 Authentication

This API is protected using Microsoft Entra ID via OAuth 2.0. All routes (except `/` and `/git-pull`) require a valid **access token** issued by the registered Azure application.

### Azure App Registration

This application is registered in Azure Active Directory at:

👉 [Azure Portal App Registration](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Overview/appId/43a01068-983b-41b9-bb61-7ed191bd0e29/objectId/37a2b1b3-cbca-4524-b8b0-bb5e8dac9072/isMSAApp~/false/defaultBlade/Overview/appSignInAudience/AzureADMyOrg/servicePrincipalCreated~/true)

- **Client ID**: `43a01068-983b-41b9-bb61-7ed191bd0e29`
- **Audience**: `https://api.jgiquality.com`
- **Scope**: `access_as_user` (defined under *Expose an API*)

### Example Usage

```http
GET /whoami
Authorization: Bearer <access_token>
```

```http
GET /work-item-details?workItemNumber=56561-067667-01
Authorization: Bearer <access_token>
```

## 🧪 Local Development

### Prerequisites
- Python 3.8+
- Azure AD access for authentication testing
- Qualer API access (for full functionality)

### Environment Setup

1. **Clone the repository**
   ```powershell
   git clone <repository-url>
   cd api
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **🔐 Environment Configuration**

   This project uses a **two-tier environment setup** for security:

   - **`config/settings.env`**: Safe defaults (checked into Git)
   - **`.env`**: Secrets (DO NOT COMMIT)

   **Create your `.env` file** with secrets:
   ```env
   # .env (secrets only - DO NOT COMMIT)
   
   # Qualer API Integration
   QUALER_API_KEY=your-qualer-api-key
   
   # Azure Authentication
   AZURE_CLIENT_SECRET=your-azure-client-secret
   
   # Database Connection
   DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname
   
   # Development Settings (optional)
   SKIP_AUTH=false  # Set to 'true' for testing without Azure AD
   ```

   **Safe configuration** is already in `config/settings.env`:
   - Azure client ID, tenant ID, API audience
   - SharePoint site and drive IDs
   - Other non-sensitive defaults

4. **Run the application**
   ```powershell
   python app.py
   ```

### Development vs Testing Modes

**Production Mode** (`SKIP_AUTH=false`):
- Full authentication required with real Azure AD tokens
- All business logic executes against real Qualer API
- Use for integration testing and debugging

**Development/CI Mode** (`SKIP_AUTH=true`):
- Mock authentication with fake tokens
- Fast testing without external dependencies
- Ideal for unit testing and CI/CD

### Getting Access Tokens

Use the provided helper script to acquire valid Azure AD tokens:

```powershell
python utils/get_token.py
```

This will open a browser for interactive Azure AD login and return a valid access token.

## 🧰 Testing

This project includes a comprehensive testing framework supporting both unit and integration testing.

### Running Tests

```powershell
# Full test suite with coverage
python -m pytest --cov=. --cov-report=term-missing

# Test with production authentication
$env:SKIP_AUTH="false"; python -m pytest

# Test with mock authentication (CI mode)
$env:SKIP_AUTH="true"; python -m pytest

# Run specific test file
python -m pytest tests/test_whoami.py

# Verbose output
python -m pytest -v
```

### Testing Modes

- **CI Mode** (`SKIP_AUTH=true`): Fast testing with mocked authentication and external APIs
- **Integration Mode** (`SKIP_AUTH=false`): Full testing with real Azure AD tokens and Qualer API calls

**📝 See [`TESTING.md`](docs/TESTING.md) for comprehensive testing documentation**

## 🏗️ Project Structure

```
├── app.py               # Main Flask application
├── config/              # Environment configuration
│   └── settings.
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── routes/              # API endpoint blueprints
│   ├── whoami.py        # User authentication info
│   ├── work_item_details.py  # Work item data from Qualer
│   ├── pyro_assets.py   # Pyrotechnic assets
│   ├── employees.py     # Employee listings
│   ├── clients.py       # Client companies
│   └── git_ops.py       # Deployment automation
├── utils/               # Shared utilities
│   ├── auth.py          # Authentication decorators
│   ├── qualer_client.py # Qualer SDK configuration
│   ├── get_token.py     # Azure AD token helper
│   └── schemas.py       # Marshmallow schemas
└── tests/               # Test suite
    ├── conftest.py      # Test fixtures
    ├── mock_view_bindings.py  # Mock implementations
    └── test_*.py        # Individual test files
```

## 🔧 Development Guidelines

### Adding New Endpoints

1. Create route file in `/routes/` as Flask-Smorest blueprint
2. Add authentication with `@require_auth` decorator  
3. Define schemas for request/response serialization
4. Register blueprint in `app.py`
5. Create corresponding test file in `/tests/`
6. Add mock implementation if needed

### Code Style

- **Import Organization**: Standard library, third-party, local imports
- **Error Handling**: Use Flask-Smorest `abort()` for API errors
- **Documentation**: Include docstrings for complex business logic
- **Type Hints**: Use type hints for better code clarity

## 🚀 Deployment

### Production Environment

- **URL**: `https://api.jgiquality.com`
- **Deployment**: Automated via GitHub Actions
- **Proxy**: Uses ProxyFix middleware for reverse proxy support
- **CORS**: Enabled for cross-origin requests from Excel/Power Query

### Deployment Process

1. **Code Push**: Push to `main` branch triggers deployment
2. **GitHub Action**: Calls `/git-pull` endpoint on production server
3. **Server Update**: Production server pulls latest code and restarts
4. **Health Check**: Verify endpoints respond correctly

## 📚 Documentation & Resources

### API Documentation

- **Interactive Docs**: [`/docs`](https://api.jgiquality.com/docs) - Swagger UI for testing endpoints
- **OpenAPI Spec**: [`/openapi.json`](https://api.jgiquality.com/openapi.json) - Machine-readable API specification

### Development Documentation

- **Testing Guide**: [`TESTING.md`](docs/TESTING.md) - Comprehensive testing strategies and patterns
- **Copilot Instructions**: [`.github/.copilot-instructions.md`](.github/.copilot-instructions.md) - GitHub Copilot development guidance
- **Qualer SDK**: [OpenAPI Specification](https://raw.githubusercontent.com/Johnson-Gage-Inspection-Inc/qualer-sdk-python/refs/heads/master/spec.json)

### External Integrations

- **Qualer SDK**: Primary integration for quality management data
- **Azure AD**: Authentication and user management
- **Excel/Power Query**: Designed for consumption by Microsoft tools

## 🔒 Security Considerations

- **Secret Management**: Never commit API keys or secrets to git
- **Environment Variables**: Use environment variables for all configuration  
- **Input Validation**: All input parameters are validated via Marshmallow schemas
- **Token Security**: Proper scope checking for Azure AD tokens
- **Audit Logging**: Security-relevant events are logged for monitoring

## 📞 Support & Troubleshooting

### Common Issues

- **Authentication failures**: Check environment variables and Azure AD configuration
- **Qualer API errors**: Verify `QUALER_API_KEY` permissions and format
- **CORS issues**: Ensure requests include proper headers for cross-origin access
- **Testing failures**: See [`TESTING.md`](docs/TESTING.md) for debugging strategies

### Development Help

- **VS Code**: Use the Testing panel for running and debugging individual tests
- **Debugging**: Set `SKIP_AUTH=true` for development without Azure AD setup
- **Logs**: Check Flask application logs for detailed error information

---

## 🎯 Usage in Excel/Power Query

This API is designed for easy consumption in Microsoft Excel using Power Query:

1. **Data** → **Get Data** → **From Web**
2. **URL**: `https://api.jgiquality.com/endpoint`
3. **Authentication**: Choose **Organizational Account**
4. **Sign in**: Use your JGI Azure AD credentials
5. **Load**: Data loads automatically with proper authentication headers

Example Power Query M code:
```m
let
    Source = Json.Document(
        Web.Contents(
            "https://api.jgiquality.com/employees",
            [Headers=[Authorization="Bearer " & AccessToken.Token]]
        )
    )
in
    Source
```
