# garmin-connect-mcp-python

A Model Context Protocol (MCP) server for Garmin Connect written in Python. It uses `mcp` and `python-garminconnect` to expose your fitness, health, and activity data.

## Requirements
- Python
- `uv` (recommended)

## Setup and MFA (Multi-Factor Authentication)

Set your Garmin Connect credentials as environment variables:
```bash
export GARMIN_EMAIL="your_email@example.com"
export GARMIN_PASSWORD="your_password"
```

If your Garmin account has MFA enabled, you must run the interactive setup step **before** running the server. The MCP server runs headlessly and cannot prompt you for an MFA code.

Run the setup script:
```bash
uv run python -m src.garmin_mcp.setup
```
*(If you are running from outside the directory, make sure `PYTHONPATH` points to the project root).*

This script will:
1. Log you in.
2. Prompt you to enter your MFA code in the terminal.
3. Save your authentication tokens to `~/.garmin-mcp/tokens` (or the path set by `GARMINTOKENS`).

After this, the server will automatically use the saved tokens and bypass the MFA prompt. You still need to provide `GARMIN_EMAIL` and `GARMIN_PASSWORD` environment variables when starting the server.

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
