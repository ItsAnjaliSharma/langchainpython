from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from decouple import config

# Load Gemini API Key
GEMINI_KEY = config("secret_gemini_key")

# Initialize Gemini model in LangChain
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-1.5-pro"
    google_api_key=GEMINI_KEY
)

# Example 1: Simple prompt

response = chat.invoke("Hey Gemini, Tell Me The Levels of Knowledge You Have?")
print(response.content)

