from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# Load Gemini key
GEMINI_KEY = config("secret_gemini_key")

# Initialize Gemini 2.5 Flash model
chat = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_KEY
)

# Chat Model - Prompt Template

# Example 1 - Message Prompt Templates as Tuples

# chatPrompt= ChatPromptTemplate.from_messages([
#     ("system","You are a helpful assistant that translate {input_language} to {output_language}."),
#      ("human","{text}"),
#     #  ("ai":"")
# ])

# print("Chat Prompt: ", chatPrompt)
# print("Chat Prompt Input Variables: ", chatPrompt.input_variables)

# formattedChatPrompt= chatPrompt.format_messages(
#     input_language="English",
#     output_language="Korean",
#     text="Anjali"
# )

# print("Formatted Chat Prompt: ", formattedChatPrompt)
# response=chat.invoke(formattedChatPrompt)

# print("Response: ", response.content)


## Example 2 - Using Message Prompt Classes

# sys_template="You are a helpful assistant that translates {input_language} to {output_language}."
# human_template="{text}"

# chatPrompt =ChatPromptTemplate.from_messages([
#     SystemMessagePromptTemplate.from_template(sys_template),
#     HumanMessagePromptTemplate.from_template(human_template)
# ])
# # print("Chat Prompt: ", chatPrompt)
# # print("Chat Prompt Input Variables: ", chatPrompt.input_variables)

# formattedChatPrompt= chatPrompt.format_messages(
#     input_language="English",
#     output_language="Hindi",
#     text="I am an software developer"
# )

# print("Formatted Chat Prompt is: ", formattedChatPrompt)
# # response=chat.invoke(formattedChatPrompt)
# # print("response", response.content)


## Example 3

# systemPrompt= PromptTemplate(
#     input_variables=["input_language", "output_language"],
#     template="You are a helpful assistant that translates {input_language} to {output_language}."
# )

# print(systemPrompt)

systemPrompt= PromptTemplate.from_template(
    "You are a helpful assistant that translates {input_language} to {output_language}."
)

humanPrompt=PromptTemplate.from_template("{text}")
SystemMessagePrompt= SystemMessagePromptTemplate(prompt=systemPrompt)
HumanMessagePrompt=HumanMessagePromptTemplate(prompt=humanPrompt)


chatPrompt=ChatPromptTemplate.from_messages([
    SystemMessagePrompt,HumanMessagePrompt
])

# print("Chat Prompt:", chatPrompt)

formattedChatPrompt= chatPrompt.format_messages(
    input_language="English",
    output_language="French",
    text="I love Music"
)

print("Formatted Chat Prompt:", formattedChatPrompt)
response= chat.invoke(formattedChatPrompt)
print("Response: ", response)
print("Response Content:", response.content)
