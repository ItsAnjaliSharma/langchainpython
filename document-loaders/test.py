from utils.gemini_client import get_gemini
from langchain.prompts import (
   SystemMessagePromptTemplate, HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

from langchain_community.document_loaders import TextLoader, CSVLoader, BSHTMLLoader, PyPDFLoader

chat= get_gemini()

# Example 1- Text File Loader
# loader = TextLoader('./data/sample.txt')
# mydata= loader.load()
# print(mydata, "My Data from text file")
# print(mydata[0], "My Data from text file 0th index")
# print(mydata[0].page_content, "My Data from text file page content")

# Example 2 - CSV Loader
# loader = CSVLoader('./data/sample.csv')
# mydata= loader.load()   
# # print(mydata, "My Data from CSV file")
# # print(mydata[0], "My Data from CSV file 0th index") 
# print(mydata[0].page_content, "My Data from CSV file page content")


# Example 3 - HTML File Loader
# loader = BSHTMLLoader('./data/sample.html')
# mydata= loader.load()
# # print(mydata, "My Data")
# print(mydata[0].page_content.replace('\n', ' '))


# Example 4 - PDF File

# loader= PyPDFLoader('./data/sample1.pdf')
# mydata= loader.load()
# # print(mydata, "My Data from PDF file")
# print(mydata[0].page_content.replace('\n', ' '), "My Data from PDF file page content")
# # print(mydata[0], "My Data from PDF file 0th index")

# Example 5 - Legal File
loader= TextLoader('./data/legal.txt')
mydata= loader.load()[0].page_content
human_template= "{question}\n{text}"
human_message_prompt= HumanMessagePromptTemplate.from_template(human_template)
# print(mydata, "My Data ")
 
formatted_prompt = human_message_prompt.format_messages(
    question="How Can I Apply for a Addhar Card?",
    text=mydata
)

# print(formatted_prompt[0].content, "My Data ")

response= chat.invoke(formatted_prompt)
# print(response, "My Data from Gemini")
print(response.content, "My Response")