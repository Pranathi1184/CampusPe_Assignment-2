import requests

def query_api(prompt):
    """Query Ollama local API"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Ollama...\n")
    print(query_api(user_prompt))