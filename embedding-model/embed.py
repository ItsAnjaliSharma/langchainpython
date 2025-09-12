from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY")

# Initialize client
client = genai.Client(
    api_key=API_KEY,
    http_options=types.HttpOptions(api_version="v1alpha")
)

# Input text
word = "Health care"

# Generate embeddings
response = client.models.embed_content(
    model="models/embedding-001",   # ✅ Correct embedding model path
    contents=[word],                # ✅ Pass as a list, not just a string
)

# Extract embedding vector
word_embedding = response.embeddings[0].values

print(f"Embedding length: {len(word_embedding)}")
print(word_embedding[:10])  # print first 10 values