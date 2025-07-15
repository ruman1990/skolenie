## 1. Prepísanie (override) metódy

**Vysvetlenie:**
Ak má potomkovská trieda metódu s rovnakým názvom ako rodič, táto metóda rodiča sa „prepíše“ (override).

```python
class Animal:
    def speak(self):
        print("Zviera vydáva zvuk")

class Dog(Animal):
    def speak(self):
        print("Hav hav!")

a = Animal()
a.speak()  # Zviera vydáva zvuk

d = Dog()
d.speak()  # Hav hav!
```

> **Pes** dedí od **Animal**. Vlastnou metódou `speak()` prepíše tú z rodiča.

---

## 2. Viacdedičnosť (Multiple Inheritance)

**Vysvetlenie:**
Trieda môže dediť od viacerých rodičov naraz a získať tak vlastnosti a metódy zo všetkých.

```python
class Flyer:
    def fly(self):
        print("Letím vo vzduchu!")

class Swimmer:
    def swim(self):
        print("Plávam vo vode!")

class Duck(Flyer, Swimmer):
    pass

kacka = Duck()
kacka.fly()   # Letím vo vzduchu!
kacka.swim()  # Plávam vo vode!
```

> **Duck** dedí od **Flyer** aj **Swimmer**, takže môže volať metódy z oboch.

---

## 3. Použitie `super()` v prepísanej metóde

**Vysvetlenie:**
Pomocou `super()` vieš v prepísanej metóde zavolať pôvodnú (rodičovskú) verziu metódy.

```python
class A:
    def do(self):
        print("A robí niečo")

class B(A):
    def do(self):
        print("B robí niečo navyše")
        super().do()  # zavolá A.do()

b = B()
b.do()
# Výstup:
# B robí niečo navyše
# A robí niečo
```

> **B** rozšíri funkcionalitu metódy `do()` rodiča **A**.

---

## 4. Kontrola typu a dedičnosti

**Vysvetlenie:**
Pomocou funkcií `isinstance()` a `issubclass()` vieš overiť typ objektu alebo dedičnosť tried.

```python
print(isinstance(d, Dog))       # True
print(isinstance(d, Animal))    # True
print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
```

> `isinstance()` zisťuje, či je objekt inštanciou triedy alebo jej potomka.
> `issubclass()` zisťuje, či trieda dedí z inej triedy.

---

## 5. Dedičnosť so vstavanými triedami

**Vysvetlenie:**
Aj vstavané typy môžeš rozšíriť (napríklad `list`) a pridať im vlastné metódy.

```python
class MyList(list):
    def sum(self):
        return sum(self)

m = MyList([1, 2, 3])
print(m.sum())  # 6
```

> **MyList** dedí zo zabudovanej triedy **list** a pridáva vlastnú metódu `sum()`.

---

## 6. Príklad hierarchie

**Vysvetlenie:**
Ukážka „stromu“ dedičnosti, kde každá podtrieda prepíše metódu podľa vlastného správania.

```python
class Vehicle:
    def move(self):
        print("Presúvam sa...")

class Car(Vehicle):
    def move(self):
        print("Idem po ceste.")

class Boat(Vehicle):
    def move(self):
        print("Plávam na vode.")

v = Vehicle()
c = Car()
b = Boat()
v.move()  # Presúvam sa...
c.move()  # Idem po ceste.
b.move()  # Plávam na vode.
```

> **Car** aj **Boat** dedí od **Vehicle**, ale každá si prispôsobí metódu `move()`.

---

## 7. Abstraktné triedy

**Vysvetlenie:**
Abstraktná trieda je trieda, ktorú nemožno priamo inštancovať – slúži ako základ pre ďalšie triedy a môže obsahovať abstraktné (neimplementované) metódy, ktoré potomkovia **musia** implementovať.
V Pythone sa na to používa modul `abc` a dekorátor `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Hav hav!")

class Cat(Animal):
    def speak(self):
        print("Mňau!")

# animal = Animal()  # Toto spôsobí chybu: Can't instantiate abstract class
dog = Dog()
dog.speak()  # Hav hav!
cat = Cat()
cat.speak()  # Mňau!
```

