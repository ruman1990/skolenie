# pouzivatel nech hada tajne cislo a ked uhadne, tak vyhral inak prehral
import random

secret_number = random.randint(1,100)
pocet_pokusov = 7
while(pocet_pokusov > 0):
    number = int(input(f"Hadaj cislo od 1 po 100 (mas {pocet_pokusov} pokusov): "))
    pocet_pokusov -= 1
    if number == secret_number:
        print("Uhadol si!")
        break
    elif number > secret_number:
        print("Hadaj nizsie")
    elif number < secret_number:
        print("Hadaj vyssie")

    if pocet_pokusov == 0:
        print("Prehral si!")
        x = input("Ak chces hrat znovu, zadaj Y: ")
        if x.upper() == 'Y':
            pocet_pokusov = 7
