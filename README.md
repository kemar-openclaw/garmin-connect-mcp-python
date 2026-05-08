# garmin-connect-mcp-python

A Model Context Protocol (MCP) server for Garmin Connect written in Python. It uses `mcp` and `python-garminconnect` to expose your fitness, health, and activity data.

## Requirements
- Python
- `uv` (recommended)

## Setup

Set your Garmin Connect credentials as environment variables:
```bash
export GARMIN_EMAIL="your_email@example.com"
export GARMIN_PASSWORD="your_password"
```

## Running the Server

Run it using `uv` to let it manage dependencies:

```bash
uv run main.py
```

Or configure your MCP client (like Claude Desktop or mcporter) to run it:

```json
{
  "mcpServers": {
    "garmin": {
      "command": "uv",
      "args": ["run", "/path/to/garmin-connect-mcp-python/main.py"],
      "env": {
        "GARMIN_EMAIL": "your_email@example.com",
        "GARMIN_PASSWORD": "your_password"
      }
    }
  }
}
```

## Available Tools

- `get_daily_steps(date: str)`
- `get_heart_rate(date: str)`
- `get_sleep_data(date: str)`
- `get_activities(start: int, limit: int)`
- `get_daily_stats(date: str)`

## Development & Testing

Run tests with `pytest` and coverage:
```bash
PYTHONPATH=. uv run pytest --cov=main --cov-report=term-missing
```
