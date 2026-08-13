# hra hadaj cislo
# budeme si pytat od pouzivatela, aby uhadol cislo
# bude mat 7 pokusov
# ak hada nizsie cislo alebo vyssie tak mu poradime
# tajne cislo bude ako literal
import random


tajne_cislo = random.randint(1,100)
pokusy = 7

while pokusy > 0:
    number = int(input(f"Hadaj cislo od 1-100 (Mas {pokusy} pokusov): "))
    if number == tajne_cislo:
        print("Uhadol si")
        break
    elif number < tajne_cislo:
        print("Hadaj vyssie")
    else:
        print("Hadaj nizsie")
    pokusy -= 1

if pokusy==0:
    print("Prehral si")