import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REGION_NAME = os.getenv("REGION_NAME")
BUCKET_NAME = os.getenv("BUCKET_NAME")
DOWNLOAD_FOLDER = os.getenv("DOWNLOAD_FOLDER")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
