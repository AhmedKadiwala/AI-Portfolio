import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment")