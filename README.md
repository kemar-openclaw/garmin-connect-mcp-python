# garmin-connect-mcp-python

A Model Context Protocol (MCP) server for Garmin Connect written in Python. It uses `mcp` and `python-garminconnect` to expose your fitness, health, and activity data.

## Requirements
- Python
- `uv` (recommended)

## Setup and MFA (Multi-Factor Authentication)

Set your Garmin Connect credentials as environment variables:
```bash
export GARMIN_EMAIL="your_email@example.com"
export GARMIN_PASSWORD="***"
```

If your Garmin account has MFA enabled, you must run the interactive setup step **before** running the server. The MCP server runs headlessly and cannot prompt you for an MFA code.

Run the setup script:
```bash
uv run setup-garmin-mcp
```
*(If you are running from outside the directory, make sure `uv --directory` is pointing to the project root).*

This script will:
1. Log you in.
2. Prompt you to enter your MFA code in the terminal.
3. Save your authentication tokens securely.

After this, the server will automatically use the saved tokens and bypass the MFA prompt. You still need to provide `GARMIN_EMAIL` and `GARMIN_PASSWORD` environment variables when starting the server.

## Running the Server

Run the MCP server using `uv`:

```bash
uv run start-garmin-mcp
```

Or configure your MCP client (like Claude Desktop or mcporter) to run it:

```json
{
  "mcpServers": {
    "garmin-python": {
      "command": "uv",
      "args": ["--directory", "/path/to/garmin-connect-mcp-python", "run", "start-garmin-mcp"],
      "env": {
        "GARMIN_EMAIL": "your_email@example.com",
        "GARMIN_PASSWORD": "your_password"
      }
    }
  }
}
```

## Available Tools (60+ Tools)

### Activities (12 tools)
| Tool | Description |
|------|-------------|
| `get_activities` | List recent activities with pagination |
| `get_activities_by_date` | Search activities within a date range |
| `get_last_activity` | Get the most recent activity |
| `count_activities` | Get total number of activities |
| `get_activity` | Summary data for a specific activity |
| `get_activity_details` | Detailed metrics: HR, pace, elevation time series |
| `get_activity_splits` | Per-km or per-mile split data |
| `get_activity_weather` | Weather conditions during activity |
| `get_activity_hr_zones` | Time in each heart rate zone |
| `get_activity_exercise_sets` | Strength training sets (reps, weight) |
| `get_activity_types` | All available activity types |
| `get_progress_summary` | Fitness stats over a date range by activity type |

### Daily Health (14 tools)
| Tool | Description |
|------|-------------|
| `get_daily_summary` | Full daily summary (steps, calories, distance, etc.) |
| `get_steps` | Step count for a date |
| `get_steps_chart` | Intraday step data throughout the day |
| `get_heart_rate` | Heart rate data (resting, max, zones, time series) |
| `get_resting_heart_rate` | Resting heart rate for a date |
| `get_stress` | Stress levels and time series |
| `get_body_battery` | Body Battery energy levels (date range) |
| `get_body_battery_events` | Battery charge/drain events for a day |
| `get_respiration` | Breathing rate data |
| `get_spo2` | Blood oxygen saturation |
| `get_intensity_minutes` | Moderate/vigorous intensity minutes |
| `get_floors` | Floors climbed chart data |
| `get_hydration` | Daily hydration/water intake |
| `get_daily_events` | Daily wellness events |

### Trends (4 tools)
| Tool | Description |
|------|-------------|
| `get_daily_steps_range` | Daily step counts over a date range |
| `get_weekly_steps` | Weekly step aggregates |
| `get_weekly_stress` | Weekly stress aggregates |
| `get_weekly_intensity_minutes` | Weekly intensity minutes |

### Sleep (2 tools)
| Tool | Description |
|------|-------------|
| `get_sleep_data` | Sleep stages, score, bed/wake times |
| `get_sleep_data_raw` | Raw sleep data with HR and SpO2 |

### Body Composition (5 tools)
| Tool | Description |
|------|-------------|
| `get_body_composition` | Weight, BMI, body fat %, muscle mass (date range) |
| `get_latest_weight` | Most recent weight entry |
| `get_daily_weigh_ins` | All weigh-ins for a date |
| `get_weigh_ins` | Weigh-in records over a date range |
| `get_blood_pressure` | Blood pressure readings (date range) |

### Performance & Training (11 tools)
| Tool | Description |
|------|-------------|
| `get_vo2max` | VO2 Max estimate (running/cycling) |
| `get_training_readiness` | Training Readiness score |
| `get_training_status` | Training status and load |
| `get_hrv` | Heart Rate Variability |
| `get_endurance_score` | Endurance fitness score |
| `get_hill_score` | Climbing performance score |
| `get_race_predictions` | 5K/10K/half/full marathon predictions |
| `get_fitness_age` | Estimated fitness age |
| `get_personal_records` | All personal records |
| `get_lactate_threshold` | Lactate threshold HR and pace |
| `get_cycling_ftp` | Functional Threshold Power (cycling) |

### Profile & Devices (13 tools)
| Tool | Description |
|------|-------------|
| `get_user_profile` | User social profile and preferences |
| `get_user_settings` | User settings, measurement system, sleep schedule |
| `get_devices` | Registered Garmin devices |
| `get_device_settings` | Settings for a specific device |
| `get_device_last_used` | Last used device info |
| `get_primary_training_device` | Primary training device |
| `get_device_solar_data` | Solar charging data |
| `get_gear` | All tracked gear/equipment |
| `get_gear_stats` | Usage stats for a gear item |
| `get_goals` | Active goals and progress |
| `get_earned_badges` | Earned badges and achievements |
| `get_workouts` | Saved workouts |
| `get_workout` | Specific workout by ID |

## Development & Testing

Run tests with `pytest` and coverage:
```bash
uv run pytest --cov=src --cov-report=term-missing
```
