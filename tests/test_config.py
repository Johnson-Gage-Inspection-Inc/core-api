import sys
import types


def test_load_dotenv_called(monkeypatch):
    # Create a mock for load_dotenv
    called = {}

    # Mock function for load_dotenv. Captures *args and **kwargs to verify
    # the function's call signature during testing.
    def mock_load_dotenv(*args, **kwargs):
        called["was_called"] = True
        called["args"] = args
        called["kwargs"] = kwargs

    # Patch sys.modules to inject the mock before import
    mock_dotenv = types.ModuleType("dotenv")
    mock_dotenv.load_dotenv = mock_load_dotenv
    sys.modules["dotenv"] = mock_dotenv

    # Remove config from sys.modules if already imported
    sys.modules.pop("config", None)

    import config  # noqa: F401

    assert called.get("was_called") is True
