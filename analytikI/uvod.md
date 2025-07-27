# 🧠 Opakovanie: Práca s dátami a funkciami v Pythone

---

## 🧩 1. Pokročilá práca s funkciami

Funkcie v Pythone sú **prvotriedne objekty** – môžu sa ukladať do premenných, prenášať ako argumenty alebo vracať ako výsledky.

### ✅ Lambda výrazy (anonymné funkcie)

```python
zvys_o = lambda x: x + 1
print(zvys_o(4))  # 5
```

Použitie napr. pri `sorted`, `map`, `filter`.

---

### ✅ Funkcie ako argumenty

```python
def vykonaj(funkcia, x):
    return funkcia(x)

print(vykonaj(abs, -5))  # 5
```

---

### ✅ \*args a \*\*kwargs

* `*args`: ľubovoľný počet pozičných argumentov
* `**kwargs`: ľubovoľný počet pomenovaných argumentov

```python
def vypis(*args, **kwargs):
    print(args)
    print(kwargs)

vypis(1, 2, 3, meno="Jana", vek=30)
```

---

## 🗂️ 2. Selekcia dát

Selekcia znamená výber konkrétnych prvkov zo zoznamu, slovníka alebo inej kolekcie.

### ✅ List comprehension

```python
cisla = [1, 2, 3, 4, 5]
parne = [x for x in cisla if x % 2 == 0]
```

### ✅ Z reťazca len čísla

```python
text = "abc123def456"
cisla = [c for c in text if c.isdigit()]  # ['1', '2', '3', '4', '5', '6']
```

---

## 🧹 3. Filtrovanie a triedenie

### ✅ `filter()` – vyberie len tie prvky, ktoré splnia podmienku

```python
cisla = [1, 2, 3, 4, 5]
parne = list(filter(lambda x: x % 2 == 0, cisla))  # [2, 4]
```

### ✅ `sorted()` – zoradí zoznam podľa kľúča

```python
mena = ["Jana", "adam", "Zuzana"]
zoradene = sorted(mena, key=lambda x: x.lower())  # podľa abecedy bez ohľadu na veľkosť
```

---

## 🧮 4. Zoskupovanie dát

Na zoskupovanie údajov (napr. podľa kategórie, roka, typu) sa často používa knižnica `itertools` alebo `collections`.

### ✅ Použitie `groupby` z `itertools` (nutné zoradiť podľa kľúča!)

```python
from itertools import groupby

data = [
    ("jablko", "ovocie"),
    ("mrkva", "zelenina"),
    ("banán", "ovocie"),
]

# najprv zoradiť!
data.sort(key=lambda x: x[1])

for typ, skupina in groupby(data, key=lambda x: x[1]):
    print(f"{typ}: {[item[0] for item in skupina]}")
```

### ✅ Alternatíva: zoskupovanie do slovníka

```python
from collections import defaultdict

skupiny = defaultdict(list)
for nazov, kategoria in data:
    skupiny[kategoria].append(nazov)

print(dict(skupiny))
```

---

## 🔢 5. `float` vs `Decimal`

### ✅ `float` (64-bitové čísla s desatinnou čiarkou)

* Rýchle, ale **nemajú presné desatinné hodnoty** (napr. pri sčítaní peňazí)

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

---

### ✅ `Decimal` – presné desatinné čísla (napr. pre účtovníctvo)

```python
from decimal import Decimal

a = Decimal("0.1")
b = Decimal("0.2")
print(a + b)  # 0.3
```

📌 Odporúčané použiť v prípadoch ako: ceny, dane, meny, presné výpočty

---

## ✍️ Rýchla rekapitulácia:

| Téma                     | Použitie                       |
| ------------------------ | ------------------------------ |
| `lambda`, `*args`        | Dynamické a flexibilné funkcie |
| List comprehension       | Výber a úprava dát z kolekcií  |
| `filter`, `sorted`       | Filtrovanie a triedenie        |
| `groupby`, `defaultdict` | Zoskupovanie podľa kľúča       |
| `float` vs `Decimal`     | Presnosť vs výkon              |

---
