from chalice.app import Chalice, Response
from chalicelib.storage_service import StorageService
from chalicelib.textract_service import TextractService
from chalicelib.translation_service import TranslationService
import base64
import json

#####
# chalice app configuration
#####
app = Chalice(app_name="Capabilities")
app.debug = True

#####
# services initialization
#####
STORAGE_LOCATION = "contentsawsai-hos02"  # Your actual S3 bucket name
storage_service = StorageService(STORAGE_LOCATION)
recognition_service = TextractService(storage_service)
translation_service = TranslationService()


#####
# RESTful endpoints
#####
@app.route("/images/{image_id}/text", methods=["POST"], cors=True)
def extract_text(image_id):
    """
    Extract text from the specified image.
    """
    # Detect text in the image
    text_lines = recognition_service.detect_text(image_id)

    # Return extracted text
    extracted_text = [
        {
            "text": line["text"],
            "confidence": line["confidence"],
            "boundingBox": line["boundingBox"],
        }
        for line in text_lines
    ]
    return extracted_text


@app.route("/translate", methods=["POST"], cors=True)
def translate_text():
    """
    Translate the provided text to the target language.
    """
    # Parse request data
    request = app.current_request
    if request is None:
        return Response(body={"error": "Request is missing"}, status_code=400)

    request_data = json.loads(request.raw_body)
    text = request_data.get("text")
    from_lang = request_data.get("fromLang", "auto")
    to_lang = request_data.get("toLang", "en")

    if not text:
        return Response(body={"error": "Text is missing"}, status_code=400)

    # Translate text
    translated_text = translation_service.translate_text(text, from_lang, to_lang)
    return translated_text


@app.route("/images", methods=["POST"], cors=True)
def upload_image():
    """
    Processes file upload and saves file to storage service.
    """
    request = app.current_request
    if request is None:
        return Response(body={"error": "Request is missing"}, status_code=400)
    request_data = json.loads(request.raw_body)

    # Get the file name and file bytes
    file_name = request_data.get("filename")
    file_bytes = base64.b64decode(request_data.get("filebytes", ""))

    # Check if file bytes are empty
    if not file_bytes:
        return Response(
            body={"error": "Uploaded file is empty or invalid"}, status_code=400
        )

    # Upload the file to the storage service
    image_info = storage_service.upload_file(file_bytes, file_name)

    return image_info
