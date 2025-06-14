# utils/get_token.py
import logging
import os
import tempfile

import msal


class TokenAcquisitionError(Exception):
    """Exception raised when token acquisition fails."""


def get_access_token() -> str:
    # Import config to load environment variables from both files
    if __name__ == "__main__":
        # If running as script, add parent directory to path
        import sys

        sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

    import config  # noqa: F401

    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        logging.info("Skipping get_access_token() because SKIP_AUTH is true")
        return "fake-token"

    client_id = os.getenv("AZURE_CLIENT_ID")
    tenant_id = os.getenv("AZURE_TENANT_ID")

    # Use a persistent token cache to avoid repeated interactive logins
    cache_file = os.path.join(tempfile.gettempdir(), "msal_token_cache.bin")
    cache = msal.SerializableTokenCache()
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cache.deserialize(f.read())

    app = msal.PublicClientApplication(
        client_id=client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        token_cache=cache,
        client_capabilities=["CP1"],
    )

    scopes = [
        f"{os.getenv('AZURE_API_AUDIENCE')}/{os.getenv('AZURE_REQUIRED_SCOPE', 'access_as_user')}"
    ]
    accounts = app.get_accounts()
    result = None
    if accounts:
        logging.info("Attempting to acquire token silently...")
        result = app.acquire_token_silent(scopes, account=accounts[0])

    # Fall back to interactive if silent acquisition failed
    if not result:
        logging.info("No cached token found, acquiring token interactively...")
        result = app.acquire_token_interactive(
            scopes=scopes, prompt="select_account", claims_challenge=None
        )

    # Save the token cache
    if cache.has_state_changed:
        with open(cache_file, "w") as f:
            f.write(cache.serialize())

    if result.get("error"):
        logging.error("Error acquiring token: %s", result.get("error_description"))
        raise TokenAcquisitionError(
            f"Failed to acquire token: {result.get('error_description')}"
        )
    else:
        logging.info("Access token acquired successfully")
    return result["access_token"]


if __name__ == "__main__":
    token = get_access_token()
    print(f"Access Token: {token}")
