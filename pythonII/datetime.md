Samozrejme! Tu je **učebný text pre prácu s dátumom a časom v Pythone**, vhodný ako úvod aj pre mierne pokročilých, s ukážkami a vysvetlením:

---

# 🕓 Dátum a čas v Pythone

## Úvod

Práca s dátumom a časom je v programovaní veľmi častá úloha.
Python má na to viacero knižníc, pričom najčastejšie používanou je **`datetime`** (súčasť štandardnej knižnice).
Existujú aj ďalšie – napríklad **`time`**, **`calendar`**, či pokročilé balíky ako **`pytz`** (pre časové pásma) a **`dateutil`** (pre rozšírenú manipuláciu).

---

## 1. Modul `datetime`

### Základné triedy

* **`datetime.date`** – reprezentuje iba dátum (rok, mesiac, deň)
* **`datetime.time`** – reprezentuje iba čas (hodina, minúta, sekunda, mikrosekunda)
* **`datetime.datetime`** – obsahuje dátum aj čas
* **`datetime.timedelta`** – predstavuje rozdiel medzi dvoma dátumami/časmi

---

### Aktuálny dátum a čas

```python
import datetime

now = datetime.datetime.now()
print("Aktuálny dátum a čas:", now)

today = datetime.date.today()
print("Dnešný dátum:", today)
```

---

### Vytvorenie konkrétneho dátumu/času

```python
import datetime

d = datetime.date(2024, 5, 1)      # 1. máj 2024
t = datetime.time(15, 30, 0)       # 15:30:00
dt = datetime.datetime(2024, 5, 1, 15, 30, 0)
print(dt)
```

---

### Formátovanie dátumu a času (prevod na text)

Použi metódu **`strftime`**:

```python
import datetime

now = datetime.datetime.now()
print(now.strftime("%d.%m.%Y %H:%M"))  # napr. 01.07.2025 14:25
```

Najčastejšie kódy:

* `%d` – deň (01-31)
* `%m` – mesiac (01-12)
* `%Y` – rok (celý, napr. 2025)
* `%H` – hodina (00-23)
* `%M` – minúta
* `%S` – sekunda

---

### Parsovanie dátumu a času (text → datetime)

Použi **`strptime`**:

```python
import datetime

s = "25.12.2023 14:00"
dt = datetime.datetime.strptime(s, "%d.%m.%Y %H:%M")
print(dt)
```

---

## 2. Rozdiel medzi dátumami (timedelta)

Na zistenie počtu dní alebo sekúnd medzi dvoma dátumami použiješ **`timedelta`**:

```python
import datetime

d1 = datetime.date(2025, 7, 1)
d2 = datetime.date(2025, 8, 1)
delta = d2 - d1
print("Rozdiel v dňoch:", delta.days)
```

---

## 3. Práca s časovými pásmami

Python štandardne pracuje s "naivnými" dátumami (bez pásma).
Na podporu časových pásiem použiješ balíky **`pytz`** alebo **`zoneinfo`** (od Python 3.9):

```python
from datetime import datetime
from zoneinfo import ZoneInfo  # od Python 3.9

dt = datetime.now(ZoneInfo("Europe/Bratislava"))
print(dt)
```

---

## 4. Modul `time` – práca s časom v sekundách

Trieda `time` poskytuje nižšiu úroveň, hlavne na meranie času (napr. `sleep`, časové pečiatky):

```python
import time

print("Čakám 2 sekundy...")
time.sleep(2)
print("Hotovo!")
```

Získať aktuálny čas ako "timestamp" (sekundy od 1.1.1970):

```python
import time

timestamp = time.time()
print(timestamp)
```

---

## 5. Modul `calendar` – práca s kalendárom

Na zobrazenie mesiacov, dní v týždni, pracovných dní a pod. je vhodný modul **`calendar`**:

```python
import calendar

# Vytlačí kalendár na júl 2025
print(calendar.month(2025, 7))
```

---

## 6. Praktické príklady

### a) Odpočítavanie dní do Vianoc

```python
import datetime

today = datetime.date.today()
vianoce = datetime.date(today.year, 12, 24)
if today > vianoce:
    vianoce = datetime.date(today.year + 1, 12, 24)
days = (vianoce - today).days
print(f"Do Vianoc zostáva {days} dní.")
```

---

### b) Časová pečiatka (timestamp) ↔ dátum

```python
import datetime
import time

ts = time.time()
dt = datetime.datetime.fromtimestamp(ts)
print(dt)
```

---

### c) Automatické generovanie času do logov

```python
import datetime

def log(msg):
    now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    print(now, msg)

log("Začínam úlohu.")
```

---

## 7. Prehľad najdôležitejších funkcií

| Funkcia/trieda                 | Popis                   |
| ------------------------------ | ----------------------- |
| `datetime.now()`               | Aktuálny dátum a čas    |
| `date.today()`                 | Dnešný dátum            |
| `datetime.strptime(s, format)` | Text → datetime         |
| `datetime.strftime(format)`    | datetime → text         |
| `timedelta(days=n)`            | Rozdiel n dní           |
| `time.sleep(n)`                | Spánok na n sekúnd      |
| `calendar.month(y, m)`         | Kalendár daného mesiaca |
| `fromtimestamp(ts)`            | Timestamp → dátum a čas |

---

## 8. Užitočné rady

* Dátum a čas sú citlivé na formátovanie – buď dôsledný v zápise a čítaní.
* Pri práci s časom v rôznych krajinách/pásmach vždy mysli na časové pásma!
* Ak často konvertuješ medzi stringom a dátumom, používaj stále rovnaký formát.

---
