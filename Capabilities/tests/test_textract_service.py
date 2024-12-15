import unittest
from unittest.mock import patch, Mock
from Capabilities.chalicelib.textract_service import TextractService


class TextractServiceTest(unittest.TestCase):
    @patch("Capabilities.chalicelib.textract_service.boto3.client")
    def setUp(self, mock_boto_client):
        # Mock storage_service
        self.mock_storage_service = Mock()
        self.mock_storage_service.get_storage_location.return_value = "mock-bucket-name"

        # Create the mock Textract client
        self.mock_textract_client = mock_boto_client.return_value

        # Initialize TextractService with the mocked storage_service
        self.service = TextractService(self.mock_storage_service)

    @patch("Capabilities.chalicelib.textract_service.boto3.client")
    def test_detect_text(self, mock_boto_client):
        # Mock the Textract response
        self.mock_textract_client.detect_document_text.return_value = {
            "Blocks": [
                {
                    "BlockType": "LINE",
                    "Text": "This is a sample line",
                    "Confidence": 98.5,
                    "Geometry": {
                        "BoundingBox": {
                            "Width": 0.5,
                            "Height": 0.1,
                            "Left": 0.1,
                            "Top": 0.1,
                        }
                    },
                }
            ]
        }

        # Call the method
        result = self.service.detect_text("sample_image.jpg")

        # Assert the result
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "This is a sample line")
        self.assertEqual(result[0]["confidence"], 98.5)
        self.assertAlmostEqual(result[0]["boundingBox"]["Width"], 0.5)
        self.assertAlmostEqual(result[0]["boundingBox"]["Height"], 0.1)


if __name__ == "__main__":
    unittest.main()
