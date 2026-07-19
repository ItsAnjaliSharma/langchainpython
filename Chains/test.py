from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from operator import itemgetter



# Create the local Hugging Face pipeline
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=150
)

# # Wrap it for LangChain (makes it Runnable)
llm = HuggingFacePipeline(pipeline=generator)

# # Define the prompt
# prompt = PromptTemplate(
#     input_variables=["topic"],
#     template="Explain the concept of {topic} in simple terms."
# )

# # 🔥 New LCEL syntax: combine prompt and model directly
# chain = prompt | llm

# # Run it
# response = chain.invoke({"topic": "LlM chains"})
# print(response)


# Example 2 Multiple Chains 
#In this example we use first question resonse as an input for next question

chat_prompt1= ChatPromptTemplate.from_template(
    "What is the city {person} is from?"
)

chat_prompt2= ChatPromptTemplate.from_template(
    "What country is the city {city} in? respond in {language}"
)

city_chain= chat_prompt1 | llm | StrOutputParser()

country_chain=({"city": city_chain, "language":itemgetter("language")}
| chat_prompt2 | llm | StrOutputParser()
)

resonse = country_chain.invoke({"person": "Virat Kohli", "language": "English"})
print(resonse)

