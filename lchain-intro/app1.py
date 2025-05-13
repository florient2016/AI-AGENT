import os

import openai
from dotenv import load_dotenv, find_dotenv
# Load environment variables from a .env file
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

print("OpenAI API Key:", openai.api_key)
# Check if the API key is loaded correctly

llm_mode = "gpt-3.5-turbo"  # or "gpt-4"

llm = OpenAI(temperature=0.7, model_name=llm_mode)

print(llm.predict("Who is steeve job ?"))
# The above code is a simple script that demonstrates how to use the OpenAI API to create a chat-based agent.
# It uses the OpenAI library to interact with the OpenAI API and the langchain library to create a chat-based agent.

