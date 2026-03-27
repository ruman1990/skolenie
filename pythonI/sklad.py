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

produkty = [["voda",25,1.5],["mlieko",50,2],["chlieb",40,2.5]]

def hodnota_skladu():
    suma = 0
    for x in produkty:
        suma += x[1] * x[2]
    print(f"Celkova hodnota skladu je {suma}€")

def odstranenie_tovaru():
    product_name = input("Zadaj nazov produktu: ")
    found = False
    for x in produkty:
        if product_name in x:
            produkty.remove(x)
            found = True
            print("Zadany tovar bol odstraneny")
            break
    if not found:
        print("Zadany tovar neexistuje")

def pridanie_tovaru():
    product_name = input("Zadaj nazov produktu: ")
    if product_name in produkty:
        print("Zadany produkt uz existuje")
    else:
        pocet_kusov = int(input("Zadaj pocet kusov"))
        cena = float(input("Zadaj jednotkovu cenu"))
        produkty.append([product_name,pocet_kusov,cena])
        print("Produkt bol pridany do skladu")

def vypis_skladu():
    for x in produkty:
        print(f'Produkt {x[0]}, pocet {x[1]}ks, cena {x[2]}€')

while True:
    print("-"*10+'MENU'+"-"*10)
    print("0. ukoncenie programu")
    print("1. vypis skladu")
    print("2. pridanie tovaru")
    print("3. odstranenie tovaru")
    print("4. hodnota skladu")
    volba = input("Zadaj volbu: ")

    if volba == "0":
        print("Koniec")
        break
    elif volba == "1":
        vypis_skladu()
    elif volba == "2":
        pridanie_tovaru()
    elif volba == "3":
        odstranenie_tovaru()
    elif volba == "4":
        hodnota_skladu()
    else:
        print("Neplatna volba")
