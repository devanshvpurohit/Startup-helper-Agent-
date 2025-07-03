import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def gemini_call(prompt, model="models/gemini-pro"):
    url = f"https://generativelanguage.googleapis.com/v1beta1/{model}:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 1,
            "maxOutputTokens": 2048
        }
    }
    res = requests.post(url, json=payload)
    return res.json()["candidates"][0]["content"]["parts"][0]["text"]
