import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3.6-flash"
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")