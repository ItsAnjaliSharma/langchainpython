from decouple import config
from langchain_google_genai import ChatGoogleGenerativeAI

def get_gemini(model_name: str = "gemini-2.5-flash") -> ChatGoogleGenerativeAI:
    """
    Returns a reusable Gemini model instance.
    Reads the secret_gemini_key from .env using python-decouple.
    """
    secret_gemini_key = config("secret_gemini_key", default=None)
    if not secret_gemini_key:
        raise ValueError("❌ secret_gemini_key not found in environment. Check your .env file.")

    return ChatGoogleGenerativeAI(
        model=model_name,
        api_key=secret_gemini_key
    )