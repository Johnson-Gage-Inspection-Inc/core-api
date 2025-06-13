# utils/qualer_client.py
from os import getenv
from uuid import UUID

from qualer_sdk.client import AuthenticatedClient


def make_qualer_client() -> AuthenticatedClient:
    api_token = getenv("QUALER_API_KEY")
    if not api_token:
        raise EnvironmentError("QUALER_API_KEY environment variable is not set")
    try:
        UUID(api_token)
    except ValueError:
        raise ValueError("Invalid API token format")
    return AuthenticatedClient(
        base_url="https://jgiquality.qualer.com", token=api_token, prefix="Api-Token"
    )
