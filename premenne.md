# Základy Pythonu: Premenné, literály, operátory a odsadenie

Tento dokument je určený pre začiatočníkov, ktorí sa učia jazyk Python. Prejdeme si spoločne najzákladnejšie koncepty: premenné, konvencie pomenovania, literály, operátory a odsadenie (indentáciu).

---

## Premenné v Pythone

Premenná je pomenovaná referencia na hodnotu. V Pythone sa premenné vytvárajú jednoducho:

```python
a = 5
meno = "Jana"
pi = 3.14159
```

Python je **dynamicky typovaný jazyk**, čo znamená, že nemusíme deklarovať typ premenné dopredu. Typ sa odvodzuje automaticky z hodnoty.

```python
cislo = 42         # int
text = "ahoj"      # str
hodnota = True     # bool
```

### Neexistujúce konštanty

V Pythone nie je oficiálny mechanizmus pre tvorbu konštant.
Zvykovo sa konštanty zapisujú VEĽKÝMI PÍSMENAMI:

```python
PI = 3.14159
DNI_V_TYŽDNI = 7
```

Tento štýl je len dohodnutý, a konštanty môže program meniť (aj keď by nemal).

---

## Konvencie pomenovania premenných

Python nemá prísne pravidlá pre pomenovanie premenných, ale používajú sa štandardné konvencie:

* `snake_case` – preferovaný štýl v Pythone
* `camelCase` – bežne používaný v iných jazykoch, v Pythone menej
* `PascalCase` – používa sa na pomenovanie tried

### Príklady:

```python
pocet_studentov = 25      # snake_case
menoPouzivatela = "Eva"   # camelCase – neodporúčané
TridaAuto = "Tesla"        # PascalCase – pre triedy
```

---

## Literály

Literál je pevná hodnota priamo v kóde. Napríklad:

* **Čelé čísla**: `10`, `-3`
* **Desatinné čísla**: `3.14`, `0.0`
* **Reťazce**: `'ahoj'`, `"svet"`
* **Boolovské hodnoty**: `True`, `False`

---

## Operátory

Python podporuje klasické typy operátorov:

### Aritmetické operátory:

| Operátor | Popis               | Príklad         |
| -------- | ------------------- | --------------- |
| `+`      | sčítanie            | `3 + 2` = `5`   |
| `-`      | odčítanie           | `7 - 4` = `3`   |
| `*`      | násobenie           | `2 * 5` = `10`  |
| `/`      | delenie             | `8 / 2` = `4.0` |
| `//`     | celočíselné delenie | `7 // 2` = `3`  |
| `%`      | zvyšok po del.      | `9 % 4` = `1`   |
| `**`     | mocnenie            | `2 ** 3` = `8`  |

### Porovnávacie operátory:

| Operátor | Popis              |
| -------- | ------------------ |
| `==`     | rovnosť            |
| `!=`     | nerovnosť          |
| `>`      | väčšie ako         |
| `<`      | menšie ako         |
| `>=`     | väčšie alebo rovné |
| `<=`     | menšie alebo rovné |

---

## Odsadenie (indentácia)

V iných jazykoch sa bloky kódu ohraničujú zloženými zátvorkami `{}`.
V Pythone sa používa **odsadenie pomocou medzier alebo tabulátorov**.

Odporúané je používať **4 medzery** na jedno odsadenie.

### Príklad:

```python
vek = 18
if vek >= 18:
    print("Máš plnolety vek")
    print("Môžeš voliť")
else:
    print("Ešte si mladý")
```

Ak by sme vynechali odsadenie, program skončí chybou `IndentationError`.


# Kľúčové slová v Pythone

| Kľúčové slovo | Kľúčové slovo | Kľúčové slovo | Kľúčové slovo |
|---------------|---------------|---------------|---------------|
| False         | None          | True          | and           |
| as            | assert        | async         | await         |
| break         | class         | continue      | def           |
| del           | elif          | else          | except        |
| finally       | for           | from          | global        |
| if            | import        | in            | is            |
| lambda        | nonlocal      | not           | or            |
| pass          | raise         | return        | try           |
| while         | with          | yield         |               |


Ak chcete získať tento zoznam priamo v Pythone, môžete použiť:

```python
import keyword
print(keyword.kwlist)


Jasné! Tu máš **prehľad, ako komentovať kód v Pythone**, stručne a prehľadne:

---

## 📝 Typy komentárov v Pythone

Python má 2 hlavné typy komentárov:

### 1. **Jednoriadkové komentáre**

Používajú znak `#`.

```python
# Toto je komentár
x = 10  # Nastavíme premennú x na hodnotu 10
```

### 2. **Viacriadkové komentáre (technicky viacero #)**

V Pythone neexistuje špeciálna syntax na blok komentárov – jednoducho použiješ viacero riadkov so znakom `#`.

```python
# Toto je viacriadkový komentár
# ktorý vysvetľuje zložitejší kód
# alebo popisuje funkciu.
```

---

## 📚 Docstring (dokumentačný reťazec)

Používa sa na dokumentovanie **funkcií, tried alebo modulov**. Je to špeciálny reťazec uzavretý v trojitých úvodzovkách `"""`.

```python
def vypocitaj_obsah_kruhu(r):
    """
    Vypočíta obsah kruhu so zadaným polomerom.
    
    Parametre:
        r (float): polomer kruhu
        
    Návratová hodnota:
        float: obsah kruhu
    """
    from math import pi
    return pi * r ** 2
```

✅ Tento docstring si môže prečítať aj funkcia `help()`:

```python
help(vypocitaj_obsah_kruhu)
```

---

## 🔍 Zhrnutie

| Typ           | Syntax              | Použitie                             |
| ------------- | ------------------- | ------------------------------------ |
| Jednoriadkový | `# Komentár`        | Rýchle poznámky k riadku kódu        |
| Viacriadkový  | viacero `#` riadkov | Vysvetlenie blokov kódu              |
| Docstring     | `""" popis """`     | Dokumentácia funkcie, triedy, modulu |

---

## ✅ Odporúčania pre komentovanie

* **Komentuj len tam, kde je to potrebné.**
* Komentár má **vysvetliť „prečo“**, nie len „čo“:

  ```python
  # Zrýchlime výpočet cache-ovaním výsledkov
  ```
* Používaj **angličtinu**, ak je projekt medzinárodný. Inak môžeš pokojne po slovensky.
* Docstring by mal byť **v každej funkcii a triede**.

---

Toto bol rýchly úvod do základov Pythonu. Pokračujeme v ďalších kapitolách so vstupmi, funkciami a prácou s dátami ✔️.
