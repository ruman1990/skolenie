# 🧩 Python – Moduly

## Čo je modul?

Modul je v podstate **knižnica**, teda súbor funkcií (a ďalšieho kódu), ktorý môžeš includovať do svojich programov. Ide o `.py` súbor, ktorý môžeš importovať .

---

## Vytvorenie modulu

Stačí, ak uložíš svoj kód do súboru s príponou `.py`. Napríklad:

```python
# mymodule.py
def greeting(name):
    print("Hello, " + name)
```


---

## Použitie modulu

Importuješ ho pomocou `import`:

```python
import mymodule

mymodule.greeting("Jonathan")
```

Voláš funkcie cez `modul_názov.funkcia()` 

---

## Premenné v module

Modul okrem funkcií môže obsahovať aj premenné, napr. slovníky, polia:

```python
# mymodule.py
person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

Potom:

````python
import mymodule
print(mymodule.person1["age"])
````

---

## Premenovanie modulu pri importe

Pomocou `as` môžeš zmeniť názov modulu pri importe:

```python
import mymodule as mx
print(mx.person1["age"])
``` 

---

## Vstavané moduly

Python obsahuje množstvo **vstavaných modulov**, ktoré môžeš importovať bez inštalácie, napr.:

```python
import platform
x = platform.system()
print(x)
``` 

---

## Používanie funkcie `dir()`

Funkcia `dir(modul)` ti zobrazí všetky mená (funkcie, premenné, triedy...) definované v module:

```python
import platform
print(dir(platform))
``` 

---

## Výberový import

Ak chceš importovať len konkrétnu časť modulu:

```python
from mymodule import person1
print(person1["age"])
``` 

---

## Ďalšie pojmy

- **Balík (package)**: zoskupenie modulov spolu s `__init__.py`, ktoré umožňuje organizáciu súborov.
- **PIP**: správca balíkov na inštaláciu modulov z PyPI (napr. `pip install requests`).

---

## Príklad: Použitie modulu `requests`

Inštalácia:

````

pip install requests

````

Použitie:

```python
import requests

r = requests.get('https://w3schools.com/python/demopage.htm')
print(r.text)
``` 

---

## Zhrnutie

| Krok                         | Popis |
|------------------------------|-------|
| **definovanie modulu**      | `.py` súbor s kódom |
| **import modulu**           | `import modul_name` alebo `from modul import x` |
| **premenovanie (alias)**    | `import modul as alias` |
| **vstavané moduly**         | napr. `math`, `os`, `platform` |
| **preskúmanie obsahu**      | `dir(modul)` |
| **inštalované balíky**      | pomocou `pip install` |


---

# 🐍 **Python Balíky (Packages)**

---

## Čo je **balík** (package)?

* **Balík** je priečinok obsahujúci súbory s kódom (moduly) a špeciálny súbor `__init__.py`.
* Balíky slúžia na lepšiu **organizáciu kódu** – umožňujú rozdeliť väčší projekt do menších, logických celkov.

---

## Základná štruktúra balíka

```
mojbalik/
│
├── __init__.py      # označuje, že ide o balík
├── modul1.py
├── modul2.py
└── podbalik/
    ├── __init__.py
    └── dalsi_modul.py
```

* **`__init__.py`** – môže byť prázdny, ale musí tam byť!
* **modul1.py, modul2.py** – ľubovoľné Python skripty.

---

## Ako vytvoriť vlastný balík

1. **Vytvor priečinok** s názvom balíka, napr. `mojbalik/`
2. **Pridaj doň súbor** `__init__.py` (stačí aj prázdny)
3. **Pridaj ďalšie `.py` súbory** (moduly) – napr. `kalkulacka.py`, `matematika.py`
4. **Voliteľne** môžeš v balíku vytvárať aj ďalšie podbalíky (priečinky s vlastným `__init__.py`)

---

## Príklad:

### Štruktúra:

```
mojbalik/
├── __init__.py
├── kalkulacka.py
└── matematika.py
```

### Obsah modulov:

**kalkulacka.py**

```python
def sucet(a, b):
    return a + b
