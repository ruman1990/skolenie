import random

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