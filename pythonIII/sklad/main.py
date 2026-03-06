from sklad import Sklad

import gettext

lang = gettext.translation('messages', localedir='translations', languages=['zh'])
lang.install()

sklad = Sklad()

while True:
    print('-----MENU------')
    print(_('0. ukoncenie programu'))
    print(_('1. vypis skladu'))
    print(_('2. pridanie tovaru na sklad'))
    print(_('3. sucet ceny tovarov'))
    print(_('4. odstranenie tovaru zo skladu'))
    print(_('5. exportovanie skladu do CSV'))
    print(_('6. exportovanie skladu do JSON'))
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
    elif volba == '5':
        sklad.export_skladu("csv")
    elif volba == '6':
        sklad.export_skladu("json")