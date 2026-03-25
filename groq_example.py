import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# API CONFIGURATION
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def query_api(prompt):
    """Query Groq API (latest responses API)"""
    try:
        response = client.responses.create(
            model="openai/gpt-oss-20b",   
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Error: {str(e)}"


# MAIN EXECUTION
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    print("Querying Groq...\n")

    result = query_api(user_prompt)

    print("Response:\n")
    print(result)