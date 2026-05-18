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