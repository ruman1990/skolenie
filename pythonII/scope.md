# 🧠 Python – Scope (viditeľnosť premenných)

Premenná je dostupná len v rámci oblasti (scope), kde je vytvorená.

---

## 1. Lokálny rozsah (Local Scope)

Premenná definovaná **vnútri funkcie** patrí do **lokálneho rozsahu** a je dostupná iba v tej funkcii.

```python
def myfunc():
    x = 300
    print(x)

myfunc()
```

> `x` existuje len v `myfunc()` a mimo nej ju nemôžeš použiť .

### Vnorené funkcie

Premenná z funkcie je dostupná aj vo vnútri vnorených (inner) funkcií:

```python
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()
```

> `x` sa dedí do vnútornej funkcie .

---

## 2. Globálny rozsah (Global Scope)

Premenná definovaná **mimo všetkých funkcií** patrí do **globálneho rozsahu** a je dostupná všade – aj v lokálnych kontextoch.

```python
x = 300

def myfunc():
    print(x)

myfunc()
print(x)
```

> `x` je globálna a viditeľná vo funkcii aj mimo nej ([w3schools.com][1]).

### Pozor na premenné s rovnakým menom

Ak vo funkcii použiješ rovnaké meno, stane sa z nej **lokálna premenná**, globálna zostane nezmenená:

```python
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()  # vypíše 200 (lokálne)
print(x)  # vypíše 300 (globálne)
```

> Python nepremení referenciu na globálnu, ak nie je upresnená ako `global` .

---

## 3. Kľúčové slovo `global`

Ak potrebuješ **zmeniť alebo vytvoriť globálnu premennú vo funkcii**, použiješ `global`:

```python
def myfunc():
    global x
    x = 300

myfunc()
print(x)  # vypíše 300
```

Alebo na zmenu už existujúcej globálnej premenné:

```python
x = 300

def myfunc():
    global x
    x = 200

myfunc()
print(x)  # vypíše 200
```

> `global` hovorí: „táto premenná je mimo funkcie“ ([w3schools.com][1]).

---

## 4. Kľúčové slovo `nonlocal`

Používa sa vo **vnorených funkciách**, aby si upravil premennú z **okolia**, nie úplne globálnu:

```python
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())  # vypíše "hello"
```

> `nonlocal` modifikuje premennú z vonkajšej (enclosing) funkcie .

---

## 📝 Zhrnutie

| Scope     | Viditeľnosť                                           | Použité kľúčové slovo |
| --------- | ----------------------------------------------------- | --------------------- |
| Lokálny   | Vo funkcii                                            | –                     |
| Globálny  | Kdekoľvek v module                                    | `global`              |
| Enclosing | Vo vnútornej funkcii mení premennú z okolitej funkcie | `nonlocal`            |


---

# 🌐 Scope Chain (Reťazec viditeľnosti)

Python hľadá premenné v špecifickom poradí nazývanom **LEGB rule**:

* **L**ocal (lokálny)
* **E**nclosing (obklopujúci, z vonkajšej funkcie)
* **G**lobal (globálny)
* **B**uilt-in (vstavaný)

Ak Python nenájde premennú lokálne, hľadá ju postupne vyššie v reťazci.

---

### Príklad: Scope chain v akcii

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # local
    inner()
    print(x)      # enclosing

outer()
print(x)          # global
```

> **Najbližší scope vyhráva!**
> Vo funkcii `inner` má najvyššiu prioritu lokálny `x`.

---

# 🛠️ `locals()` a `globals()`

**`locals()`** vráti slovník lokálnych premenných (v aktuálnom scope).
**`globals()`** vráti slovník všetkých globálnych premenných.

### Príklad:

```python
a = 1
def test():
    b = 2
    print("Locals vo funkcii:", locals())
    print("Globals vo funkcii:", globals().keys())

test()
print("Globals mimo funkcie:", globals().keys())
```

> Vypíšu sa ti všetky dostupné premenné v aktuálnom scope.

---

# 🗂️ Namespaces (Menné priestory)

**Namespace** je „kontajner“ pre mená – napríklad každý modul, funkcia či trieda má vlastný menný priestor.

* **Globálny menný priestor:** premenné na úrovni modulu
* **Lokálny menný priestor:** premenné vo funkciách
* **Built-in menný priestor:** všetky vstavané funkcie (napr. `print`, `len`...)

---

### Príklad: Rôzne menné priestory

```python
def outer():
    msg = "ahoj"
    def inner():
        print(msg)  # msg je z enclosing namespace
    inner()

outer()
```

---

# 🏗️ Built-in scope

Ak premennú nenájdeš nikde vyššie, Python hľadá vo **vstavanom scope**:

```python
print(len([1,2,3]))  # 'len' je built-in
```

> Skús zmeniť meno svojej premennej na `len` a uvidíš, čo sa stane! 😅

---

# 🔄 Príklad na vyskúšanie: Shadowing a reťazec scopu

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        # nonlocal x     # odkomentuj pre zmenu enclosing scope!
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)
```

> Ak použiješ `nonlocal x`, zmeníš hodnotu `x` v „enclosing“ scope namiesto vytvorenia novej v „local“ scope.

---
