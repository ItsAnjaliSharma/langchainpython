from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from decouple import config

# Load OpenAI API Key
OPENAI_KEY = config("secret_openai_key")

# Initialize OpenAI model in LangChain
chat = ChatOpenAI(
    model="gpt-4o-mini",   # or "gpt-4o", "gpt-3.5-turbo"
    api_key=OPENAI_KEY
)

# Example 1: Simple prompt
response = chat.invoke("Hey GPT, Tell Me The Levels of Knowledge You Have?")
print(response.content)
