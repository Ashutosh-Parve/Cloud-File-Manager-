import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

load_dotenv()

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

bucket_name = os.getenv("AWS_BUCKET_NAME")

def upload_file(file_path, filename):
    try:
        s3.upload_file(file_path, bucket_name, filename)
        print(f"Uploaded: {filename}")
    except Exception as e:
        print("Error:", e)

def download_file(filename, download_path):
    try:
        s3.download_file(bucket_name, filename, download_path)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print("Error:", e)

def delete_file(filename):
    try:
        s3.delete_object(Bucket=bucket_name, Key=filename)
        print(f"Deleted: {filename}")
    except Exception as e:
        print("Error:", e)
