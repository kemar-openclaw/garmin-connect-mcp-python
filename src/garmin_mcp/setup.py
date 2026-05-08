import os
from garminconnect import Garmin

def setup_mfa():
    email = os.getenv("GARMIN_EMAIL")
    password = os.getenv("GARMIN_PASSWORD")
    tokenstore = os.getenv("GARMINTOKENS") or os.path.expanduser("~/.garmin-mcp/tokens")
    
    if not email or not password:
        print("Error: GARMIN_EMAIL and GARMIN_PASSWORD environment variables are required.")
        return

    os.makedirs(os.path.dirname(tokenstore), exist_ok=True)
    
    def mfa_prompt():
        return input("Enter MFA code from email/authenticator: ")
        
    print(f"Logging in to Garmin Connect as {email}...")
    try:
        client = Garmin(email, password, prompt_mfa=mfa_prompt)
        client.login(tokenstore=tokenstore)
        print(f"\nSuccess! Tokens saved to {tokenstore}")
        print("You can now run the MCP server normally without MFA prompts.")
    except Exception as e:
        print(f"\nAuthentication failed: {e}")

if __name__ == "__main__":
    setup_mfa()
