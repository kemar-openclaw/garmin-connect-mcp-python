import pytest
from unittest.mock import patch, MagicMock
from garmin_mcp.server import garmin_server, with_garmin

@pytest.fixture
def mock_garmin():
    with patch("garmin_mcp.server.Garmin") as mock:
        instance = mock.return_value
        instance.login = MagicMock()
        garmin_server.client = instance
        yield instance

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("GARMIN_EMAIL", "test@test.com")
    monkeypatch.setenv("GARMIN_PASSWORD", "testpass")

def test_get_client(mock_garmin):
    garmin_server.client = None
    client = garmin_server.get_client()
    assert client is not None
    client.login.assert_called_once()

def test_missing_env(monkeypatch):
    monkeypatch.delenv("GARMIN_EMAIL", raising=False)
    garmin_server.client = None
    with pytest.raises(ValueError):
        garmin_server.get_client()

def test_with_garmin(mock_garmin):
    @with_garmin
    def dummy(client, arg1):
        return arg1
    
    assert dummy("test") == "test"
