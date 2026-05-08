from garminconnect import Garmin
from .server import mcp_app, with_garmin

@mcp_app.tool()
@with_garmin
def get_daily_summary(client, date: str):
    """Full daily summary (steps, calories, distance, etc.) for YYYY-MM-DD."""
    return client.get_user_summary(date)

@mcp_app.tool()
@with_garmin
def get_steps(client, date: str):
    """Step count for a date."""
    return client.get_daily_steps(date)

@mcp_app.tool()
@with_garmin
def get_steps_chart(client, date: str):
    """Intraday step data throughout the day."""
    return client.get_steps_data(date)

@mcp_app.tool()
@with_garmin
def get_heart_rate(client, date: str):
    """Heart rate data (resting, max, zones, time series)."""
    return client.get_heart_rates(date)

@mcp_app.tool()
@with_garmin
def get_resting_heart_rate(client, date: str):
    """Resting heart rate for a date."""
    return client.get_rhr_day(date)

@mcp_app.tool()
@with_garmin
def get_stress(client, date: str):
    """Stress levels and time series."""
    return client.get_stress_data(date)

@mcp_app.tool()
@with_garmin
def get_body_battery(client, date: str):
    """Body Battery energy levels."""
    return client.get_body_battery(date)

@mcp_app.tool()
@with_garmin
def get_body_battery_events(client, date: str):
    """Battery charge/drain events for a day."""
    return client.get_body_battery_events(date)

@mcp_app.tool()
@with_garmin
def get_respiration(client, date: str):
    """Breathing rate data."""
    return client.get_respiration_data(date)

@mcp_app.tool()
@with_garmin
def get_spo2(client, date: str):
    """Blood oxygen saturation."""
    return client.get_spo2_data(date)

@mcp_app.tool()
@with_garmin
def get_intensity_minutes(client, date: str):
    """Moderate/vigorous intensity minutes."""
    return client.get_intensity_minutes_data(date)

@mcp_app.tool()
@with_garmin
def get_floors(client, date: str):
    """Floors climbed chart data."""
    return client.get_floors(date)

@mcp_app.tool()
@with_garmin
def get_hydration(client, date: str):
    """Daily hydration/water intake."""
    return client.get_hydration_data(date)

@mcp_app.tool()
@with_garmin
def get_daily_events(client, date: str):
    """Daily wellness events."""
    return client.get_all_day_events(date)
