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

products = [["voda",1.5,20],["chlieb",2,50],["cola",2.5,10]]

def vypis_skladu():
    for x in products:
        print(f"Nazov {x[0]}, cena {x[1]}€, pocet kusov {x[2]}")

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in products:
        if nazov == x[0]:
            print("Produkt uz je evidovany na sklade")
            return
    try:
        cena = float(input("Zadaj cenu tovaru: "))
        pocet_kusov = int(input("Zadaj pocet kusov tovaru: "))
    except:
        print("Zadal si zlu hodnotu")
        return
    products.append([nazov,cena,pocet_kusov])
    print("Tovar bol uspesne pridany")

def odstranenie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    found = -1
    for i,x in enumerate(products):
        if nazov == x[0]:
            found = i
            break
    if found >= 0:
        products.pop(found)
        print("Tovar bol uspesne odstraneny")
    else:
        print("Tovar sa nenasiel")

def celkova_cena():
    suma = 0
    for x in products:
        suma += x[1]*x[2]
    print(f"Celkova suma tovarov je {suma}€")

while True:
    print('-----MENU-----')
    print('1. vypis skladu')
    print('2. pridanie tovaru')
    print('3. odstranenie tovaru')
    print('4. celkova cena tovarov')
    print('0. ukoncenie programu')

    volba = input("Zadaj svoju volbu: ")
    volba = volba.strip()

    match volba:
        case "0":
            print("Program ukonceny")
            break
        case "1":
            vypis_skladu()
        case "2":
            pridanie_tovaru()
        case "3":
            odstranenie_tovaru()
        case "4":
            celkova_cena()