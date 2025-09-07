from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from gemini_client import chat

def askChef(asked_recipe: str):
    # Human message template (fixed from form_template -> from_template)
    humanMessagePrompt = HumanMessagePromptTemplate.from_template("{asked_recipe}")

    chatPrompt = ChatPromptTemplate.from_messages([
        ("system", "Your name is Jarvis. You are a master chef so First Introduce yourself as Jarivs The Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food related queries. If You don't know the answer then tell I don't know the answer."),
        humanMessagePrompt,
    ])

    formattedPrompt = chatPrompt.format_messages(asked_recipe=asked_recipe)

    response = chat.invoke(formattedPrompt)
    return response.content
