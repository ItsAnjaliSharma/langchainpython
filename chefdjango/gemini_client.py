# gemini_client.py

from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI

# Load Gemini key from .env
GEMINI_KEY = config("secret_gemini_key")

# Initialize Gemini 2.5 Flash model
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_KEY
)
