"""Microsoft Graph authentication utilities using MSAL."""

import os

import msal


def get_app_only_token() -> str:
    """Get an app-only access token for Microsoft Graph API.

    This uses the client credentials flow to get an application token
    that can access SharePoint on behalf of the app, not a specific user.

    Returns:
        Access token string for Microsoft Graph API

    Raises:
        RuntimeError: If token acquisition fails
        ValueError: If required environment variables are missing
    """
    # Get required environment variables
    tenant_id = os.environ.get("AZURE_TENANT_ID")
    client_id = os.environ.get("AZURE_CLIENT_ID")
    client_secret = os.environ.get("AZURE_CLIENT_SECRET")

    if not all([tenant_id, client_id, client_secret]):
        missing = []
        if not tenant_id:
            missing.append("AZURE_TENANT_ID")
        if not client_id:
            missing.append("AZURE_CLIENT_ID")
        if not client_secret:
            missing.append("AZURE_CLIENT_SECRET")
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    # Create MSAL app for client credentials flow
    authority = f"https://login.microsoftonline.com/{tenant_id}"
    scope = ["https://graph.microsoft.com/.default"]

    app = msal.ConfidentialClientApplication(
        client_id=client_id,
        authority=authority,
        client_credential=client_secret,
    )

    # Acquire token for client (app-only)
    result = app.acquire_token_for_client(scopes=scope)

    if "access_token" in result:
        return result["access_token"]

    # Handle error cases
    error_description = result.get("error_description", "Unknown error")
    error_code = result.get("error", "unknown_error")
    raise RuntimeError(f"Token acquisition failed [{error_code}]: {error_description}")


def get_delegated_token(user_token: str) -> str:
    """Get a delegated access token using on-behalf-of flow.

    This would be used to act on behalf of a specific user, but requires
    additional setup and is not needed for basic SharePoint file access.

    Args:
        user_token: The user's access token from Azure AD

    Returns:
        Delegated access token for Microsoft Graph API

    Note:
        This is a placeholder for future implementation if needed.
    """
    # TODO: Implement on-behalf-of flow if needed for user-specific access
    raise NotImplementedError("Delegated token flow not yet implemented")
