# 🧩 `namedtuple` v Pythone

## 🔍 Čo je `namedtuple`?

`namedtuple` je **nepremenná** (immutable) trieda v Pythone, ktorá funguje ako obyčajný tuple, ale s pomenovanými poľami – takže namiesto prístupu cez indexy môžeš použiť mená.

Je to rýchla a ľahká alternatíva ku klasickej triede alebo `dataclass`, ak chceš len **uložiť dáta** a nepotrebuješ nič meniť.

---

## ✅ Import

```python
from collections import namedtuple
```

---

## 🛠️ Vytvorenie vlastného `namedtuple`

```python
from collections import namedtuple

# Definujeme nový typ: Osoba
Osoba = namedtuple("Osoba", ["meno", "vek"])

# Vytvorenie inštancie
o = Osoba("Jana", 30)
```

---

## 💡 Prístup k hodnotám

```python
print(o.meno)  # "Jana"
print(o.vek)   # 30

# Alebo cez index (ako pri obyčajnom tuple)
print(o[0])    # "Jana"
```

---

## 🔐 Vlastnosti

* ✅ **Immutable** – nemožno meniť hodnoty:

  ```python
  o.vek = 40  # ❌ TypeError
  ```

* ✅ Automaticky vytvára metódy ako:

  * `__repr__` → pre čitateľný výpis
  * `__eq__` → porovnávanie hodnôt
  * `._asdict()` → konverzia na slovník

---

## 🧪 Užitočné metódy

```python
o = Osoba("Jana", 30)

print(o._asdict())  
# {'meno': 'Jana', 'vek': 30}

# Erb tuple do nového s jednou zmenou
nova = o._replace(vek=31)
print(nova)
# Osoba(meno='Jana', vek=31)
```

---

## 🆚 Porovnanie s inými typmi

| Typ          | Mutable | Jednoduchý zápis | Pomenované polia | Porovnanie hodnôt         |
| ------------ | ------- | ---------------- | ---------------- | ------------------------- |
| `tuple`      | ✅       | ✅                | ❌                | ✅                         |
| `namedtuple` | ❌       | ✅                | ✅                | ✅                         |
| `dataclass`  | ✅       | ✅                | ✅                | ✅                         |
| Bežná trieda | ✅       | ❌                | ✅                | ❌ (ak neuvedieš `__eq__`) |

---

## 📦 Kedy použiť `namedtuple`

Použi `namedtuple`, keď:

* Potrebuješ jednoduchú štruktúru na čítanie dát
* Hodnoty sa **nebudú meniť**
* Chceš niečo jednoduchšie a rýchlejšie ako `class` alebo `dataclass`
* Chceš lepší zápis ako `("Jana", 30)` → `Osoba(meno="Jana", vek=30)`

---

## 🚫 Kedy **nepoužívať** `namedtuple`

* Ak potrebuješ meniť hodnoty → použi `dataclass`
* Ak potrebuješ metódy alebo logiku → použi bežnú triedu
* Ak potrebuješ dediť alebo vytvárať zložité hierarchie

---

## 🧠 Tip: Používaj `namedtuple` ako "read-only" záznamy

Je to ideálne napríklad pre:

* Súradnice (`Bod = namedtuple("Bod", ["x", "y"])`)
* Konfigurácie
* Výsledky funkcií


---

## 🧩 Príklad 1: 2D bod a vzdialenosť

```python
from collections import namedtuple
from math import sqrt

# Definícia namedtuple
Bod = namedtuple("Bod", ["x", "y"])

# Vytvorenie dvoch bodov
bod1 = Bod(0, 0)
bod2 = Bod(3, 4)

# Výpočet vzdialenosti (Pytagorova veta)
dx = bod2.x - bod1.x
dy = bod2.y - bod1.y
vzdialenost = sqrt(dx**2 + dy**2)

print(f"Vzdialenosť medzi bodmi je: {vzdialenost}")  # 5.0
```

---

## 🧩 Príklad 2: Študenti a výber podľa známky

```python
from collections import namedtuple

Student = namedtuple("Student", ["meno", "rocnik", "znamka"])

# Zoznam študentov
studenti = [
    Student("Anna", 1, 1),
    Student("Boris", 2, 2),
    Student("Cyril", 3, 1)
]

# Výber tých s jednotkou
for s in studenti:
    if s.znamka == 1:
        print(f"{s.meno} má známku 1")
```

---

## 🧩 Príklad 3: Konverzia na slovník

```python
from collections import namedtuple

Produkt = namedtuple("Produkt", ["nazov", "cena"])

p = Produkt("Chleba", 1.49)

# Konverzia na slovník
d = p._asdict()
print(d)  # {'nazov': 'Chleba', 'cena': 1.49}
```

---

## 🧩 Príklad 4: Zmena hodnoty pomocou `_replace`

```python
from collections import namedtuple

Auto = namedtuple("Auto", ["znacka", "rok", "najazdene"])

a = Auto("Škoda", 2020, 25000)

# Zmena najazdených km
a_nove = a._replace(najazdene=30000)

print(a)       # Auto(znacka='Škoda', rok=2020, najazdene=25000)
print(a_nove)  # Auto(znacka='Škoda', rok=2020, najazdene=30000)
```

---

## 🧩 Príklad 5: Triedenie filmov podľa hodnotenia

```python
from collections import namedtuple

Film = namedtuple("Film", ["nazov", "rok", "hodnotenie"])

filmy = [
    Film("Inception", 2010, 9.0),
    Film("Interstellar", 2014, 8.6),
    Film("Tenet", 2020, 7.4),
    Film("Memento", 2000, 8.4),
    Film("Dunkirk", 2017, 7.9)
]

# Triedenie podľa hodnotenia (od najvyššieho po najnižšie)
zoradene = sorted(filmy, key=lambda f: f.hodnotenie, reverse=True)

for f in zoradene:
    print(f"{f.nazov} ({f.rok}) – hodnotenie: {f.hodnotenie}")
```
