# Základy funkcionálneho programovania v Pythone

## Čo je funkcionálne programovanie?

Funkcionálne programovanie je štýl programovania, v ktorom sa výpočty vyjadrujú ako **funkcie**, nie ako sekvencie príkazov.
Kľúčové znaky:

* **Funkcie sú „objekty“:** môžu byť ukladané do premenných, odovzdávané ako argumenty, vracané z iných funkcií.
* **Immutabilita**: meníme čo najmenej údajov „na mieste“, používame mapovanie, filtrovanie, zreťazovanie atď.

Python nie je čisto funkcionálny jazyk, ale poskytuje silnú podporu funkcionálneho štýlu.

---

## Lambda výrazy

**Lambda** je spôsob, ako vytvoriť **malú anonymnú funkciu** (bez mena) na jeden riadok.

```python
f = lambda x: x * 2
print(f(5))  # Výstup: 10
```

Typické použitie je ako argument pre funkcie ako `map`, `filter`, `sorted` atď.

```python
cisla = [1, 2, 3, 4, 5, 6, 7, 8]

# 1. map – každý prvok vynásobíme dvomi
dvojnasobky = list(map(lambda x: x * 2, cisla))
print("Dvojnásobky:", dvojnasobky)  # [2, 4, 6, 8, 10, 12, 14, 16]

# 2. filter – ponecháme len párne čísla
parne = list(filter(lambda x: x % 2 == 0, cisla))
print("Párne čísla:", parne)  # [2, 4, 6, 8]

# 3. sorted – zoradíme čísla zostupne
zoradene = sorted(cisla, reverse=True)
print("Zoradené (zostupne):", zoradene)  # [8, 7, 6, 5, 4, 3, 2, 1]
```

---

## List comprehensions (a set/dict comprehensions)

**List comprehension** je elegantný spôsob, ako rýchlo vytvoriť nový zoznam z iného zoznamu (podobne funguje pre množiny a slovníky).

```python
cisla = [1, 2, 3, 4]
dvojnasobky = [x * 2 for x in cisla]
print(dvojnasobky)  # [2, 4, 6, 8]

parne = [x for x in cisla if x % 2 == 0]
print(parne)  # [2, 4]
```

Podobne množiny a slovníky:

```python
mocniny = {x: x**2 for x in range(5)}
print(mocniny)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Modul `functools`

Modul **`functools`** obsahuje užitočné funkcie pre pokročilejšiu prácu s funkciami (tzv. vyššieho rádu):

### Najčastejšie používané funkcie:

| Funkcia                                       | Popis                                                                                        |
| --------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `functools.reduce(funkcia, zoznam)`           | Aplikuje funkciu akumulatívne na prvky zoznamu, vráti jeden výsledok (napr. súčet, súčin...) |
| `functools.partial(funkcia, *args, **kwargs)` | Vytvorí „polofunkciu“ – niektoré argumenty už nastavené dopredu                              |


**Príklady:**

```python
from functools import reduce

zoznam = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, zoznam)
print(suma)  # 10
```

```python
from functools import partial

def mocnina(x, n):
    return x ** n

stvorcova = partial(mocnina, n=2)
print(stvorcova(5))  # 25
```

---
```python
from functools import cache

@cache
def slow_fn(x):
    print("Computing...")
    return x * 2
```
---

## Modul `itertools`

Modul **`itertools`** poskytuje rýchle funkcie na prácu s iterátormi, generovanie kombinácií, permutácií a nekonečných sekvencií.

### Príklady užitočných funkcií:

| Funkcia                                         | Popis                                             |
| ----------------------------------------------- | ------------------------------------------------- |
| `itertools.chain(a, b, ...)`                    | Zreťazí viac iterátorov do jedného                |
| `itertools.cycle(iterable)`                     | Nekonečne opakuje prvky sekvencie                 |
| `itertools.combinations(iterable, k)`           | Všetky kombinácie k prvkov                        |
| `itertools.permutations(iterable, k)`           | Všetky permutácie k prvkov                        |
| `itertools.groupby(iterable, key=...)`          | Skupinuje po sebe idúce rovnaké prvky podľa kľúča |
| `itertools.islice(iterable, start, stop, step)` | Výrez z iterátora (ako slice pre zoznam)          |
| `itertools.product(a, b, ...)`                  | Kartézsky súčin sekvencií                         |

**Príklady:**

```python
from itertools import combinations, chain

print(list(combinations([1, 2, 3], 2)))  # [(1, 2), (1, 3), (2, 3)]

zoznam1 = [1, 2]
zoznam2 = [3, 4]
print(list(chain(zoznam1, zoznam2)))  # [1, 2, 3, 4]
```

---

from itertools import groupby

data = [1, 1, 2, 2, 2, 3, 1, 1]

for key, group in groupby(data):
    print(key, list(group))



#1 [1, 1]
#2 [2, 2, 2]
#3 [3]
#1 [1, 1]
---

## Knižnica `funcy`

**`funcy`** je externá Python knižnica, ktorá rozširuje funkcionálne programovanie o množstvo užitočných funkcií navyše.
Poskytuje pokročilé verzie **map**, **filter**, **memoizáciu**, **prácu s iterátormi a sekvenciami**, podporu pre curry a ďalšie „funkcionálne špeciality“.

### Inštalácia:

```bash
pip install funcy
```

### Príklad použitia:

```python
from funcy import lmap, lfilter, partial, compose

print(lmap(lambda x: x + 1, [1, 2, 3]))  # [2, 3, 4]
print(lfilter(lambda x: x % 2 == 0, range(10)))  # [0, 2, 4, 6, 8]

# Zreťazenie funkcií (compose)
f = compose(str, abs)
print(f(-15))  # '15'
```

**Memoizácia** (uloženie výsledku funkcie):

```python
from funcy import memoize

@memoize
def draha_funkcia(x):
    print("Volám funkciu...")
    return x * 2

print(draha_funkcia(10))  # vypočíta
print(draha_funkcia(10))  # použije cache, nevypíše "Volám funkciu..."
```

---

## Zhrnutie

* **Funkcionálne programovanie** umožňuje efektívne, bezpečné a čitateľné spracovanie údajov v Pythone.
* Dôležité stavebné prvky: **lambdy, comprehensions, map/filter/reduce, itertools, functools, funcy**.
* Vhodné na analýzy, prácu s veľkými zoznamami, generovanie kombinácií, transformácie, bez potreby zmeniť pôvodné údaje.
