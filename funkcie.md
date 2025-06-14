# Zabudované funkcie v Pythone

| Funkcia      | Funkcia  | Funkcia    | Funkcia     |
| ------------ | -------- | ---------- | ----------- |
| abs          | all      | any        | ascii       |
| bin          | bool     | breakpoint | bytearray   |
| bytes        | callable | chr        | classmethod |
| compile      | complex  | delattr    | dict        |
| dir          | divmod   | enumerate  | eval        |
| exec         | filter   | float      | format      |
| frozenset    | getattr  | globals    | hasattr     |
| hash         | help     | hex        | id          |
| input        | int      | isinstance | issubclass  |
| iter         | len      | list       | locals      |
| map          | max      | memoryview | min         |
| next         | object   | oct        | open        |
| ord          | pow      | print      | property    |
| range        | repr     | reversed   | round       |
| set          | setattr  | slice      | sorted      |
| staticmethod | str      | sum        | super       |
| tuple        | type     | vars       | zip         |
| **import**   |          |            |             |


---

# Funkcie

Funkcia je mapovanie nulového alebo viacerých vstupných parametrov na nulový alebo viacerý počet výstupných parametrov.

Výhody používania funkcií:

* organizácia kódu
* zníženie duplicity kódu
* rozkladanie zložitých problémov na jednoduchšie časti
* zvýšenie prehľadnosti kódu
* opätovné použitie kódu
* skrytie informácií

Funkcie v Pythone sú **prvotriedne objekty**. Znamená to, že majú rovnaké postavenie ako iné objekty. Môžu sa priraďovať premenným, ukladať do kolekcií alebo odovzdávať ako argumenty. To prináša do jazyka veľkú flexibilitu.

#### Obsah:

* [Definovanie funkcie](#function-definition)
* [Typy funkcií](#kinds-of-functions)
* [Funkcie tretích strán](#third-party-functions)
* [Inštančné, triedové, obyčajné, vnorené funkcie](#instance-class-plain-inner-functions)
* [Funkcie ako objekty](#functions-are-objects)
* [Rozsah platnosti funkcií](#function-scope)
* [Implicitné hodnoty argumentov](#implicit-arg-value)
* [Rozbalenie (unpacking)](#unpacking)
* [Odkazom vs hodnotou](#passing-by-reference)
* [Globálne premenné](#global-variables)
* [Kľúčové slovo `pass`](#the-pass-keyword)
* [Návratové hodnoty](#returning-values)
* [Ľubovoľný počet argumentov](#arbitrary-number-of-args)
* [Vnorené funkcie](#nested-functions)
* [Odosielanie funkcie ako argumentu](#passing-functions-as-parameters)
* [Redefinícia funkcie](#function-redefinition)
* [Funkcie musia byť definované pred použitím](#no-function-hoisting)
* [Kolekcia funkcií](#collection-of-functions)
* [Uzávery (closures)](#closures)

---

## Definovanie funkcie

Funkcie sa definujú pomocou kľúčového slova `def`.

```python
def cel_to_fahr(c):
    return c * 9/5 + 32

print(cel_to_fahr(100))
```

---

## Typy funkcií

* zabudované (builtin)
* štandardné moduly
* vlastné

```python
from math import sqrt

def cube(x):
    return x * x * x    

print(abs(-1))
print(cube(9))
print(sqrt(81))
```

---

## Funkcie tretích strán

Funkcie definované v externých knižniciach (napr. `numpy`):

```bash
$ pip install numpy
```

```python
import numpy as np

r_vals = np.random.randint(1, 100, 10)
print(r_vals)
```

---

## Inštančné, triedové, obyčajné, vnorené funkcie

Funkcie definované v triedach sa nazývajú **metódy**.

```python
class Info:
    def say(self):
        print('Trieda Info')

class Some:
    @staticmethod
    def f():
        print("statická metóda")

def f():
    print("obyčajná funkcia")

def g():
    def f():
        print("vnorená funkcia")
    f()
```

---

## Funkcie sú objekty

Funkcie sú objekty a majú atribúty ako `__name__`, `__doc__`, atď.

```python
def f():
    """Táto funkcia vypíše správu"""
    return 'f() funkcia'

print(f.__name__)
print(f.__doc__)
```

---

## Rozsah platnosti funkcie

Premenné definované vo funkcii sú **lokálne**:

```python
name = "Jack"

def f():
   name = "Robert"
   print("Vo funkcii:", name)

print("Mimo funkcie:", name)
f()
```

---

## Implicitné hodnoty argumentov

```python
def power(x, y=2):
    r = 1
    for i in range(y):
        r *= x
    return r
```

---

## Rozbalenie (unpacking)

Rozbalenie zoznamu alebo návratových hodnôt:

```python
def fn():
    return [1, 2, 3, 4, 5, 6]

a, *mid, b = fn()
print(a, mid, b)
```

Rozbalenie argumentov:

```python
def fn(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

vals = [1, 2, 3, 4, 5, 6]
fn(*vals)
```

Rozbalenie pomenovaných argumentov (`**kwargs`):

```python
def display(**user):
    for k, v in user.items():
        print(f'{k}: {v}')

display(name='Jone Doe', age=35)
```

---

## Odkazom vs hodnotou

Zoznam (mutable objekt) sa odovzdáva **odkazom**:

```python
n = [1, 2, 3, 4, 5]

def f(x):
    x.pop()
    x.insert(0, 0)
```

---

## Globálne premenné

Premenné definované mimo funkcie sú **globálne**:

```python
name = "Jack"

def f():
   print(name)
```

Použitie `global` na zmenu globálnej premennej:

```python
def f():
   global name
   name = "Robert"
```

---

## Kľúčové slovo `pass`

Používa sa na vytvorenie "prázdnych" funkcií (zatiaľ nedefinovaných):

```python
def f():
    pass
```

---

## Návratové hodnoty

Funkcia vracia hodnotu pomocou `return`. Bez neho vracia `None`.

```python
def cube(x):
    return x * x * x
```

Viacero hodnôt sa vracia ako **n-tica** (tuple):

```python
def stats(x):
    return max(x), min(x), len(x), sum(x)
```

---

## Ľubovoľný počet argumentov

Používa sa `*args`:

```python
def do_sum(*args):
    return sum(args)
```

---

## Vnorené funkcie

```python
def myfun():
    def greet():
        return "pozdrav"
    print(greet())
```

---

## Odovzdanie funkcie ako argumentu

```python
def inc(x): return x + 1
def operate(fun, x): return fun(x)
```

---

## Redefinícia funkcie

Python umožňuje **predefinovať** funkciu (prepíše sa poslednou definíciou):

```python
def showMessage(msg): print("prvý")
def showMessage(msg): print("druhý")  # táto bude platiť
```

---

## Funkcie musia byť definované pred volaním

Python **nepodporuje hoisting** (ako JavaScript):

```python
f1()
def f1(): print("ok")
```

---

## Kolekcia funkcií

Funkcie môžu byť uložené v kolekciách:

```python
a = (f, g, h)
for i in a:
    print(i)
```

---

## Uzávery (Closures)

Uzáver (closure) je funkcia, ktorá má prístup k premenným zo svojej vonkajšej funkcie,
aj po tom, čo táto funkcia skončila.

```python
def create_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

---

### Bežné použitia uzáverov:

* súkromné premenné
* spätné volania (callbacks)
* dekorátory
* memoizácia

---
