# hra - hadaj cislo, mas 7 pokusov, ak uhadnes vyhral si.
# cislo moze byt od 0 do 100
# ked neuhadne, tak mu povieme, ci hadane cislo je mensie alebo je vacsie
import random

secret_number = random.randint(0,100)

pocet_pokusov = 7
vyhral = False
while pocet_pokusov > 0:
    number = int(input(f'Hadaj cislo od 0 do 100 (Mas este {pocet_pokusov} pokusov): '))

    if number == secret_number:
        print('Vyhral si!')
        vyhral = True
        break
    else:
        print('Neuhadol si')
        pocet_pokusov = pocet_pokusov - 1
        if number < secret_number:
            print("Cislo je vacsie")
        else:
            print("Cislo je mensie")
if not vyhral:
    print('Minul si vsetky pokusy a neuhadol si.')



