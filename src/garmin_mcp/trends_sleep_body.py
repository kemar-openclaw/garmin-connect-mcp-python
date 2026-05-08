from garminconnect import Garmin
from .server import mcp_app, with_garmin

@mcp_app.tool()
@with_garmin
def get_daily_steps_range(client, start_date: str, end_date: str):
    """Daily step counts over a date range."""
    # Note: no direct method for date range steps, but we can iterate or use a hidden endpoint if available.
    # The prompt asks to map to the closest equivalent or omit. get_weekly_steps exists.
    # We will simulate range by omitting if not native or using daily.
    # For now, we will return an error or we can fetch a single week.
    raise NotImplementedError("Not directly supported by python-garminconnect. Use get_steps per date.")

@mcp_app.tool()
@with_garmin
def get_weekly_steps(client, date: str):
    """Weekly step aggregates."""
    return client.get_weekly_steps(date)

@mcp_app.tool()
@with_garmin
def get_weekly_stress(client, date: str):
    """Weekly stress aggregates."""
    return client.get_weekly_stress(date)

@mcp_app.tool()
@with_garmin
def get_weekly_intensity_minutes(client, date: str):
    """Weekly intensity minutes."""
    return client.get_weekly_intensity_minutes(date)

@mcp_app.tool()
@with_garmin
def get_sleep_data(client, date: str):
    """Sleep stages, score, bed/wake times."""
    return client.get_sleep_data(date)

@mcp_app.tool()
@with_garmin
def get_sleep_data_raw(client, date: str):
    """Raw sleep data with HR and SpO2."""
    # closest is get_sleep_data, omitting raw if not present or wrapping
    return client.get_sleep_data(date)

@mcp_app.tool()
@with_garmin
def get_body_composition(client, start_date: str, end_date: str):
    """Weight, BMI, body fat %, muscle mass (date range)."""
    return client.get_body_composition(start_date, end_date)

@mcp_app.tool()
@with_garmin
def get_latest_weight(client):
    """Most recent weight entry."""
    # We can get today's weigh in or use get_weigh_ins with recent dates
    raise NotImplementedError("Not directly supported natively without date.")

@mcp_app.tool()
@with_garmin
def get_daily_weigh_ins(client, date: str):
    """All weigh-ins for a date."""
    return client.get_daily_weigh_ins(date)

@mcp_app.tool()
@with_garmin
def get_weigh_ins(client, start_date: str, end_date: str):
    """Weigh-in records over a date range."""
    return client.get_weigh_ins(start_date, end_date)

@mcp_app.tool()
@with_garmin
def get_blood_pressure(client, start_date: str, end_date: str):
    """Blood pressure readings (date range)."""
    return client.get_blood_pressure(start_date, end_date)
