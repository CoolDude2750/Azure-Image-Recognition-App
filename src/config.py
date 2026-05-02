from dotenv import load_dotenv
import os
# This module is responsible for loading environment variables and providing configuration settings for the application.
def load_env():
    load_dotenv()

class Settings:
    ENDPOINT = os.getenv("VISION_ENDPOINT")
    KEY = os.getenv("VISION_KEY")

settings = Settings()
