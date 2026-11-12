# vytvorime jednoduche textove menu
# pouzivatel zvoli volbu a vykoname potrebnu akciu
# skladovy softver, ukladame si udaje o produktoch
# nazov, cena, pocet kusov na sklade
# vypis obsah skladu
# pridat tovar na sklad
# odobrat tovar zo skladu
# zobrazit hodnotu tovaru na sklade
# naskladnenie
# vyskladnenie
# produkt sa sklada v poradi nazov, cena, pocet kusov
#produkty = [["voda",2.5,50],["cola",2,100],["pepsi",2.20,150]]
from sklad import Sklad
import os

sklad = Sklad("sklad")

while True:
    print("-----MENU-----")
    print("1. vypis skladu")
    print("2. pridanie tovaru")
    print("3. odobratie tovaru")
    print("4. hodnota skladu")
    print("5. export do csv")
    print("6. export do json")
    print("0. ukoncenie programu")
    print()
    volba = input("Zadaj volbu z MENU: ")

    if volba == '0':
        print()
        print("Dovidenia")
        break
    elif volba == '1':
        print("Vypis skladu")
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()
    elif volba == '3':
        sklad.odobratie_tovaru()
    elif volba == '4':
        sklad.hodnota_skladu()
        sklad._ulozenie_do_databazy()
    elif volba == '5':
        sklad.export_skladu('csv')
    elif volba == '6':
        sklad.export_skladu('json')
    else:
        print()
        print("Zadal si zlu volbu.")