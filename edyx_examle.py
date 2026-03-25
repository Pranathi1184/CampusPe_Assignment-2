import os
import requests
from dotenv import load_dotenv

load_dotenv()

# API CONFIGURATION
API_KEY = os.getenv("EDYX_API_KEY")
URL = "https://edyx-backend.onrender.com/chat"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def query_api(prompt):
    """Query Edyx Situation-Aware API"""
    try:
        data = {
            "model": "situation-aware",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.7
        }

        response = requests.post(URL, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# MAIN EXECUTION
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")

    print("Querying Edyx API...\n")

    result = query_api(user_prompt)

    print("Response:\n")
    print(result)