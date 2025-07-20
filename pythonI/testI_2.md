Tu je kompletný test zo základov práce s funkciami v Pythone, vhodný pre začiatočníkov:

---

# 🧪 TEST Z PYTHON FUNKCIÍ

## ❓ Otázky typu *„čo sa vypíše / nastane chyba“*

**1.** Čo vypíše tento kód?

```python
def my_function():
    print("Hello from a function")

my_function()
```

a) Hello from a function
b) SyntaxError
c) None
d) Hello

**2.** Čo sa stane?

```python
def my_function():
    pass

my_function()
```

a) SyntaxError
b) Funkcia nič nevypíše
c) RuntimeError
d) None

**3.** Čo vypíše tento kód?

```python
def my_function(x):
    return 5 * x

print(my_function(3))
```

a) 8
b) 15
c) 5
d) 3

**4.** Čo vypíše tento kód?

```python
def my_function(*kids):
    print(kids[0])

my_function("Emil", "Tobias")
```

a) Tobias
b) Emil
c) kids
d) SyntaxError

**5.** Čo spôsobí tento kód?

```python
def my_function(**kid):
    print(kid["lname"])

my_function(fname="Tobias", lname="Refsnes")
```

a) Tobias
b) Refsnes
c) SyntaxError
d) None

**6.** Bude tento kód fungovať?

```python
def my_function(fname, lname):
    print(fname + lname)

my_function("Emil")
```

a) SyntaxError
b) TypeError
c) Emil
d) Emillname

**7.** Čo vypíše tento kód?

```python
def my_function(country="Norway"):
    print("I am from " + country)

my_function()
```

a) I am from country
b) I am from Norway
c) SyntaxError
d) None

**8.** Čo vypíše tento kód?

```python
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana"]
my_function(fruits)
```

a) apple banana
b) banana apple
c) SyntaxError
d) \['apple', 'banana']

**9.** Čo sa vypíše?

```python
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

tri_recursion(2)
```

a) 3\n1
b) 1\n2
c) 0
d) 2\n3

**10.** Čo vypíše tento kód?

```python
def my_function(*args):
    print(args)

my_function(1, 2, 3)
```

a) 1 2 3
b) (1, 2, 3)
c) \[1, 2, 3]
d) args

---

## 🧑‍💻 Úlohy na programovanie

**1.** Napíš funkciu `multiply(x, y)`, ktorá vráti súčin dvoch čísel.

**2.** Napíš funkciu, ktorá vypíše všetky prvky zoznamu odovzdaného ako argument.

**3.** Napíš funkciu, ktorá prijme ľubovoľný počet čísel a vráti ich súčet.

**4.** Napíš funkciu, ktorá má predvolený parameter `lang='Python'` a vypíše `'I code in <lang>'`.

**5.** Napíš rekurzívnu funkciu, ktorá spočíta súčet čísel od `n` po `0`.

**6.** Napíš funkciu, ktorá prijíma meno a priezvisko a vráti ich vo formáte `'Priezvisko, Meno'`.

**7.** Napíš funkciu, ktorá prijíma zoznam a vráti nový zoznam, kde sú všetky prvky vynásobené dvoma.

**8.** Napíš funkciu, ktorá vypíše `'Hello'` bez použitia argumentov.

**9.** Napíš funkciu, ktorá prijíma ľubovoľné `**kwargs` a vráti hodnotu kľúča `'name'`, ak existuje.

**10.** Napíš funkciu, ktorá vypíše čísla od 1 do 5 pomocou `for` cyklu.

---

## ✅ Riešenia testových otázok

1. Hello from a function
2. Funkcia nič nevypíše
3. 15
4. Emil
5. Refsnes
6. TypeError
7. I am from Norway
8. apple\nbanana
9. 1\n3
10. (1, 2, 3)

Ak chceš, môžem ti tieto otázky vygenerovať aj ako PDF alebo interaktívny test.
