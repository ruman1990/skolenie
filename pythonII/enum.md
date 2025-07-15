# 🔢 Enum (výčtové typy) v Pythone

## Čo je enumerátor (Enum)?

**Enumerátor** (alebo *výčtový typ*) je špeciálny typ dátovej štruktúry, ktorý umožňuje vytvoriť pomenované konštanty.
Používa sa, keď máš premennú, ktorá môže nadobúdať len vopred určené hodnoty (napr. dni v týždni, stav objednávky, typ užívateľa...).

Vďaka `Enum`:

* Kód je prehľadnejší, čitateľnejší a menej náchylný na chyby.
* Môžeš porovnávať hodnoty podľa mena, nie podľa čísla alebo reťazca.

---

## 1. Základné použitie – modul `enum`

Od Pythonu 3.4 je vstavaný modul `enum`:

```python
from enum import Enum

class Day(Enum):
    PONDELOK = 1
    UTOROK = 2
    STREDA = 3
    STVRTOK = 4
    PIATOK = 5
    SOBOTA = 6
    NEDELA = 7

# Prístup k hodnotám:
print(Day.PONDELOK)
print(Day.PONDELOK.name)   # 'PONDELOK'
print(Day.PONDELOK.value)  # 1
```

---

## 2. Porovnávanie enumov

```python
d = Day.PONDELOK
if d == Day.PONDELOK:
    print("Je pondelok!")
```

> Porovnávaš priamo členy Enum, nie len hodnoty.

---

## 3. Iterácia cez Enum

```python
for day in Day:
    print(day.name, day.value)
```

> Každý člen výčtového typu má meno (`name`) a hodnotu (`value`).

---

## 4. Automatické číslovanie: `auto()`

Ak nechceš ručne prideľovať hodnoty, použi `auto()`:

```python
from enum import Enum, auto

class StavObjednavky(Enum):
    VYTVORENA = auto()
    ODOSLANA = auto()
    DORUCENA = auto()
    ZRUSENA = auto()

for stav in StavObjednavky:
    print(stav.name, stav.value)
```

> Hodnoty budú automaticky číslované od 1.

---

## 5. Enum s reťazcovými hodnotami

Hodnoty enumu nemusia byť len čísla – môžu byť aj reťazce:

```python
from enum import Enum

class Farba(Enum):
    CERVENA = "red"
    MODRA = "blue"
    ZELENA = "green"

print(Farba.CERVENA.value)  # 'red'
```

---

## 6. Enum a bezpečnosť

Priradenie inej hodnoty ako vymenovanej nie je povolené:

```python
# Toto spôsobí chybu:
# d = Day(8)  # ValueError: 8 nie je platná hodnota pre Day
```

---

## 7. Praktický príklad

Použitie enumu na reprezentáciu stavu úlohy:

```python
from enum import Enum, auto

class StavUlohy(Enum):
    NOVA = auto()
    SPRACOVANA = auto()
    DOKONCENA = auto()
    ZRUSENA = auto()

def popis_stavu(stav):
    if stav == StavUlohy.NOVA:
        return "Úloha je nová."
    elif stav == StavUlohy.DOKONCENA:
        return "Úloha je hotová."
    else:
        return "Iný stav."

stav = StavUlohy.NOVA
print(popis_stavu(stav))
```

---

## 8. Zhrnutie

* Enumy sú skvelé na použitie, keď premenná má nadobúdať len *určité hodnoty*.
* Sú čitateľné, bezpečné, umožňujú ľahké porovnávanie a iteráciu.
* Pracujú s číslami aj reťazcami.
* Sú súčasťou Pythonu od verzie 3.4 (modul `enum`).

---
