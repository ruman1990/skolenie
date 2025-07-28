import requests
import time
import uuid
import random
# 💡 Konfigurácia
BASE_URL = "https://ui.smartiepal.com"
ASSISTANT_ID = "1725e0806d48412df3d6ba67d45384362be2febbbcba2ac182edaf5b72a66595"
QUESTION = "koLKO JE 2+2"

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
