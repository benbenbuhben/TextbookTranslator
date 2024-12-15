import boto3


class StorageService:
    def __init__(self, storage_location):
        # Create an S3 client using Boto3
        self.client = boto3.client("s3")
        # Store the S3 bucket name
        self.bucket_name = storage_location

    # Method to return the bucket name
    def get_storage_location(self):
        return self.bucket_name

    # Method to upload a file to S3
    def upload_file(self, file_bytes, file_name):
        # Upload the file to S3 without specifying the ACL
        self.client.put_object(
            Bucket=self.bucket_name,
            Body=file_bytes,  # The raw bytes of the file
            Key=file_name,  # The file name (or key) under which the file will be saved
        )

        # Return the file information, including a public URL to access the file
        return {
            "fileId": file_name,
            "fileUrl": f"http://{self.bucket_name}.s3.amazonaws.com/{file_name}",
        }
