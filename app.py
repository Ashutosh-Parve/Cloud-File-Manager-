from s3_manager import upload_file, download_file, delete_file
from database_logs import log_action, create_log_table

create_log_table()

print("1. Upload File")
print("2. Download File")
print("3. Delete File")
choice = input("Enter option: ")

if choice == "1":
    file_path = input("Enter local file path: ").strip('"')

    filename = input("Enter filename for S3: ")
    upload_file(file_path, filename)
    log_action("UPLOAD", filename)

elif choice == "2":
    filename = input("Enter filename to download: ")
    download_path = input("Enter local download path: ")
    download_file(filename, download_path)
    log_action("DOWNLOAD", filename)

elif choice == "3":
    filename = input("Enter filename to delete: ")
    delete_file(filename)
    log_action("DELETE", filename)

else:
    print("Invalid choice")
