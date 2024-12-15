# Textbook Translator

Textbook Translator is a web-based application designed to extract text from uploaded images and provide translations for the extracted text. This project demonstrates the integration of several AWS services to create a robust, serverless architecture for text extraction and translation.

---

## Features
1. **Upload Images:** Users can upload images containing text.
2. **Text Extraction:** Extracts text from uploaded images using AWS Textract.
3. **Text Translation:** Translates extracted text into a variety of languages using AWS Translate.
4. **User-Friendly Interface:** A frontend built for easy interaction with backend services.

---

## Architecture Overview

The application leverages a **serverless architecture** that separates concerns into two layers:
- **Orchestration Layer:** AWS Chalice serves as the API gateway and orchestrator, routing requests and handling user interactions.
- **Services Implementation:** Backend logic that integrates with AWS services such as Textract, Translate, and S3 for handling requests.

### Key Components

#### 1. **AWS Chalice**
- Acts as the **orchestration layer** for the application.
- Manages API endpoints:
  - `/images`: Upload images to S3.
  - `/images/{image_id}/text`: Extract text using Textract.
  - `/translate`: Translate extracted text using AWS Translate.
- Deploys the application as AWS Lambda functions.

#### 2. **AWS S3**
- Serves as the storage service for uploaded images.
- Enables public access to the images for processing and viewing.

#### 3. **AWS Textract**
- Extracts text from images.
- Utilized for document analysis to detect lines of text in various formats.

#### 4. **AWS Translate**
- Provides translations for the extracted text.
- Supports multiple source and target languages for translation.

---

## Installation

### Prerequisites
- AWS CLI installed and configured.
- Python 3.9+ with Pipenv for managing dependencies.
- An AWS account with appropriate permissions.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/benbenbuhben/TextbookTranslator.git
   cd TextbookTranslator
  ```

  TODO: Add the remaining steps