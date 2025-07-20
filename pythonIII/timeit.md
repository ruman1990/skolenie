## Modul `timeit` v Pythone

### Na čo slúži `timeit`?

Modul `timeit` v Pythone slúži na **meranie času vykonávania malých kúskov kódu**. Pomáha nám objektívne porovnávať, ktorá verzia algoritmu alebo funkcie je rýchlejšia. Je to veľmi užitočné najmä pri optimalizácii výkonu.

### Prečo nepoužívať len `time`?

Je možné merať čas aj pomocou modulu `time`, napríklad:

```python
import time
start = time.time()
# ... nejaký kód ...
end = time.time()
print(end - start)
```

Tento spôsob ale môže byť nepresný kvôli iným procesom na počítači alebo rýchlym operáciám, kde rozdiel je veľmi malý. **`timeit`** opakovane spúšťa kód a vypočíta priemerný čas, čím je meranie presnejšie.

---

### Základné použitie

#### 1. Použitie priamo v skripte

Najjednoduchšie použitie je cez funkciu **`timeit.timeit()`**:

```python
import timeit

# Meranie jednoduchého príkazu
čas = timeit.timeit("x = 2 + 2")
print(čas)
```

Tento príkaz vykoná výraz `"x = 2 + 2"` **miliónkrát** (predvolene `number=1000000`) a vráti celkový čas v sekundách.

#### 2. Meranie funkcie

Ak chceme merať vlastnú funkciu, môžeme ju importovať cez `setup` parameter:

```python
import timeit

def sucet():
    return sum(range(100))

čas = timeit.timeit("sucet()", setup="from __main__ import sucet", number=10000)
print(čas)
```

* `setup` obsahuje kód, ktorý sa vykoná len raz na začiatku (napr. importy alebo definície funkcií).
* `number` určuje, koľkokrát sa kód má opakovať.

---

### Použitie z príkazového riadku

Modul `timeit` sa dá spustiť aj priamo z terminálu:

```bash
python -m timeit "x = 2 + 2"
```

---

### Praktické tipy

* Pri meraní vždy opakujte test viackrát (`number`) a použite rovnaké podmienky.
* Porovnávajte len krátke, jednoduché kúsky kódu (napr. rôzne spôsoby sčítania, triedenia).
* Pri porovnávaní funkcií je dobré mať identické vstupné dáta.

---

### Príklad: Porovnanie dvoch spôsobov vytvorenia zoznamu

```python
import timeit

# Pomocou cyklu
čas1 = timeit.timeit('lst = []\nfor i in range(100): lst.append(i)', number=10000)

# Pomocou generátora (list comprehension)
čas2 = timeit.timeit('lst = [i for i in range(100)]', number=10000)

print("Cyklus:", čas1)
print("List comprehension:", čas2)
```

---

### Zhrnutie

* `timeit` je štandardný modul na presné meranie rýchlosti kódu.
* Spúšťa kód veľakrát a vypočíta priemerný čas.
* Je užitočný pri optimalizácii a porovnávaní rôznych riešení.

---
