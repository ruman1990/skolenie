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
# rozdelit skript do modulov
# pridat automaticke ukladanie do suboru
# pridat dennik - log a volbu vypis dennika

from sklad import Sklad

sklad =  Sklad('test')
while True:
    print(f'{'-'*10}MENU{'-'*10}')
    print('0. ukoncenie programu')
    print('1. vypis tovary')
    print('2. hodnota skladu')
    print('3. pridanie tovaru')
    print('4. odobranie tovaru')
    print('5. naskladnenie tovaru')
    print('6. vyskladnenie tovaru')
    print('7. exportovat sklad')
    print('8. import skladu')
    print('9. nastav cenu tovaru')
    print('10. vypis dennik')
    print('11. export do CSV')
    print()
    x = input("Zadaj volbu: ")
    if x == '0':
        break
    elif x == '1':
        sklad.vypis_skladu()
    elif x == '2':
        sklad.hodnota_skladu()
    elif x == '3':
        sklad.pridat_tovar()
    elif x == '4':
        sklad.odobratie_tovaru()
    elif x == '5':
        sklad.naskladnit()
    elif x == '6':
        sklad.vyskladnit()
    elif x == '7':
        sklad.export_print()
    elif x == '8':
        sklad.importovanie_from_user()
    elif x == '9':
        sklad.nastav_cenu()
    elif x == '10':
        sklad.vypis_log()
    elif x == '11':
        sklad.export_csv()
    else:
        print("Neplatna volba")