# pouzivatel nech hada tajne cislo a ked uhadne, tak vyhral inak prehral
import random

def get_pokusy_format(pokusy):
    match pokusy:
        case 7 | 6 | 5:
            return f"{pokusy} pokusov"
        case 4 | 3 | 2:
            return f"{pokusy} pokusy"
        case 1:
            return f"{pokusy} pokus"

secret_number = random.randint(1,100)
pocet_pokusov = 7
while(pocet_pokusov > 0):
    number = int(input(f"Hadaj cislo od 1 po 100 (mas {get_pokusy_format(pocet_pokusov)}): "))
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
