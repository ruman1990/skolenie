from sklad import Sklad

sklad = Sklad()

while True:
    print("-----MENU-----")
    print("1. Vypis skladu")
    print("2. pridanie produktu na sklad")
    print("3. odobratie produktu zo skladu")
    print("4. sucet ceny tovarov")
    print("5. export skladu")
    print("6. import skladu")
    print("0. ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")

    if volba == '0':
        print("Program sa ukoncuje")
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_produktu()
    elif volba == '3':
        sklad.odstranenie_produktu()
    elif volba == '4':
        sklad.cena_tovarov()
    elif volba == '5':
        sklad.export_skladu()
    elif volba == '6':
        sklad.import_skladu()
    else:
        print("Nespravna volba")