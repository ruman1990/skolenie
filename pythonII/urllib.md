# 📘 **Modul `urllib` v Pythone**

Modul **`urllib`** je súčasť štandardnej knižnice Pythonu, čo znamená, že ho možno používať bez inštalácie ďalších balíkov. Poskytuje nástroje na prácu s URL adresami, posielanie HTTP požiadaviek, dekódovanie parametrov či čítanie robots.txt.

Pozostáva zo 4 hlavných podmodulov:

1. `urllib.request` – odosielanie HTTP požiadaviek (GET, POST, hlavičky...)
2. `urllib.parse` – parsovanie a skladanie URL adries
3. `urllib.error` – zachytávanie HTTP a URL chýb
4. `urllib.robotparser` – čítanie a spracovanie robots.txt

---

# 🧩 **1. urllib.request – odosielanie HTTP požiadaviek**

Toto je najdôležitejšia časť `urllib`. Umožňuje:

* odoslať HTTP GET a POST požiadavku,
* získavať odpoveď zo servera,
* čítať stavové kódy a hlavičky,
* sťahovať súbory,
* pracovať s vlastnými hlavičkami.

## 1.1 Základný GET request

Najjednoduchší spôsob, ako načítať stránku:

```python
from urllib import request

response = request.urlopen("https://www.example.com")

html = response.read().decode("utf-8")
print(html)
```

Objekt `response` obsahuje stavový kód, hlavičky aj telo odpovede.

### Dôležité metódy:

* `response.status` – HTTP status (200 = OK)
* `response.getheaders()` – zoznam hlavičiek
* `response.read()` – načítanie dát

---

## 1.2 Posielanie POST žiadosti

POST request sa používa, keď chceme odosielať dáta.

```python
from urllib import request, parse

url = "https://httpbin.org/post"
data = {"name": "Peter", "age": 21}

encoded = parse.urlencode(data).encode("utf-8")
req = request.Request(url, data=encoded, method="POST")

resp = request.urlopen(req)
print(resp.read().decode())
```

---

## 1.3 Pridávanie vlastných hlavičiek

Hlavičky môžu byť kľúčové napr. pri pristupovaní k API.

```python
req = request.Request(
    "https://www.example.com",
    headers={"User-Agent": "Mozilla/5.0"}
)

response = request.urlopen(req)
```

---

## 1.4 Sťahovanie súborov

Stačí jedna funkcia:

```python
from urllib import request

request.urlretrieve("https://example.com/img.png", "obrazok.png")
```

---

## 📝 **Úlohy – Kapitola 1 (urllib.request)**

1. Načítaj obsah ľubovoľnej webovej stránky a vypíš prvých 200 znakov.
2. Napíš skript, ktorý odošle POST požiadavku na `https://httpbin.org/post` a odošle meno a email.
3. Stiahni akýkoľvek obrázok z internetu a ulož ho do súboru `foto.png`.
4. Odosli GET požiadavku s vlastnou hlavičkou `User-Agent: TestBot/1.0`.

---

# 🧩 **2. urllib.parse – parsovanie URL**

Modul `urllib.parse` slúži na:

* rozklad URL na jednotlivé časti (scheme, hostname, path…),
* dekódovanie a kódovanie parametrov,
* skladanie URL adries,
* parsovanie query stringov (`?name=Jano&age=20`).

---

## 2.1 Rozklad URL na časti

```python
from urllib import parse

url = "https://example.com/products/item?id=15&color=red"
parsed = parse.urlparse(url)

print(parsed.scheme)   # https
print(parsed.netloc)   # example.com
print(parsed.path)     # /products/item
print(parsed.query)    # id=15&color=red
```

---

## 2.2 Parsovanie query parametrov

```python
from urllib import parse

params = parse.parse_qs("name=Peter&age=30&age=31")
print(params)
```

Výstup:

```
{'name': ['Peter'], 'age': ['30', '31']}
```

---

## 2.3 Skladanie URL

