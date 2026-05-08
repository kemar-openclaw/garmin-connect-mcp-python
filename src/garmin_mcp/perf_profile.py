from garminconnect import Garmin
from .server import mcp_app, with_garmin

@mcp_app.tool()
@with_garmin
def get_vo2max(client, date: str):
    """VO2 Max estimate (running/cycling)."""
    # max_metrics often has this
    return client.get_max_metrics(date)

@mcp_app.tool()
@with_garmin
def get_training_readiness(client, date: str):
    """Training Readiness score."""
    return client.get_training_readiness(date)

@mcp_app.tool()
@with_garmin
def get_training_status(client, date: str):
    """Training status and load."""
    return client.get_training_status(date)

@mcp_app.tool()
@with_garmin
def get_hrv(client, date: str):
    """Heart Rate Variability."""
    return client.get_hrv_data(date)

@mcp_app.tool()
@with_garmin
def get_endurance_score(client):
    """Endurance fitness score."""
    return client.get_endurance_score()

@mcp_app.tool()
@with_garmin
def get_hill_score(client):
    """Climbing performance score."""
    return client.get_hill_score()

@mcp_app.tool()
@with_garmin
def get_race_predictions(client, date: str):
    """5K/10K/half/full marathon predictions."""
    return client.get_race_predictions(date)

@mcp_app.tool()
@with_garmin
def get_fitness_age(client, date: str):
    """Estimated fitness age."""
    return client.get_fitnessage_data(date)

@mcp_app.tool()
@with_garmin
def get_personal_records(client):
    """All personal records."""
    return client.get_personal_record()

@mcp_app.tool()
@with_garmin
def get_lactate_threshold(client, date: str):
    """Lactate threshold HR and pace."""
    return client.get_lactate_threshold(date)

@mcp_app.tool()
@with_garmin
def get_cycling_ftp(client, date: str):
    """Functional Threshold Power (cycling)."""
    return client.get_cycling_ftp(date)

@mcp_app.tool()
@with_garmin
def get_user_profile(client):
    """User social profile and preferences."""
    return client.get_user_profile()

@mcp_app.tool()
@with_garmin
def get_user_settings(client):
    """User settings, measurement system, sleep schedule."""
    return client.get_userprofile_settings()

@mcp_app.tool()
@with_garmin
def get_devices(client):
    """Registered Garmin devices."""
    return client.get_devices()

@mcp_app.tool()
@with_garmin
def get_device_settings(client, device_id: str):
    """Settings for a specific device."""
    return client.get_device_settings(device_id)

@mcp_app.tool()
@with_garmin
def get_device_last_used(client):
    """Last used device info."""
    return client.get_device_last_used()

@mcp_app.tool()
@with_garmin
def get_primary_training_device(client):
    """Primary training device."""
    return client.get_primary_training_device()

@mcp_app.tool()
@with_garmin
def get_device_solar_data(client, device_id: str, date: str):
    """Solar charging data."""
    return client.get_device_solar_data(device_id, date)

@mcp_app.tool()
@with_garmin
def get_gear(client, user_id: str):
    """All tracked gear/equipment."""
    return client.get_gear(user_id)

@mcp_app.tool()
@with_garmin
def get_gear_stats(client, gear_id: str):
    """Usage stats for a gear item."""
    return client.get_gear_stats(gear_id)

@mcp_app.tool()
@with_garmin
def get_goals(client):
    """Active goals and progress."""
    return client.get_goals("active")

@mcp_app.tool()
@with_garmin
def get_earned_badges(client):
    """Earned badges and achievements."""
    return client.get_earned_badges()

@mcp_app.tool()
@with_garmin
def get_workouts(client):
    """Saved workouts."""
    return client.get_workouts()

@mcp_app.tool()
@with_garmin
def get_workout(client, workout_id: str):
    """Specific workout by ID."""
    return client.get_workout_by_id(workout_id)
