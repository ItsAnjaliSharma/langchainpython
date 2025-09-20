from decouple import config
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

emb_model = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
result = emb_model.embed_query("Hello world")
print(result)
