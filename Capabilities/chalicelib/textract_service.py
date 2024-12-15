import boto3


class TextractService:
    def __init__(self, storage_service):
        # Creates a boto3 client for Textract
        self.client = boto3.client("textract")
        # Get the S3 bucket name from the storage service
        self.bucket_name = storage_service.get_storage_location()

    def detect_text(self, file_name):
        # Call Textract's detect_document_text method with the S3 bucket and file name
        response = self.client.detect_document_text(
            Document={"S3Object": {"Bucket": self.bucket_name, "Name": file_name}}
        )

        # Filter out only the 'LINE' types of text detections
        lines = []
        for block in response.get("Blocks", []):
            if block["BlockType"] == "LINE":
                lines.append(
                    {
                        "text": block["Text"],
                        "confidence": block["Confidence"],
                        "boundingBox": block["Geometry"]["BoundingBox"],
                    }
                )

        return lines
