# utils/qualer_client.py
from os import getenv
from qualer_sdk import Configuration, ApiClient

def make_qualer_client() -> ApiClient:
    config = Configuration()
    config.host = "https://jgiquality.qualer.com"
    client = ApiClient(configuration=config)
    client.default_headers["Authorization"] = f'Api-Token {getenv("QUALER_API_KEY")}'
    return client
