# 🌥️ Cloud File Manager

A lightweight Python-based cloud file manager that allows you to **upload, download, list, and manage files** stored on **AWS S3**.  
Built with a clean structure, logging system, and modular architecture.

---

## 🚀 Features

- 📤 Upload files to AWS S3  
- 📥 Download files from AWS S3  
- 📄 List all files stored in S3 bucket  
- 🗑️ Delete files  
- 🛠️ Modular architecture  
- 📝 SQLite-based logs  
- 🔐 Secure environment variables using `.env`  
- 🌐 Easy to extend with APIs or GUI

---

## 🗂️ Project Structure

cloud-file-manager/
│
├── src/
│ ├── app.py
│ ├── main.py
│ ├── config.py
│ ├── s3_manager.py
│ └── database_logs.py
│
├── .gitignore
└── README.md


---

## 🔧 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/cloud-file-manager.git
cd cloud-file-manager


2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Create .env in src/ folder
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_REGION=ap-south-1
AWS_BUCKET_NAME=your_bucket
LOG_DB_PATH=file_logs.db


⚠️ Never upload .env to GitHub.

▶️ How to Run the Project
python src/main.py


You will see menu options:

1. Upload File
2. Download File
3. List Files
4. Delete File
5. View Logs
6. Exit

📝 Logging System

All actions are stored in file_logs.db to track uploads, downloads, and deletions.

☁️ AWS Requirements

AWS Account

S3 Bucket

IAM User with S3 permissions

Keys stored securely in .env

👤 Author

Ashutosh Parve
Made with ❤️ in India 🇮🇳


---


