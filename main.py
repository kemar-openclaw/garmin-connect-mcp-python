import os
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

mcp = FastMCP("garmin_connect")

_garmin_client = None

def get_client() -> Garmin:
    global _garmin_client
    if _garmin_client is not None:
        return _garmin_client
    
    email = os.getenv("GARMIN_EMAIL")
    password = os.getenv("GARMIN_PASSWORD")
    
    if not email or not password:
        raise ValueError("GARMIN_EMAIL and GARMIN_PASSWORD environment variables are required.")
        
    client = Garmin(email, password)
    try:
        client.login()
    except (
        GarminConnectAuthenticationError,
        GarminConnectConnectionError,
        GarminConnectTooManyRequestsError
    ) as e:
        raise RuntimeError(f"Failed to authenticate with Garmin Connect: {e}")
        
    _garmin_client = client
    return client

@mcp.tool()
def get_daily_steps(date: str) -> Dict[str, Any]:
    """Get daily steps for a specific date (YYYY-MM-DD)."""
    client = get_client()
    return client.get_steps_data(date)

@mcp.tool()
def get_heart_rate(date: str) -> Dict[str, Any]:
    """Get heart rate data for a specific date (YYYY-MM-DD)."""
    client = get_client()
    return client.get_heart_rates(date)

@mcp.tool()
def get_sleep_data(date: str) -> Dict[str, Any]:
    """Get sleep data for a specific date (YYYY-MM-DD)."""
    client = get_client()
    return client.get_sleep_data(date)

@mcp.tool()
def get_activities(start: int = 0, limit: int = 10) -> List[Dict[str, Any]]:
    """Get a list of activities."""
    client = get_client()
    return client.get_activities(start, limit)

@mcp.tool()
def get_daily_stats(date: str) -> Dict[str, Any]:
    """Get overall daily stats (steps, calories, etc) for a specific date (YYYY-MM-DD)."""
    client = get_client()
    return client.get_stats(date)

if __name__ == "__main__":
    mcp.run(transport="stdio")
