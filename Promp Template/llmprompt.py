from langchain_google_genai import ChatGoogleGenerativeAI
from decouple import config
from langchain.prompts import PromptTemplate

# Load Gemini key
GEMINI_KEY = config("secret_gemini_key")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # or "gemini-2.5-flash"
    google_api_key=GEMINI_KEY
)


# # Example 1 - Prompt having no input variable
# noInputPrompt = PromptTemplate.from_template("Tell me a Python Trick")

# # Format the prompt (this gives you a plain string)
# formattedNoInputPrompt = noInputPrompt.format()

# # Pass the string to the LLM
# response = llm.invoke(formattedNoInputPrompt)

# print("Response:", response.content)


# Example 2 - Prompt having One input variable

# oneInputPrompt = PromptTemplate(
#     input_variable=["language"], 
#     template="Tell me a {language} Trick"
#     )

# language = input("Enter a programming language: ")
# # Format the prompt (this gives you a plain string)
# formattedOneInputPrompt = oneInputPrompt.format(language=language)

# # Pass the string to the LLM
# response = llm.invoke(formattedOneInputPrompt)

# print("Response:", response.content)


# Example 3 - Prompt having Multiple input variable

mutipleInputPrompt = PromptTemplate(
    input_variable=["language", "topic"], 
    template="Tell me a {language} {topic} Trick"
    )

# print("User Inputs Variable are:", mutipleInputPrompt.input_variables)
language = input("Enter a programming language: ")
topic=input("Enter the topic you want to know about: ")



# Format the prompt (this gives you a plain string)
formattedMutipleInputPrompt = mutipleInputPrompt.format(language=language, topic=topic)
print("Multiple Input Prompt: ", formattedMutipleInputPrompt)
# Pass the string to the LLM
# response = llm.invoke(formattedOneInputPrompt)

# print("Response:", response.content)