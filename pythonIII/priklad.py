import json

data = {
    "meno": "Peter Š.",
    "vek": 30,
    "email": "peter@email.com",
    "aktivny": False
}

with open('peter.json', 'w', encoding='utf-8') as f:
    json.dump(data, f,indent=4,ensure_ascii=False)