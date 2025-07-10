Vypis aritmetickych operacii dvoch cisiel
```python
a = int(input("Zadaj prve cislo: "))
b = int(input("Zadaj druhe cislo: "))
if b == 0:
    print('Delenie nulou nie je mozne')
else:
    print(f'Sucet: {a+b}, rozdiel: {a-b}, sucin: {a*b}, podiel: {a/b} ')
```

Scitanie sekvencie
```python
n = int(input("zadaj N: "))
suma = 0

for i in range(1, n + 1):
    suma += i
print(f'Vysledok je {suma}')
```

Hra na hadanie cisla
```python
import random
tajne = random.randint(1,11)
cislo = 0
while cislo != tajne:
    cislo = int(input("Hadaj cislo: "))
print("Uhadol si")
```
