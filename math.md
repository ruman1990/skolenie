
# 📘 Python modul `math` (slovensky)

Modul `math` poskytuje základné matematické funkcie, ktoré pracujú s číslami typu `float` (desatinné čísla). Tento modul je súčasťou štandardnej knižnice Pythonu, takže ho netreba inštalovať.

## 📦 Import modulu

```python
import math
````

---

## 🔢 Základné matematické funkcie

| Funkcia             | Popis                                 | Príklad                             |
| ------------------- | ------------------------------------- | ----------------------------------- |
| `math.sqrt(x)`      | Druhá odmocnina z `x`                 | `math.sqrt(16)` → `4.0`             |
| `math.pow(x, y)`    | Mocnina – `x` na `y`                  | `math.pow(2, 3)` → `8.0`            |
| `math.exp(x)`       | Eulerovo číslo `e` umocnené na `x`    | `math.exp(1)` → `2.718...`          |
| `math.log(x)`       | Prirodzený logaritmus (základ `e`)    | `math.log(10)`                      |
| `math.log10(x)`     | Logaritmus o základe 10               | `math.log10(100)` → `2.0`           |
| `math.floor(x)`     | Zaokrúhlenie nadol                    | `math.floor(3.7)` → `3`             |
| `math.ceil(x)`      | Zaokrúhlenie nahor                    | `math.ceil(3.1)` → `4`              |
| `math.fabs(x)`      | Absolútna hodnota                     | `math.fabs(-5)` → `5.0`             |
| `math.factorial(x)` | Faktoriál (iba pre celé kladné čísla) | `math.factorial(5)` → `120`         |
| `math.isfinite(x)`  | Testuje, či je číslo konečné          | `math.isfinite(1.0)` → `True`       |
| `math.isinf(x)`     | Testuje, či je číslo nekonečné        | `math.isinf(math.inf)` → `True`     |
| `math.isnan(x)`     | Testuje, či je číslo NaN              | `math.isnan(float('nan'))` → `True` |

---

## 📐 Trigonometrické funkcie (v radiánoch)

| Funkcia           | Popis                     | Príklad                         |
| ----------------- | ------------------------- | ------------------------------- |
| `math.sin(x)`     | Sinus                     | `math.sin(math.pi / 2)` → `1`   |
| `math.cos(x)`     | Kosinus                   | `math.cos(0)` → `1`             |
| `math.tan(x)`     | Tangens                   | `math.tan(0)` → `0`             |
| `math.asin(x)`    | Arkus sinus               | `math.asin(1)` → `π/2`          |
| `math.acos(x)`    | Arkus kosinus             | `math.acos(1)` → `0`            |
| `math.atan(x)`    | Arkus tangens             | `math.atan(1)` → \~`0.785`      |
| `math.radians(x)` | Premení stupne na radiány | `math.radians(180)` → `π`       |
| `math.degrees(x)` | Premení radiány na stupne | `math.degrees(math.pi)` → `180` |

---

## 🧮 Hyperbolické funkcie

| Funkcia         | Popis                      |
| --------------- | -------------------------- |
| `math.sinh(x)`  | Hyperbolický sinus         |
| `math.cosh(x)`  | Hyperbolický kosinus       |
| `math.tanh(x)`  | Hyperbolický tangens       |
| `math.asinh(x)` | Arkus hyperbolický sinus   |
| `math.acosh(x)` | Arkus hyperbolický kosinus |
| `math.atanh(x)` | Arkus hyperbolický tangens |

---

## 🔢 Kombinatorika

| Funkcia             | Popis               |
| ------------------- | ------------------- |
| `math.comb(n, k)`   | Počet kombinácií    |
| `math.perm(n, k)`   | Počet permutácií    |
| `math.factorial(n)` | Faktoriál čísla `n` |

---

## 📌 Konštanty

| Konštanta  | Hodnota           | Popis                    |
| ---------- | ----------------- | ------------------------ |
| `math.pi`  | 3.141592653589793 | Ludolfovo číslo π        |
| `math.e`   | 2.718281828459045 | Eulerovo číslo e         |
| `math.tau` | 6.283185307179586 | Tau (2π)                 |
| `math.inf` | ∞ (nekonečno)     | Použitie: `float('inf')` |
| `math.nan` | Not a Number      | Nepoužiteľná hodnota     |

---

## 🔍 Zobrazenie všetkých funkcií (v Pythone)

```python
import math
print(dir(math))
```

---

## ✅ Príklad použitia

```python
import math

r = 5
obsah = math.pi * math.pow(r, 2)
print(f"Obsah kruhu s polomerom {r} je: {obsah}")
```

---

## 🔗 Oficiálna dokumentácia

👉 [https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

```

