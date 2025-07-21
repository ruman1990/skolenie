import requests
import time
import uuid
import random
# 💡 Konfigurácia
BASE_URL = "https://ui.smartiepal.com"
ASSISTANT_ID = "6f7d2523063237ab23521b8a5d024e30bd829e0abcedb9df4d5e392bd8b3250a"
QUESTION = "Ahoj, kto si?"

# random 8 letters string
def random_string(length=8):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

# 1. Vygeneruj sessionId
session_id = str(random_string(8))

# 2. Vytvor payload pre POST /ask
ask_payload = {
    "session": session_id,
    "id": 0,
    "ask": QUESTION
}

headers = {
    "Content-Type": "application/json",
    "X-assistant-id": ASSISTANT_ID
}

# 3. Odoslanie otázky
post_response = requests.post(f"{BASE_URL}/ask", json=ask_payload, headers=headers)
if post_response.status_code == 200:
    print("Otázka bola odoslaná.")
else:
    print(f"Chyba pri odoslaní otázky: {post_response.status_code}")

# 4. Čakanie na odpoveď cez GET /ask/<sessionId>
for _ in range(10):
    time.sleep(2)  # počkaj 2 sekundy
    get_response = requests.get(f"{BASE_URL}/ask/{session_id}", headers={
        'Content-Type': 'application/json',
        "X-assistant-id": ASSISTANT_ID
    })

    if get_response.status_code == 200:
        data = get_response.json()
        if data.get("unread"):
            chat = data.get("chat", [])
            if chat:
                last = chat[-1]
                if last.get("answer"):
                    print("Odpoveď:", last["text"])
                    break
    else:
        print(f"Chyba pri získavaní odpovede: {get_response.status_code}")
        break
else:
    print("Vypršal čas čakania na odpoveď.")
