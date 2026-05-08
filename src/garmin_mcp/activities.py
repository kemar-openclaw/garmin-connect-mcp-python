from garminconnect import Garmin
from mcp.server.fastmcp import FastMCP
from .server import mcp_app, with_garmin

@mcp_app.tool()
@with_garmin
def get_activities(client, start: int = 0, limit: int = 20):
    """List recent activities with pagination."""
    return client.get_activities(start, limit)

@mcp_app.tool()
@with_garmin
def get_activities_by_date(client, start_date: str, end_date: str, activity_type: str = ""):
    """Search activities within a date range (YYYY-MM-DD)."""
    return client.get_activities_by_date(start_date, end_date, activity_type)

@mcp_app.tool()
@with_garmin
def get_last_activity(client):
    """Get the most recent activity."""
    return client.get_last_activity()

@mcp_app.tool()
@with_garmin
def count_activities(client):
    """Get total number of activities."""
    return client.count_activities()

@mcp_app.tool()
@with_garmin
def get_activity(client, activity_id: int):
    """Summary data for a specific activity."""
    return client.get_activity(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_details(client, activity_id: int):
    """Detailed metrics: HR, pace, elevation time series for an activity."""
    return client.get_activity_details(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_splits(client, activity_id: int):
    """Per-km or per-mile split data for an activity."""
    return client.get_activity_splits(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_weather(client, activity_id: int):
    """Weather conditions during an activity."""
    return client.get_activity_weather(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_hr_zones(client, activity_id: int):
    """Time in each heart rate zone for an activity."""
    return client.get_activity_hr_in_timezones(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_exercise_sets(client, activity_id: int):
    """Strength training sets (reps, weight) for an activity."""
    return client.get_activity_exercise_sets(activity_id)

@mcp_app.tool()
@with_garmin
def get_activity_types(client):
    """All available activity types."""
    return client.get_activity_types()

@mcp_app.tool()
@with_garmin
def get_progress_summary(client, start_date: str, end_date: str):
    """Fitness stats over a date range by activity type."""
    # Not directly in dir, but get_progress_summary_between_dates exists
    return client.get_progress_summary_between_dates(start_date, end_date)
