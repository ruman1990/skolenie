# 🎲 Náhoda v NumPy – modul `random`

NumPy obsahuje špeciálny podmodul `numpy.random`, ktorý slúži na **generovanie náhodných čísel**, tvorbu náhodných polí, miešanie údajov a náhodné výbery.

---

## ✅ Generovanie náhodných čísel

```python
import numpy as np

# Náhodné číslo z intervalu [0, 1)
cislo = np.random.rand()
print(cislo)
```

---

## 📏 Náhodné polia

```python
# 1D pole 5 náhodných čísel z [0, 1)
pole = np.random.rand(5)
print(pole)

# 2D pole 3x3 náhodných čísel
pole2 = np.random.rand(3, 3)
print(pole2)
```

---

## 🎲 Náhodné celé čísla

```python
# Náhodné celé číslo od 0 do 9 (bez 10)
c = np.random.randint(0, 10)
print(c)

# Pole 1D s 4 náhodnými číslami od 10 do 99
pole = np.random.randint(10, 100, size=4)
print(pole)
```

---

## 🔄 Miešanie polí (shuffle)

```python
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
```

---

## 🎯 Náhodný výber z poľa (choice)

```python
arr = np.array([3, 5, 7, 9])
vyber = np.random.choice(arr, size=2)
print(vyber)  # napr. [9 3]
```

---

## 🎲 Náhodné hodnoty z normálneho rozdelenia

```python
# 1D pole s 5 hodnotami z normálneho rozdelenia (priemer 0, smerodajná odchýlka 1)
n = np.random.randn(5)
print(n)
```

---

## ⚙️ Nastavenie semena generátora (seed)

Ak chceš opakovateľné výsledky (napr. na testovanie):

```python
np.random.seed(42)
print(np.random.rand(3))  # Vždy tie isté čísla
```

---

# ⚡ NumPy – Univerzálne funkcie (`ufunc`)

## 🧠 Čo je ufunc?

**Univerzálna funkcia** (universal function, skratka **ufunc**) je špeciálna funkcia v NumPy, ktorá efektívne vykonáva operácie **prvok-po-prvku** nad poľami.

Vďaka tomu môžeš namiesto cyklov jednoducho písať:

```python
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

sucet = np.add(a, b)
print(sucet)  # [11 22 33 44]
```

---

## ✅ Najčastejšie ufunc

| Funkcia       | Popis            | Príklad             |
| ------------- | ---------------- | ------------------- |
| `np.add`      | sčítanie         | `np.add(a, b)`      |
| `np.subtract` | odčítanie        | `np.subtract(a, b)` |
| `np.multiply` | násobenie        | `np.multiply(a, b)` |
| `np.divide`   | delenie          | `np.divide(a, b)`   |
| `np.power`    | mocnina          | `np.power(a, 2)`    |
| `np.mod`      | zvyšok po delení | `np.mod(a, 2)`      |
| `np.sqrt`     | druhá odmocnina  | `np.sqrt(a)`        |
| `np.sin`      | sínus            | `np.sin(a)`         |
| `np.maximum`  | max z dvojice    | `np.maximum(a, b)`  |

---

## 📝 Ufunc pracujú s celými poľami naraz

```python
a = np.array([1, 4, 9, 16])
print(np.sqrt(a))  # [1. 2. 3. 4.]
```

---

## ⚡ Vlastná ufunc – príklad

Môžeš si vytvoriť vlastnú univerzálnu funkciu pomocou `np.frompyfunc`:

```python
def moje_scitanie(x, y):
    return x + y

ufunc = np.frompyfunc(moje_scitanie, 2, 1)
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(ufunc(a, b))  # [11 22 33]
```

---

## ✅ Zhrnutie

* `numpy.random` slúži na generovanie náhodných čísel, tvorbu náhodných polí, výber a miešanie
* Ufunc sú univerzálne funkcie, ktoré rýchlo vykonávajú operácie na celých poliach
* Používaj ufunc vždy, keď potrebuješ rýchlo spracovať celé pole naraz bez cyklov

---
