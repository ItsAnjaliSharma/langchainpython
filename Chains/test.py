from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from operator import itemgetter

# Choose a model from Hugging Face Hub (e.g., FLAN-T5)
#LCEL (Langchain Expression Language)
#Example 1
llm = HuggingFaceHub(repo_id="google/flan-t5-xl", model_kwargs={"temperature":0.7, "max_length":100})

# Prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the concept of {topic} in simple terms."
)

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

# Run it
response = chain.run("quantum computing")
# response = chain.invoke("quantum computing") sometimes it runs this


print(response)


# Example 2 Multiple Chains 
#In this example we use first question resonse as an input for next question

chat_prompt1= ChatPromptTemplate.from_template(
    "What is the city {person} is from?"
)

chat_prompt2= ChatPromptTemplate.from_template(
    "What country is the city {city} in? respond in {language}"
)

city_chain= chat_prompt1 | chat | StrOutputParser()

country_chain=({"city": city_chain, "language":itemgetter("language")}
| chat_prompt2 | chat | StrOutputParser()
)

resonse = country_chain.invoke({"person": "Virat Kohli", "language": "English"})
print(resonse)

