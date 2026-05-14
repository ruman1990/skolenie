from sklad import Sklad

sklad = Sklad()

while True:

    print("-----MENU-----")
    print("1. Vypis skladu")
    print("2. Pridanie tovaru na sklad")
    print("0. Ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()