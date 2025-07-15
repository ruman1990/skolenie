# Python – Triedy a objekty

## Python Classes/Objects

Python je objektovo orientovaný programovací jazyk. Takmer všetko v Pythone je objekt, s vlastnosťami a metódami.

Trieda je ako konštruktor objektov, alebo "matrica" na vytváranie objektov.

---

## Vytvorenie triedy

Na vytvorenie triedy použite kľúčové slovo `class`:

```python
class MyClass:
    x = 5
```

---

## Vytvorenie objektu

Teraz môžeme použiť triedu `MyClass` na vytvorenie objektu:

```python
p1 = MyClass()
print(p1.x)
```

---

## Funkcia `__init__()`

Predchádzajúce ukážky sú veľmi jednoduché. V skutočných aplikáciách sa bežne používa špeciálna metóda `__init__()`, ktorá sa automaticky volá pri vytváraní inštancie:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
```

Metódu `__init__()` používame na inicializáciu vlastností objektu.&#x20;

---

## Funkcia `__str__()`

Metóda `__str__()` určuje, čo sa vráti, keď objekt reprezentujeme ako reťazec:

**Bez `__str__()`**:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1)  # napr. <__main__.Person object at 0x...>
```

**S `__str__()`**:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)  # John(36)
```

---

## Metódy objektu

Objekty môžu tiež obsahovať metódy, čo sú funkcie patriace inštanciám:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()  # Hello my name is John
```

Parameter `self` je odkaz na aktuálnu inštanciu triedy.

---

## Parameter `self`

Parameter `self` nemusí byť pomenovaný práve tak, ale musí byť prvým parametrom:

```python
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```

---

## Zmena vlastností objektu

Môžete zmeniť hodnotu vlastnosti objektu:

```python
p1.age = 40
```

---

## Vymazanie vlastností objektu

Rovnako môžete vlastnosti odstrániť pomocou `del`:

```python
del p1.age
```

---

## Vymazanie objektu

Na odstránenie celej inštancie použite `del`:

```python
del p1
```

---

## Výraz `pass`

Ak potrebujete definovať triedu, ktorá je zatiaľ prázdna, použite `pass`:

```python
class Person:
    pass
```

---
