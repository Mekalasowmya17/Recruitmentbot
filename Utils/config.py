import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
GOOGLE_API = os.getenv("GOOGLE_API")
OPENAI_API = os.getenv("OPENAI_API")

# ChromaDB
CHROMA_DB_PATH = "chroma_db"

# Embedding Model
EMBEDDING_MODEL = "models/embedding-001"

# Gemini Model
LLM_MODEL = "gemini-2.5-flash"

# Upload Folder
UPLOAD_FOLDER = "data"

# Number of retrieved documents
TOP_K = 5
