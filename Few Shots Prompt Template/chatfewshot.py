from utils.gemini_client import get_gemini
from langchain.prompts import (
    PromptTemplate,
    FewShotPromptTemplate,
    FewShotChatMessagePromptTemplate,
    ChatPromptTemplate,
)

chat = get_gemini()

# Few Shot Examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

# Correct class name here
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

# print("few shot prompt:", few_shot_prompt.format())

final_prompt= ChatPromptTemplate.from_messages([
    ("system", "You are a helpful math problem solver."),
   few_shot_prompt,
   ("human", "{input}")

])

# print("final prompt:", final_prompt)

formattedChatPrompt= final_prompt.format(
    input="What's the square of a triangle?"
)

# print("formatted chat prompt:", formattedChatPrompt)
response= chat.invoke(formattedChatPrompt)
print("response is", response.content)