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
