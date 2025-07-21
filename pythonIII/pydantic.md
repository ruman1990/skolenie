## 📁 `data.json` – vstupný súbor (príklad údajov o používateľoch):

```json
{
  "name": "Jana",
  "age": "28",
  "email": "jana@example.com"
}
```

---

## 🟦 1. Cerberus – Validácia bez typovania

```python
import json
from cerberus import Validator

# Načítanie JSON zo súboru
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Definícia schémy
schema = {
    "name": {"type": "string", "minlength": 2, "required": True},
    "age": {"type": "integer", "min": 0, "max": 120, "required": True},
    "email": {"type": "string", "regex": r".+@.+\..+", "required": True}
}

# Validácia
v = Validator(schema)
if v.validate(data):
    print("✅ Dáta sú platné:", v.document)
else:
    print("❌ Chyby:", v.errors)
```

📝 **Poznámka**: Cerberus nedokáže automaticky prekonvertovať `"age": "28"` na číslo – vráti chybu, ak nie je správny typ.

---

## 🟩 2. Pydantic – Validácia s typovaním a konverziou

```python
import json
from pydantic import BaseModel, EmailStr, ValidationError

# Načítanie JSON
with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

# Definícia modelu
class User(BaseModel):
    name: str
    age: int
    email: EmailStr

# Validácia a konverzia
try:
    user = User(**data)
    print("✅ Dáta sú platné:", user.dict())
except ValidationError as e:
    print("❌ Chyby:")
    print(e.json())
```

📝 **Výhoda Pydantic**: Ak `age` je reťazec `"28"`, automaticky ho skonvertuje na `int`.

---

## 🧠 Kedy čo použiť?

* Používaš **čisto `dict` alebo JSON** → Cerberus stačí
* Chceš **typovanú validáciu**, konverziu a objektovo orientovaný prístup → Pydantic je lepší
