import random

print("Vitaj v hre")
level = input("Vyber si obtiaznost (1. lahka, 2. stredna, 3. tazka): ")

secret = random.randint(1,100)
if level == '1':
    pocet_pokusov = 10
elif level == '2':
    pocet_pokusov = 7
else:
    pocet_pokusov = 6

while True:
    number = int(input(f"Hadaj cislo (1-100) Mas este {pocet_pokusov} pokusov: "))

    if number == secret:
        print("uhadol si!")
        break
    elif number < secret and number >= 1:
        print("zadal si mensie cislo")
    elif number > secret and number <= 100:
        print("zadal si vacsie cislo")
    else:
        print("zadal si cislo mimo rozsah")
    pocet_pokusov -= 1
    if pocet_pokusov == 0:
        print(f"Prehral si! Tajne cislo bolo {secret}.")
        break
