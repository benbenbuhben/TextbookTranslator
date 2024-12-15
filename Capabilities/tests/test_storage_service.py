import unittest
from unittest.mock import patch
from chalicelib.storage_service import StorageService


class StorageServiceTest(unittest.TestCase):
    @patch("Capabilities.chalicelib.storage_service.boto3.client")
    def setUp(self, mock_boto_client):
        mock_s3_client = mock_boto_client.return_value
        self.service = StorageService("test-bucket")

    @patch("Capabilities.chalicelib.storage_service.boto3.client")
    def test_upload_file(self, mock_boto_client):
        # Simulate a successful S3 upload
        mock_s3_client = mock_boto_client.return_value
        mock_s3_client.put_object.return_value = {}

        # Call the method
        result = self.service.upload_file(b"file data", "testfile.txt")

        # Assert the result
        self.assertEqual(result["fileId"], "testfile.txt")
        self.assertIn(
            "http://test-bucket.s3.amazonaws.com/testfile.txt", result["fileUrl"]
        )


if __name__ == "__main__":
    unittest.main()
