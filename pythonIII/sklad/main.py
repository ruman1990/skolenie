from sklad import Sklad
def display_menu():
    print('Skladovy softver 1.0')
    print(f'{'-'*10}MENU{'-'*10}')
    print('0. Ukoncit program')
    print('1. Vypis skladu')
    print('2. Pridanie tovaru na sklad')   
    print('3. Naskladnenie tovaru')
    print('4. Vyskladnenie tovaru')
    print('5. Nastavenie ceny tovaru')
    print('6. Sucet ceny tovarov na sklade')
    print('7. Odstranenie tovaru zo skladu')
    print('8. Exportovat sklad do stringu')
    print('9. Importovat sklad zo stringu')

sklad = Sklad('test')

while True:
    display_menu()
    volba = input('Zadaj svoju volbu: ')
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()
    elif volba == '3':
        sklad.naskladnenie()
    elif volba == '4':
        sklad.vyskladnenie()
    elif volba == '5':
        sklad.nastav_cenu()
    elif volba == '6':
        sklad.hodnota_skladu()
    elif volba == '7':
        sklad.odstranenie_tovaru()
    elif volba == '8':
        sklad.export_skladu()
    elif volba == '9':
        sklad.import_skladu()

