import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def query_api(prompt):
    """Query Gemini API"""
    try:
        model = genai.GenerativeModel("gemini-3-flash-preview")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying Gemini...\n")
    print(query_api(user_prompt))