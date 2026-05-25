# import random

# secret_number = random.randint(1,100)
# counter = 6
# while True:
#     number = int(input(f"Zadaj cislo 1-100 (Pocet pokusov {counter}): "))
#     counter -= 1
#     if secret_number == number:
#         print("Gratulujem, uhadol si.")
#         break
    
#     if counter == 0:
#         print(f"Prehral si! Tajne cislo bolo {secret_number}")
#         break
#     elif secret_number < number:
#         print("Hadaj nizsie")
#     elif secret_number > number:
#         print("Hadaj vyssie")




# pouzivatel nech hada cislo, a ked uhadne vypiseme vyhral a ked nie, tak prehral
import random

secret_number = random.randint(1,100)
failed = True
for x in range(6,0,-1):
    number = int(input(f"Hadaj cislo od 1 do 100 pocet pokusov {x}: "))

    if secret_number == number:
        print("Vyhral si BINGO!")
        failed = False
        break
    else:
        if secret_number < number:
            if x > 1:
                print("Neuhadol si, hadaj nizsie!")
        else:
            if x > 1:
                print("Neuhadol si, hadaj vyssie!")

if failed:
    print("Prehral si!")