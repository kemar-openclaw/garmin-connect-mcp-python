import os
import httpx
from garminconnect import Garmin
from mcp.server.fastmcp import FastMCP
from functools import wraps
from typing import Callable, Any

class GarminMCPServer:
    def __init__(self):
        self.mcp = FastMCP("garmin-connect")
        self.client = None

    def get_client(self) -> Garmin:
        if not self.client:
            email = os.getenv("GARMIN_EMAIL")
            password = os.getenv("GARMIN_PASSWORD")
            tokenstore = os.getenv("GARMINTOKENS") or os.path.expanduser("~/.garmin-mcp/tokens")
            
            if not email or not password:
                raise ValueError("GARMIN_EMAIL and GARMIN_PASSWORD environment variables are required.")
            
            # python-garminconnect uses requests internally.
            self.client = Garmin(email, password)
            self.client.login(tokenstore=tokenstore)
        return self.client

    def run(self):
        self.mcp.run()

garmin_server = GarminMCPServer()
mcp_app = garmin_server.mcp

def with_garmin(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        kwargs.pop("client", None)
        client = garmin_server.get_client()
        return func(client, *args, **kwargs)
    return wrapper
