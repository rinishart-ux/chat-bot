import json
import random

with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

intents = data["intents"]


def handle_intents(text: str):
    text = text.lower()

    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in text:
                return random.choice(intent["responses"])

    return None