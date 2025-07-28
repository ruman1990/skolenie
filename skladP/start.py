from sklad import Sklad
import export

import gettext

lang = gettext.translation('messages', localedir='translations', languages=['zh'])
lang.install()

print("------ SKLAD v1.0 ------")
sklad = Sklad()
while True:
    print("------- MENU ------")
    print(_("1. Vypis produktov"))
    print(_("2. Pridat produkt"))
    print(_("3. Naskladnit produkt"))
    print(_("4. Vyskladnit produkt"))
    print(_("5. Nastav cenu"))
    print(_("6. Hodnota skladu"))
    print(_("7. Odstranenie produktu"))
    print(_("8. Export skladu"))
    print(_("9. Import skladu"))
    print(_("10. Vypisat dennik"))
    print(_("11. Export do XML"))
    print(_("12. Import z XML"))
    print(_("13. Vyhladat produkt"))
    print(_("14. Export do CSV"))
    print(_("15. Import z CSV"))
    print(_("0. Ukoncit program"))
    
    volba = input("Zvol moznost: ")
    if volba == '1':
        sklad.vypis_produktov()
    elif volba == '2':
        sklad.pridanie_produktu()
    elif volba == '3':
        sklad.naskladnit()
    elif volba == '4':
        sklad.vyskladnit()
    elif volba == '5':
        sklad.nastav_cenu()
    elif volba == '6':
        sklad.celkova_suma()
    elif volba == '7':
        sklad.odstranit_produkt()
    elif volba == '8':
        export.export_skladu(sklad)
    elif volba == '9':
        export.import_skladu(sklad)
    elif volba == '10':
        sklad.vypisat_dennik()
    elif volba == '11':
        export.export_skladu_xml(sklad)
    elif volba == '12':
        export.import_skladu_xml(sklad)
    elif volba == '13':
        sklad.vyhladat_nazov()
    elif volba == '14':
        export.export_skladu_csv(sklad)
    elif volba == '15':
        export.import_skladu_csv(sklad)
    elif volba == '0':
        print(_("Ukoncenie programu"))
        sklad.zavri()
        break
    else:
        print(_("Neplatna volba, Skus znova."))