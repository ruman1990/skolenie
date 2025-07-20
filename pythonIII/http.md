# **HTTP – Hypertext Transfer Protocol**

**HTTP** je základný protokol, ktorý sa používa na **komunikáciu medzi webovým prehliadačom (klientom) a webovým serverom**.
Keď zadáš do prehliadača adresu, pošleš požiadavku cez HTTP a server ti vráti odpoveď (napr. webovú stránku, obrázok, JSON...).

---

## **Ako funguje HTTP?**

* Je to **textový, bezstavový protokol** (každá požiadavka je samostatná, server si „nepamätá“ predchádzajúce požiadavky).
* Prebieha ako výmena **požiadavka (request)** a **odpoveď (response)**.

---

### **Typická komunikácia**

1. **Klient (prehliadač) pošle HTTP požiadavku na server**
2. **Server spracuje požiadavku a pošle HTTP odpoveď**

---

## **Čo obsahuje HTTP požiadavka (request)?**

Príklad jednoduchej požiadavky:

```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

* **Prvý riadok**: metóda (napr. GET), cesta k súboru, verzia protokolu
* **Hlavičky** (headers): doplňujúce informácie (napr. kto žiada, čo akceptuje...)
* (Voliteľne) **Telo** požiadavky – najmä pri metóde POST, PUT (napr. dáta formulára, JSON...)

---

## **Základné HTTP metódy**

| Metóda  | Popis                                       |
| ------- | ------------------------------------------- |
| GET     | Získať dáta/stránku (najčastejšie použitie) |
| POST    | Poslať dáta na server (formulár, API...)    |
| PUT     | Nahraď existujúci zdroj                     |
| DELETE  | Zmazať zdroj                                |
| HEAD    | Získať len hlavičky (nie obsah)             |
| PATCH   | Čiastočne zmeniť zdroj                      |
| OPTIONS | Zistiť, čo server podporuje                 |

---

## **HTTP odpoveď (response)**

Príklad odpovede servera:

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1024

<html>
  <body>...</body>
</html>
```

* **Prvý riadok:** verzia HTTP, **status kód** (napr. 200 = OK, 404 = Nenájdené), krátka správa
* **Hlavičky**: informácie o odpovedi (typ obsahu, dĺžka, cookies...)
* **Telo odpovede**: samotný obsah (HTML, obrázok, JSON...)

---

## **Najčastejšie HTTP status kódy**

| Kód | Význam                                   |
| --- | ---------------------------------------- |
| 200 | OK (všetko v poriadku)                   |
| 201 | Created (vytvorené)                      |
| 204 | No Content (bez obsahu)                  |
| 301 | Moved Permanently (presmerované)         |
| 302 | Found (dočasné presmerovanie)            |
| 400 | Bad Request (chybná požiadavka)          |
| 401 | Unauthorized (neautorizované)            |
| 403 | Forbidden (zakázané)                     |
| 404 | Not Found (nenájdené)                    |
| 500 | Internal Server Error (chyba na serveri) |

---

## **HTTP a HTTPS**

* **HTTP** = bežný protokol (dáta sú posielané nešifrovane)
* **HTTPS** = zabezpečený HTTP (dáta sú šifrované pomocou SSL/TLS)

---

## **HTTP v Pythone**

V Pythone môžeš posielať HTTP požiadavky napríklad pomocou modulu `requests`:

```python
import requests

r = requests.get("https://api.example.com/data")
print(r.status_code)         # napr. 200
print(r.headers["Content-Type"])
print(r.text)                # samotné dáta (napr. JSON)
```

---

## **Zhrnutie**

* HTTP je základný protokol webu, slúži na výmenu dát medzi klientom a serverom.
* Každá komunikácia prebieha cez požiadavky a odpovede, kde sú jasne stanovené metódy, statusy a formát.
* Je dôležité vedieť čítať HTTP komunikáciu aj rozumieť kódom odpovedí.
