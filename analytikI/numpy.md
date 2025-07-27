# 🔧 NumPy – Vytváranie polí (`ndarray`)

NumPy je knižnica určená na prácu s poľami (**arrays**). Hlavný typ je `ndarray`, ktorý vytvoríme pomocou funkcie `array()`.

### 📘 Základný príklad

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
```

Funkcia `type()` ukáže, že `arr` je typu `numpy.ndarray`.

Polia môžeme vytvárať z **listu, tuplu alebo iného “array-like” objektu**:

```python
arr = np.array((1, 2, 3, 4, 5))
print(arr)
```

---

## 📏 Dimenzie polí

Dimenzia definuje úroveň vnorenia v poli. Napr.:

* **0-D** (skalár): jednočíslo
* **1-D**: jednorozmerné pole
* **2-D**: dvojrozmerné pole (napr. matica)
* **3-D**: trojrozmerné pole

### ❗ Príklady:

```python
import numpy as np

# 0-D pole
arr0 = np.array(42)

# 1-D pole
arr1 = np.array([1, 2, 3, 4, 5])

# 2-D pole
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 3-D pole
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
```

---

## 📐 Overenie dimenzie pomocou `ndim`

Atribút `ndim` vráti počet dimenzií poľa:

```python
print(arr0.ndim)  # 0
print(arr1.ndim)  # 1
print(arr2.ndim)  # 2
print(arr3.ndim)  # 3
```

---

## 👆 Vynútenie minimálneho počtu dimenzií – `ndmin`

Môžeš špecifikovať minimálny počet rozmerov pomocou parametra `ndmin`:

```python
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print("Rozmerov:", arr.ndim)  # bude 5
```

---

# 🔍 NumPy – Prístup k prvkom polí (Indexovanie)

Prístup k prvku v poli (`ndarray`) funguje rovnako ako pri bežných zoznamoch – pomocou indexu.

---

## 📌 Základný index

Prvý prvok má index 0, druhý index 1, atď.

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])  # 1
print(arr[1])  # 2
print(arr[2] + arr[3])  # 3 + 4 = 7
```


---

## 🧩 Indexovanie 2D polí

Pri dvojrozmernom poli zadáš index riadku a stĺpca:

```python
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(arr[0, 1])  # hodnota v 1. riadku, 2. stĺpci = 2
print(arr[1, 4])  # hodnota v 2. riadku, 5. stĺpci = 10
```


---

## 📊 Indexovanie 3D polí

Pri trojrozmernom poli definujeme dimenzie:

```python
arr = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9], [10,11,12]]
])

print(arr[0, 1, 2])  # 6
```

To znamená:

* prvá časť `arr[0]` → prvý 2D blok (`[[1,2,3],[4,5,6]]`)
* `arr[0, 1]` → druhý riadok tohto bloku (`[4,5,6]`)
* `arr[0, 1, 2]` → tretí prvok toho riadku (`6`)
  ([W3Schools][2])

---

## ➖ Negatívne indexovanie

Negatívne indexy pristupujú od konca:

```python
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(arr[1, -1])  # posledný prvok v druhom riadku = 10
```

([W3Schools][2])

---

## 📝 Zhrnutie

* Python/NumPy indexovanie začína od **0**
* Pre 1–3 dimenzie píš `arr[i]`, `arr[i, j]`, `arr[i, j, k]`
* Negatívne indexy `-1, -2, ...` počítajú od konca


---

# 🔍 NumPy – Slicing polí

**Slicing** znamená vybrať časť poľa pomocou indexov. Používa sa syntax:

```python
array[start : end : step]
```

* `start` – index prvého prvku (vrátane)
* `end` – index posledného prvku (vylučujúci)
* `step` – veľkosť kroku (voliteľné)

Ak niektorý z týchto parametrov vynecháš:

* `start` sa predvolene nastaví na `0`
* `end` sa nastaví na koniec poľa
* `step` bude `1`

---

