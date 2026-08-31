# Azure Image Recognition App

A cloud-native Python application that uses Microsoft Azure AI Vision to analyze uploaded images and return intelligent insights such as image captions, object tags, and scene-level understanding.

## Overview

This project demonstrates practical software engineering skills in cloud application development, AI integration, and production-ready API design. It combines a FastAPI backend, a browser-based upload interface, Azure AI integration, and automated deployment workflow patterns to create a complete end-to-end image analysis application.

This repository is suitable for a software engineering portfolio because it reflects real-world engineering concerns: secure configuration, API validation, testable backend logic, deployment automation, and cloud-native service integration.

## Why this project matters

- Builds a full-stack solution using Python, FastAPI, and browser-based UI components
- Integrates with Microsoft Azure AI Vision for real image intelligence features
- Shows cloud deployment readiness using Azure App Service and GitHub Actions
- Includes automated tests for API validation and service behavior
- Uses environment variables and separation of concerns to keep secrets and configuration manageable
- Demonstrates an end-to-end workflow from upload to AI inference to user-visible result

## Features

- Image upload through a simple web interface
- AI analysis using Azure Computer Vision
- Generated image captions with confidence values
- Tag extraction for labels and common scene/object categories
- Object detection summaries from the Vision API
- REST API endpoint for programmatic image analysis
- Local development workflow plus Azure deployment configuration

## Architecture

```text
Browser / Client
      |
      v
FastAPI App (src/api.py)
      |
      +--> Azure AI Vision SDK (src/vision_client.py)
      |
      +--> Azure Computer Vision endpoint + key
      |
      +--> HTML template rendering (src/templates/index.html)
```

## Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, FastAPI |
| Frontend | HTML, Jinja2 templates |
| AI Service | Azure AI Vision Image Analysis |
| Deployment | Azure App Service, Gunicorn, Uvicorn |
| CI/CD | GitHub Actions |
| Testing | pytest |
| Configuration | python-dotenv |

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── main_azure-vision-simon.yml   # Azure deployment workflow
├── src/
│   ├── api.py                             # FastAPI routes and web handlers
│   ├── config.py                          # Environment configuration loader
│   ├── main.py                            # CLI entry point
│   ├── templates/
│   │   └── index.html                     # Upload UI
│   └── vision_client.py                   # Azure Vision client wrapper
├── tests/
│   ├── test_api.py                        # API validation tests
│   └── test_vision_client.py              # Client behavior tests
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── startup.sh
└── project-plan.md
```

## Prerequisites

- Python 3.11+
- An Azure subscription
- Azure AI Vision resource with a valid endpoint and key
- Git installed locally

## Local Setup

1. Clone the repository:

```bash
git clone https://github.com/CoolDude2750/Azure-Image-Recognition-App.git
cd Azure-Image-Recognition-App
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Azure credentials:

```env
VISION_ENDPOINT=https://<your-resource-name>.cognitiveservices.azure.com/
VISION_KEY=<your-azure-vision-key>
```

5. Run the app locally:

```bash
uvicorn src.api:app --reload
```

Then open the browser at http://localhost:8000

## Usage

### Web interface

1. Open the homepage in a browser.
2. Upload an image file.
3. View the generated caption, tags, and object summary returned by Azure AI Vision.

### CLI usage

```bash
python -m src.main path/to/image.jpg
```

### API endpoint

The app exposes a JSON API for analysis requests:

```http
POST /analyze
Content-Type: multipart/form-data
```

Example request:

```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@sample.jpg"
```

Example response:

```json
{
  "caption": "A cat sitting on a sofa",
  "caption_confidence": 0.92,
  "tags": [
    {"name": "cat", "confidence": 0.96},
    {"name": "indoor", "confidence": 0.88}
  ],
  "objects": [
    {"name": "cat", "confidence": 0.94}
  ]
}
```

## Tests

Run the automated test suite with:

```bash
pytest -q
```

The project includes tests for:

- upload validation and error handling
- result normalization and formatting logic
- Azure Vision client invocation behavior

## Deployment

This application is configured for Azure App Service deployment. The repo includes:

- a production startup script in [startup.sh](startup.sh)
- a GitHub Actions deployment workflow in [.github/workflows/main_azure-vision-simon.yml](.github/workflows/main_azure-vision-simon.yml)

Production deployment uses Gunicorn and Uvicorn workers to serve the FastAPI app.

## Live Demo

The current deployment is available here:

- [Azure Image Recognition App](https://azure-vision-simon-e6hugef3ejagdmbh.ukwest-01.azurewebsites.net/)

## Portfolio impact

This project highlights core software engineering strengths relevant to AI and cloud roles:

- Python backend development with FastAPI and modular service design
- Azure cloud integration using managed AI services and deployment tooling
- Secure configuration patterns with environment-based secrets management
- API validation and resilient error handling for user uploads
- Automated testing to protect core functionality and reduce regressions
- End-to-end deployment flow for a production-style web app

## Project summary

Users can upload an image, send it to Azure AI Vision, and receive structured results including captions, confidence-based tags, and detected objects. The solution is intentionally simple, readable, and production-minded, making it a strong example of building and shipping a cloud-connected AI application with clear engineering boundaries.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome. If you want to improve the app, add features, or extend the Azure integration, open a pull request with a clear description of the change.

