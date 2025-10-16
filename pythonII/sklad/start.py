
from sklad import Sklad

def vypis_menu():
    print()
    print('-------------MENU-------------')
    print('0. Ukoncenie programu ')
    print('1. Vypis skladu')
    print('2. pridanie tovaru')
    print('3. odobranie tovaru')
    print('4. naskladnenie')
    print('5. vyskladnenie')
    print('6. nastavenie ceny')
    print('7. sucet cien tovarov')
    print('8. exportovat sklad')
    print('9. importovat sklad')
    print('10. vypisanie logu')
    print()

s = Sklad('test')

while True:
    vypis_menu()
    volba = input("Zvol moznost (napriklad 4): ")
    if volba == '0':
        s.zapis_skladu()
        print("Program sa ukoncuje")
        break
    elif volba == '1':
        s.vypis_skladu()
    elif volba == '2':
        s.pridanie_tovaru()
    elif volba == '3':
        s.odobranie_tovaru()
    elif volba == '4':
        s.naskladnenie()
    elif volba == '5':
        s.vyskladnenie()
    elif volba == '6':
        s.nastav_cenu()
    elif volba == '7':
        s.zobraz_sumu()
    elif volba == '8':
        s.export_skladu()
    elif volba == '9':
        s.import_skladu()
    elif volba == '10':
        s.audit.log_vypis()
    else:
        print("Neplatna volba. Skus znova.")