import os
from datetime import datetime

def ensure_directory(path):
    """
    Create a directory if it doesn't exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)


def save_uploaded_file(uploaded_file, upload_folder):
    """
    Save uploaded file and return its path.
    """
    ensure_directory(upload_folder)

    file_path = os.path.join(upload_folder, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    return file_path


def format_response(title, content):
    """
    Format output nicely.
    """
    return f"\n{'='*60}\n{title}\n{'='*60}\n{content}\n"


def get_timestamp():
    """
    Return current timestamp.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
