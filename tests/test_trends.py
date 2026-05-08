import pytest
from unittest.mock import patch, MagicMock
from garmin_mcp.server import garmin_server
import garmin_mcp.trends_sleep_body as tsb

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

def test_get_daily_steps_range(mock_garmin):
    with pytest.raises(NotImplementedError):
        tsb.get_daily_steps_range("2023-01-01", "2023-01-07")

def test_get_weekly_steps(mock_garmin):
    tsb.get_weekly_steps("2023-01-01")
    mock_garmin.get_weekly_steps.assert_called_with("2023-01-01")

def test_get_weekly_stress(mock_garmin):
    tsb.get_weekly_stress("2023-01-01")
    mock_garmin.get_weekly_stress.assert_called_with("2023-01-01")

def test_get_weekly_intensity_minutes(mock_garmin):
    tsb.get_weekly_intensity_minutes("2023-01-01")
    mock_garmin.get_weekly_intensity_minutes.assert_called_with("2023-01-01")

def test_get_sleep_data(mock_garmin):
    tsb.get_sleep_data("2023-01-01")
    mock_garmin.get_sleep_data.assert_called_with("2023-01-01")

def test_get_sleep_data_raw(mock_garmin):
    tsb.get_sleep_data_raw("2023-01-01")
    mock_garmin.get_sleep_data.assert_called_with("2023-01-01")

def test_get_body_composition(mock_garmin):
    tsb.get_body_composition("2023-01-01", "2023-01-07")
    mock_garmin.get_body_composition.assert_called_with("2023-01-01", "2023-01-07")

def test_get_latest_weight(mock_garmin):
    with pytest.raises(NotImplementedError):
        tsb.get_latest_weight()

def test_get_daily_weigh_ins(mock_garmin):
    tsb.get_daily_weigh_ins("2023-01-01")
    mock_garmin.get_daily_weigh_ins.assert_called_with("2023-01-01")

def test_get_weigh_ins(mock_garmin):
    tsb.get_weigh_ins("2023-01-01", "2023-01-07")
    mock_garmin.get_weigh_ins.assert_called_with("2023-01-01", "2023-01-07")

def test_get_blood_pressure(mock_garmin):
    tsb.get_blood_pressure("2023-01-01", "2023-01-07")
    mock_garmin.get_blood_pressure.assert_called_with("2023-01-01", "2023-01-07")
