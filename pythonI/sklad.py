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

def vypis_skladu():
    for x in produkty:
        print(f"{x[0]:15}, cena {x[1]:10.2f}€, pocet kusov {x[2]:10}")

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov in x:
            print("Tovar uz existuje")
            return
    cena = float(input("Zadaj cenu: "))
    pocet = int(input("Zadaj pocet kusov: "))
    produkty.append([nazov,cena,pocet])

def odstranenie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for i,x in enumerate(produkty):
        if nazov in x:
                produkty.pop(i)

produkty = [["voda",1.0,50],["cola",2.5,100],["pepsi",2,250]]
#              0     1   2
while True:
    print("-----MENU-----")
    print("1. vypis obsahu skladu")
    print("2. pridat tovar")
    print("3. odobrat tovar")
    print("4. hodnota tovaru na sklade")
    print("0. ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")

    if volba == "1":
        print()
        vypis_skladu()
        print()
    elif volba == "2":
        pridanie_tovaru()
    elif volba == "3":
        odstranenie_tovaru()
    elif volba == "4":
        pass
    elif volba == "0":
        break
    else:
        print("Zadal si zlu volbu")
