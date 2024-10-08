import os
from config.aws_config import get_s3_client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def upload_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to an S3 bucket."""

    s3_client = get_s3_client()
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File uploaded successfully: {object_name}")
    except Exception as e:
        print(f"Failed to upload file: {e}")
