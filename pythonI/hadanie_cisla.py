import random

<<<<<<< HEAD
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
vyherne_cislo = random.randint(0,100)
number = int(input("Hadaj cislo 0-100: "))
pocet_pokusov = 6
while number != vyherne_cislo:
    pocet_pokusov -= 1
    if pocet_pokusov == 0:
        break
    if number < vyherne_cislo:
        print("Hadaj vyssie!")
    else:
        print("Hadaj nizsie!")

    number = int(input(f"Hadaj cislo 0-100 (Zostavajucich pokusov {pocet_pokusov}): "))

if pocet_pokusov == 0:
    print("Prehral si!")
else:
    print("Vyhral si!")
>>>>>>> 36bb11240ea46d7461a66da311d6e39e3fc7a012
