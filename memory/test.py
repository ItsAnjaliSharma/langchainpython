
# Chains
from transformers import pipeline
from langchain.schema import BaseOutputParser
from langchain_community.chains.conversation.base import ConversationChain

# Memory
from langchain_community.memory import (
    ChatMessageHistory,
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
    ConversationEntityMemory,
    ConversationSummaryBufferMemory,
    VectorStoreRetrieverMemory,
)
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE

# LLMs / Embeddings
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEmbeddings

from operator import itemgetter

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


# Example 1 ChatMessageHistory
history= ChatMessageHistory()
history.add_user_message("Hi! How Are You?")
history.add_ai_message("Hello, I'm Great. What About You?")
history.add_user_message("I'm Fine. Are You Interested In Talk, Right Now?")
history.add_ai_message("Yes We Can Talk. Tell me what is in your mind?")
print(history)
# To See conversation in Array Format 
print(history.message)


# Conversational Buffer Memory  

# memory= ConversationBufferMemory()

# memory.save_context({"input":"Hi! there"}, {"output": "Hello Whats up"})
# print(memory)
# print(memory.Buffer) # to see actual
# print(memory.load_memory_variables({}))

# Using Conversational Buffer Memory In Chain
# memory=ConversationBufferMemory()
# conversation= ConversationChain(llm=HuggingFaceHub, memory=memory, verbose=True) # Here Verbose used to show all in terminal its not used in production
# conversation.predict(input="Hi AI")
# conversation.predict(input="Who is Current Prime Minister of India?")

# print(memory.Buffer)

# # Conversational Buffer Window Memory  
# memory = ConversationBufferWindowMemory(k=1) #k=1 here used to how many last or latest interaction you want to print 
# memory.save_context({"input":"Hi! there"}, {"output": "Hello Whats up"})
# memory.save_context({"input":"1234"}, {"output": "12345"})


# print(memory.Buffer)


# Using Conversational Buffer Window Memory in Chain
# memory = ConversationBufferWindowMemory(k=1) #k=1 here used to how many last or latest interaction you want to print 
# conversation= ConversationChain(llm=HuggingFaceHub, memory=memory, verbose=True)
# conversation.predict(input="Hi AI")
# conversation.predict(input="Who is Current Prime Minister of India?")
# print(memory.Buffer)

# ConversationEntityMemory
# memory= ConversationEntityMemory(llm=HuggingFaceHub)
# conversation= ConversationChain(llm=HuggingFaceHub, memory=memory, prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE, verbose=True)
# conversation.predict(input="Virat Kohli is living currently in London")
# conversation.predict(input="Conversational Buffer Window Memory keeps a list of interactions of the conversation over time")
# conversation.predict(input="Entity Memory Remembers given facts about specific entities in a conversation. It extracts information on entities (Using LLms) and build up its knowledge about that Entity over time(also Using an LLM)")

# print(memory.Buffer)
# print(conversation.memory.entity_store.store)

# ConversationSummaryBufferMemory

# memory= ConversationSummaryBufferMemory(llm=HuggingFaceHub, max_token_limit=50)
# conversation_with_summary=ConversationChain(llm=HuggingFaceHub, memory=memory, verbose=True)
# conversation_with_summary.predict(input="Why People are Scared of AI")
# conversation_with_summary.predict(input="What will be impact of AI on animals?")

# print(memory.load_memory_variables({}))


#Backed By Vector Store
# Vector Store Retriever Memory



