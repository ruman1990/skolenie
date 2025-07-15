# Python – Dedičnosť (Inheritance)

Dedičnosť nám umožňuje definovať triedu, ktorá **dedi všetky metódy a vlastnosti** z inej triedy.
**Rodičovská trieda** (parent class) je tá, od ktorej dedíme, nazývaná aj **základná trieda** (base class).
**Potomkovská trieda** (child class) je tá, ktorá dedí, nazývaná aj **odvodená trieda** (derived class).

---

## Vytvorenie rodičovskej triedy

Každá trieda môže byť rodičovskou triedou:

```python
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Vytvorenie objektu triedy Person a volanie metódy:
x = Person("John", "Doe")
x.printname()
```

---

## Vytvorenie potomkovej triedy

Ak chceme vytvoriť triedu, ktorá dedí funkčnosť z inej triedy:

```python
class Student(Person):
    pass
```

Používame `pass`, ak nechceme pridávať žiadne ďalšie vlastnosti alebo metódy.
Teraz trieda `Student` má všetky vlastnosti a metódy triedy `Person`.

```python
x = Student("Mike", "Olsen")
x.printname()
```

---

## Pridanie `__init__()` funkcie do potonda

Keď pridáme vlastný `__init__()`, **prepíšeme** rodičovský konštruktor:

```python
class Student(Person):
    def __init__(self, fname, lname):
        # Tu by sme mohli inicializovať vlastnosti
        pass
```

### Volanie rodičovského `__init__()` priamo:

Ak chceme zachovať inicializáciu z rodiča:

```python
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
```

---

## Použitie `super()`

Lepšou voľbou je použiť `super()`, ktorá automaticky načíta konštruktor rodiča:

```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
```

Takto netreba explicitne uvádzať meno rodičovskej triedy.

---

## Pridanie vlastností

Pridáme vlastnú vlastnosť, napríklad `graduationyear`:

```python
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019
```

Lepšie je rok posielať ako argument:

```python
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
```

---

## Pridanie metódy

Pridajme metódu `welcome`:

```python
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome", self.firstname,
            self.lastname,
            "to the class of", self.graduationyear
        )
```
---