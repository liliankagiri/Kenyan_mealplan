import os

# Fetch the GEMINI_API_KEY from the environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def configure_api():
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    return GEMINI_API_KEY
