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

sklad = Sklad("test")

while True:
    print("-----MENU-----")
    print("1. vypis skladu")
    print("2. pridanie tovaru")
    print("3. odobratie tovaru")
    print("4. hodnota skladu")
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
    else:
        print()
        print("Zadal si zlu volbu.")