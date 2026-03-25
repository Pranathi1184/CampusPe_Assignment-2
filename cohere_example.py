import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_api(prompt):
    """Query Cohere Chat API (latest model)"""
    try:
        response = co.chat(
            model="command-a-03-2025", 
            message=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    print("Querying Cohere...\n")

    result = query_api(user_prompt)

    print("Response:\n")
    print(result)