## ✅ Príklady so 1D poľom

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
```

### Výber prvkov od indexu 1 po 4:

```python
print(arr[1:5])  # [2 3 4 5]
```

### Od indexu 4 po koniec:

```python
print(arr[4:])  # [5 6 7]
```

### Od začiatku po index 3:

```python
print(arr[:4])  # [1 2 3 4]
```

### Použitie kroku:

```python
print(arr[1:6:2])  # [2 4 6]
```

### Každý druhý prvok v celom poli:

```python
print(arr[::2])  # [1 3 5 7]
```

---

## ➖ Negatívne indexovanie

Negatívne indexy počítajú od konca:

```python
print(arr[-3:-1])  # [5 6]
```

---

## 📐 Slicing v 2D poľoch

```python
arr2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
```

### Prístup k prvkom v druhom riadku (index 1), stĺpce 1 až 3:

```python
print(arr2[1, 1:4])  # [7 8 9]
```

### Výber druhého stĺpca z oboch riadkov:

```python
print(arr2[0:2, 2])  # [3 8]
```

---

## 📝 Zhrnutie

| Syntax                 | Popis                       |
| ---------------------- | --------------------------- |
| `arr[start:end]`       | Výber od `start` po `end-1` |
| `arr[:end]`            | Od začiatku po `end-1`      |
| `arr[start:]`          | Od `start` po koniec        |
| `arr[::step]`          | Celé pole s krokom `step`   |
| `arr[-n:]`             | Posledné `n` prvky          |
| `arr2[row, col]`       | Prvok v 2D poli             |
| `arr2[row, start:end]` | Slicing stĺpcov v riadku    |


---

# 📦 NumPy – Dátové typy (`dtype`)

NumPy rozširuje štandardné Python typy a používa špeciálne typové označenia, napríklad `i` pre celé čísla, `f` pre desatinné a podobne.

---

## 🧠 Základné typy v Pythone

Python má základné typy:

* `strings` – text (napr. `"ABCD"`)
* `integer` – celé čísla (napr. `-1`, `0`, `42`)
* `float` – desatinné čísla (napr. `1.2`, `42.42`)
* `boolean` – hodnoty `True`/`False`
* `complex` – zložité čísla (napr. `1.0 + 2.0j`)

---

## 🧬 Typy v NumPy

NumPy pridáva ďalšie typy a používa skratky jedným znakom:

| Skratka | Typ                            |
| ------- | ------------------------------ |
| `i`     | integer (celé číslo)           |
| `u`     | unsigned integer (kladné celé) |
| `f`     | float (desatinné číslo)        |
| `b`     | boolean (True/False)           |
| `c`     | complex float (zložné čísla)   |
| `m`     | timedelta (časový rozdiel)     |
| `M`     | datetime (dátum a čas)         |
| `O`     | object (ľubovoľný typ)         |
| `S`     | byte string (řetazec)          |
| `U`     | unicode string                 |
| `V`     | void (fixný blok pamäte)       |

---

## 🔍 Kontrola typu poľa

Použi atribút `.dtype` na `ndarray` na zistenie typu prvkov:

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # napr. int64

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)  # napr. <U6 (unicode)
```

---

## 🎯 Vytvorenie poľa s konkrétnym typom

Parametr `dtype` určuje typ poľa:

```python
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr.dtype)  # S1, bajtový string
```

Pre niektoré typy môžeš špecifikovať veľkosť:

```python
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr.dtype)  # int32 (4-bajtové celé číslo)
```

---

## ⚠️ Konverzná chyba

Ak vybraný typ nedokáže previesť hodnoty, NumPy vyhodí `ValueError`:

```python
np.array(['a', '2', '3'], dtype='i')  # ValueError
```

---

## 🔄 Konverzia existujúceho poľa: `astype()`

Ak chceš zmeniť typ existujúceho poľa, použije sa `astype()`, ktorý vracia novú kópiu:

```python
arr = np.array([1.1, 2.2, 3.3])

newarr = arr.astype('i')  # na celé čísla
print(newarr.dtype)       # int64

newarr2 = arr.astype(float)
print(newarr2.dtype)      # float64

arr3 = np.array([1, 0, 3])
boolarr = arr3.astype(bool)
print(boolarr.dtype)      # bool
```

---

## ✅ Zhrnutie

* NumPy má špecifické typové skratky ako `i`, `f`, `u`, `b`, `c`, `S`, `U`, atď.
* Pomocou `dtype` môžeš kontrolovať alebo definovať typ poľa
* Nesprávna konverzia vyvolá chybu
* `astype()` vytvorí nové pole s požadovaným typom

---

# 🔀 NumPy – Rozdiel medzi kopiou a pohľadom (copy vs view)

Pri práci s NumPy poľami (arrays) je dôležité rozumieť rozdielu medzi **kopiou** a **pohľadom** (`view`).

---

## 🟩 Kopia poľa (`copy()`)

Kópia je **úplne nové pole** so svojimi vlastnými dátami. Zmena v kópii **neovplyvní pôvodné pole**.

