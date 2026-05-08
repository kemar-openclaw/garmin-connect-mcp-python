import pytest
from unittest.mock import patch, MagicMock
from garmin_mcp.server import garmin_server
import garmin_mcp.activities as activities

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

def test_get_activities(mock_garmin):
    mock_garmin.get_activities.return_value = []
    activities.get_activities(0, 20)
    mock_garmin.get_activities.assert_called_with(0, 20)

def test_get_activities_by_date(mock_garmin):
    activities.get_activities_by_date("2023-01-01", "2023-01-02", "")
    mock_garmin.get_activities_by_date.assert_called_with("2023-01-01", "2023-01-02", "")

def test_get_last_activity(mock_garmin):
    activities.get_last_activity()
    mock_garmin.get_last_activity.assert_called_once()

def test_count_activities(mock_garmin):
    activities.count_activities()
    mock_garmin.count_activities.assert_called_once()

def test_get_activity(mock_garmin):
    activities.get_activity(123)
    mock_garmin.get_activity.assert_called_with(123)

def test_get_activity_details(mock_garmin):
    activities.get_activity_details(123)
    mock_garmin.get_activity_details.assert_called_with(123)

def test_get_activity_splits(mock_garmin):
    activities.get_activity_splits(123)
    mock_garmin.get_activity_splits.assert_called_with(123)

def test_get_activity_weather(mock_garmin):
    activities.get_activity_weather(123)
    mock_garmin.get_activity_weather.assert_called_with(123)

def test_get_activity_hr_zones(mock_garmin):
    activities.get_activity_hr_zones(123)
    mock_garmin.get_activity_hr_in_timezones.assert_called_with(123)

def test_get_activity_exercise_sets(mock_garmin):
    activities.get_activity_exercise_sets(123)
    mock_garmin.get_activity_exercise_sets.assert_called_with(123)

def test_get_activity_types(mock_garmin):
    activities.get_activity_types()
    mock_garmin.get_activity_types.assert_called_once()

def test_get_progress_summary(mock_garmin):
    activities.get_progress_summary("2023-01-01", "2023-01-02")
    mock_garmin.get_progress_summary_between_dates.assert_called_with("2023-01-01", "2023-01-02")
