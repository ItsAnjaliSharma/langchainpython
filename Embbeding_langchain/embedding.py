import os
from decouple import config

from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings, HuggingFaceEmbeddings

def get_embeddings():
    provider = config("PROVIDER", default="ollama").lower()

    if provider == "openai":
        return OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_key=config("secret_openai_key")
        )

    elif provider == "ollama":
        # Requires Ollama running locally: `ollama run nomic-embed-text`
        return OllamaEmbeddings(model="nomic-embed-text")

    elif provider == "hf":
        # HuggingFace Sentence Transformers
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    else:
        raise ValueError(f"Unknown PROVIDER: {provider}")
