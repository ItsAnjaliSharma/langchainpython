from utils.gemini_client import get_gemini
from langchain.prompts import (
   SystemMessagePromptTemplate, HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

from langchain.text_splitter import CharacterTextSplitter,  Language, RecursiveCharacterTextSplitter, TokenTextSplitter, MarkdownHeaderTextSplitter, PythonCodeTextSplitter

chat=get_gemini()

# # Example 1: Character Text Splitter

# with open("./data/sample.txt", "r") as file:
#     sample_data = file.read()
# #in character text splitter we can define the separator and chunk size but it will not split the text if the chunk size is not reached  

# text_splitter = CharacterTextSplitter(
#     separator="\n\n", 
#     chunk_size=200
# )

# myData = text_splitter.create_documents([sample_data])
# print(myData)
# print(len(myData))
# print(myData[0].page_content)

# Example 2: Split Code

PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0
)
python_docs = python_splitter.create_documents([PYTHON_CODE])
print(python_docs)
