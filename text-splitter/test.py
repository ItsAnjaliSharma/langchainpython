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

# Example 2: Split Code of python

# PYTHON_CODE = """
# def hello_world():
#     print("Hello, World!")

# # Call the function
# hello_world()
# """
# python_splitter = RecursiveCharacterTextSplitter.from_language(
#     language=Language.PYTHON, chunk_size=100, chunk_overlap=0
# )
# python_docs = python_splitter.create_documents([PYTHON_CODE])
# print(python_docs)


# Example 3: Split markdown file

markdown_text = """
# 🦜️🔗 LangChain

⚡ Building applications with LLMs through composability ⚡

## What is LangChain?

# Hopefully this code block isn't split
LangChain is a framework for...

As an open-source project in a rapidly developing field, we are extremely open to contributions.
"""

md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=60, chunk_overlap=0
)
md_docs = md_splitter.create_documents([markdown_text])
print(md_docs)

# Example 4: Split text based on tokens