```

**matematika.py**

```python
def rozdiel(a, b):
    return a - b
```

---

### Použitie balíka v inom súbore (napr. `main.py`):

```python
from mojbalik.kalkulacka import sucet
from mojbalik.matematika import rozdiel

print(sucet(2, 3))      # Výstup: 5
print(rozsiel(5, 2))    # Výstup: 3
```

---

## Dôležité pojmy

* **Modul:** každý `.py` súbor (napr. `kalkulacka.py`)
* **Balík:** priečinok s `__init__.py`, obsahujúci moduly/podbalíky
* **Podbalík:** balík v balíku (napr. `mojbalik/podbalik/`)

---

## Bonus: Importy v balíkoch

* Z hlavného projektu:

  ```python
  from mojbalik.kalkulacka import sucet
  ```
* Medzi modulmi v balíku môžeš použiť relatívny import:

  ```python
  # v matematika.py
  from .kalkulacka import sucet
  ```

---

## Tip: Ako z balíka spraviť "pip installovateľný" balík?

1. Priprav štruktúru balíka (viď vyššie)
2. Pridaj súbor `setup.py` a ďalšie metadáta
3. Nahraj balík na [PyPI](https://pypi.org/) (návod na [oficiálnej dokumentácii](https://packaging.python.org/en/latest/tutorials/packaging-projects/))

---

## Zhrnutie

* **Balík** = priečinok s `__init__.py`
* **Organizácia:** balíky = skupiny modulov
* **Importy:** `from mojbalik.modul import funkcia`
* **Podbalíky:** možné vnorovať do seba

---

### ✨ Na čo sú balíky dobré?

* Organizácia veľkého projektu
* Opätovné použitie kódu (môžeš ho importovať kdekoľvek)
* Jednoduchšia údržba a testovanie

---

## **Čo je `__init__.py`?**

* Označuje, že priečinok je **balík** (package).
* Spúšťa sa automaticky, keď niekto balík importuje.
* Slúži aj na **nastavenie toho, ako sa bude balík správať pri importe**.

---

## **Čo môže obsahovať `__init__.py`?**

### 1. **Môže byť prázdny**

* Ak ti stačí, že priečinok je balík, nemusíš doň nič písať.

### 2. **Importovanie vecí z iných modulov balíka**

* Uľahčí používateľovi importy.
* Príklad:

  ```python
  from .kalkulacka import sucet
  from .matematika import rozdiel
  ```

  Potom vieš spraviť:

  ```python
  from mojbalik import sucet, rozdiel
  ```

### 3. **Premenné, nastavenia, inicializácie**

* Môžeš nastaviť globálne premenné, načítať konfigurácie, spustiť inicializačný kód.

  ```python
  print("Balík mojbalik sa importoval!")
  konfiguracia = {"autor": "Peter", "verzia": "1.0"}
  ```

### 4. **Definovať `__all__`**

* Určuje, čo sa importuje pri `from mojbalik import *`

  ```python
  __all__ = ['sucet', 'rozdiel']
  ```

### 5. **Triedy, funkcie**

* Môžeš priamo definovať triedy a funkcie, ktoré chceš dať „von“ cez balík.

  ```python
  def pozdrav():
      print("Ahoj z balíka!")
  ```

### 6. **Importovanie podbalíkov**

* Môžeš importovať moduly alebo podbalíky, ktoré sa majú automaticky sprístupniť pri importe hlavného balíka.

---

## **Príklad `__init__.py`**

```python
# mojbalik/__init__.py

from .kalkulacka import sucet
from .matematika import rozdiel

__all__ = ['sucet', 'rozdiel']

print("Balík mojbalik je pripravený!")
```

Potom môžeš v main.py:

```python
from mojbalik import sucet, rozdiel
```

---

## **Zhrnutie**

* `__init__.py` môže byť prázdny, ale môžeš tam aj importovať, definovať premenné, funkcie, inicializačný kód, nastaviť `__all__`, atď.
* Pomáha vytvoriť „vstupnú bránu“ do balíka a uľahčiť jeho použitie.

---
