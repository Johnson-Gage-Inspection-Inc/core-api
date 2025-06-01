# tests/test_qualer_client.py
import os

import pytest

from utils.qualer_client import make_qualer_client


@pytest.fixture
def patch_env(monkeypatch):
    monkeypatch.setenv("QUALER_API_KEY", "fake-qualer-token")


def test_make_qualer_client_sets_host_and_token(patch_env):
    client = make_qualer_client()

    # Check the host
    assert client.configuration.host == "https://jgiquality.qualer.com"

    # Check the authorization header
    auth_header = client.default_headers.get("Authorization")
    assert auth_header == "Api-Token fake-qualer-token"
