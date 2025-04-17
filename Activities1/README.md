# AI-Agent: Simple Chat-Based Agent with OpenAI API

This repository demonstrates how to create a simple chat-based agent using the OpenAI API. The agent interacts with the OpenAI GPT model to provide responses to user queries. It uses environment variables to securely manage API keys and includes a basic validation script to ensure the API key is properly loaded.

## Table of Contents

- [Overview](#overview)
- [Files](#files)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Overview

The AI-Agent project includes:
1. A script to validate the presence of the OpenAI API key in the environment.
2. A simple agent script that interacts with the OpenAI GPT model to answer user queries.
3. A `requirements.txt` file to manage dependencies.

## Files

### 1. `requirements.txt`
Contains the Python dependencies required for the project:
- `openai`: Library to interact with the OpenAI API.
- `langchain`: For advanced language model interactions (optional for future extensions).
- `python-dotenv`: To load environment variables from a `.env` file.

### 2. `validate.py`
A script to validate whether the `OPENAI_API_KEY` environment variable is set. It prints `True` if the key is found, otherwise `False`.

### 3. `simple-agent.py`
The main script that:
- Loads the OpenAI API key from environment variables.
- Initializes the OpenAI client.
- Sends a chat message to the GPT model and prints the response.

## Prerequisites

Before running the project, ensure you have the following:
1. Python 3.8 or higher installed on your system.
2. An OpenAI API key. You can obtain one from [OpenAI](https://platform.openai.com/signup/).
3. A `.env` file in the project directory containing the following line:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```
Setup
   1. Clone the repository:
```bash
git clone https://github.com/your-username/AI-Agent.git
cd AI-Agent/Activities1
```
2.  Install dependencies: Use pip to install the required Python libraries:
```bash
pip install -r requirements.txt
```
3.  Set up the .env file: Create a .env file in the project directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```
## Usage
1.  Run the simple agent: Execute the simple-agent.py script to interact with the OpenAI GPT model:
```bash
python simple-agent.py
```
## License
This project is licensed under the MIT License. See the LICENSE file for more details.