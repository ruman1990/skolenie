## **Cvičenie 1: Vytlač čísla od 1 do 10**
#Použi cyklus `for`, aby sa vypísali čísla od 1 po 10.
for x in range(1,11):
    print(x,end=' ')


## **Cvičenie 2: Súčet čísel od 1 do N**

#Napíš program, ktorý si vypýta číslo **N** a spočíta súčet čísel od 1 po N pomocou `for`:
number = int(input("Zadaj cislo: "))

suma = 0
for x in range(1,number+1):
    suma = suma + x
print(suma)
r = range(1,number+1)
suma = sum(r)
print(suma)

print(sum(range(1,number+1)))



## **Cvičenie 6: Počet párnych čísel v zozname**

#Zisti, koľko **párnych čísel** je v zozname:

cisla = [2, 7, 4, 9, 6, 1, 10]

parne_cisla = 0
for x in cisla:
    if x % 2 == 0:
        parne_cisla += 1
        print(x,end=' ')

print()
print(parne_cisla)