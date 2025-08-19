# Modul `requests` v Pythone

## Teória

**`requests`** je najpoužívanejšia externá knižnica v Pythone na posielanie **HTTP požiadaviek** (GET, POST, PUT, DELETE...) na webové servery.
Vďaka `requests` môžeme z Pythona jednoducho:

* sťahovať webové stránky,
* komunikovať s API (napríklad OpenWeather, Google Maps, REST služby...),
* posielať formuláre, uploadovať a sťahovať súbory,
* automatizovať prácu s webom bez prehliadača.

Knižnica je **jednoduchšia a prehľadnejšia** než vstavaný modul `urllib`.

---

## Inštalácia

`requests` nie je v základnej výbave Pythonu, treba ju doinštalovať príkazom:

```bash
pip install requests
```

---

## Základné použitie

### 1. Stiahnutie webovej stránky (GET požiadavka)

```python
import requests

response = requests.get('https://www.example.com')
print(response.status_code)   # Kód odpovede (200 = OK)
print(response.text)          # Obsah stránky (ako text)
```

### 2. Práca s JSON odpoveďou (napr. z API)

Ak webová služba vracia JSON, môžeme priamo dostať výsledok ako Python dict:

```python
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)
data = response.json()
print(data)
# Výstup: {'userId': 1, 'id': 1, 'title': '...', 'completed': False}
```

---

## Posielanie údajov na server

### 3. Posielanie formulára (POST požiadavka)

```python
import requests

url = "https://httpbin.org/post"
udaje = {'meno': 'Anna', 'vek': 23}

response = requests.post(url, data=udaje)
print(response.text)
```

---

## Dôležité vlastnosti objektu `response`

| Vlastnosť              | Popis                                                   |
| ---------------------- | ------------------------------------------------------- |
| `response.status_code` | HTTP status kód (200, 404, 500...)                      |
| `response.text`        | Obsah odpovede ako text                                 |
| `response.content`     | Obsah ako binárne dáta (napr. pri sťahovaní obrázkov)   |
| `response.json()`      | Parsuje JSON odpoveď na Python dict                     |
| `response.headers`     | Hlavičky odpovede (informácie o serveri, type dát atď.) |
| `response.url`         | Finálna URL (po presmerovaní)                           |

---

## Pridanie vlastných hlavičiek (napr. user-agent)

```python
import requests

hlavicky = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://www.example.com', headers=hlavicky)
print(response.status_code)
```

---

## Sťahovanie súborov

```python
import requests

url = 'https://www.example.com/image.jpg'
response = requests.get(url)

with open('obrazok.jpg', 'wb') as f:
    f.write(response.content)
```

---

## Práca s parametrami v URL

```python
import requests

params = {'q': 'python', 'lang': 'sk'}
response = requests.get('https://www.google.com/search', params=params)
print(response.url)
```

Táto funkcia automaticky pridá parametre do URL (napr. [https://www.google.com/search?q=python\&lang=sk](https://www.google.com/search?q=python&lang=sk)).

---

## Ošetrenie chýb

Pri práci s webom môžu nastať chyby (nedostupná stránka, zlý server...). Preto odporúčame použiť výnimky:

```python
import requests

try:
    response = requests.get('https://www.example.com', timeout=5)
    response.raise_for_status()  # vyhodí výnimku ak status != 200
    print(response.text)
except requests.RequestException as e:
    print('Chyba pri požiadavke:', e)
```

---

## Zhrnutie

* **`requests`** je najpohodlnejší modul na HTTP požiadavky v Pythone.
* Umožňuje GET, POST, PUT, DELETE a ďalšie HTTP operácie.
* Jednoduché čítanie a posielanie JSON, prácu s formulármi, upload/sťahovanie súborov.
* Kód je prehľadný a zrozumiteľný – vhodný aj pre začiatočníkov.




## 1️⃣ GET – získanie dát

Používa sa na **čítanie** (napr. zoznam užívateľov, články, …).

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print(response.status_code)   # 200 = OK
print(response.headers)       # HTTP hlavičky
print(response.text[:100])    # prvých 100 znakov surového textu
print(response.json()[:2])    # dekódovaný JSON (prvé 2 položky)
```

➡️ Parametre do query stringu (`?id=1&sort=asc`):

```python
response = requests.get(url, params={"userId": 1})
print(response.json())
```

---

## 2️⃣ POST – vytvorenie dát

Používa sa na **odoslanie nových dát** na server (napr. registrácia, nový článok).

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": "Môj príspevok", "body": "Obsah...", "userId": 1}

response = requests.post(url, json=payload)

print(response.status_code)   # 201 = Created
print(response.json())        # odpoveď s uloženým objektom
```

* `json=...` → pošle JSON (`Content-Type: application/json`)
* `data=...` → pošle formulárové dáta (`application/x-www-form-urlencoded`)

---

## 3️⃣ PUT – úplná aktualizácia

Používa sa na **úplnú zmenu existujúceho záznamu**.

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"id": 1, "title": "Nový titulok", "body": "Nový obsah", "userId": 1}

response = requests.put(url, json=payload)

print(response.status_code)   # 200 = OK
print(response.json())
```

---

## 4️⃣ PATCH – čiastočná aktualizácia

Keď meníš len časť údajov:

```python
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"title": "Zmenený titulok"}

response = requests.patch(url, json=payload)

print(response.json())
```

---

## 5️⃣ DELETE – zmazanie dát

Používa sa na **odstránenie** záznamu.

```python
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

print(response.status_code)   # 200 alebo 204 (No Content)
```

---

## 🔹 Hlavičky (headers)

Napr. keď API vyžaduje autentifikáciu alebo špeciálny formát:

```python
headers = {"Authorization": "Bearer MOJ_TOKEN"}
response = requests.get("https://api.example.com/data", headers=headers)
```

---

## 🔹 Timeout a error handling

Nikdy nenechaj request visieť donekonečna:

```python
try:
    response = requests.get("https://api.example.com", timeout=5)
    response.raise_for_status()   # vyhodí chybu pri 4xx / 5xx
except requests.exceptions.RequestException as e:
    print("Chyba:", e)
```

---

## 🔹 Rýchle porovnanie metód

| Metóda   | Účel                        | Typický status              |
| -------- | --------------------------- | --------------------------- |
| `GET`    | Získať dáta                 | `200 OK`                    |
| `POST`   | Vytvoriť nové dáta          | `201 Created`               |
| `PUT`    | Úplne nahradiť existujúce   | `200 OK`                    |
| `PATCH`  | Čiastočne zmeniť existujúce | `200 OK`                    |
| `DELETE` | Odstrániť dáta              | `200 OK` / `204 No Content` |

---
