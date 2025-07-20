# Modul `decimal` v Pythone

## Teória

Modul **`decimal`** v Pythone poskytuje podporu pre **presné desatinné výpočty s ľubovoľnou presnosťou**.
Bežné číselné typy `float` v Pythone (a väčšine jazykov) môžu mať **zaokrúhľovacie chyby** pri práci s desatinnými číslami, čo je problém napríklad vo financiách, účtovníctve, alebo pri veľmi presných výpočtoch.

**`decimal.Decimal`** je špeciálny typ čísla, ktorý:

* **Presne reprezentuje desatinné hodnoty** (napr. 0.1 + 0.2 bude presne 0.3)
* Umožňuje nastaviť presnosť a spôsob zaokrúhľovania
* Správa sa podobne ako kalkulačka – žiadne skryté binárne chyby

---

## Kedy použiť `decimal`?

* Pri výpočtoch, kde záleží na **presnosti** (peniaze, dane, merania...)
* Pri porovnávaní, sčítaní a odčítaní desatinných čísel
* Keď nestačí bežný typ `float`

---

## Základné použitie

### 1. Import a vytvorenie čísla Decimal

```python
from decimal import Decimal

a = Decimal('0.1')
b = Decimal('0.2')
c = a + b
print(c)  # Výstup: 0.3
```

**Pozor:** Vždy používajte **reťazce** (stringy) pri vytváraní Decimal čísel!
Ak by ste použili priamo float, chyba by sa preniesla:

```python
Decimal(0.1)    # NENÍ presné!
Decimal('0.1')  # Správne!
```

---

### 2. Porovnanie s float

```python
print(0.1 + 0.2)                 # Výstup: 0.30000000000000004
print(Decimal('0.1') + Decimal('0.2'))  # Výstup: 0.3
```

---

### 3. Nastavenie presnosti výpočtov

Presnosť môžete nastaviť pomocou objektu **`getcontext()`**:

```python
from decimal import Decimal, getcontext

getcontext().prec = 4  # nastavenie presnosti na 4 číslice

a = Decimal('1') / Decimal('7')
print(a)  # Výstup: 0.1429
```

---

### 4. Zaokrúhľovanie a formátovanie

Môžete určovať spôsob zaokrúhľovania:

```python
from decimal import Decimal, ROUND_HALF_UP

cena = Decimal('4.567')
zaokruhlene = cena.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(zaokruhlene)  # Výstup: 4.57
```

---

### 5. Výpočty a operácie

Decimal podporuje všetky základné matematické operácie:

```python
from decimal import Decimal

a = Decimal('10.5')
b = Decimal('3')
print(a + b)    # 13.5
print(a - b)    # 7.5
print(a * b)    # 31.5
print(a / b)    # 3.5
```

---

### 6. Príklad – výpočet s peniazmi

```python
from decimal import Decimal, ROUND_DOWN

cena = Decimal('19.99')
dph = Decimal('0.20')
cena_s_dph = cena * (1 + dph)
cena_s_dph = cena_s_dph.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
print(cena_s_dph)  # Výstup: 23.98
```

---

## Dôležité funkcie a metódy

| Funkcia/metóda                           | Popis                                                 |
| ---------------------------------------- | ----------------------------------------------------- |
| `Decimal(x)`                             | Vytvorí desatinné číslo zo stringu alebo čísla        |
| `getcontext().prec = n`                  | Nastaví globálnu presnosť na n číslic                 |
| `quantize()`                             | Zaokrúhli číslo na požadovaný počet desatinných miest |
| `ROUND_HALF_UP, ROUND_DOWN, ROUND_UP...` | Rôzne spôsoby zaokrúhľovania                          |

---

## Zhrnutie

* **`decimal`** je ideálny pre presné a spoľahlivé desatinné výpočty v Pythone.
* Vždy vytvárajte Decimal čísla zo **stringov**.
* Umožňuje nastaviť presnosť a spôsob zaokrúhľovania podľa potreby.
* Vyhnete sa chybám, ktoré by vznikli pri použití klasických floatov.
