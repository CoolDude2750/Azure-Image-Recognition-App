from config import settings
from src.vision_client import VisionClient

def main():
    client = VisionClient(settings.ENDPOINT, settings.KEY)

    # Image Upload
    image_path = input("Enter the path to an image: ")
    result = client.analyze(image_path)

   # Captions
    print("Caption:", result.caption.text)

    # Tags
    tags = result.tags.get("values", [])
    print("Tags:", [tag["name"] for tag in tags])

    # Objects
    objects = result.objects.get("values", [])
    print("Objects:", [obj["tags"][0] for obj in objects if obj.get("tags")])



if __name__ == "__main__":
    main()


