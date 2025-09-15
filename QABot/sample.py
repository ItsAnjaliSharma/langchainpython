from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize components
llm = ChatGoogleGenerativeAI(model="gemini-pro")
parser = StrOutputParser()

# Create prompt
prompt = ChatPromptTemplate.from_template(
    "Answer the following question in a helpful way: {question}"
)

# Build chain
chain = prompt | llm | parser

# Use the bot
while True:
    user_question = input("Ask a question (or 'quit' to exit): ")
    if user_question.lower() == 'quit':
        break
    
    answer = chain.invoke({"question": user_question})
    print(f"Bot: {answer}\n")