import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from src.config import load_env


class VisionClient:
    def __init__(self):
        load_env()
        self.client = ImageAnalysisClient(
            endpoint=os.getenv("VISION_ENDPOINT"),
            credential=AzureKeyCredential(os.getenv("VISION_KEY"))
        )

    def analyze(self, image_path: str):
        with open(image_path, "rb") as f:
            image_data = f.read()

        result = self.client.analyze(
            image_data=image_data,
            features=["Caption", "Tags", "Objects"]
        )
        return result

    # FastAPI Backend Method
    def analyze_bytes(self, image_bytes: bytes):
        result = self.client.analyze(
            image_data=image_bytes,
            features=["Caption", "Tags", "Objects"]
        )
        return result
