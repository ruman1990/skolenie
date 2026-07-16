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

nazvy = ["muka","chlieb","voda"]
ceny = [1.5,2.5,1]
pocty = [20,50,40]

def vypis_skladu():
    for i,x in enumerate(nazvy):
        print(f"{x} cena: {ceny[i]:.2f}€ pocet kusov: {pocty[i]}")

def pridanie_produktu():
    nazov = input("Zadaj nazov produktu: ")
    cena = float(input("Zadaj cenu produktu: "))
    pocet_kusov = int(input("Zadaj pocet kusov produktu: "))
    nazvy.append(nazov)
    ceny.append(cena)
    pocty.append(pocet_kusov)
    print("Produkt bol uspesne pridany")

def odstranenie_produktu():
    nazov = input("Zadaj nazov produktu: ")
    index = nazvy.index(nazov)
    nazvy.pop(index)
    ceny.pop(index)
    pocty.pop(index)
    print("Produkt bol uspesne odstraneny")

while True:
    print("-----MENU-----")
    print("1. Vypis skladu")
    print("2. pridanie produktu na sklad")
    print("3. odobratie produktu zo skladu")
    print("0. ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")

    if volba == '0':
        print("Program sa ukoncuje")
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_produktu()
    elif volba == '3':
        odstranenie_produktu()
    else:
        print("Nespravna volba")