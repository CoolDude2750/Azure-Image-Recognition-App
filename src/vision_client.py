import os
import logging
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from src.config import load_env

logger = logging.getLogger(__name__)

# VisionClient encapsulates the logic for interacting with Azure's Computer Vision API
class VisionClient:
    def __init__(self, endpoint: str | None = None, key: str | None = None):
        load_env()
        endpoint = endpoint or os.getenv("VISION_ENDPOINT")
        key = key or os.getenv("VISION_KEY")

        if not endpoint or not key:
            raise ValueError("VISION_ENDPOINT and VISION_KEY must be set as environment variables.")

        self.client = ImageAnalysisClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )
        logger.info(f"VisionClient initialized with endpoint: {endpoint}")

    # Method for analyzing an image from a file path (used in CLI)
    def analyze(self, image_path: str):
        with open(image_path, "rb") as f:
            image_data = f.read()

        result = self.client.analyze(
            image_data=image_data,
            visual_features=["Caption", "Tags", "Objects"]
        )
        return result

    # FastAPI Backend Method
    def analyze_bytes(self, image_bytes: bytes):
        try:
            result = self.client.analyze(
                image_data=image_bytes,
                visual_features=["Caption", "Tags", "Objects"]
            )
            return result
        except Exception as e:
            logger.error(f"Computer Vision API error: {type(e).__name__}: {e}")
            raise
