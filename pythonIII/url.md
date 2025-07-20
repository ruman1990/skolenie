# **Čo je URL?**

**URL** (Uniform Resource Locator) je **adresa**, ktorou v internete alebo v sieti jednoznačne označujeme umiestnenie nejakého zdroja – napríklad webovej stránky, obrázku, videa, súboru, či API.

Inými slovami, **URL je „adresa na internete“**.

---

## **Štruktúra URL**

Bežná URL vyzerá napríklad takto:

```
https://www.example.com:443/adresar/podadresar/subor.html?param1=hodnota1&param2=hodnota2#sekcia
```

### **Časti URL:**

1. **Schéma (protokol)**

   * Určuje, aký spôsob prístupu sa použije
   * Príklady: `http`, `https`, `ftp`, `file`
   * **Príklad:** `https://`
2. **Doména (názov servera, hostiteľ)**

   * Meno počítača/servera na internete
   * **Príklad:** `www.example.com`
3. **Port**

   * (Voliteľné) číslo portu na serveri, kde služba beží
   * Bežne sa neuvádza (štandardne 80 pre http, 443 pre https)
   * **Príklad:** `:443`
4. **Cesta (path)**

   * Presná cesta k súboru alebo zdroju na serveri
   * **Príklad:** `/adresar/podadresar/subor.html`
5. **Parametre (query)**

   * (Voliteľné) Doplňujúce informácie v tvare kľúč=hodnota, za znakom `?`
   * Viacero parametrov sa oddeľuje znakom `&`
   * **Príklad:** `?param1=hodnota1&param2=hodnota2`
6. **Fragment (hash, kotva)**

   * (Voliteľné) Odkazuje na konkrétnu časť dokumentu, za znakom `#`
   * **Príklad:** `#sekcia`

---

## **Príklady URL**

* **Webová stránka:**
  `https://sk.wikipedia.org/wiki/Python_(programovací_jazyk)`

* **Súbor na stiahnutie:**
  `https://www.priklad.sk/downloads/soubor.zip`

* **Obrázok:**
  `https://upload.wikimedia.org/wikipedia/commons/0/0a/Python.svg`

* **API volanie:**
  `https://api.example.com/data?typ=student&id=123`

---

## **Čo znamená kódovanie v URL?**

Niektoré znaky v URL nie je možné používať priamo (medzery, špeciálne znaky), preto sa nahrádzajú tzv. **percent encodingom** – napríklad medzera ako `%20`.

* `Môj súbor.html` sa v URL píše ako:
  `M%C3%B4j%20s%C3%BAbor.html`

---

## **Práca s URL v Pythone**

V Pythone môžeš URL analyzovať, skladať a rozkladať pomocou modulu `urllib.parse`:

```python
from urllib.parse import urlparse

url = "https://www.example.com:443/adresar/subor.html?x=1&y=2#nadpis"
parsed = urlparse(url)
print(parsed.scheme)    # 'https'
print(parsed.hostname)  # 'www.example.com'
print(parsed.path)      # '/adresar/subor.html'
print(parsed.query)     # 'x=1&y=2'
print(parsed.fragment)  # 'nadpis'
```

---

## **Čo je URI a čo je URN?**

* **URI** (Uniform Resource Identifier): všeobecný identifikátor zdroja (URL je typ URI).
* **URN** (Uniform Resource Name): jedinečný názov bez určenia umiestnenia (napr. ISBN:978-3-16-148410-0).

---

## **Zhrnutie**

* **URL je internetová adresa** – jedinečne identifikuje zdroj na internete alebo v sieti.
* Každá URL môže obsahovať viacero častí (protokol, doména, cesta, parametre...).
* V Pythone pracuj s URL pomocou modulu `urllib.parse`.
