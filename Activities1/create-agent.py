# This script demonstrates how to use the OpenAI API to create a simple chat-based agent.
# It loads the API key from an environment variable, initializes the OpenAI client, and sends a chat message to the model.
# The response from the model is then printed to the console.

# Import the os module to interact with the operating system
import os

# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv

# Import the OpenAI library to interact with the OpenAI API
from  openai import OpenAI

# Load environment variables from a .env file in the current directory
# This allows us to keep sensitive information like API keys out of the codebase
load_dotenv()

# Load environment variables from environment variables
# This is useful for deployment environments where .env files are not used
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded correctly
if openai_api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
# This client will be used to interact with the OpenAI API
llm_name = "gpt-3.5-turbo"  # or "gpt-4"

# Create an instance of the OpenAI client with the API key
# This client will be used to interact with the OpenAI API
client=OpenAI(api_key=openai_api_key)

# Send a chat message to the model and get the response
# The model will respond to the message based on its training and capabilities
response = client.chat.completions.create(
    model=llm_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who is Sam Altman ?"}
        ],
)

# Create our own simple agent class
class SimpleAgent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        # Send the messages to the model and get the response
        # The model will respond to the messages based on its training and capabilities
        response = client.chat.completions.create(
            model=llm_name,
            temperature=0.0,
            messages=self.messages,
        )
        return response.choices[0].message.content