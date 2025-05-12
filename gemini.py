import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini(prompt: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    # Debug toàn bộ phản hồi
    print("👉 Gemini response:")
    print(result)

    try:
        return result['candidates'][0]['content']['parts'][0]['text']
    except KeyError:
        return "⚠️ Gemini API response error."

