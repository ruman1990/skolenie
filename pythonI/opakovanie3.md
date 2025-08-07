## **Cvičenie 1: Vytlač čísla od 1 do 10**

Použi cyklus `for`, aby sa vypísali čísla od 1 po 10.

```python
# Výstup:
# 1
# 2
# ...
# 10
```

---

## **Cvičenie 2: Súčet čísel od 1 do N**

Napíš program, ktorý si vypýta číslo **N** a spočíta súčet čísel od 1 po N pomocou `for`:

```python
# Vstup: N = 5
# Výstup: Súčet je 15
```
```python
 n = int(input("Zadaj N: "))
 suma = 0
 for i in range(1,n+1):
     suma += i
 print(f'Sucet je {suma}')

```
---

## **Cvičenie 3: While cyklus – hádaj číslo**

Vytvor program, ktorý bude opakovane pýtať číslo od používateľa, **kým nezadá správne číslo (napr. 7)**.

```python
# Opakuje sa:
# "Zadaj číslo:"
# ... až kým nezadá 7
```

---

## **Cvičenie 4: Násobilka**

Vypíš násobilku čísla 8 od 1 po 10:

```python
# Výstup:
# 8 × 1 = 8
# 8 × 2 = 16
# ...
# 8 × 10 = 80
```
```python
for i in range(1,6):
     print('*' * i)

```
---

## **Cvičenie 5: Vnorený cyklus – hviezdičky**

Vytvor pravouhlý trojuholník z hviezdičiek:

```python
# Výstup:
#
# *
# **
# ***
# ****
# *****
```

---

## **Cvičenie 6: Počet párnych čísel v zozname**

Zisti, koľko **párnych čísel** je v zozname:

```python
cisla = [2, 7, 4, 9, 6, 1, 10]
# Výstup: 4
```
```python
for x in cisla:
     if x % 2 == 0:
         pocet_parnych += 1
```
---

## **Cvičenie 7: Pyramida**

```
    *        *
   ***      ***
  *****    *****
 *******  *******
******************
```
```python
n = int(input("Zadaj pocet riadkov: "))

for i in range(1,n+1):
    print(' ' * (n-i), end='')

    print('*' * (2 * i - 1), end='')

    print(' ' * (2 * (n-i)), end='')

    print('*' * (2 * i - 1))


```
---

