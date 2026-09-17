# hra hadaj cislo
# budeme si pytat od pouzivatela, aby uhadol cislo
# bude mat 7 pokusov
# ak hada nizsie cislo alebo vyssie tak mu poradime
# tajne cislo bude ako literal
import random
secret_number = random.randint(1,100)
pokusy = 7
while pokusy > 0:
    number = input(f"Hadaj cislo od 1 do 100 (Pocet pokusov {pokusy}): ")
    if not number.isdigit():
        print("Zadal si zle cislo")
        continue
    else:
        number = int(number)
    pokusy -= 1
    if secret_number == number:
        print("Uhadol si!")
        break
    elif pokusy == 0:
        print(f"Prehral si! Tajne cislo bolo {secret_number}")
    elif secret_number > number:
        print("Hadaj vyssie")
    elif secret_number < number:
        print("Hadaj nizsie")


