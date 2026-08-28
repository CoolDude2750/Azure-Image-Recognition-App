import argparse

from src.config import settings
from src.vision_client import VisionClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze an image with Azure Vision.")
    parser.add_argument("image", help="Path to the image to analyze")
    args = parser.parse_args()

    client = VisionClient(settings.ENDPOINT, settings.KEY)

    result = client.analyze(args.image)

    caption = result.caption.text if result.caption else "No caption detected."
    print("Caption:", caption)

    tags = result.tags.get("values", [])
    print("Tags:", [tag["name"] for tag in tags if tag.get("name")])

    objects = result.objects.get("values", [])
    print("Objects:", [obj["tags"][0].get("name") for obj in objects if obj.get("tags")])

if __name__ == "__main__":
    main()


