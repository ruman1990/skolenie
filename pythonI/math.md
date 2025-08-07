# 📘 Učebný text: Modul `math` v Pythone

Modul `math` v Pythone poskytuje množstvo užitočných matematických funkcií a konštánt. Je súčasťou štandardnej knižnice, takže ho netreba inštalovať, len importovať.

## ✅ Ako importovať modul

```python
import math
```

Alebo môžete importovať len konkrétnu funkciu:

```python
from math import sqrt, pi
```

---

## 🔢 Základné funkcie

### `math.sqrt(x)`

Vracia druhú odmocninu z čísla `x`.

```python
math.sqrt(16)  # Výsledok: 4.0
```

### `math.pow(x, y)`

Umocní číslo `x` na exponent `y`.

```python
math.pow(2, 3)  # Výsledok: 8.0
```

> Poznámka: `math.pow()` vždy vracia `float`. Ak chcete celú mocninu, použite operátor `**`.

---

## 🧮 Zaokrúhľovanie a absolútne hodnoty

### `math.floor(x)`

Zaokrúhli číslo nadol (na najbližšie celé číslo menšie alebo rovné `x`).

```python
math.floor(3.7)  # Výsledok: 3
```

### `math.ceil(x)`

Zaokrúhli číslo nahor.

```python
math.ceil(3.2)  # Výsledok: 4
```

### `math.fabs(x)`

Vracia absolútnu hodnotu čísla (vždy kladná hodnota typu `float`).

```python
math.fabs(-5)  # Výsledok: 5.0
```

---

## 📐 Trigonometria

Všetky trigonometrické funkcie používajú **radiány** (nie stupne!).

### `math.sin(x)`, `math.cos(x)`, `math.tan(x)`

```python
math.sin(math.pi/2)  # Výsledok: 1.0
```

### Prevod medzi radianmi a stupňami:

* `math.degrees(x)` – z radianov na stupne
* `math.radians(x)` – zo stupňov na radiány

```python
math.degrees(math.pi)   # Výsledok: 180.0
math.radians(180)       # Výsledok: 3.141592...
```

---

## 🧾 Logaritmy a exponenciály

### `math.log(x, base)`

Logaritmus čísla `x` so základom `base`. Ak sa nezadá základ, predpokladá sa `e` (prirodzený logaritmus).

```python
math.log(8, 2)   # Výsledok: 3.0
math.log(10)     # logaritmus pri základe e
```

### `math.exp(x)`

Vracia hodnotu `e^x`.

```python
math.exp(2)  # Výsledok: približne 7.389
```

---

## 📌 Dôležité konštanty

* `math.pi` – Ludolfovo číslo (≈ 3.14159)
* `math.e` – Eulerovo číslo (≈ 2.71828)
* `math.tau` – 2π (≈ 6.28318)
* `math.inf` – nekonečno
* `math.nan` – „not a number“ (neplatná hodnota)

---

## ✅ Príklad: Výpočet obsahu kruhu

```python
import math

r = 5
area = math.pi * math.pow(r, 2)
print(f"Obsah kruhu s polomerom {r} je {area}")
```

---

## 💡 Zhrnutie

| Funkcia/Konštanta | Popis                 |
| ----------------- | --------------------- |
| `sqrt(x)`         | Druhá odmocnina       |
| `pow(x, y)`       | Mocnina               |
| `floor(x)`        | Zaokrúhlenie nadol    |
| `ceil(x)`         | Zaokrúhlenie nahor    |
| `fabs(x)`         | Absolútna hodnota     |
| `sin(x)`          | Sínus                 |
| `log(x, base)`    | Logaritmus            |
| `exp(x)`          | e^x                   |
| `pi`, `e`, `tau`  | Matematické konštanty |

---
