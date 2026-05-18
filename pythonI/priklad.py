<<<<<<< HEAD
import random

secret_number = random.randint(1,100)
counter = 6
while True:
    number = int(input(f"Zadaj cislo 1-100 (Pocet pokusov {counter}): "))
    counter -= 1
    if secret_number == number:
        print("Gratulujem, uhadol si.")
        break
    
    if counter == 0:
        print(f"Prehral si! Tajne cislo bolo {secret_number}")
        break
    elif secret_number < number:
        print("Hadaj nizsie")
    elif secret_number > number:
        print("Hadaj vyssie")
    

=======
zoznam = [0,1,2,3]

zoznam.append(100)
zoznam.insert(0,200)

zoznam.remove(3)
print(zoznam)
>>>>>>> 36bb11240ea46d7461a66da311d6e39e3fc7a012
