from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

class VisionClient:
    def __init__(self, endpoint, key):
        self.client = ImageAnalysisClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )

    def analyze(self, image_path):
        with open(image_path, "rb") as f:
            result = self.client.analyze(
                image_data=f,
                visual_features=[
                    VisualFeatures.CAPTION,
                    VisualFeatures.TAGS,
                    VisualFeatures.OBJECTS
                ]
            )
        return result
