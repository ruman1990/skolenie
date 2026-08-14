# skladovy softver
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
# produkty maju - nazov, cena, pocet kusov

def vypis_skladu():
    for x in produkty:
        print(f"{x[0]}, cena {x[1]}€, pocet kusov {x[2]}")

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov in x:
            print("Zadany produkt uz existuje")
            return
    cena = float(input("Zadaj cenu: "))
    pocet_kusov = int(input("Zadaj pocet kusov: "))
    produkty.append([nazov,cena,pocet_kusov])
    print("Pridanie tovaru bolo uspesne")

def odobratie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov in x:
            produkty.remove(x)
            print("Odobratie tovaru bolo uspesne")
            return
    print("Zadany tovar neexistuje")

def sucet_ceny():
    sucet = 0
    for x in produkty:
        sucet += x[1]*x[2]
    print(f"Hodnota skladu je {sucet:.2f}€")

produkty = [["voda",2.5,20],["chlieb",2,50],["muka",1,100]]

nazvy = ["voda","chlieb","muka"]
ceny = [2.5,2,1]
pocty = [20,50,100]

while True:
    print("-----MENU-----")
    print("1. vypis skladu")
    print("2. pridanie tovaru")
    print("3. odobratie tovaru")
    print("4. sucet ceny tovarov")
    print("0. ukoncenie programu")
    volba = input("Zadaj svoju volbu: ")

    if volba == '0':
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        odobratie_tovaru()
    elif volba == '4':
        sucet_ceny()
    else:
        print("Nespravna volba")