# 🧩 Python `dataclass` – dátové triedy jednoducho

---

## 🔍 Čo je `dataclass`?

`@dataclass` je dekorátor v Pythone (od verzie 3.7), ktorý **zjednodušuje písanie tried** určených na **uchovávanie dát**.

Automaticky vytvorí metódy ako:

* `__init__()` – konštruktor
* `__repr__()` – reprezentácia v texte
* `__eq__()` – porovnanie objektov
* `__hash__()` – voliteľne

---

## ✅ Základný príklad:

```python
from dataclasses import dataclass

@dataclass
class Osoba:
    meno: str
    vek: int

o = Osoba("Jana", 30)
print(o)  # Osoba(meno='Jana', vek=30)
```

---

## ✍️ Výhody `dataclass`

* Menej boilerplate kódu (nepíšeš `__init__`, `__repr__`, ...)
* Typová kontrola v IDE (pomocou anotácií)
* Možnosť predvolených hodnôt
* Funguje dobre so `tuple`, `dict`, JSON, atď.

---

## 🧱 Predvolené hodnoty

```python
@dataclass
class Produkt:
    nazov: str
    cena: float = 0.0

p = Produkt("Chleba")
print(p)  # Produkt(nazov='Chleba', cena=0.0)
```

---

## 🔐 Úprava správania poľa

Použi `field()` na detailnejšiu kontrolu:

```python
from dataclasses import field

@dataclass
class Uzivatel:
    meno: str
    heslo: str = field(repr=False)  # nezobrazí heslo v __repr__
```

---

## ⚙️ `__post_init__()` – logika po vytvorení objektu

Na overenie alebo úpravu hodnôt po inicializácii:

```python
@dataclass
class Osoba:
    meno: str
    vek: int

    def __post_init__(self):
        if self.vek < 0:
            raise ValueError("Vek nemôže byť záporný")
```

---

## 🧮 Porovnanie objektov

```python
@dataclass
class Bod:
    x: int
    y: int

b1 = Bod(1, 2)
b2 = Bod(1, 2)
print(b1 == b2)  # True
```

---

## 🔁 Poradie a triedenie (`order=True`)

```python
@dataclass(order=True)
class Osoba:
    vek: int
    meno: str

o1 = Osoba(30, "Anna")
o2 = Osoba(25, "Boris")
print(o1 > o2)  # True
```

---

## 🧠 `dataclass` vs klasická trieda

| Funkcia                  | `dataclass`              | Bežná trieda |
| ------------------------ | ------------------------ | ------------ |
| Automatický `__init__`   | ✅                        | ❌            |
| Automatický `__repr__`   | ✅                        | ❌            |
| Podpora typov            | ✅                        | Nepovinná    |
| Skratka na ukladanie dát | ✅                        | ✅            |
| Pokročilá logika         | 🔸 (cez `__post_init__`) | ✅            |

---

## 🚫 Kedy radšej NEPOUŽÍVAŤ `dataclass`

* Ak trieda má veľa vlastnej logiky alebo komplexné metódy
* Ak potrebuješ plnú kontrolu nad `__init__`
* Ak atribúty sa budú často meniť dynamicky (napr. dictionary-like objekty)

---

## ✍️ Rýchla rekapitulácia

```python
from dataclasses import dataclass

@dataclass
class Auto:
    znacka: str
    rok: int
```

* Ušetríš desiatky riadkov kódu
* Triedy vyzerajú čistejšie
* Stále môžeš doplniť metódy, validáciu alebo vlastné správanie

---