```python
from urllib import parse

parts = ("https", "example.com", "/login", "", "user=admin", "")
url = parse.urlunparse(parts)

print(url)
```

---

## 2.4 Encode/Decode (kódovanie Unicode textu)

```python
from urllib import parse

encoded = parse.quote("Ján Želinský")
print(encoded)   # J%C3%A1n%20%C5%BDelinsk%C3%BD
print(parse.unquote(encoded))
```

---

## 📝 **Úlohy – Kapitola 2 (urllib.parse)**

1. Rozparsuj URL `https://example.com/test/page?x=10&y=20` a vypíš iba query parametre.
2. Z textu `"Milan Šťastný"` vytvor URL-enkódovanú verziu.
3. Znovu zlož URL z častí:

   * scheme: `https`
   * host: `api.test.com`
   * path: `/v1/user`
   * query: `id=99`
4. Preveď text `"python urllib modul"` na formát vhodný do URL a potom späť.

---

# 🧩 **3. urllib.error – práca s chybami**

Pri HTTP komunikácii často nastanú chyby (404, 403, 500…).

`urllib.error` poskytuje dve výnimky:

* `HTTPError` – server odpovie chybovým HTTP kódom
* `URLError` – DNS chyba, nedostupná stránka, nesprávny formát URL…

## Príklad:

```python
from urllib import request, error

try:
    response = request.urlopen("https://example.com/neexistuje")
except error.HTTPError as e:
    print("HTTP chyba:", e.code, e.reason)
except error.URLError as e:
    print("URL chyba:", e.reason)
```

---

## 📝 **Úlohy – Kapitola 3 (urllib.error)**

1. Skús načítať stránku `https://example.com/404` a zachyť HTTPError.
2. Skús spracovať URL `"ht!tp://zle"` a zachyť URLError.
3. Uprav skript tak, aby pri chybe vypísal vlastnú správu:
   „Nepodarilo sa načítať stránku.“

---

# 🧩 **4. urllib.robotparser – robot.txt**

Modul `robotparser` umožňuje načítať a interpretovať pravidlá v `robots.txt`.

## 4.1 Základný príklad

```python
from urllib import robotparser

rp = robotparser.RobotFileParser()
rp.set_url("https://www.example.com/robots.txt")
rp.read()

print(rp.can_fetch("*", "https://www.example.com/secret"))
```

Funkcia `can_fetch()` povie, či je povolené načítať danú URL podľa pravidiel webu.

---

## 📝 **Úlohy – Kapitola 4 (urllib.robotparser)**

1. Načítaj robots.txt z `https://www.python.org/robots.txt`.
2. Skontroluj, či agent `"*"` môže pristúpiť na `/downloads/`.
3. Zisti, či je povolený prístup na `/private/`.

---

# 🧩 **5. Zhrnutie celého modulu `urllib`**

* `urllib.request` – načítavanie webu, requesty, sťahovanie.
* `urllib.parse` – práca s URL, kódovanie, dekódovanie.
* `urllib.error` – spracovanie chýb.
* `urllib.robotparser` – interpretácia robots.txt.

Modul je menej pohodlný ako moderné knižnice typu **`requests`**, ale je dôležitý pre prípady, keď sa musí použiť štandardná knižnica alebo tam, kde sa knižnice inštalovať nesmú (napr. skúšky, certifikáty, obmedzené prostredia).

---

# 🏁 **Záverečné komplexné cvičenie**

Vytvor program, ktorý:

1. Načíta robots.txt z ľubovoľnej stránky.
2. Skontroluje, či je povolené načítať stránku `/`.
3. Ak áno:

   * vykoná GET požiadavku,
   * uloží kompletný HTML obsah do súboru `stranka.html`,
   * vypíše štatistiku:

     * stavový kód,
     * počet znakov v HTML,
     * počet prijatých hlavičiek.
4. Ak nie:

   * vypíše správu „Stránku nie je dovolené načítať podľa robots.txt“.
