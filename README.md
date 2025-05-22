# JGI Flask API

This is a lightweight Flask-based API for internal use at Johnson Gage and Inspection, Inc. It supports authentication using Microsoft Entra ID (Azure AD) and is intended to be called from Power Query, Excel, or internal automation tools.

## 🔐 Authentication

This API is protected using Microsoft Entra ID via OAuth 2.0. All routes require a valid **access token** issued by the registered Azure application.

### Azure App Registration

This application is registered in Azure Active Directory at:

👉 [Azure Portal App Registration](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/~/Overview/appId/43a01068-983b-41b9-bb61-7ed191bd0e29/objectId/37a2b1b3-cbca-4524-b8b0-bb5e8dac9072/isMSAApp~/false/defaultBlade/Overview/appSignInAudience/AzureADMyOrg/servicePrincipalCreated~/true)

- **Client ID**: `43a01068-983b-41b9-bb61-7ed191bd0e29`
- **Audience**: Usually set to the `client_id` or `api://jgiquality.com/core-api`
- **Scope**: `access_as_user` (defined under *Expose an API*)

## 🧪 Local Development

You can run the API locally for testing:

```bash
python app.py
```

You must authenticate using the registered Entra app and pass a Bearer token to call endpoints like:

```http
GET /whoami
Authorization: Bearer <access_token>
```

## 🧰 Related Files

* `get_token.py` – helper script to acquire a valid Entra access token using MSAL
* `routes/whoami.py` – protected route that returns your Entra username

## 📎 Next Steps

Once deployed behind `https://api.jgiquality.com`, this API can be queried from Excel using the **Organizational Account** credential type with no extra token-pasting required.

---

## 🔎 API Documentation

This API exposes an OpenAPI 3.0 schema and a live Swagger UI for interactive exploration.

* **OpenAPI Spec (machine-readable)**
  [`GET /openapi.json`](http://localhost:5000/openapi.json)

* **Swagger UI (interactive docs)**
  [`GET /docs`](http://localhost:5000/docs)

These endpoints are available during local development and can be exposed in production for documentation consumers if desired.

---
