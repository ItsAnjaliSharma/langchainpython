from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever
# Replace with your LLM chain instance

#load documents

loader = TextLoader("data/notes.txt", encoding="utf-8")
documents = loader.load()

#split documents
text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)

my_documents = text_splitter.split_documents(documents)

#embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

#vectorstore
vectorstore = Chroma.from_documents(my_documents, embeddings, collection_name="my_collection", persist_directory="./chroma_db")
vectorstore.persist()

# Read from ChromaDB
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings, collection_name="my_collection")

query = "When Royal Enfield launches the all-new Meteor 350 line-up in India?."
docs = vectorstore.similarity_search(query, k=4)
print(f"Number of docs from vectorstore: {len(docs)}")
print(docs[0].page_content, "Answer not compressed")