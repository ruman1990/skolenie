# vyrobime skladovy softver
# textove menu s volbami
    # ukoncenie programu
    # vypis skladu
    # pridanie tovaru na sklad
    # naskladnenie
    # vyskladnenie
    # nastavenie ceny tovaru
    # sucet ceny tovarov
    # odstranenie tovaru zo skladu
    # exportovat sklad
    # importovat sklad
produkty = [["banany",1.5,50],["jablka",2.5,40],["pomarance",1.5,20]]

def vypis_produktov():
    for x in produkty:
        print(f"{x[0]:{max(q)}} cena je {x[1]:6.2f}€, pocet kusov {x[2]:6}, celkova cena {x[1]*x[2]:6.2f}€")

def pridanie_produktu():
    nazov = input("Zadaj nazov produktu: ")
    for x in produkty:
        if nazov in x[0]:
            print("Zadany produkt uz existuje")
            return
    cena = float(input("zadaj cenu: "))
    pocet = int(input("pocet kusov: "))
    produkty.append([nazov,cena,pocet])
    print("Pridanie produktu bolo uspesne")

def odobranie_produktu():
    nazov = input("Zadaj nazov produktu: ")
    for x in produkty:
        if nazov in x[0]:
            produkty.remove(x)
            print("Odobranie produktu bolo uspesne")
            return
    print("Produkt sa nenasiel!")

def celkova_cena():
    spolu = 0
    for x in produkty:
        spolu += (x[1]*x[2])
    print(f"Celkova cena je {spolu}€")

while True:
    print("-----MENU-----")
    print("1. vypis skladu")
    print("2. pridanie produktu na sklad")
    print("3. odstranenie tovaru zo skladu")
    print("4. celkova cena produktov")
    print("0. ukoncenie programu")

    volba = input("zadaj svoju volbu: ")

    if volba == "1":
        vypis_produktov()
    elif volba == "2":
        pridanie_produktu()
    elif volba == "3":
        odobranie_produktu()
    elif volba == "4":
        celkova_cena()
    elif volba == "0":
        break
    else:
        print("nespravna volba!")