# 🧩 Python – Polymorfizmus

**Polymorfizmus** (z gréckeho „mnoho foriem“) v programovaní znamená, že rovnaký názov metódy/funkcie/opera­tora môže fungovať rôzne v závislosti od objektu či triedy.

---

## 1. Funkčný polymorfizmus

Príkladom je vstavaná funkcia `len()`, ktorá sa správa rôzne podľa typu objektu:

```python
x = "Hello World!"
print(len(x))  # počet znakov v reťazci

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))  # počet položiek v n-tici

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))  # počet párov kľúč/hodnota v slovníku
```

> Funkcia `len()` sa správa podľa typu: reťazec, n-tica aj slovník vrátia relevantný počet položiek.

---

## 2. Polymorfizmus tried (Class Polymorphism)

Polymorfizmus sa dobre uplatňuje v metódach tried – rôzne triedy môžu mať metódu rovnakého názvu s odlišným správaním:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
```

> V cykle môžete zavolať `move()` pre každý objekt bez ohľadu na triedu – správanie sa určuje jeho implementácia.

---

## 3. Polymorfizmus s dedičnosťou

Polymorfizmus funguje aj pri dedičnosti – potomkovia môžu prepísať metódy rodiča:

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass  # dedí celé správanie

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
```

> Trieda `Car` dedí bez zmien, `Boat` a `Plane` prepísali metódu `move()`. Všetci používatelia volajú tú istú metódu, no správanie je rôzne.

---

## ✅ Zhrnutie

* **Funkčný polymorfizmus**: rovnaká funkcia (`len()`) funguje s rôznymi typmi dát.
* **Metódový polymorfizmus**: pomocou dedičnosti a prepísania umožňuje objektom rovnaké rozhranie, no rozdielnu implementáciu.

---
