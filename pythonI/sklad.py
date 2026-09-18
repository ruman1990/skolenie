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
produkty = [["voda",2.5,50],["cola",2,100],["pepsi",2.20,150]]

def vypis_skladu():
    for x in produkty:
        print(f"nazov produktu {x[0]:10}, jednotkova cena {x[1]:10}€, pocet kusov {x[2]:10}")

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov == x[0]:
            print("Zadany tovar uz existuje")
            return
    cena = float(input("Zadaj cenu: "))
    pocet = int(input("Zadaj pocet kusov: "))
    produkty.append([nazov,cena,pocet])
    print("Produkt bol uspesne pridany")

def odobratie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov == x[0]:
            produkty.remove(x)
            print("Tovar bol uspesne odstraneny")
            return
    print("Zadany produkt sa nenasiel")

def hodnota_skladu():
    hodnota = 0
    for x in produkty:
        hodnota += x[1] * x[2]
    print(f"Hodnota skladu je {hodnota}")

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
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        odobratie_tovaru()
    elif volba == '4':
        hodnota_skladu()
    else:
        print()
        print("Zadal si zlu volbu.")