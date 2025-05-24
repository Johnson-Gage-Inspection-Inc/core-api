import sys
import types

def test_load_dotenv_called(monkeypatch):
    # Create a mock for load_dotenv
    called = {}

    def mock_load_dotenv():
        called['was_called'] = True

    # Patch sys.modules to inject the mock before import
    mock_dotenv = types.ModuleType("dotenv")
    mock_dotenv.load_dotenv = mock_load_dotenv
    sys.modules["dotenv"] = mock_dotenv

    # Remove config from sys.modules if already imported
    sys.modules.pop("config", None)

    import config  # noqa: F401

    assert called.get('was_called') is True