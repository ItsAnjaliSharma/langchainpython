from decouple import config
import google.generativeai as genai

# get the key from .env
secret_gemini_key = config("secret_gemini_key")

# configure Gemini
genai.configure(api_key=secret_gemini_key)

model = "models/embedding-001"

result = genai.embed_content(
    model=model,
    content="this is a text to be embedded"
)

print(result)
