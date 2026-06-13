# Project Plan – Azure Image Recognition App

## 1. Project Overview
A cloud-based image recognition web application that allows users to upload an image and receive AI-generated insights using Azure Computer Vision. The goal is to demonstrate practical skills in AI engineering, cloud development, and end-to-end solution design.

## 2. Objectives
- Build a functional image recognition web app using Python.
- Integrate Azure Computer Vision for image analysis.
- Deploy the application to Azure App Service.
- Create clean, professional documentation suitable for portfolio use.

## 3. Features (MVP)
- Upload an image through a web interface.
- Send the image to Azure Computer Vision.
- Display detected objects, tags, and descriptions.
- Show confidence scores.
- Provide a simple, clean UI.

## 4. Optional Future Enhancements
- Bounding boxes around detected objects.
- Store uploaded images in Azure Blob Storage.
- Add a history/log of previous analyses.
- Add user authentication.
- Add additional Azure AI services (Face API, OCR, etc.)

## 5. Architecture (High-Level)
User → Web App (Streamlit or Flask) → Azure Computer Vision → Results → Web App

## 6 UI Layout Sketch (Text-Based Wireframe)
 ---------------------------------------------------------
|                 Azure Image Recognition App             |
 ---------------------------------------------------------

 [ Upload an Image ]
 (Button to select JPG/PNG file)

 ---------------------------------------------------------
|                     Image Preview                       |
|   [ Display the uploaded image here ]                   |
 ---------------------------------------------------------

 ---------------------------------------------------------
|                     Analysis Results                    |
|  - Description: "A person riding a bicycle..."          |
|  - Tags: bicycle, person, street, outdoor               |
|  - Objects Detected:                                    |
|       • Person (confidence: 0.98)                       |
|       • Bicycle (confidence: 0.95)                      |
|  - Confidence Scores displayed clearly                  |
 ---------------------------------------------------------

 [ Re‑upload another image ]   [ Clear ]

 Footer: "Powered by Azure Computer Vision"

## 7. Technology Stack
- Python 3.x
- Streamlit or Flask (UI)
- Azure Computer Vision (AI service)
- Azure App Service (deployment)

## 8. Folder Structure
azure-image-recognition-app/ │ ├── app/ │   ├── main.py │   ├── azure_client.py │   ├── utils.py │   ├── static/ │   └── templates/ (if using Flask) │ ├── tests/ ├── docs/ │   ├── architecture.png │   └── ui-sketch.png │ ├── README.md ├── project-plan.md ├── requirements.txt ├── .gitignore └── LICENSE


## 9. Development Timeline (April 2026)
**Week 1:**  
- Set up repo, folder structure, and environment  
- Create Azure Computer Vision resource  
- Write first Python script to call the API  

**Week 2:**  
- Build Streamlit/Flask UI  
- Connect UI to Azure API  
- Display results  

**Week 3:**  
- Polish UI  
- Add optional features  
- Add documentation and screenshots  

**Week 4:**  
- Deploy to Azure App Service  
- Final testing  
- Update README and portfolio  

## 10. Testing Approach
- Manual testing with different images.
- Validate API responses.
- Fix errors as they appear.
- Optional: add simple automated tests.

## 11. Deployment Plan
- Push code to GitHub.
- Deploy via Azure App Service (free tier).
- Configure environment variables for API keys.
- Test live version.

## 12. Success Criteria
- App runs locally and in Azure.
- Users can upload images and receive AI results.
- Clean, professional documentation.
- Demonstrates cloud + AI + Python skills.
- GitHub (version control)

