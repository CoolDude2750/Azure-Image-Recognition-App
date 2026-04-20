from dotenv import load_dotenv
import os

def load_env():
    load_dotenv()

class Settings:
    ENDPOINT = os.getenv("VISION_ENDPOINT")
    KEY = os.getenv("VISION_KEY")

settings = Settings()
