# Zoznamy (Lists) v Pythone

Zoznam (list) je usporiadaná množina hodnôt. Môže obsahovať hodnoty rôznych typov a vieme ho upravovať – teda pridávať, mazať alebo meniť hodnoty.

---

## 📌 Čo je zoznam?

Zoznam v Pythone je ako rad škatuliek, kde si môžeš uložiť viacero hodnôt pod jedným menom. Každá hodnota má svoje miesto – index (číslo). Prvý prvok má index 0.

---

## 🧪 Jednoduchý príklad

```python
nums = [1, 2, 3, 4, 5]

print(nums[0])
print(nums[-1])
print(nums)
```

📘 Vysvetlenie:

* `nums[0]` – vypíše prvý prvok (1)
* `nums[-1]` – záporné indexy znamenajú od konca (posledný prvok)

Zoznam sa píše do hranatých zátvoriek `[]` a prvky sa oddeľujú čiarkou.

---

## 🔄 Rôzne typy v zozname

Zoznamy môžu obsahovať rôzne typy údajov naraz:

```python
class Being:
    pass

objects = [1, -2, 3.4, None, False, [1, 2], "Python", (2, 3), Being(), {}]
print(objects)
```

📘 Vysvetlenie:

* Môžeš mať čísla, reťazce, objekty, vnorené zoznamy atď.

---

## 🏗️ Inicializácia zoznamu

```python
n1 = [0 for i in range(15)]
n2 = [0] * 15

print(n1)
print(n2)

n1[0:10] = [10] * 10

print(n1)
```

📘 Vysvetlenie:

* Takto si vieš vopred pripraviť zoznam s 15 nulami.
* Prvých 10 hodnôt potom prepisujeme na hodnotu 10.

---

## 🛠️ Funkcia `list()`

Funkcia `list()` vie vytvoriť zoznam z iného objektu (napr. reťazca, n-tice):

```python
a = []
b = list()

print(a == b)

print(list((1, 2, 3)))
print(list("ZetCode"))
print(list(['Ruby', 'Python', 'Perl']))
```

📘 Vysvetlenie:

* `[]` a `list()` vytvárajú prázdny zoznam
* `list("abc")` → `['a', 'b', 'c']`

---

## ➕ Operácie so zoznamami

```python
n1 = [1, 2, 3, 4, 5]
n2 = [3, 4, 5, 6, 7]

print(n1 == n2)
print(n1 + n2)
print(n1 * 3)
print(2 in n1)
```

📘 Vysvetlenie:

* `+` spája dva zoznamy
* `*` zopakuje zoznam niekoľkokrát
* `in` – zisťuje, či hodnota je v zozname

---

## 📏 Základné funkcie pre sekvencie

```python
n = [1, 2, 3, 4, 5, 6, 7, 8]

print(len(n))
print(max(n))
print(min(n))
print(sum(n))
```

📘 Vysvetlenie:

* `len` – počet prvkov
* `max`, `min` – najvyššia a najnižšia hodnota
* `sum` – súčet

---

## ➕ Pridávanie prvkov

```python
langs = []

langs.append("Python")
langs.insert(0, "PHP")
langs.extend(["JS", "Lua"])
```

📘 Vysvetlenie:

* `append()` – pridá na koniec
* `insert(i, val)` – vloží na pozíciu `i`
* `extend()` – pridá viacero hodnôt naraz

---

## ❌ Mazanie prvkov

```python
langs = ["Python", "Ruby", "Lua"]
langs.pop(1)
langs.remove("Lua")
del langs[0]
```

📘 Vysvetlenie:

* `pop(i)` – vyberie a vráti prvok na indexe `i`
* `remove(val)` – vymaže prvý výskyt hodnoty
* `del` – zmaže podľa indexu alebo celý zoznam

---

## ✏️ Úprava prvkov

```python
langs = ["Python", "Perl"]
langs[1] = "PHP"
```

📘 Vysvetlenie:

* Prvky možno nahradiť novou hodnotou cez index

---

## 📋 Kopírovanie zoznamov

```python
c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
```

📘 Vysvetlenie:

* `[:]` a `list()` robia plytkú (shallow) kópiu
* `deepcopy()` robí hlbokú – aj vnorené objekty sa kopírujú

---

## 🔍 Prístup cez index

```python
n = [10, 20, 30]
print(n[0])  # prvý
print(n[-1]) # posledný
```

📘 Vysvetlenie:

* Index 0 je prvý prvok
* Index -1 je posledný

---

## 🔪 Rezanie (slicing)

```python
n = [1, 2, 3, 4, 5]
print(n[1:4])  # indexy 1 až 3
print(n[::-1]) # otočený zoznam
```

📘 Vysvetlenie:

* `list[start:end]` – výber časti zoznamu
* `[::-1]` – otočí zoznam

---

## 🔁 Prechádzanie zoznamu

```python
for x in n:
    print(x)

for i, x in enumerate(n):
    print(i, x)
```

📘 Vysvetlenie:

* `for x in n:` – postupne vypíše prvky
* `enumerate()` – dá aj index aj hodnotu

---

## 🔢 Počet výskytov

```python
n = [1, 1, 2, 3, 4]
print(n.count(1))  # 2x
```

📘 Vysvetlenie:

* `count()` vráti, koľkokrát sa hodnota v zozname vyskytuje

---

## 🧱 Vnorené zoznamy

```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # 2
```

📘 Vysvetlenie:

* Vnorený zoznam = zoznam v zozname
* Potrebujeme dva indexy: prvý pre riadok, druhý pre stĺpec

---

## 📊 Triedenie

```python
nums.sort()               # zoradí vzostupne
nums.sort(reverse=True)  # zostupne
sorted(nums)             # vytvorí novú kópiu
```

📘 Vysvetlenie:

* `sort()` mení pôvodný zoznam
* `sorted()` vytvára novú verziu

---

## 🔁 Otočenie zoznamu

```python
lst[::-1]    # cez slicing
reversed(lst)  # iterator
lst.reverse()  # in-place
```

📘 Vysvetlenie:

* `[::-1]` alebo `reverse()` – otočí poradie prvkov

---

## ✅ List comprehension

```python
nums = [1, 2, 3, 4, 5]
odd = [x for x in nums if x % 2 == 1]
```

📘 Vysvetlenie:

* Kratší spôsob vytvárania zoznamu z iného zoznamu

---

## ⚙️ map() a filter()

```python
words = ["cat", "dog"]
upper = list(map(str.upper, words))
```

📘 Vysvetlenie:

* `map()` – aplikuje funkciu na každý prvok

```python
nums = [-1, 0, 1, 2]
positive = list(filter(lambda x: x > 0, nums))
```

📘 Vysvetlenie:

* `filter()` – ponechá len tie prvky, ktoré spĺňajú podmienku

---
