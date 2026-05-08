import pytest
from unittest.mock import patch, MagicMock
from garmin_mcp.server import garmin_server
import garmin_mcp.daily_health as dh

@pytest.fixture
def mock_garmin():
    with patch("garmin_mcp.server.Garmin") as mock:
        instance = mock.return_value
        garmin_server.client = instance
        yield instance

@pytest.fixture(autouse=True)
def mock_env(monkeypatch):
    monkeypatch.setenv("GARMIN_EMAIL", "test@test.com")
    monkeypatch.setenv("GARMIN_PASSWORD", "testpass")

def test_get_daily_summary(mock_garmin):
    dh.get_daily_summary("2023-01-01")
    mock_garmin.get_user_summary.assert_called_with("2023-01-01")

def test_get_steps(mock_garmin):
    dh.get_steps("2023-01-01")
    mock_garmin.get_daily_steps.assert_called_with("2023-01-01")

def test_get_steps_chart(mock_garmin):
    dh.get_steps_chart("2023-01-01")
    mock_garmin.get_steps_data.assert_called_with("2023-01-01")

def test_get_heart_rate(mock_garmin):
    dh.get_heart_rate("2023-01-01")
    mock_garmin.get_heart_rates.assert_called_with("2023-01-01")

def test_get_resting_heart_rate(mock_garmin):
    dh.get_resting_heart_rate("2023-01-01")
    mock_garmin.get_rhr_day.assert_called_with("2023-01-01")

def test_get_stress(mock_garmin):
    dh.get_stress("2023-01-01")
    mock_garmin.get_stress_data.assert_called_with("2023-01-01")

def test_get_body_battery(mock_garmin):
    dh.get_body_battery("2023-01-01")
    mock_garmin.get_body_battery.assert_called_with("2023-01-01")

def test_get_body_battery_events(mock_garmin):
    dh.get_body_battery_events("2023-01-01")
    mock_garmin.get_body_battery_events.assert_called_with("2023-01-01")

def test_get_respiration(mock_garmin):
    dh.get_respiration("2023-01-01")
    mock_garmin.get_respiration_data.assert_called_with("2023-01-01")

def test_get_spo2(mock_garmin):
    dh.get_spo2("2023-01-01")
    mock_garmin.get_spo2_data.assert_called_with("2023-01-01")

def test_get_intensity_minutes(mock_garmin):
    dh.get_intensity_minutes("2023-01-01")
    mock_garmin.get_intensity_minutes_data.assert_called_with("2023-01-01")

def test_get_floors(mock_garmin):
    dh.get_floors("2023-01-01")
    mock_garmin.get_floors.assert_called_with("2023-01-01")

def test_get_hydration(mock_garmin):
    dh.get_hydration("2023-01-01")
    mock_garmin.get_hydration_data.assert_called_with("2023-01-01")

def test_get_daily_events(mock_garmin):
    dh.get_daily_events("2023-01-01")
    mock_garmin.get_all_day_events.assert_called_with("2023-01-01")
