from langchain.output_parsers import DatetimeOutputParser, CommaSeparatedListOutputParser, PydanticOutputParser
from utils.gemini_client import get_gemini
from langchain.prompts import (
   SystemMessagePromptTemplate, HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
# If you see "No module named 'pydantic_v1'", you should install the correct package.
# Try installing 'pydantic' (version 1.x) using:
# pip install "pydantic<2"
# Then, you can import BaseModel and Field from 'pydantic' instead of 'pydantic_v1':
# from pydantic import BaseModel, Field
from pydantic import BaseModel, Field

chat= get_gemini()

#Example 1

# date_time_parser=DatetimeOutputParser()
# # print(date_time_parser.get_format_instructions())
# # langchain predefined the format of text to specify user only give input into that format 


# comma_sep_parser=CommaSeparatedListOutputParser()
# print(comma_sep_parser.get_format_instructions())
# langchain predefined the format of text to specify user only give input into that format like this Your response should be a list of comma separated values


#Example 2
# date_time_parser=DatetimeOutputParser()
# human_temp="{request}\n{format_instruction}"
# chat_prompt = ChatPromptTemplate.from_messages([
#     ("human", human_temp)
# ])


# # print(chat_prompt, "chat prompts")

# formatted_chat_prompt = chat_prompt.format_messages(
#     request="What date was when the first world traveller travel",
#     format_instruction=date_time_parser.get_format_instructions()
# )


# # print("Formatted Chat Prompt: ", formatted_chat_prompt)

# response= chat.invoke(formatted_chat_prompt)

# print("response", response.content)
# print("response content parse", date_time_parser.parse(response.content))


## Example 3
## define your desired data structure

class Cricketer(BaseModel):
    name: str= Field(description="Name of Cricketer")
    records:list=Field(description="Python List of Records")

parser = PydanticOutputParser(pydantic_object=Cricketer)
# print(parser.get_format_instructions())

human_temp="{request}\n{format_instruction}"
chat_prompt = ChatPromptTemplate.from_messages([
    ("human", human_temp)
])

# print(chat_prompt, "chat prompts")
formatted_chat_prompt = chat_prompt.format_messages(
    request="Tell me about Sachin Tendulkar",
    format_instruction=parser.get_format_instructions()
)
# print("Formatted Chat Prompt: ", formatted_chat_prompt)

response= chat.invoke(formatted_chat_prompt)
print("response", response.content)
print("response content parse", parser.parse(response.content))