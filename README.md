# Azure Image Recognition App

A cloud-native web application that leverages Microsoft Azure Computer Vision to provide intelligent image analysis and recognition capabilities. Users can upload images and receive AI-powered insights including object detection, scene understanding, text extraction, and detailed descriptions with confidence scores.

## Overview

This project demonstrates end-to-end expertise in AI engineering, cloud architecture, and full-stack development using modern cloud services. It combines a responsive web frontend with a robust backend API, showcasing best practices in API design, cloud integration, and scalable application deployment on Microsoft Azure.

## Features

- **Image Upload & Analysis**: Upload images through an intuitive web interface
- **AI-Powered Insights**: Leverage Azure Computer Vision for:
  - Object and scene detection
  - Automated image labeling and tagging
  - Generated image descriptions
  - Confidence scoring for all predictions
- **RESTful API**: Comprehensive API for programmatic access
- **Cloud-Native Architecture**: Deployed on Azure App Service for scalability and reliability
- **Responsive Design**: Modern, mobile-friendly user interface

## Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python with FastAPI |
| **Frontend** | HTML5 with responsive CSS |
| **AI Service** | Azure Computer Vision API |
| **Cloud Deployment** | Azure App Service |
| **Storage** | Azure Blob Storage (optional) |
| **Testing** | pytest |

## Project Structure

```
.
├── app.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── src/
│   ├── api.py            # FastAPI routes and endpoints
│   ├── main.py           # Application initialization
│   ├── vision_client.py   # Azure Computer Vision integration
│   ├── config.py         # Configuration management
│   └── templates/
│       └── index.html    # Web interface
├── tests/
│   └── test_vision_client.py  # Unit tests
└── README.md
```

## Installation

### Prerequisites

- Python 3.8 or higher
- Azure subscription with Computer Vision API access
- Azure Computer Vision API key and endpoint

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/CoolDude2750/Azure-Image-Recognition-App.git
   cd Azure-Image-Recognition-App
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure Azure credentials:
   Create a `.env` file in the project root:
   ```
   AZURE_VISION_KEY=your_api_key
   AZURE_VISION_ENDPOINT=your_api_endpoint
   ```

5. Run the application:
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:8000`

## Usage

### Web Interface

1. Navigate to the application URL
2. Click "Upload Image" and select an image file
3. View AI-generated analysis including:
   - Object labels and categories
   - Image description
   - Detected text (if any)
   - Confidence scores

### API Endpoints

**Analyze Image**
```
POST /api/analyze
Content-Type: multipart/form-data

Parameters:
  - image: Image file (JPEG, PNG, BMP, GIF)

Response:
{
  "description": "string",
  "tags": ["tag1", "tag2"],
  "objects": [{"name": "object", "confidence": 0.95}],
  "text": "detected text if present"
}
```

## Running Tests

Execute the test suite:
```bash
pytest tests/
```

## Deployment

The application is designed for Azure App Service deployment. For detailed deployment 
instructions, see `project-plan.md`.

## Live Demo

Try the application here: [Azure Image Recognition App](https://azure-vision-simon-e6hugef3ejagdmbh.ukwest-01.azurewebsites.net/)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or inquiries, please open an issue in the GitHub repository.

