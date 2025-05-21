# get_token.py
import msal
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("AZURE_CLIENT_ID")
print("Client ID:", client_id)

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
