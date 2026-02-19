import random

secret_number = random.randint(0,100)
pocet_pokusov = 6
while pocet_pokusov > 0:
    guess_number = int(input(f"Hadaj cislo (0-100), zostava {pocet_pokusov} pokusov: "))
    
    if guess_number < secret_number:
        print('too low')
    elif guess_number > secret_number:
        print('too high')
    else:
        print('You won')
        break
    pocet_pokusov -= 1
if pocet_pokusov == 0:
    print('You failed. Play again.')

