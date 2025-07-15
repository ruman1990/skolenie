# 🔍 Python – Regulárne výrazy (RegEx)

RegEx (Regular Expression) je **reťazec znakov**, ktorý tvorí vyhľadávací vzor. Pomocou neho môžeš zistiť, či reťazec obsahuje daný vzor.

---

## 🧩 Modulu `re`

V Pythone existuje zabudovaný modul `re`, ktorý umožňuje pracovať s regulárnymi výrazmi:

```python
import re
```



---

## Základné použitie

### Príklad – kontrola začiatku a konca reťazca:

```python
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```

* `^The` – zodpovedá iba na začiatku reťazca
* `.*` – ľubovoľné znaky (0 alebo viac)
* `Spain$` – ukončenie reťazca


---

## Funkcie modulu `re`

| Funkcia              | Popis                                                               |
| -------------------- | ------------------------------------------------------------------- |
| `findall`            | Nájde **všetky výskyty** a vráti ich ako zoznam                     |
| `search`             | Hľadá **prvé** zhodné miesto a vráti **Match objekt**, alebo `None` |
| `split`              | Rozdelí reťazec podľa vzoru, vráti zoznam častí                     |
| `sub`                | Nahradí výskyty vzoru novým reťazcom                                |


---

## Meta-znaky

Základné meta-znaky v RegEx:

* `[]` – množina znakov, napr. `[a-m]`
* `\` – špeciálna sekvencia / escape znaku
* `.` – ľubovoľný znak (okrem nového riadku)
* `^` – začiatok reťazca
* `$` – koniec reťazca
* `*` – 0 alebo viac výskytov
* `+` – 1 alebo viac výskytov
* `?` – 0 alebo 1 výskyt
* `{}` – presný počet výskytov
* `|` – logická alternatíva (alebo)
* `()` – zoskupovanie či zachytávanie

---

## Vlajky (Flags)

Vlajky upravujú vzor:

* `re.ASCII` alebo `re.A` – iba ASCII zhody
* `re.DEBUG` – debugovacie informácie
* `re.DOTALL` (`re.S`) – `.` zodpovedá aj novým riadkom
* `re.IGNORECASE` (`re.I`) – ignorovanie veľkosti písmen
* `re.MULTILINE` (`re.M`) – `^` a `$` reagujú na začiatok/koniec riadku
* `re.UNICODE` (`re.U`) – Unicode zhody (prednastavené v Pythone 3)
* `re.VERBOSE` (`re.X`) – povolenie komentárov a rozostupov v zápise

---

## Špeciálne sekvencie

* `\A` – na začiatku reťazca
* `\b` – hranica slova
* `\B` – negované `\b`
* `\d` – digit (0–9)
* `\D` – nie digit
* `\s` – biely znak
* `\S` – nie-biely znak
* `\w` – písmeno, číslica alebo \_
* `\W` – negované `\w`
* `\Z` – na konci reťazca


*(Pri `\b` a `\B` je dobré používať surové reťazce, napr. `r"\bain"`)*

---

## Množiny (sets)

Príklady množín:

* `[arn]` – `a`, `r` alebo `n`
* `[a-n]` – malé písmená od `a` do `n`
* `[^arn]` – všetko **okrem** `a`, `r`, `n`
* `[0-9]`, `[0123]`, `[0-5][0-9]`, `[a-zA-Z]`
* `[+]` – doslova `+` (meta-znaky v `[]` sú obyčajné)

---

## Funkcia `findall()`

Vracia **zoznam všetkých výskytov**:

```python
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # ['ai', 'ai']
```

Ak nenájde nič, vráti prázdny zoznam.


---

## Funkcia `search()`

Hľadá **prvý výskyt**, vracia **Match objekt**:

```python
import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print("Pozícia medzery:", x.start())
```

Ak nenájde, vráti `None`.

---

## Funkcia `split()`

Rozdelí reťazec podľa vzoru:

```python
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
# alebo
x = re.split("\s", txt, 1)  # iba prvý deliteľ
```

---

## Funkcia `sub()`

Nahradí výskyty vzoru:

```python
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)        # nahradí všetky medzery
x = re.sub("\s", "9", txt, 2)     # iba prvé dve
```



---

## 🧩 Match objekt

Ak `search()` nájde zhodu, vráti **Match objekt** s metódami:

* `.span()` –  `(start, end)` pozície
* `.string` – pôvodný reťazec
* `.group()` – presná zhoda

### Príklad:

```python
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
```

Ak nie je zhoda, `x` je `None`.


---
```python
import re

txt = "The rain in Spain stays mainly in the plain."

# nájde všetky slová končiace na 'ain'
vzor = r"\b\w*ain\b"

