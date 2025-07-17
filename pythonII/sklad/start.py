from sklad import Sklad
import export

print("------ SKLAD v1.0 ------")
sklad = Sklad()
while True:
    print("------- MENU ------")
    print("1. Vypis produktov")
    print("2. Pridat produkt")
    print("3. Naskladnit produkt")
    print("4. Vyskladnit produkt")
    print("5. Nastav cenu")
    print("6. Hodnota skladu")
    print("7. Odstranenie produktu")
    print("8. Export skladu")
    print("9. Import skladu")
    print("10. Vypisat dennik")
    print("11. Export do XML")
    print("12. Import z XML")
    print("13. Vyhladat produkt")
    print("0. Ukoncit program")
    
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
    elif volba == '0':
        print("Ukoncenie programu")
        break
    else:
        print("Neplatna volba, Skus znova.")