## ✅ **Test: Hodnota vs. referencia v Pythone**

---

### 1. Čo sa vypíše?

```python
x = 5
y = x
y += 1
print(x, y)
```

a) `6 6`
b) `5 6`
c) `6 5`
d) `5 5`

---

### 2. Čo sa vypíše?

```python
a = [1, 2, 3]
b = a
b[0] = 10
print(a)
```

a) `[10, 2, 3]`
b) `[1, 2, 3]`
c) chyba
d) `None`

---

### 3. Čo urobí funkcia?

```python
def add_element(lst):
    lst.append(4)

data = [1, 2, 3]
add_element(data)
print(data)
```

a) `[1, 2, 3, 4]`
b) `[1, 2, 3]`
c) `[4]`
d) chyba

---

### 4. Doplň: `sorted()` funkcia...

a) mení pôvodný zoznam na mieste
b) vracia nový zoradený zoznam
c) neexistuje
d) funguje len na `tuple`

---

### 5. Čo je výsledok?

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 100
print(a[0][0])
```

a) `1`
b) `100`
c) `[1, 2]`
d) `[100, 2]`

---

### 6. Doplň výrok:

`vals = [1, 2, 3]` → `vals2 = vals.copy()` vytvorí...

a) úplne nový zoznam vrátane všetkých vnorených objektov
b) referenciu na pôvodný zoznam
c) plytkú (shallow) kópiu
d) hlbokú (deep) kópiu

---

### 7. Rozhodni, či sa kopíruje hodnotou alebo referenciou

| Výraz           | Hodnota / referencia |
| --------------- | -------------------- |
| `x = "text"`    | ?                    |
| `y = [1, 2, 3]` | ?                    |
| `z = {"a": 1}`  | ?                    |
| `t = (1, 2, 3)` | ?                    |

---

### 8. Oprav chybu v kóde:

```python
lst = [1, 2, 3]
new_lst = lst
new_lst[0] = 99
# Ako vytvoriť takú kópiu, aby sa pôvodný lst nezmenil?
```

✍️ Doplň správnu úpravu kódu:

---

### 9. Ktorý príkaz vytvorí **hlbokú kópiu** objektu?

a) `obj.copy()`
b) `copy.copy(obj)`
c) `copy.deepcopy(obj)`
d) `obj[:]`

---

## ✅ **Správne odpovede:**

1. **b**
2. **a**
3. **a**
4. **b**
5. **b**
6. **c**
7.

* `x = "text"` → **hodnota**
* `y = [1, 2, 3]` → **referencia**
* `z = {"a": 1}` → **referencia**
* `t = (1, 2, 3)` → **hodnota**

8. `new_lst = lst.copy()` **alebo** `new_lst = lst[:]`
9. **c**

---
