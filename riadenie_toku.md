## Podmienené príkazy: `if` a `match`

### `if`, `elif`, `else`

Používa sa na vetvenie logiky programu:

```python
vek = 20
if vek < 18:
    print("Neplnoletý")
elif vek == 18:
    print("Práve si dovršil 18")
else:
    print("Plnoletý")
```

### `match` (od verzie Python 3.10)

`match` je nový prístup k vetveniu, podobný `switch` v iných jazykoch:

```python
hodnota = "A"

match hodnota:
    case "A":
        print("Vybral si A")
    case "B":
        print("Vybral si B")
    case _:
        print("Iná hodnota")
```

```
def popis_cislo(x):
    match x:
        case int() if x < 0:
            print("Záporné číslo")
        case int() if x == 0:
            print("Nula")
        case int() if x > 0:
            print("Kladné číslo")
        case _:
            print("Nie je celé číslo")
```

---

## Cykly: `for` a `while`

### `for` cyklus

Používa sa na prechod cez iterovateľné objekty:

```python
zoznam = [1, 2, 3]
for cislo in zoznam:
    print(cislo)
```

### `while` cyklus

Spúšťa sa, pokiaľ platí podmienka:

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

---

## `break`, `continue`, `pass`

### `break`

Ukončí cyklus:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue`

Preskočí zvyšok iterácie:

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### `pass`

Používa sa ako zástupca príkazu (napr. v prípade, že kód ešte len budeme dopĺňať):

```python
if True:
    pass  # tu bude kód neskôr
```

---
