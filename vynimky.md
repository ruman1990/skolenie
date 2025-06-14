# 🧨 Výnimky

Chyby zistené počas vykonávania programu sa nazývajú **výnimky** (`exceptions`).

Príklady:

* plný disk
* logické chyby
* syntaktická chyba
* nedostatočné oprávnenia

`Warnings` sú upozornenia generované počas kompilácie alebo vykonávania kódu. Na rozdiel od výnimiek:

* **neprerušujú vykonávanie programu**
* upozorňujú na potenciálne problémy (napr. zastarané funkcie, nepoužité premenné, nezhody typov)

---

## 🛠️ Ošetrovanie výnimiek

```python
try:
   # vykonaj niečo

except ValueError:
   # spracuj výnimku typu ValueError

except (IndexError, ZeroDivisionError):
   # spracuj viacero výnimiek

except:
   # spracuj všetky ostatné výnimky

finally:
   # uvoľnenie zdrojov
```

---

## 📋 Zoznam základných výnimiek

| Výnimka             | Vysvetlenie                                    |
| ------------------- | ---------------------------------------------- |
| `ZeroDivisionError` | delenie nulou                                  |
| `NameError`         | neexistujúci názov premennej                   |
| `IndentationError`  | zlá odsadenosť v kóde                          |
| `IOError`           | chyba pri I/O operácii (napr. súbor nenájdený) |
| `EOFError`          | neočakávaný koniec súboru                      |
| `TypeError`         | nesprávny typ pre operáciu                     |
| `ValueError`        | správny typ, ale nevhodná hodnota              |
| `IndexError`        | index mimo rozsah                              |
| `KeyError`          | chýbajúci kľúč v slovníku                      |
| `AttributeError`    | neexistujúci atribút                           |
| `ImportError`       | zlyhaný import modulu                          |
| `AssertionError`    | neúspešné `assert` vyhlásenie                  |
| `RuntimeError`      | všeobecná chyba počas behu                     |
| `MemoryError`       | nedostatok pamäte                              |
| `FileNotFoundError` | špecifická `IOError`, súbor neexistuje         |
| `PermissionError`   | nedostatok oprávnení                           |
| `OverflowError`     | výsledok operácie je príliš veľký              |
| `RecursionError`    | prekročená maximálna hĺbka rekurzie            |
| `SystemExit`        | vyvolaná `sys.exit()`                          |
| `KeyboardInterrupt` | prerušenie používateľom (napr. Ctrl+C)         |

---

## 🔁 Funkcie vracajúce chyby

Niektoré jazyky ako C, Go a Rust **nepoužívajú výnimky**, ale **vracajú chyby z funkcií**:

**Príklad v Go:**

```go
content, err := ioutil.ReadFile("subor.txt")

if err != nil {
    log.Fatal(err)
}

fmt.Println(string(content))
```

---

## ❌ `ValueError` – neplatná hodnota

```python
try:
    x = int(input("Zadaj číslo: "))
    y = int(input("Zadaj ďalšie číslo: "))

    print(f'súčet: {x + y}')
    print(f'násobok: {x * y}')

except ValueError:
    print("neplatné číslo")
```

---

## 🧾 Výnimkový objekt

```python
except ValueError as e:
    print("neplatné číslo")
    print(e)  # výpis chybovej správy
```

---

## ➗ `ZeroDivisionError` – delenie nulou

```python
try:
    print(f"{x} / {y} = {x/y}")
except ZeroDivisionError:
    print("Nulou deliť nemožno")
```

### Oprava cez podmienku:

```python
if y == 0:
    print("Nulou deliť nemožno")
    sys.exit(1)
```

---

## 📦 `IndexError` – index mimo rozsah

```python
words = ['slovo1', 'slovo2']
r_idx = random.randint(0, len(words))  # chyba: môže vygenerovať mimo rozsah
```

➡️ Oprava: `random.randint(0, len(words) - 1)`

---

## 🧮 `TypeError` – zlý typ

```python
n = [1, 2, 3]

try:
    print(n[1])
    print(n['2'])  # chyba

except TypeError as e:
    print("Chyba:", e)
```

---

## 🔄 `ImportError` – import zlyhal

```python
try:
    import requests
except ImportError:
    print("Nainštaluj knižnicu 'requests'")
    sys.exit(1)
```

---

## 🔥 `OverflowError` – príliš veľký výsledok

```python
try:
    f = 3.0
    for _ in range(100):
        f = f ** 2
        print(f)
except OverflowError as err:
    print("Pretečenie:", err)
```

---

## ⚠️ `raise` – vyvolanie výnimky

```python
if age < 0:
    raise ValueError("Neplatný vek")
```

---

## 👤 Vlastná výnimka

```python
class InvalidAgeError(Exception):
    def __str__(self):
        return "Neplatný vek"
```

Použitie:

```python
if age < 0:
    raise InvalidAgeError()
```

---

## 🎯 Viac výnimiek

```python
except (RuntimeError, ValueError, ZeroDivisionError) as e:
    print(type(e).__name__, e)
```

S `match`:

```python
match e:
    case RuntimeError():
        print("Zlý operátor")
```

---

## 🧹 `finally` blok

Vždy sa vykoná – napr. zatvorenie súboru:

```python
finally:
    if f:
        f.close()
```

---

## 📚 `with` – automatické spravovanie zdrojov

```python
with open('subor.txt', 'r') as f:
    obsah = f.readlines()
```

---

## 🚫 Len jedna výnimka sa chytí

```python
for e in exceptions:
    raise e  # iba prvá sa spracuje
```

---

## 🧵 Viacnásobné výnimky v paralelizme – `except*` (Python 3.11+)

```python
try:
    raise ExceptionGroup("Chyby", [TypeError(), IndexError()])
except* TypeError:
    print("Chyba typu")
```

---

## 🪵 Logovanie výnimiek

```python
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

try:
    raise RuntimeError("Chyba")
except Exception as e:
    logging.error(f'Chyba: {e}')
```

---
