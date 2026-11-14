
from app.services.storage import (
    upload_file,
    list_files,
    delete_file
)

upload_file(
    file_path="test_files/Pritam_Mahanta_Resume.pdf",
    storage_path="Pritam_Mahanta_Resume.pdf"
)

print("Upload successful!")

files = list_files()

print("Available files:", files)

assert "Pritam_Mahanta_Resume.pdf" in files

print("File listing successful!")

delete_file("Pritam_Mahanta_Resume.pdf")

print("Deletion successful!")

files = list_files()

assert "Pritam_Mahanta_Resume.pdf" not in files

print("All integration tests passed!")
