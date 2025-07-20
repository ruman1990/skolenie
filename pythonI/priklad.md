```python
import math

x = int(input('Zadaj cislo '))
y = int(input('Zadaj cislo2 '))

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x % y)
print(x // y)
print(x ** y)
```



```python
vek = input('Kolko mas rokov? ')
match vek:
    case "18" | '20' if int(vek)>10:
        print("Ma 18")
    case "19":
        print("Ma 19")
    case _:
        print("Iná hodnota")

print('hotovo')
```


```python
# vypytame od pouzivatela jeho meno nasledne jeho vek. Vypiseme dlzku mena a zistime a vypiseme ci je vek pouzivatel parne cislo.
meno = input("Zadaj svoje meno: ")
vek = int(input("Zadaj svoj vek: "))
if vek % 2 == 0: print('Vek je parne cislo')
else: print('Vek je neparne cislo')
print('Dlzka mena je' , len(meno))
# i = 0
# for x in meno:
#     i += 1

# vysledok = 'Dlzka mena je: ' + str(i)

# print(vysledok)
```

```python
pocet_hviezd = input("Zadaj počet hviezd: ")

pocet_hviezd = int(pocet_hviezd)

for i in range(1, pocet_hviezd + 1):
    for j in range(i):
        print("*", end=" ")
    print('')
```


