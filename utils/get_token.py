# utils/get_token.py
import msal
import os
import tempfile

class TokenAcquisitionError(Exception):
    """Exception raised when token acquisition fails."""
    pass

def get_access_token():
    from dotenv import load_dotenv
    load_dotenv()

    if os.getenv("SKIP_AUTH", "false").lower() == "true":
        print(">>> Skipping get_access_token() because SKIP_AUTH is true")
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
        client_capabilities=["CP1"]
    )

    scopes = [f"{os.getenv('AZURE_API_AUDIENCE')}/{os.getenv('AZURE_REQUIRED_SCOPE', 'access_as_user')}"]

    # Try to get token silently first
    accounts = app.get_accounts()
    result = None
    if accounts:
        print(">>> Attempting to acquire token silently...")
        result = app.acquire_token_silent(scopes, account=accounts[0])

    # Fall back to interactive if silent acquisition failed
    if not result:
        print(">>> No cached token found, acquiring token interactively...")
        result = app.acquire_token_interactive(
            scopes=scopes,
            prompt="select_account",
            claims_challenge=None
        )

    # Save the token cache
    if cache.has_state_changed:
        with open(cache_file, "w") as f:
            f.write(cache.serialize())

    if result.get("error"):
        print("Error acquiring token:", result.get("error_description"))
        raise TokenAcquisitionError(f"Failed to acquire token: {result.get('error_description')}")
    else:
        print("Access token acquired successfully")
    return result["access_token"]

if __name__ == "__main__":
    get_access_token()