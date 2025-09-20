from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Add memory to remember conversation
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=gemini,
    memory=memory,
    verbose=True
)

# Now it remembers previous messages
response1 = conversation.predict(input="My name is Alice")
response2 = conversation.predict(input="What's my name?")