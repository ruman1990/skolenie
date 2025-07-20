# Python – Generátory

## Čo je generátor?

**Generátor** je špeciálny typ iterátora, ktorý sa vytvára pomocou funkcie a kľúčového slova `yield` namiesto `return`.
Generátory sú výhodné, keď potrebujeme veľké množstvo dát generovať postupne, šetria pamäť a jednoducho sa používajú.

---

## Základná ukážka generátora

```python
def moje_cisla():
    a = 1
    while a <= 5:
        yield a
        a += 1

for cislo in moje_cisla():
    print(cislo)
```

> Tento generátor vypíše čísla od 1 do 5.
> Každé volanie `yield` si „pamätá“ stav funkcie a pri ďalšom použití pokračuje tam, kde skončil.

---

## Porovnanie: Generátor vs. Klasický iterátor

* **Klasický iterátor**: Potrebuješ implementovať metódy `__iter__()` a `__next__()`.
* **Generátor**: Stačí jednoduchá funkcia s `yield`.

**Príklad: Generátor číselného radu**

```python
def range_generator(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in range_generator(3):
    print(x)
# 0, 1, 2
```

---

## Vytvorenie nekonečného generátora

```python
def nekonecny():
    i = 0
    while True:
        yield i
        i += 1

g = nekonecny()
for _ in range(5):
    print(next(g))  # vypíše 0, 1, 2, 3, 4
```

> Pozor: **Takýto generátor je nekonečný** – na bežné použitie ho obmedzuj cyklom alebo podmienkou.

---

## Generátorové výrazy (generator expressions)

Podobne ako „list comprehension“, ale s okrúhlymi zátvorkami:

```python
gen = (x*x for x in range(5))
for cislo in gen:
    print(cislo)
# 0, 1, 4, 9, 16
```

---

## Praktická ukážka: Spracovanie veľkých súborov

Predstav si, že máš obrovský súbor a potrebuješ načítavať riadky po jednom (napr. log súbor):

```python
def citaj_riadky(subor):
    with open(subor, "r") as f:
        for riadok in f:
            yield riadok.strip()

for riadok in citaj_riadky("velky_log.txt"):
    print(riadok)
```

> Takto nikdy nenahráš celý súbor do pamäte naraz!

---

## Zaujímavosť: Generátor Fibonacciho čísel

```python
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for cislo in fibonacci(20):
    print(cislo)
# 0, 1, 1, 2, 3, 5, 8, 13
```

---

Ak ťa zaujíma ešte viac:

* rozdiel medzi generátorom a iterátorom v praxi
* pokročilé použitie (napr. pre pipeline spracovania dát)
* alebo úloha na skúšku
  napíš a rád rozšírim alebo zadám cvičenie! 😊
