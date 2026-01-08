import random

secret_number = random.randint(1,100)

pocet_pokusov = 0

while pocet_pokusov < 7: 
    cislo = int(input(f'Hadaj cislo (Zostavajuce pokusy {7 - pocet_pokusov}): '))
    if cislo == secret_number:
        print('Vyhral si')
        break
    elif cislo < secret_number:
        print('Vacsie')
    else:
        print('Mensie')
    pocet_pokusov += 1

if pocet_pokusov == 7:
    print('Prehral si!')


