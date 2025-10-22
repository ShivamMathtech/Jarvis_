import json

def load_intents(path="modules/intents.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict) and "intents" in data:
            data = data["intents"]  # extract the list
        if not isinstance(data, list):
            print("⚠️ Invalid intents format, should be a list of dictionaries")
            return []
        return data
    except Exception as e:
        print(f"⚠️ Failed to load intents: {e}")
        return []

def match_intent(intents, text):
    for intent in intents:
        if not isinstance(intent, dict):
            continue
        for pattern in intent.get("patterns", []):
            if pattern.lower() in text.lower():
                return intent
    return None
