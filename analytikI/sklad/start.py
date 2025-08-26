from sklad import Sklad


import gettext

lang = gettext.translation('messages', localedir='translations', languages=['sk'])
lang.install()



volby = [
    _("1. Vypísať zoznam produktov na sklade"),
    _("2. Pridať produkt do skladu"),
    _("3. Odstrániť produkt"),
    _("4. Nastavenie ceny produktu"),
    _("5. Naskladnenie produktu"),
    _("6. Vyskladnenie produktu"),
    _("7. Hodnota skladu"),
    _("8. Export skladu"),
    _("9. Import skladu"),
    _("10. Vypis logu"),
    _("0. Ukoncit program")
]


def menu():
    print(_('Skladovy softver v. 1.0'))
    print('-' * 10,'MENU','-' * 10)
    for x in volby:
        print(x)

sklad = Sklad('Firemny')

while True:
    menu()
    try:
        volba = int(input(_("Zadaj cislo volby: ")))
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
            print(_("Program sa ukoncuje."))
            break
        else:
            print(_("Zadal si neexistujucu volbu !!!"))
    except ValueError:
        print(_("Zadal si zlu volbu!"))
