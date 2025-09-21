from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter

# # Example 1 

# # three step process to load, split, and store documents in ChromaDB

# # Load documents from a text file
# loader = TextLoader("./data/history.txt")
# history_documents = loader.load()

# # Split documents into smaller chunks
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# history_docs = text_splitter.split_documents(history_documents)

# # Embed and store documents in ChromaDB
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# # Create a ChromaDB vector store from the documents
# vectorstore = Chroma.from_documents(history_docs, embeddings, collection_name="history_collection")

# query = "When was Johannes Gutenberg introduced the printing?"

# # similar_docs = vectorstore.similarity_search(query)

# # print(similar_docs)

# #vector store retrieval example

# retriver = vectorstore.as_retriever()
# similar_docs = retriver.get_relevant_documents(query)
# print(similar_docs[0].page_content)

# Example 2

# three step process to load, split, and store documents in ChromaDB

# Load documents from a text file
loader = TextLoader("./data/history.txt")
history_documents = loader.load()

# Split documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
history_docs = text_splitter.split_documents(history_documents)

# Embed and store documents in ChromaDB
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create a ChromaDB vector store from the documents
vectorstore = Chroma.from_documents(history_docs, embeddings, collection_name="history_collection", persist_directory="./chroma_db")

# persist the database to disk so that it can be loaded later without needing to re-ingest the documents
vectorstore.persist()

# Read the persisted database from disk
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings , collection_name="history_collection")
query = "When was Johannes Gutenberg introduced the printing?"


# similar_docs = vectorstore.similarity_search(query)



# print(similar_docs)

#vector store retrieval example

retriver = vectorstore.as_retriever(search_kwargs={"k":2})
similar_docs = retriver.get_relevant_documents(query)
print(similar_docs[0])