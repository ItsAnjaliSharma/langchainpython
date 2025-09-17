# langchainpython
Large Language Models

- To run python program install code runner extension

- To add langchain into my simple project you can go to the folder of your project and run 
```bash  pip i langchain```   

- OR

- You can create virtual env by run 
```bash 
 virtualenv env
 ```  

 the name of env at the last which are our virtual env or you can run
```bash    
python -m venv env
```
- to activate env 
  ```
  bash  
  env\scripts\activate
  ```
  or ```bash  env\bin\activate```    or 
  ```bash  venv\Scripts\activate.bat(for windows)```
  ```bash  
  env\scripts\activate```
  or 
  ```bash
    env\bin\activate```
        or 
  ```bash 
   venv\Scripts\activate.bat(for windows)
   ```


- pip freeze to check which package are installed
- pip install langchain

- When we used model in this we used hugging face access token

- to install all requirement.txt file run
```bash
pip freeze > requirements.txt
```
```bash  
pip install -r requirements.txt
```  

- To Create django Project start 
```bash
django-admin startproject
```

- to start django app
```bash
python manage.py startapp chef 
```

- To Use Embbeding Model Free you can use HuggingFace + Ollama are free & unlimited once set up. Let me show you both step by step so you can pick the one that fits your machine.

🔹 1. HuggingFace Embeddings (CPU-only, simple setup)

👉 Best if you don’t want to install heavy models locally.

Install requirements:
pip install sentence-transformers langchain-huggingface

Example code:
from langchain_huggingface import HuggingFaceEmbeddings

# Small, fast model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Embed text
vector = embeddings.embed_query("Hello Sonam")
print(len(vector), vector[:10])  # length + preview of embedding


✅ This downloads the model once from HuggingFace Hub and caches it locally.
✅ Works offline after first download.
⚡ Runs on CPU, lightweight.

🔹 2. Ollama Embeddings (local LLM server)

👉 Best if you want to run models fully offline.

Step 1: Install Ollama

Download from 👉 https://ollama.com/download

Run Ollama server (it runs automatically in background after install).

Step 2: Pull an embedding model
ollama pull mxbai-embed-large


(You can also use nomic-embed-text if you want smaller + faster.)

Step 3: Install LangChain Ollama
pip install langchain-community

Step 4: Example code
from langchain_community.embeddings import OllamaEmbeddings

# Use pulled model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Embed text
vector = embeddings.embed_query("Hello Sonam")
print(len(vector), vector[:10])


✅ Runs fully local (no quota, no API key).
✅ Works offline.
⚡ Faster on GPU, but also works on CPU.

🔹 Recommendation

If you want easy + light → HuggingFace (all-MiniLM-L6-v2).

If you want offline + powerful → Ollama (mxbai-embed-large).

👉 Do you want me to update your embedding.py factory so you can just set .env like:

PROVIDER=hf
PROVIDER=ollama


and it will automatically switch without changing your Python code?
