import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# API CONFIGURATION
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACE_API_KEY")   # from .env
)

def query_api(prompt):
    """Query Hugging Face LLM using OpenAI-compatible API"""
    try:
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


# MAIN EXECUTION
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    print("Querying Hugging Face...\n")

    result = query_api(user_prompt)

    print("Response:\n")
    print(result)