import garmin_mcp.activities
import garmin_mcp.daily_health
import garmin_mcp.trends_sleep_body
import garmin_mcp.perf_profile
from garmin_mcp.server import mcp_app

def main():
    mcp_app.run()

if __name__ == "__main__":
    main()
