# hra hadaj cislo
# budeme si pytat od pouzivatela, aby uhadol cislo
# bude mat 7 pokusov
# ak hada nizsie cislo alebo vyssie tak mu poradime
# tajne cislo bude ako literal
# hra hadaj cislo
# pouzivatel hada cislo 1-100
# tajne cislo ak sa trafi povieme ze vyhral
# ked sa netrafi tak musi hadat znovu
# dajme mu 7 pokusov
import random

secret_number = random.randint(1,100)
pocet_pokusov = 7

while pocet_pokusov > 0:
    number = int(input(f"Hadaj cislo od 1 do 100 (Mas {pocet_pokusov} pokusov): "))
    
    if number > 100 or number < 1:
        print("Zadal si zle cislo")

    if number == secret_number:
        print("Vyhral si!")
        break
    else:
        if number > secret_number:
            print("Hadaj nizsie")
        else:
            print("Hadaj vyssie")

    pocet_pokusov -= 1

if pocet_pokusov==0:
    print(f"Prehral si! Tajne cislo bolo {secret_number}")