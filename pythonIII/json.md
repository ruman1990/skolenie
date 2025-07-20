# JSON (JavaScript Object Notation)

## Teória

**JSON** (JavaScript Object Notation) je **ľahký textový formát** na ukladanie a výmenu dát. Pôvodne vznikol pre JavaScript, ale dnes je štandardom vo všetkých moderných programovacích jazykoch vrátane Pythonu.

### Základné vlastnosti JSON:

* Je **ľahko čitateľný pre človeka** aj stroj.
* Používa sa na **výměnu dát medzi serverom a klientom** (webové aplikácie, API).
* Dáta sú uložené ako páry **kľúč: hodnota** (podobne ako slovník v Pythone).
* Podporuje tieto typy údajov:

  * **Čísla** (celé, desatinné)
  * **Reťazce** (stringy)
  * **Boolean** (true/false)
  * **Pole (list/array)**
  * **Objekt (dict/slovník)**
  * **null** (ekvivalent None v Pythone)

### Príklad JSON súboru:

```json
{
    "meno": "Anna",
    "vek": 25,
    "email": "anna@email.com",
    "aktivny": true,
    "zaujmy": ["šport", "knihy", "hudba"]
}
```

---

## Práca s JSON v Pythone

Python má vstavaný **modul `json`**, ktorý umožňuje:

* **Konvertovať Python objekty na JSON** (serializácia – ukladanie do JSON)
* **Konvertovať JSON na Python objekty** (deserializácia – načítanie z JSON)

### 1. Základné funkcie modulu `json`

| Funkcia        | Popis                                          |
| -------------- | ---------------------------------------------- |
| `json.dumps()` | Prevedie Python objekt na JSON reťazec         |
| `json.loads()` | Prevedie JSON reťazec na Python objekt         |
| `json.dump()`  | Zapíše Python objekt do súboru vo formáte JSON |
| `json.load()`  | Načíta Python objekt zo súboru vo formáte JSON |

---

### 2. Príklady použitia

#### a) Konverzia Python objektu na JSON reťazec (`dumps`)

```python
import json

data = {
    "meno": "Anna",
    "vek": 25,
    "email": "anna@email.com",
    "aktivny": True,
    "zaujmy": ["šport", "knihy", "hudba"]
}

json_str = json.dumps(data)
print(json_str)
```

**Výstup:**

```json
{"meno": "Anna", "vek": 25, "email": "anna@email.com", "aktivny": true, "zaujmy": ["šport", "knihy", "hudba"]}
```

---

#### b) Načítanie JSON reťazca do Python objektu (`loads`)

```python
import json

json_str = '{"meno": "Anna", "vek": 25, "email": "anna@email.com", "aktivny": true, "zaujmy": ["šport", "knihy", "hudba"]}'
data = json.loads(json_str)
print(data)
print(data["meno"])
```

---

#### c) Ukladanie Python objektu do JSON súboru (`dump`)

```python
import json

data = {
    "meno": "Peter",
    "vek": 30,
    "email": "peter@email.com",
    "aktivny": False
}

with open('peter.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```

* Parameter `indent=4` spôsobí, že JSON bude pekne formátovaný (odsadzuje sa 4 medzerami).
* `ensure_ascii=False` umožní zapisovať aj znaky mimo ASCII (napr. diakritiku).

---

#### d) Načítanie údajov z JSON súboru (`load`)

```python
import json

with open('peter.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
```

---

### 3. Prevod medzi Python a JSON typmi

| Python      | JSON         |
| ----------- | ------------ |
| dict        | objekt       |
| list, tuple | pole (array) |
| str         | string       |
| int, float  | číslo        |
| True        | true         |
| False       | false        |
| None        | null         |

---

### 4. Praktický príklad – načítanie a úprava zoznamu zo súboru

Povedzme, že máme súbor `zoznam.json`:

```json
["Anna", "Peter", "Juraj"]
```

Načítame a pridáme meno:

```python
import json

with open('zoznam.json', 'r', encoding='utf-8') as f:
    osoby = json.load(f)

osoby.append("Martina")

with open('zoznam.json', 'w', encoding='utf-8') as f:
    json.dump(osoby, f, ensure_ascii=False, indent=4)
```

---

### 5. Formátovanie a čítateľnosť

Pri používaní `json.dumps()` a `json.dump()` je dobré nastaviť parametre:

* `indent=4` – pre lepšiu čitateľnosť
* `sort_keys=True` – zoradí kľúče v JSON abecedne

---

## Zhrnutie

* **JSON** je univerzálny a ľahko čitateľný formát na výmenu dát.
* V Pythone je práca s JSON veľmi jednoduchá vďaka modulu `json`.
* Najčastejšie funkcie: `dump/load` (práca so súborom), `dumps/loads` (práca s reťazcom).
* Dôležitá je znalosť mapovania typov medzi Python a JSON.
* Pri ukladání JSON nezabúdajte na parametre pre kódovanie a formátovanie.

