# 🧵 Reťazce (strings) v Pythone

## 🧩 Základ

Reťazec je **sekvencia znakov**. V Pythone sú reťazce **nemenné** – po vytvorení ich nemožno meniť. Metódy ako `replace`, `split`, `join` vytvárajú **nový reťazec**, pôvodný nemenia.

---

## ✍️ Literály reťazcov

Reťazce môžeš zapísať:

* jednoduchými úvodzovkami `'text'`
* dvojitými úvodzovkami `"text"`
* trojitými úvodzovkami `'''text'''` alebo `"""text"""` – umožňujú viacriadkové reťazce

```python
a = "text"
b = 'slovo'
c = """viac
riadkov
textu"""
```

---

## 🌐 Unicode reťazce

V Pythone môžeš používať Unicode priamo:

```python
text = 'Лев Толстой: Анна Каренина'
```

Alebo cez escape sekvencie:

```python
text = u'\u041b\u0435\u0432 ...'
```

---

## 🧾 Formátovanie reťazcov

```python
name = 'Peter'
age = 23

print('%s má %d rokov' % (name, age))                  # starý spôsob
print('{} má {} rokov'.format(name, age))              # od Python 3
print(f'{name} má {age} rokov')                        # od Python 3.6 (f-string)
```

---

## 📐 Dĺžka reťazca

```python
text = "Eagle  "
print(len(text))  # počíta aj medzery, znaky ako \n, \t
```

---

## ✂️ Odstraňovanie medzier

* `strip()` – odstráni zľava aj sprava
* `lstrip()` – zľava
* `rstrip()` – sprava

```python
s = " text "
print(s.strip())   # "text"
```

---

## 🔡 Zmena veľkosti písmen

```python
a = "ZetCode"

print(a.upper())     # ZETCODE
print(a.lower())     # zetcode
print(a.swapcase())  # zETcODE
print(a.title())     # Zetcode
```

---

## 🎭 Úvodzovky v reťazcoch

```python
print("He said: \"Hello!\"")
print('He said: "Hello!"')
```

---

## 🔎 Porovnávanie reťazcov

```python
print("abc" == "abc")   # True
print("abc" != "xyz")   # True
```

---

## 🎯 Prístup k znakom

```python
s = "Eagle"
print(s[0])     # E
print(s[-1])    # e
print(s[1:4])   # agl
```

---

## 🔁 Prechod reťazcom

```python
for ch in "ZetCode":
    print(ch, end=" ")
```

---

## ➕ Operácie s reťazcami

```python
print("eagle " * 3)  # opakovanie
print("eagle" + " falcon")  # zreťazenie
```

---

## 🔢 Konverzia medzi číslami a reťazcami

```python
int("12")          # 12
str(42)            # "42"
float("3.14")      # 3.14
```

---

## 🔁 Nahradzovanie časti reťazca

```python
text = "Ahoj svet. Svet je krásny."
print(text.replace("Svet", "vesmír", 1))  # len prvý výskyt
```

---

## 🪓 Rozdelenie a spájanie reťazcov

```python
nums = "1,2,3"
parts = nums.split(",")         # ['1', '2', '3']
joined = ":".join(parts)        # '1:2:3'
```

---

## 📐 Formátovanie čísel

```python
print("%.2f" % 3.1415)                     # 3.14
print("{:.2f}".format(3.1415))             # 3.14
print("{:x}".format(300))                  # 12c (hex)
print("{:b}".format(10))                   # 1010 (binárne)
```

---

## 📏 Zarovnávanie výstupu

```python
for x in range(1, 4):
    print(f"{x:2d} {x*x:3d} {x*x*x:4d}")
```

---

## 🔍 Vyhľadávanie podreťazcov

```python
s = "vlk v lese. ďalší vlk"

print(s.find("vlk"))      # 0
print(s.rfind("vlk"))     # nájde posledný výskyt
print(s.find("líška"))    # -1 (nenájdené)

# rozdiel medzi find a index: index vyhodí výnimku, ak nič nenájde
```

---

## ⚙️ Užitočné metódy

```python
s = "Hello 123"
s.isalpha()    # False
s.isdigit()    # False
s.isspace()    # False
```

---

## ✅ Ukážka úpraveného výstupu zápasu

```python
teams = {
  0: ("Ajax", "Inter"),
  1: ("Real", "AC Milan"),
  2: ("Dortmund", "Sparta")
}

results = ("2:3", "3:3", "2:1")

for i in teams:
    print(f"{teams[i][0]:15} - {teams[i][1]:15} {results[i]}")
```

---