### Príklad:

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.copy()

arr2[0] = 42

print(arr1)  # [1 2 3 4 5]
print(arr2)  # [42 2 3 4 5]
```

---

## 🟦 Pohľad na pole (`view()`)

Pohľad je **iný objekt**, ktorý ukazuje na rovnaké dáta ako pôvodné pole.
**Zmeny v pohľade sa prejavia aj v origináli a naopak.**

### Príklad:

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.view()

arr2[0] = 42

print(arr1)  # [42 2 3 4 5]
print(arr2)  # [42 2 3 4 5]
```

---

## 🕵️ Ako zistiť, či je pole kopia alebo pohľad?

Každé pole má atribút `base`:

* Ak `arr2.base` je `None`, pole je **kopiou** (má vlastné dáta).
* Ak `arr2.base` je iné pole, je to **pohľad** (zdieľa dáta s týmto poľom).

### Príklad:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

kop = arr.copy()
pohl = arr.view()

print(kop.base)   # None
print(pohl.base)  # [1 2 3 4 5] (odkaz na pôvodné pole)
```

---

## 📝 Kedy sa pole správa ako kopia, a kedy ako pohľad?

* **Slicing** (`arr[1:4]`) vytvára **pohľad**.
* `copy()` vždy vytvorí kopiu.
* `view()` vždy vytvorí pohľad.
* Niektoré operácie (napr. metódy, ktoré menia tvar poľa) môžu vytvoriť kopiu alebo pohľad v závislosti od situácie.

---

## ✅ Zhrnutie

| Spôsob   | Nové dáta? | Zmeny v jednom sa prejavia v druhom? |
| -------- | ---------- | ------------------------------------ |
| `copy()` | Áno        | Nie                                  |
| `view()` | Nie        | Áno                                  |
| slicing  | Nie        | Áno                                  |


---

# 📐 NumPy – Tvar poľa (`shape`)

Každé NumPy pole (`ndarray`) má **tvar**, ktorý popisuje, **koľko prvkov je v každom rozmere**.

---

## 🔍 Atribút `shape`

Atribút `shape` vracia **n-ticu** (tuple) s počtom prvkov v každom rozmere.

### Príklad – 1D pole:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)  # (5,)
```

---

### Príklad – 2D pole:

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)  # (2, 3)  # 2 riadky, 3 stĺpce
```

---

### Príklad – 3D pole:

```python
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr3.shape)  # (2, 2, 3)
```

---

## 🏗️ Zmena tvaru poľa (`reshape()`)

Pomocou `reshape()` môžeš **zmeniť tvar poľa** bez zmeny obsahu.

### Príklad – z 1D na 2D:

```python
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = arr.reshape(2, 3)
print(newarr)
# Výsledok:
# [[1 2 3]
#  [4 5 6]]
```

---

### Príklad – z 1D na 3D:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, 2)
print(newarr)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
```

---

## ℹ️ Automatické určenie veľkosti pomocou -1

Ak použiješ `-1` v argumente `reshape()`, NumPy **dopočíta vhodnú veľkosť** za teba.

### Príklad:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, -1)
print(newarr)
# [[1 2 3 4]
#  [5 6 7 8]]
```

---

## 📋 Kontrola, či je pole "C-štýlu"

NumPy štandardne ukladá polia v **C-štýle** (riadky za sebou), takže `reshape` funguje očakávane. Ak pole nie je v C-štýle, môže byť nutné ho najprv kopírovať.

---

## ✅ Zhrnutie

* Každé pole má tvar (`shape`) – počet prvkov v každom rozmere
* Pomocou `reshape()` môžeš meniť tvar, ak počet prvkov sedí
* `-1` umožňuje automatické dopočítanie rozmeru

---

# 🔄 NumPy – Zmena tvaru poľa (`reshape()`)

NumPy umožňuje **meniť tvar (rozmernosť) poľa** bez zmeny samotných dát pomocou metódy `reshape()`.

---

## 🔢 Príklad: z 1D poľa na 2D pole

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
# Výsledok:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
```

---

## 📐 Príklad: z 1D poľa na 3D pole

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, 2)

