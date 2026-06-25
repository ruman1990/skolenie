# vyrobime skladovy softver
# textove menu s volbami
    # ukoncenie programu
    # vypis skladu
    # pridanie tovaru na sklad
    # naskladnenie
    # vyskladnenie
    # nastavenie ceny tovaru
    # sucet ceny tovarov
    # odstranenie tovaru zo skladu
    # exportovat sklad
    # importovat sklad
from sklad import Sklad

sklad = Sklad()

while True:
    print("-----MENU-----")
    print("1. vypis skladu")
    print("2. pridanie produktu na sklad")
    print("3. odstranenie tovaru zo skladu")
    print("4. celkova cena produktov")
    print("5. naskladnenie")
    print("6. vyskladnenie")
    print("7.export skladu")
    print("0. ukoncenie programu")

    volba = input("zadaj svoju volbu: ")

    if volba == "1":
        sklad.vypis_produktov()
    elif volba == "2":
        sklad.pridanie_produktu()
    elif volba == "3":
        sklad.odobranie_produktu()
    elif volba == "4":
        sklad.celkova_cena()
    elif volba == "5":
        sklad.naskladnenie()
    elif volba == "6":
        sklad.vyskladnenie()
    elif volba == "7":
        sklad.export_skladu()
    elif volba == "0":
        break
    else:
        print("nespravna volba!")