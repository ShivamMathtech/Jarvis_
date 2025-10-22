import requests

GEMINI_API_KEY = ""

def query_gemini(prompt):
    url = "https://api.generativeai.google/v1beta2/models/text-bison-001:generate"
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    payload = {
        "prompt": prompt,
        "temperature": 0.3,
        "maxOutputTokens": 200
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    return data.get("candidates", [{}])[0].get("content", "No response from Gemini")