for match in re.finditer(vzor, txt):
    print(f"Zhoda: {match.group()} na pozíciách {match.span()}")
```


---

## 🔍 `re.match(pattern, string)`

* Skúša zhodu **iba na začiatku reťazca**
* Ak vzor nesedí hneď na začiatku, vracia `None`

### ✅ Príklad:

```python
import re

print(re.match(r"abc", "abcdef"))  # ✅ zhoda na začiatku
print(re.match(r"abc", "123abc"))  # ❌ None – nezačína na 'abc'
```

---

## 🔒 `re.fullmatch(pattern, string)`

* Skúša, či **celý reťazec presne zodpovedá** regulárnemu výrazu
* Ak je čo i len 1 znak navyše, vracia `None`

### ✅ Príklad:

```python
print(re.fullmatch(r"\d+", "12345"))    # ✅ celé sú len čísla
print(re.fullmatch(r"\d+", "123abc"))   # ❌ obsahuje aj písmená
print(re.fullmatch(r"\d+", "123\n"))    # ❌ nový riadok navyše
```

---

## 🔁 Porovnanie:

| Funkcia          | Kde hľadá zhodu                    |
| ---------------- | ---------------------------------- |
| `re.search()`    | kdekoľvek v reťazci (najčastejšie) |
| `re.match()`     | iba na **začiatku** reťazca        |
| `re.fullmatch()` | iba ak **celý reťazec** zodpovedá  |

---

## 🧪 Praktický príklad:

```python
import re

text = "abc123"

# Skúsme rôzne prístupy
print("search:", re.search(r"\d+", text))       # ✅ nájde 123
print("match:", re.match(r"\d+", text))         # ❌ None – nezačína číslom
print("fullmatch:", re.fullmatch(r"\d+", text)) # ❌ None – obsahuje aj písmená
```

---

## ✅ Kedy použiť:

| Potrebuješ...                         | Funkcia         |
| ------------------------------------- | --------------- |
| Nájsť niečo **kdekoľvek v texte**     | `search()` ✅    |
| Overiť, či reťazec **začína na vzor** | `match()`       |
| Overiť, či reťazec **presne sedí**    | `fullmatch()` ✅ |

---


## ✅ Ako nastavovať flagy

### 1. **Priamo vo funkcii (napr. `re.search`)**:

```python
import re

text = "Hello\nworld"

# re.IGNORECASE = nerieši veľké/malé písmená
x = re.search(r"hello", text, flags=re.IGNORECASE)
print(x.group())  # Hello
```

### 2. **Cez `re.compile()` – ak regex používaš opakovane**:

```python
pattern = re.compile(r"hello", flags=re.IGNORECASE)
match = pattern.search("Hello")
print(match.group())
```

### 3. **Inline flagy (vnorené do regulárneho výrazu)**

```python
re.search(r"(?i)hello", "HELLO")  # (?i) = ignorecase
```

---

## 📋 Prehľad najčastejších flagov

| Flag            | Skratka | Význam                                                   |
| --------------- | ------- | -------------------------------------------------------- |
| `re.IGNORECASE` | `re.I`  | Nerieši veľké/malé písmená (case-insensitive)            |
| `re.MULTILINE`  | `re.M`  | `^` a `$` platia pre **každý riadok**, nie len celý text |
| `re.DOTALL`     | `re.S`  | `.` zachytí aj `\n` (inak nie)                           |
| `re.VERBOSE`    | `re.X`  | Povolené medzery a komentáre v regexe                    |
| `re.ASCII`      | `re.A`  | `\w`, `\d`, `\s` sa správajú ako v ASCII                 |

---

## 🧪 Príklady použitia:

### 🔁 `re.MULTILINE`:

```python
text = "abc\n123"

print(re.findall(r"^\d+", text))             # nič, ^ = začiatok celého reťazca
print(re.findall(r"^\d+", text, re.MULTILINE))  # nájde '123' na druhom riadku
```

---

### 🕳️ `re.DOTALL`:

```python
text = "Hello\nWorld"

print(re.search(r"Hello.*World", text))              # ❌ None – . nezachytí \n
print(re.search(r"Hello.*World", text, re.DOTALL))   # ✅ nájde
```

---

### ✍️ `re.VERBOSE` – čitateľný regex

```python
pattern = re.compile(r"""
    ^\d{3}      # predčíslie
    -           # pomlčka
    \d{2}       # číslo
    $           # koniec
""", re.VERBOSE)

print(pattern.fullmatch("123-45"))  # ✅
```

---

## ✅ Kombinovanie flagov:

```python
re.search(r"hello", "HELLO\nworld", flags=re.I | re.M)
```

alebo:

```python
re.compile(r"...", flags=re.S | re.X)
```

---