print(newarr)
# [[[1 2]
#   [3 4]]
#  [[5 6]
#   [7 8]]]
```

---

## ⚠️ Podmienka: celkový počet prvkov sa nesmie zmeniť

Môžeš reshape-ovať pole **len vtedy, ak počet prvkov ostáva rovnaký**.

Napríklad pole s 8 prvkami môžeš dať do tvaru `(2, 4)`, `(4, 2)`, `(8, 1)`, `(1, 8)`, `(2, 2, 2)`, a podobne.

---

## 🧠 Automatické určenie veľkosti s `-1`

Ak nevieš, koľko prvkov má niektorý rozmer, môžeš použiť `-1` a NumPy to dopočíta za teba.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, -1)

print(newarr)
# [[1 2 3 4]
#  [5 6 7 8]]
```

---

## 🔎 Kontrola tvaru poľa

Každé pole má atribút `shape`, ktorý vráti jeho tvar ako n-ticu.

```python
print(newarr.shape)  # napr. (2, 4)
```

---

## 🔙 Zmena tvaru späť na 1D pole

Môžeš použiť `reshape(-1)` na “splostenie” do 1D:

```python
arr2 = newarr.reshape(-1)
print(arr2)  # [1 2 3 4 5 6 7 8]
```

---

## ✅ Zhrnutie

* `reshape()` mení tvar poľa, ale nemení jeho obsah.
* Počet prvkov musí ostať rovnaký.
* `-1` nechá NumPy automaticky dopočítať chýbajúci rozmer.
* Na kontrolu rozmerov použi `shape`.

---

# 🔁 NumPy – Iterovanie (prechádzanie) cez pole

NumPy umožňuje prechádzať (iterovať) cez prvky poľa rovnako ako cez obyčajné Python zoznamy.

---

## ✅ Príklad: iterácia cez 1D pole

```python
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)
```

---

## 🧩 Iterácia cez 2D pole

Pri dvojrozmernom poli budeš iterovať po **riadkoch**:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)        # Každý x je 1D pole (riadok)
```

Ak chceš každý prvok samostatne:

```python
for x in arr:
    for y in x:
        print(y)
```

---

## 🧊 Iterácia cez 3D pole

Pri trojrozmernom poli budeš iterovať cez “bloky”:

```python
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)        # Každý x je 2D pole

# Pre všetky hodnoty jednotlivo:
for x in arr:
    for y in x:
        for z in y:
            print(z)
```

---

## ⚡ Efektívna iterácia: `nditer()`

Funkcia `np.nditer()` umožňuje efektívne prejsť všetky prvky poľa, **bez ohľadu na jeho rozmernosť**:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in np.nditer(arr):
    print(x)
```

---

## ⚙️ Iterácia s indexom: `ndenumerate()`

Ak potrebuješ aj index, použij `np.ndenumerate()`:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

for idx, x in np.ndenumerate(arr):
    print(f"Index: {idx}, Hodnota: {x}")
```

---

## ✅ Zhrnutie

* Pre jednoduché polia stačí klasický `for` cyklus
* Pri viacrozdmerných poliach použij vnorené cykly
* `np.nditer()` – efektívna iterácia pre ľubovoľný rozmer
* `np.ndenumerate()` – efektívna iterácia vrátane indexov

---

# 🔗 NumPy – Spájanie polí (joining arrays)

Spájanie (join) dvoch alebo viacerých polí znamená **vytvorenie nového poľa** spojením pôvodných polí. V NumPy to spravíš najčastejšie pomocou funkcií `concatenate()`, `stack()`, `hstack()`, `vstack()`, `dstack()`.

---

## ✅ Príklad: `concatenate()`

Funkcia `concatenate()` spojí polia **po osi** (štandardne po osi 0 – teda pod seba pri 2D poliach).

```python
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)  # [1 2 3 4 5 6]
```

---

## 🧱 Spájanie 2D polí

```python
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=0)
print(arr)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
```

Ak chceš spojiť **vedľa seba** (po stĺpcoch), použi `axis=1`:

```python
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
# [[1 2 5 6]
#  [3 4 7 8]]
```

---

## 🔢 Príklad: `stack()`

Funkcia `stack()` spojí polia do nového rozmeru:

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)
print(arr)
# [[1 4]
#  [2 5]
#  [3 6]]
```

---

## ⬆️ `hstack()`, `vstack()`, `dstack()`

* `hstack()` – spojí polia **horizontálne** (vedľa seba)
* `vstack()` – spojí polia **vertikálne** (pod seba)
* `dstack()` – spojí polia **do tretieho rozmeru**

### Príklad – `hstack()`:

```python
arr = np.hstack((arr1, arr2))
print(arr)  # [1 2 3 4 5 6]
```

### Príklad – `vstack()`:

```python
arr = np.vstack((arr1, arr2))
print(arr)
# [[1 2 3]
#  [4 5 6]]
```

### Príklad – `dstack()`:

```python
arr = np.dstack((arr1, arr2))
print(arr)
# [[[1 4]
#   [2 5]
#   [3 6]]]
```

---

## ✅ Zhrnutie

* `concatenate()` – najčastejšie používané na spájanie polí (určíš os)
* `stack()` – vytvorí nový rozmer
* `hstack()`, `vstack()`, `dstack()` – špecializované funkcie na spájanie v rôznych smeroch

---

# ✂️ NumPy – Rozdeľovanie polí (`split`)

Rozdeľovanie (split) znamená **rozdeliť pole na viacero menších polí**.
NumPy poskytuje funkcie `split()`, `array_split()` a tiež špecializované verzie ako `hsplit()`, `vsplit()`, `dsplit()`.

---

## ✅ Príklad: `split()`

Funkcia `split()` rozdelí pole na rovnaké časti.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

novepolia = np.split(arr, 3)

print(novepolia)
# [array([1, 2]), array([3, 4]), array([5, 6])]
```

---

## ⚠️ Ak nie je možné rozdeliť pole na rovnaké časti

Ak počet prvkov nie je deliteľný počtom častí, funkcia `split()` vyhodí chybu.
V takom prípade použi `array_split()`.

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7])

novepolia = np.array_split(arr, 3)

print(novepolia)
# [array([1, 2, 3]), array([4, 5]), array([6, 7])]
```

---

## 🧱 Rozdeľovanie 2D polí

Môžeš rozdeliť 2D pole podľa riadkov (`axis=0`) alebo stĺpcov (`axis=1`):

```python
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# Split podľa stĺpcov:
novepolia = np.hsplit(arr2, 2)
print(novepolia)
# [array([[1, 2],
#         [5, 6]]),
#  array([[3, 4],
#         [7, 8]])]

# Split podľa riadkov:
novepolia = np.vsplit(arr2, 2)
print(novepolia)
# [array([[1, 2, 3, 4]]),
#  array([[5, 6, 7, 8]])]
```

---

## ✅ Zhrnutie

* `split(arr, n)` – rozdelí pole na `n` rovnakých častí
* `array_split(arr, n)` – rozdelí aj keď časti nie sú rovnako veľké
* `hsplit()`, `vsplit()`, `dsplit()` – špecializované funkcie pre 2D/3D polia


---

# 🔎 NumPy – Vyhľadávanie v poli (`search`)

NumPy poskytuje funkcie na **vyhľadávanie hodnôt** v poliach. Najčastejšie sa používa funkcia `where()` a `searchsorted()`.

---

## ✅ Funkcia `where()`

Funkcia `np.where()` vráti **indexy všetkých prvkov, ktoré spĺňajú podmienku**.

### Príklad – nájdi všetky výskyty čísla 4:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

indexy = np.where(arr == 4)
print(indexy)  # (array([3, 5, 6]),)
```

Výsledkom je n-tica s poľom indexov, kde sa hodnota nachádza.

---

### Príklad – nájdi indexy všetkých párnych čísel:

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
indexy = np.where(arr % 2 == 0)
print(indexy)  # (array([1, 3, 5, 7]),)
```

---

## ➕ Prvý výskyt hodnoty

Chceš len **prvý výskyt**?
Použi `[0][0]` na extrakciu prvého indexu:

```python
arr = np.array([6, 7, 8, 9, 10])
indexy = np.where(arr == 8)
if indexy[0].size > 0:
    print("Prvý výskyt na indexe:", indexy[0][0])  # 2
```

---

## 🧮 Funkcia `searchsorted()`

Funkcia `searchsorted()` vráti **index**, na ktorý treba vložiť hodnotu, aby pole ostalo zoradené.

### Príklad – kde vložiť hodnotu 7:

```python
arr = np.array([6, 7, 8, 9])
idx = np.searchsorted(arr, 7)
print(idx)  # 1
```

Ak hľadaná hodnota už v poli je, vráti index pred túto hodnotu.

---

### Príklad – viacero hodnôt naraz

```python
arr = np.array([1, 3, 5, 7])
idxs = np.searchsorted(arr, [2, 4, 6])
print(idxs)  # [1 2 3]
```

---

### Možnosť voľby strany (`side`)

Argument `side="right"` zabezpečí, že vrátený index bude za existujúcimi zhodami:

```python
arr = np.array([1, 3, 5, 7])
idx = np.searchsorted(arr, 3, side="right")
print(idx)  # 2
```

---

## ✅ Zhrnutie

* `where()` – vráti indexy všetkých prvkov podľa podmienky
* `searchsorted()` – nájde index, kde by mala byť hodnota vložená do zoradeného poľa
* Vieš tak efektívne vyhľadávať, filtrovať alebo vkladať do polí


---

# 🔢 NumPy – Triedenie polí (`sort`)

NumPy umožňuje **triedenie polí** pomocou funkcie `sort()`. Funkcia triedi pole a vracia **nové pole**, pôvodné pole nemení.

---

## ✅ Príklad – triedenie čísel

```python
import numpy as np

arr = np.array([3, 2, 0, 1])
triedene = np.sort(arr)
print(triedene)  # [0 1 2 3]
```

---

## ✅ Príklad – triedenie reťazcov

```python
arr = np.array(['banana', 'cherry', 'apple'])
triedene = np.sort(arr)
print(triedene)  # ['apple' 'banana' 'cherry']
```

---

## ✅ Príklad – triedenie booleánov

```python
arr = np.array([True, False, True])
triedene = np.sort(arr)
print(triedene)  # [False  True  True]
```

---

## 🧩 Triedenie 2D poľa

Pri dvojrozmernom poli sa **každý riadok triedi samostatne**:

```python
arr = np.array([[3, 2, 4], [5, 0, 1]])
triedene = np.sort(arr)
print(triedene)
# [[2 3 4]
#  [0 1 5]]
```

---

## ⚙️ Triedenie podľa osí

Argument `axis` určuje, **podľa ktorého rozmeru** sa bude triediť:

* `axis=0` – po stĺpcoch (zoraďuje každý stĺpec zvlášť)
* `axis=1` – po riadkoch (štandardne)

### Príklad – triedenie po stĺpcoch:

```python
arr = np.array([[3, 2, 4], [5, 0, 1]])
triedene = np.sort(arr, axis=0)
print(triedene)
# [[3 0 1]
#  [5 2 4]]
```

---

## ⚠️ Zoradenie `in-place`

Ak chceš zmeniť pôvodné pole, použi metódu `.sort()` na objektoch typu ndarray:

```python
arr = np.array([3, 2, 1])
arr.sort()
print(arr)  # [1 2 3]
```

---

## ✅ Zhrnutie

* `np.sort(array)` – triedi a vracia **nové pole**
* `array.sort()` – triedi **in-place** (mení pôvodné pole)
* Funguje na číslach, textoch aj booleanoch
* V 2D poliach triedi po riadkoch (štandard) alebo po stĺpcoch (`axis=0`)

---

# 🔎 NumPy – Filtrovanie polí (`filter`)

**Filtrovanie** znamená vybrať prvky z poľa na základe nejakej podmienky. V NumPy sa na to používa **boolovské pole** (pole s hodnotami True/False).

---

## ✅ Vytvorenie boolovského poľa

Boolovské pole je pole, kde každá hodnota hovorí, či prvok z pôvodného poľa má byť vybraný (`True`) alebo nie (`False`).

### Príklad – vyber všetky hodnoty väčšie ako 42:

```python
import numpy as np

arr = np.array([41, 42, 43, 44])
maska = arr > 42
print(maska)  # [False False  True  True]
```

---

## ✅ Použitie masky na filtrovanie

Boolovské pole (maska) použiješ priamo na pôvodné pole:

```python
filtered = arr[maska]
print(filtered)  # [43 44]
```

Alebo priamo v jednom kroku:

```python
filtered = arr[arr > 42]
print(filtered)  # [43 44]
```

---

## 🧩 Zložitejšie podmienky

Môžeš kombinovať podmienky pomocou operátorov `&` (and), `|` (or):

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

filtered = arr[(arr > 3) & (arr < 8)]
print(filtered)  # [4 5 6 7]
```

---

## ✅ Filtrovanie textových polí

Podmienka môže byť aplikovaná aj na reťazce:

```python
arr = np.array(['apple', 'banana', 'cherry'])
filtered = arr[arr != 'banana']
print(filtered)  # ['apple' 'cherry']
```

---

## ✅ Zhrnutie

* Filtrovanie využíva boolovské pole (maska)
* Maska vzniká porovnaním pôvodného poľa s podmienkou
* Filter môžeš aplikovať aj priamo v hranatých zátvorkách
* Funguje s číslami aj textom

---

