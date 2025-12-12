from sklad import Sklad
import gettext
lang = gettext.translation('messages', localedir='translations', languages=['zh'])
lang.install()

def display_menu():
    print(_('Skladovy softver 1.0'))
    print(_(f'{'-'*10}MENU{'-'*10}'))
    print(_('0. Ukoncit program'))
    print(_('1. Vypis skladu'))
    print(_('2. Pridanie tovaru na sklad'))   
    print(_('3. Naskladnenie tovaru'))
    print(_('4. Vyskladnenie tovaru'))
    print(_('5. Nastavenie ceny tovaru'))
    print(_('6. Sucet ceny tovarov na sklade'))
    print(_('7. Odstranenie tovaru zo skladu'))
    print(_('8. Exportovat sklad do stringu'))
    print(_('9. Importovat sklad zo stringu'))

sklad = Sklad('test')

while True:
    display_menu()
    volba = input(_('Zadaj svoju volbu: '))
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

