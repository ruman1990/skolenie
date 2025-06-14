# 📋 Kopírovanie podľa hodnoty vs. podľa referencie

V Pythone sa **pre zoznamy, slovníky a množiny** používa **kopírovanie podľa referencie**.
Pre **základné typy** ako celé čísla, reťazce alebo iné **nemeniteľné objekty** (napr. `tuple`)
sa používa **kopírovanie podľa hodnoty**.

Kopírovanie podľa referencie šetrí pamäť pri práci s veľkými dátovými štruktúrami.

---

## 🧮 Kopírovanie čísel

```python
x = 10 
y = x

print(x, y)  # → 10 10

y = 11

print(x, y)  # → 10 11
```

Príkaz `y = x` vytvára **kópiu hodnoty** `x`. Neskoršia zmena `y` **neovplyvní `x`**.

---

## 🧾 Kopírovanie zoznamov (referencia)

```python
x = [1, 2, 3]
y = x

print(f'x: {x}\ny: {y}')

y[2] = 11

print('----------------------')
print(f'x: {x}\ny: {y}')
```

V prípade zoznamov príkaz `y = x` vytvára **novú referenciu** na rovnaký objekt.
Zmena `y` spôsobí aj zmenu `x`, pretože **obe premenné ukazujú na rovnaké miesto v pamäti**.

---

## 🧭 Odovzdávanie argumentov funkciám

Zoznamy sa do funkcií odovzdávajú **referenciou**:

```python
def modify(data):
    for i, _ in enumerate(data):
        data[i] *= 2

vals = [1, 2, 3, 4, 5]
print(vals)
modify(vals)
print(vals)
```

Zmena vo vnútri funkcie zmení aj pôvodné dáta.

---

## 🛡️ Ak nechceš zmeniť originál

Ak nechceš, aby funkcia menila pôvodné údaje, pošli **kópiu zoznamu**:

```python
def modify(data):
    for i, _ in enumerate(data):
        data[i] *= 2
    print(f'vo funkcii modify: {data}')

vals = [1, 2, 3, 4, 5]

print(vals)
modify(vals[:])       # kópia pomocou rezania
modify(vals.copy())   # kópia pomocou metódy copy()
print(vals)
```

---

## 🔄 Zmena na mieste alebo vytvorenie novej kópie

Niektoré funkcie **menia objekt na mieste** (in-place), iné vytvárajú **upravenú kópiu**:

```python
vals = [8, 7, 6, 0, -1, -2, 2, 1, -3, 4, 3, 5]
vals.sort()  # zmení pôvodný zoznam
```

```python
vals = [8, 7, 6, 0, -1, -2, 2, 1, -3, 4, 3, 5]
vals_s = sorted(vals)  # vytvorí novú usporiadanú kópiu
print(vals_s)
print(vals)  # pôvodné zostáva nezmenené
```

---

## 📚 Plytká vs. hlboká kópia

* **Plytká kópia (`copy`)** kopíruje **len jednu úroveň** objektu
* **Hlboká kópia (`deepcopy`)** kopíruje **aj vnorené objekty**

### Plytká kópia – jednoduché hodnoty:

```python
vals = [1, 2, 3, 4, 5, 6]
vals2 = vals.copy()
vals2[0] = 11
print(vals)   # nezmenené
print(vals2)
```

### Plytká kópia – vnorené zoznamy:

```python
vals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vals2 = vals.copy()
vals2[0][0] = 11
print(vals)   # zmenené!
print(vals2)
```

### Hlboká kópia:

```python
import copy

vals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vals2 = copy.deepcopy(vals)

vals2[0][0] = 11
print(vals)   # pôvodné nezmenené
print(vals2)
```

---

## 📊 Prehľadová tabuľka

| **Typ**        | **Príklad**           | **Kopírovanie**         |
| -------------- | --------------------- | ----------------------- |
| `int`          | `42`                  | Podľa hodnoty (`value`) |
| `float`        | `3.14`                | Podľa hodnoty           |
| `str`          | `"hello"`             | Podľa hodnoty           |
| `tuple`        | `(1, 2, 3)`           | Podľa hodnoty           |
| `list`         | `[1, 2, 3]`           | Podľa referencie        |
| `dict`         | `{"kľúč": "hodnota"}` | Podľa referencie        |
| `set`          | `{1, 2, 3}`           | Podľa referencie        |
| Vlastný objekt | `MojaTrieda()`        | Podľa referencie        |

### Poznámka:

* **Kopírovanie podľa hodnoty:** priradením vytvoríš **novú kópiu** hodnoty
* **Kopírovanie podľa referencie:** priradením len vytvoríš **ďalší odkaz na rovnaký objekt v pamäti**

---
