from langchain_google_genai import GoogleGenerativeAIEmbeddings
from decouple import config

# Get key from .env
GEMINI_KEY = config("secret_gemini_key")
print(GEMINI_KEY)

# Initialize Gemini embeddings
embeddings_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",  # Gemini embedding model
    google_api_key=GEMINI_KEY
)

# Embed Query
text = "This is sample text"
embedded_query = embeddings_model.embed_query(text)
# print(embedded_query)

# Embed Documents
texts = [
    "Hello Sonam",
    "How are you ?",
    "Where are you now ?"
]

embedded_docs = embeddings_model.embed_documents(texts)
# print(embedded_docs)
print(len(embedded_docs))
