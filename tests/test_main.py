import os
import pytest
from unittest.mock import patch, MagicMock
from garminconnect import GarminConnectAuthenticationError

from main import (
    get_client,
    get_daily_steps,
    get_heart_rate,
    get_sleep_data,
    get_activities,
    get_daily_stats
)

@pytest.fixture
def mock_env(monkeypatch):
    monkeypatch.setenv("GARMIN_EMAIL", "test@example.com")
    monkeypatch.setenv("GARMIN_PASSWORD", "password123")

@pytest.fixture
def mock_garmin_client():
    with patch("main.Garmin") as mock_garmin:
        mock_instance = MagicMock()
        mock_garmin.return_value = mock_instance
        yield mock_instance

def test_get_client_missing_credentials(monkeypatch):
    monkeypatch.delenv("GARMIN_EMAIL", raising=False)
    monkeypatch.delenv("GARMIN_PASSWORD", raising=False)
    # reset global client
    import main
    main._garmin_client = None
    with pytest.raises(ValueError, match="GARMIN_EMAIL and GARMIN_PASSWORD"):
        get_client()

def test_get_client_auth_failure(mock_env):
    with patch("main.Garmin") as mock_garmin:
        mock_instance = MagicMock()
        mock_instance.login.side_effect = GarminConnectAuthenticationError("Invalid login")
        mock_garmin.return_value = mock_instance
        
        import main
        main._garmin_client = None
        with pytest.raises(RuntimeError, match="Failed to authenticate"):
            get_client()

def test_get_client_success(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    client = get_client()
    mock_garmin_client.login.assert_called_once()
    assert client == mock_garmin_client
    
    # Test caching
    client2 = get_client()
    assert client2 == mock_garmin_client
    # login should not be called again
    assert mock_garmin_client.login.call_count == 1

def test_get_daily_steps(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    mock_garmin_client.get_steps_data.return_value = {"steps": 10000}
    result = get_daily_steps("2023-01-01")
    mock_garmin_client.get_steps_data.assert_called_once_with("2023-01-01")
    assert result == {"steps": 10000}

def test_get_heart_rate(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    mock_garmin_client.get_heart_rates.return_value = {"hr": 70}
    result = get_heart_rate("2023-01-01")
    mock_garmin_client.get_heart_rates.assert_called_once_with("2023-01-01")
    assert result == {"hr": 70}

def test_get_sleep_data(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    mock_garmin_client.get_sleep_data.return_value = {"sleep": "good"}
    result = get_sleep_data("2023-01-01")
    mock_garmin_client.get_sleep_data.assert_called_once_with("2023-01-01")
    assert result == {"sleep": "good"}

def test_get_activities(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    mock_garmin_client.get_activities.return_value = [{"activity": "running"}]
    result = get_activities(0, 5)
    mock_garmin_client.get_activities.assert_called_once_with(0, 5)
    assert result == [{"activity": "running"}]

def test_get_daily_stats(mock_env, mock_garmin_client):
    import main
    main._garmin_client = None
    mock_garmin_client.get_stats.return_value = {"calories": 2000}
    result = get_daily_stats("2023-01-01")
    mock_garmin_client.get_stats.assert_called_once_with("2023-01-01")
    assert result == {"calories": 2000}
