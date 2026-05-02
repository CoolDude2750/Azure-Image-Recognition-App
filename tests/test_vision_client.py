import pytest
from unittest.mock import MagicMock, patch

from src.vision_client import VisionClient


class DummyAnalysisResult:
    def __init__(self, caption=None, tags=None, objects=None):
        self.caption = caption
        self.tags = tags or {}
        self.objects = objects or {}


class DummyCaption:
    def __init__(self, text, confidence=None):
        self.text = text
        self.confidence = confidence

# Unit test to verify that analyze_bytes calls ImageAnalysisClient.analyze with correct parameters
def test_analyze_bytes_calls_image_analysis_client_analyze():
    with patch("src.vision_client.ImageAnalysisClient") as mock_client_cls:
        mock_client = MagicMock()
        mock_client_cls.return_value = mock_client

        client = VisionClient()
        image_bytes = b"fake-image-data"

        client.analyze_bytes(image_bytes)

        mock_client.analyze.assert_called_once()
        args, kwargs = mock_client.analyze.call_args
        assert kwargs["image_data"] == image_bytes
        assert kwargs["visual_features"] == ["Caption", "Tags", "Objects"]

# Unit test to verify that analyze_bytes returns an object with expected attributes based on the mocked response from ImageAnalysisClient.analyze()
def test_analyze_bytes_returns_analysis_result_object():
    with patch("src.vision_client.ImageAnalysisClient") as mock_client_cls:
        mock_client = MagicMock()
        mock_client.analyze.return_value = DummyAnalysisResult(
            caption=DummyCaption(text="A cat on a couch", confidence=0.87),
            tags={"values": [{"name": "cat", "confidence": 0.95}]},
            objects={"values": [{"tags": [{"name": "cat", "confidence": 0.92}]}]}
        )
        mock_client_cls.return_value = mock_client

        client = VisionClient()
        result = client.analyze_bytes(b"fake-image-data")

        assert result.caption.text == "A cat on a couch"
        assert result.caption.confidence == 0.87
        assert result.tags["values"][0]["name"] == "cat"
        assert result.objects["values"][0]["tags"][0]["name"] == "cat"