> **Animal** je abstraktná trieda. Každý potomok **musí** implementovať metódu `speak()`. Nemožno vytvoriť priamo inštanciu abstraktnej triedy.

---

## 8. Vlastnosti (property)

**Vysvetlenie:**
`property` umožňuje definovať špeciálne atribúty, ku ktorým sa pristupuje ako ku premenným, ale v skutočnosti používajú metódy na získanie (getter), nastavenie (setter) alebo odstránenie (deleter) hodnoty.

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Získavam meno...")
        return self._name

    @name.setter
    def name(self, value):
        print("Nastavujem meno...")
        if not value:
            raise ValueError("Meno nemôže byť prázdne!")
        self._name = value

    @name.deleter
    def name(self):
        print("Mazem meno...")
        del self._name

p = Person("Janko")
print(p.name)     # Získavam meno... \n Janko
p.name = "Martin" # Nastavujem meno...
print(p.name)     # Získavam meno... \n Martin
del p.name        # Mazem meno...
```

> **Person** používa `property` na bezpečné čítanie, zapisovanie a mazanie hodnoty `_name`.
> Takto môžeš pridávať validáciu a iné logiky pri prístupe k atribútom.

---


## 9. Statická metóda (`@staticmethod`)

**Vysvetlenie:**
Statická metóda je metóda, ktorá **nepristupuje ku žiadnym vlastnostiam triedy ani inštancie**. Je to v podstate „obyčajná“ funkcia, ale zaradená v rámci triedy kvôli logickej štruktúre.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(3, 5))  # 8
```

> **Statickú metódu** môžeš volať bez vytvorenia inštancie triedy. Nepotrebuje parameter `self` ani `cls`.

---

## 10. Triedna metóda (`@classmethod`)

**Vysvetlenie:**
Triedna metóda **pracuje s triedou**, nie s konkrétnou inštanciou. Ako prvý parameter dostáva `cls` (odkaz na triedu).

```python
class Person:
    people_count = 0

    def __init__(self, name):
        self.name = name
        Person.people_count += 1

    @classmethod
    def how_many(cls):
        print(f"Počet ľudí: {cls.people_count}")

Person("Anna")
Person("Miro")
Person.how_many()  # Počet ľudí: 2
```

> **Triedna metóda** má prístup ku „shared“ vlastnostiam triedy (napr. počítadlo objektov).

---

## 11. Ochrana dát (private, protected)

**Vysvetlenie:**
V Pythone neexistuje striktné súkromie premenných ako v iných jazykoch, ale používa sa zápis s podčiarkovníkmi:

* `_attribut` – **protected** (chránený): Dohodnuté, že je to len pre interné použitie.
* `__attribut` – **private** (súkromný): Python meno „name-mangluje“, takže sa k nemu nedá bežne dostať.

```python
class Demo:
    def __init__(self):
        self.public = "verejné"
        self._protected = "chránené"
        self.__private = "súkromné"

d = Demo()
print(d.public)      # verejné
print(d._protected)  # chránené (ale je to len odporúčanie)
# print(d.__private) # AttributeError: 'Demo' object has no attribute '__private'
print(d._Demo__private)  # súkromné (takto sa vieš dostať ku 'private', ale nie je to odporúčané)
```

> **Súkromné** a **chránené** vlastnosti slúžia na signalizáciu programátorovi, že by sa nemali používať priamo mimo triedy.

---

## 12. Malý praktický miniprojekt

### Príklad: Správa účtov v banke

**Vysvetlenie:**
Ukážeme použitie dedičnosti, property, ochrany dát, statickej aj triednej metódy.

