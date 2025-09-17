from langchain_huggingface import HuggingFaceEmbeddings

# Small, fast model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Embed text
# vector = embeddings.embed_query("Hello Sonam")
# print(len(vector), vector[:10])  # length + preview of embedding

# text="This is sample text"
# embedded_query = embeddings.embed_query(text)
# print(embedded_query)

# Embed documents
texts = [
    "Hello Sonam",
    "How are you ?",
    "Where are you now ?"
]

embedded_docs = embeddings.embed_documents(texts)
print(len(embedded_docs))
# print(embedded_docs)