import random

secret_number = random.randint(1,100)
number = -1
counter = 6
while number!=secret_number:
    number = int(input(f"Hadaj cislo od 1 do 100 (Pocet pokusov {counter}): "))
    counter -= 1
    if number == secret_number:
        print("Vyhral si!")
        break
    elif number < secret_number:
        print('Hadaj vacsie cislo')
    else:
        print('Hadaj mensie cislo')

    if counter == 0:
        print('Prehral si!')
        break