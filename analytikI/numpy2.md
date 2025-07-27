# **Začíname s numpy: základné operácie a funkcie**

**Numpy** je základná knižnica pre numerické výpočty v Pythone. Umožňuje efektívnu prácu s veľkými poľami (tzv. “array”) a poskytuje množstvo užitočných matematických funkcií.

---

## **1. Tvorba numpy polí**

```python
import numpy as np

# Jednoduché pole (vektor)
a = np.array([1, 2, 3, 4, 5])

# Viacrozmerné pole (matica)
b = np.array([[1, 2, 3], [4, 5, 6]])
```

---

## **2. Základné informácie o poli**

```python
print("Tvar poľa (shape):", b.shape)    # (2, 3)
print("Druh údajov (dtype):", b.dtype)  # napr. int64
print("Počet prvkov:", b.size)          # 6
```

---

## **3. Vytváranie špeciálnych polí**

```python
zeros = np.zeros((3, 3))       # 3x3 pole samých núl
ones = np.ones((2, 4))         # 2x4 pole samých jednotiek
arange = np.arange(0, 10, 2)   # Pole 0, 2, 4, 6, 8
linspace = np.linspace(0, 1, 5) # 5 čísel rovnomerne od 0 po 1
```

---

## **4. Základné matematické operácie**

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

suma = a + b           # [5 7 9]
rozdiel = a - b        # [-3 -3 -3]
nasobok = a * b        # [4 10 18]
delenie = a / b        # [0.25 0.4 0.5]
```

---

## **5. Univerzálne funkcie (ufuncs)**

```python
x = np.array([1, 4, 9, 16])

odmocnina = np.sqrt(x)          # [1. 2. 3. 4.]
logaritmus = np.log(x)          # [0. 1.386... 2.197... 2.772...]
exp = np.exp([0, 1, 2])         # [1. 2.718... 7.389...]
sinus = np.sin(np.pi * np.array([0, 0.5, 1]))  # [0. 1. 0.]
```

---

## **6. Štatistické funkcie**

```python
data = np.array([10, 12, 15, 18, 20])

print("Súčet:", np.sum(data))        # 75
print("Priemer:", np.mean(data))     # 15.0
print("Minimum:", np.min(data))      # 10
print("Maximum:", np.max(data))      # 20
print("Štandardná odchýlka:", np.std(data)) # cca 3.4
print("Medián:", np.median(data))    # 15.0
```

---

## **7. Indexovanie a rezanie (slicing)**

```python
a = np.array([10, 20, 30, 40, 50])

print(a[0])        # 10
print(a[-1])       # 50
print(a[1:4])      # [20 30 40]
print(a[::2])      # [10 30 50]  (každý druhý prvok)
```

---

## **8. Filtrovanie a maskovanie (Boolean indexing)**

```python
a = np.array([1, 2, 3, 4, 5, 6])
mask = a > 3
print(mask)           # [False False False  True  True  True]
print(a[mask])        # [4 5 6]
```

---

## **9. Hromadné operácie (broadcasting)**

```python
a = np.array([1, 2, 3])
print(a + 10)         # [11 12 13]
b = np.array([[1], [2], [3]])
print(b + a)          # [[2 3 4], [3 4 5], [4 5 6]]
```

---

## **10. Práca s náhodnými číslami**

```python
np.random.seed(42)           # pre reprodukovateľnosť
rand_nums = np.random.rand(5)   # 5 náhodných čísel z <0,1)
rand_ints = np.random.randint(0, 10, size=3)  # tri celé čísla od 0 do 9
```

---

## **Praktické zadanie:**

1. **Vytvor pole s teplotami za 7 dní a vypíš najvyššiu a najnižšiu hodnotu.**
2. **Vytvor 10 náhodných čísel od 1 do 100 a vypíš ich priemer.**
3. **Z pole čísel 1 až 20 vyber všetky párne čísla.**

---

### **Riešenia:**

1.

```python
teploty = np.array([23, 24, 19, 27, 25, 21, 22])
print("Max:", np.max(teploty))
print("Min:", np.min(teploty))
```

2.

```python
cisla = np.random.randint(1, 101, size=10)
print("Náhodné čísla:", cisla)
print("Priemer:", np.mean(cisla))
```

3.

```python
pole = np.arange(1, 21)
parne = pole[pole % 2 == 0]
print("Párne čísla:", parne)
```

---

## **Záver**

* Numpy je výborný na rýchle výpočty s množstvom dát.
* Základné operácie a funkcie sú intuitívne.
* Skúšaj, kombinuj a experimentuj v Jupyter notebooku!

