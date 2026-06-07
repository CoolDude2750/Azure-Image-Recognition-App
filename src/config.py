from dotenv import load_dotenv
import os

# Load environment variables from .env (local development) as soon as the module is imported.
load_dotenv()

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

class Settings:
    ENDPOINT = os.getenv("VISION_ENDPOINT")
    KEY = os.getenv("VISION_KEY")

settings = Settings()
