import os

from dotenv import load_dotenv
from supabase import create_client

load_dotenv(".env")

SUPABASE_PROJECT_URL = os.environ["SUPABASE_PROJECT_URL"]
SUPABASE_PUBLIC_KEY = os.environ["SUPABASE_PUBLIC_KEY"]
SUPABASE_SECRET_KEY = os.environ["SUPABASE_SECRET_KEY"] 
SUPABASE_STORAGE_BUCKET = os.environ["SUPABASE_STORAGE_BUCKET"]


supabase = create_client(
    SUPABASE_PROJECT_URL,
    SUPABASE_SECRET_KEY
)


def upload_file(file_path: str, storage_path: str) -> None:

    with open (file_path, 'rb') as file:
        supabase.storage.from_(SUPABASE_STORAGE_BUCKET).upload(
            path=storage_path,
            file=file
        )

def delete_file(storage_file: str) -> None:
    supabase.storage.from_(SUPABASE_STORAGE_BUCKET).remove(
        [storage_file]
    )

def list_files() -> list[str]:

    response = supabase.storage.from_(SUPABASE_STORAGE_BUCKET).list()

    return [item["name"] for item in response if item.get("name")]