import pytest
from unittest.mock import patch, MagicMock
from garmin_mcp.server import garmin_server
import garmin_mcp.perf_profile as pp

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

def test_get_vo2max(mock_garmin):
    pp.get_vo2max("2023-01-01")
    mock_garmin.get_max_metrics.assert_called_with("2023-01-01")

def test_get_training_readiness(mock_garmin):
    pp.get_training_readiness("2023-01-01")
    mock_garmin.get_training_readiness.assert_called_with("2023-01-01")

def test_get_training_status(mock_garmin):
    pp.get_training_status("2023-01-01")
    mock_garmin.get_training_status.assert_called_with("2023-01-01")

def test_get_hrv(mock_garmin):
    pp.get_hrv("2023-01-01")
    mock_garmin.get_hrv_data.assert_called_with("2023-01-01")

def test_get_endurance_score(mock_garmin):
    pp.get_endurance_score()
    mock_garmin.get_endurance_score.assert_called_once()

def test_get_hill_score(mock_garmin):
    pp.get_hill_score()
    mock_garmin.get_hill_score.assert_called_once()

def test_get_race_predictions(mock_garmin):
    pp.get_race_predictions("2023-01-01")
    mock_garmin.get_race_predictions.assert_called_with("2023-01-01")

def test_get_fitness_age(mock_garmin):
    pp.get_fitness_age("2023-01-01")
    mock_garmin.get_fitnessage_data.assert_called_with("2023-01-01")

def test_get_personal_records(mock_garmin):
    pp.get_personal_records()
    mock_garmin.get_personal_record.assert_called_once()

def test_get_lactate_threshold(mock_garmin):
    pp.get_lactate_threshold("2023-01-01")
    mock_garmin.get_lactate_threshold.assert_called_with("2023-01-01")

def test_get_cycling_ftp(mock_garmin):
    pp.get_cycling_ftp("2023-01-01")
    mock_garmin.get_cycling_ftp.assert_called_with("2023-01-01")

def test_get_user_profile(mock_garmin):
    pp.get_user_profile()
    mock_garmin.get_user_profile.assert_called_once()

def test_get_user_settings(mock_garmin):
    pp.get_user_settings()
    mock_garmin.get_userprofile_settings.assert_called_once()

def test_get_devices(mock_garmin):
    pp.get_devices()
    mock_garmin.get_devices.assert_called_once()

def test_get_device_settings(mock_garmin):
    pp.get_device_settings("123")
    mock_garmin.get_device_settings.assert_called_with("123")

def test_get_device_last_used(mock_garmin):
    pp.get_device_last_used()
    mock_garmin.get_device_last_used.assert_called_once()

def test_get_primary_training_device(mock_garmin):
    pp.get_primary_training_device()
    mock_garmin.get_primary_training_device.assert_called_once()

def test_get_device_solar_data(mock_garmin):
    pp.get_device_solar_data("123", "2023-01-01")
    mock_garmin.get_device_solar_data.assert_called_with("123", "2023-01-01")

def test_get_gear(mock_garmin):
    pp.get_gear("user1")
    mock_garmin.get_gear.assert_called_with("user1")

def test_get_gear_stats(mock_garmin):
    pp.get_gear_stats("gear1")
    mock_garmin.get_gear_stats.assert_called_with("gear1")

def test_get_goals(mock_garmin):
    pp.get_goals()
    mock_garmin.get_goals.assert_called_with("active")

def test_get_earned_badges(mock_garmin):
    pp.get_earned_badges()
    mock_garmin.get_earned_badges.assert_called_once()

def test_get_workouts(mock_garmin):
    pp.get_workouts()
    mock_garmin.get_workouts.assert_called_once()

def test_get_workout(mock_garmin):
    pp.get_workout("workout1")
    mock_garmin.get_workout_by_id.assert_called_with("workout1")
