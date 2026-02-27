from sklad import Sklad

sklad = Sklad()

while True:
    print('-----MENU------')
    print('0. ukoncenie programu')
    print('1. vypis skladu')
    print('2. pridanie tovaru na sklad')
    print('3. sucet ceny tovarov')
    print('4. odstranenie tovaru zo skladu')
    volba = input("Zadaj svoju volbu: ")
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()
    elif volba == '3':
        sklad.sucet_ceny()
    elif volba == '4':
        sklad.odstranenie_tovaru()