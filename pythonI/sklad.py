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
    print()
    for x in produkty:
        print(f'Nazov: {x[0]},cena: {x[1]}€, pocet kusov {x[2]}')
    print()

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov == x[0]:
            print("Produkt uz existuje")
            return
    cena = float(input("Zadaj cenu tovaru: "))
    pocet = int(input("Zadaj pocet kusov: "))
    produkty.append([nazov,cena,pocet])
    print("Produkt bol uspesne pridany")

def odstranenie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov == x[0]:
            produkty.remove(x)
            print("Tovar bol uspesne odstraneny")
            return
    print("Tovar sa nenasiel")

def sucet_ceny():
    suma = 0
    for x in produkty:
        suma = suma + (x[1]*x[2])
    print(suma)

produkty = [["voda",2.5,50],["mlieko",1.5,100],["pivo",1,250]]

while True:
    print('-----MENU------')
    print('0. ukoncenie programu')
    print('1. vypis skladu')
    print('2. pridanie tovaru na sklad')
    print('3. sucet ceny tovarov')
    print('4. odstranenie tovaru zo skladu')
    volba = input("Zadaj svoju volbu: ")
    if volba == '0':
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        sucet_ceny()
    elif volba == '4':
        odstranenie_tovaru()
