from sklad import Sklad

volby = [
    "1. Vypísať zoznam produktov na sklade",
    "2. Pridať produkt do skladu",
    "3. Odstrániť produkt",
    "4. Nastavenie ceny produktu",
    "5. Naskladnenie produktu",
    "6. Vyskladnenie produktu",
    "7. Hodnota skladu",
    "8. Export skladu",
    "9. Import skladu",
    "10. Vypis logu",
    "0. Ukoncit program"
]


def menu():
    print('Skladovy softver v. 1.0')
    print('-' * 10,'MENU','-' * 10)
    for x in volby:
        print(x)

sklad = Sklad('Firemny')

while True:
    menu()
    try:
        volba = int(input("Zadaj cislo volby: "))
        if volba == 1:
            sklad.vypis_produkty()
        elif volba == 2:
            sklad.pridaj_produkt()
        elif volba == 3:
            sklad.odstran_produkt()
        elif volba == 4:
            pass
        elif volba == 5:
            sklad.naskladnit()
        elif volba == 6:
            sklad.vyskladnit()
        elif volba == 7:
            sklad.zobraz_sumu()
        elif volba == 8:
            sklad.export_skladu()
        elif volba == 9:
            sklad.import_skladu()
        elif volba == 10:
            sklad.log.vypis()
        elif volba == 0:
            print("Program sa ukoncuje.")
            break
        else:
            print("Zadal si neexistujucu volbu !!!")
    except ValueError:
        print("Zadal si zlu volbu!")