```python
class Account:
    _account_counter = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        Account._account_counter += 1

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Nedostatok prostriedkov!")
        else:
            self._balance -= amount

    @classmethod
    def how_many_accounts(cls):
        print(f"Počet účtov: {cls._account_counter}")

    @staticmethod
    def bank_info():
        print("Bankové služby 24/7.")

class SavingsAccount(Account):
    def add_interest(self, rate):
        self._balance *= (1 + rate/100)

# Použitie:
a1 = Account("Ján", 100)
a2 = SavingsAccount("Eva", 200)
a2.add_interest(5)
print(a2.balance)  # 210.0
a2.withdraw(300)   # Nedostatok prostriedkov!
Account.how_many_accounts()  # Počet účtov: 2
Account.bank_info()  # Bankové služby 24/7.
```


| Dekorátor       | Prvý argument | Prístup k inštancii | Prístup k triede |
| --------------- | ------------- | ------------------- | ---------------- |
| Žiadny (`def`)  | self          | Áno                 | Áno              |
| `@classmethod`  | cls           | Nie                 | Áno              |
| `@staticmethod` | nič           | Nie                 | Nie              |

---



V Pythone môžeš „prekryť“ (prepísať) množstvo **špeciálnych metód** — nazývajú sa aj **dunder metódy** (double underscore, ako `__init__`, `__eq__` atď.). Tie umožňujú objektom správať sa ako vstavané typy (čísla, reťazce, zoznamy, atď.).

Tu je **prehľad najdôležitejších a najbežnejších špeciálnych metód**, ktoré môžeš prepísať:

---

### 🛠️ **KONŠTRUKCIA A IDENTITA**

| Metóda     | Účel                                            |
| ---------- | ----------------------------------------------- |
| `__init__` | Inicializácia objektu po vytvorení              |
| `__new__`  | Vytvorenie novej inštancie (zriedkavé použitie) |
| `__del__`  | Volané pri zániku objektu (ako deštruktor)      |
| `__repr__` | Oficiálny textový výstup (napr. v konzole)      |
| `__str__`  | Užívateľsky prívetivý výstup (napr. `print()`)  |
| `__hash__` | Hash hodnota objektu (napr. pre `set`, `dict`)  |
| `__eq__`   | `==` porovnanie                                 |
| `__ne__`   | `!=` porovnanie                                 |
| `__lt__`   | `<` menší než                                   |
| `__le__`   | `<=` menší alebo rovný                          |
| `__gt__`   | `>` väčší než                                   |
| `__ge__`   | `>=` väčší alebo rovný                          |

---

### 🔢 **ARITMETICKÉ OPERÁTORY**

| Metóda         | Operácia   |
| -------------- | ---------- |
| `__add__`      | `+`        |
| `__sub__`      | `-`        |
| `__mul__`      | `*`        |
| `__truediv__`  | `/`        |
| `__floordiv__` | `//`       |
| `__mod__`      | `%`        |
| `__pow__`      | `**`       |
| `__neg__`      | Unárne `-` |

---

### 📦 **KOLEKCIE (SEKVENCIE, MAPPINGY)**

| Metóda         | Účel                             |
| -------------- | -------------------------------- |
| `__len__`      | `len(obj)`                       |
| `__getitem__`  | Indexovanie: `obj[i]`            |
| `__setitem__`  | Priradenie hodnoty: `obj[i] = x` |
| `__delitem__`  | Zmazanie položky: `del obj[i]`   |
| `__iter__`     | Iterácia (napr. vo `for` slučke) |
| `__next__`     | Ďalší prvok pri iterácii         |
| `__contains__` | `x in obj`                       |

---

### 💬 **VOLATEĽNOSŤ A KONVERZIE**

| Metóda                            | Účel                        |
| --------------------------------- | --------------------------- |
| `__call__`                        | Volanie objektu ako funkcie |
| `__bool__`                        | Bool hodnota (`if obj:`)    |
| `__int__`, `__float__`, `__str__` | Konverzie                   |

---

### 🧰 **KONTEXTY (s `with`)**

| Metóda      | Účel                     |
| ----------- | ------------------------ |
| `__enter__` | Na začiatku `with` bloku |
| `__exit__`  | Na konci `with` bloku    |

---

### 🧪 Príklad: Trieda s niekoľkými prepísanými metódami

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        return abs(self.x) + abs(self.y)
```

---
