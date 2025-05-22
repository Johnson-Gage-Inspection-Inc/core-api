# get_token.py
import msal
import os

def get_access_token():
    from dotenv import load_dotenv
    load_dotenv()

    client_id = os.getenv("AZURE_CLIENT_ID")
    tenant_id = os.getenv("AZURE_TENANT_ID")

    app = msal.PublicClientApplication(
        client_id=client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        token_cache=None,
        client_capabilities=["CP1"]
    )

    scopes = ["api://jgiquality.com/core-api/access_as_user"]

    result = app.acquire_token_interactive(scopes=scopes)

    if result.get("error"):
        print("Error acquiring token:", result.get("error_description"))
    else:
        print("Access token:", result["access_token"])
    return result["access_token"]

if __name__ == "__main__":
    get_access_token()