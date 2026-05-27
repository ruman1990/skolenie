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

def vypis_skladu():
    for x in products:
        print(f"{x[0]}, cena {x[1]}€, pocet kusov {x[2]}")

def kontrola_nazvu(nazov):
    for x in products:
        if nazov == x[0]:
            return True
    return False
        
def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    if kontrola_nazvu(nazov) == True:
        print("Zadany tovar uz existuje")
        return
    try:
        cena = float(input("Zadaj cenu: "))
        pocet = int(input("Zadaj pocet kusov: "))
        if cena <= 0:
            raise Exception()
    except ZeroDivisionError:
        print("delilo sa nulou")
    except Exception:
        print("Zadal si zle cenu alebo pocet kusov")
        return
    finally:
        print("Toto sa vykona vzdy")
    products.append([nazov,cena,pocet])
    print("Produkt uspesne pridany")

def odobratie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    if kontrola_nazvu(nazov) == True:
        for i,x in enumerate(products):
            if nazov == x[0]:
                products.pop(i)
                print("Produkt uspesne odstraneny")
                return
    else:
        print("Zadany produkt neexistuje")

def vypis_ceny():
    suma = 0
    for x in products:
        suma += (x[1] * x[2])
    print(f"Celkova cena tovarov je {suma:.2f}€")

products = [["voda",2,10],["chlieb",2.5,20],["cola",2,60]]


print("-----MENU-----")
print("1. vypis skladu")
print("2. pridat tovar na sklad")
print("3. odobrat tovar zo skladu")
print("4. vypis ceny tovarov")
print("0. ukoncenie programu")
while True:
    
    volba = input("Zadaj svoju volbu: ")

    if volba == "1":
        vypis_skladu()
    elif volba == "2":
        pridanie_tovaru()
    elif volba == "3":
        odobratie_tovaru()
    elif volba == "4":
        vypis_ceny()
    elif volba == "0":
        break
    else:
        print("Neplatna volba")