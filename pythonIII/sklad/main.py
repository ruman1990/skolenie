from sklad import Sklad
import gettext

lang = gettext.translation('messages', localedir='translations', languages=['zh'])
lang.install()

sklad = Sklad()



while True:

    print(_("-----MENU-----"))
    print(_("1. Vypis skladu"))
    print(_("2. Pridanie tovaru na sklad"))
    print(_("0. Ukoncenie programu"))

    volba = input(_("Zadaj svoju volbu: "))
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()