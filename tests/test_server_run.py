from unittest.mock import patch, MagicMock
from garmin_mcp.server import GarminMCPServer

def test_run():
    server = GarminMCPServer()
    server.mcp = MagicMock()
    server.run()
    server.mcp.run.assert_called_once()
