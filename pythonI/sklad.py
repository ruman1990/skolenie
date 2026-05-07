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
from decimal import Decimal
produkty = [['voda',1.5,10],['chlieb',2,20],['jogurt',0.5,10]]

def pridanie_tovaru():
    nazov = input("Zadaj nazov tovaru: ")
    for x in produkty:
        if nazov == x[0]:
            print("Tovar uz existuje")
            return
    cena = Decimal(input("Zadaj cenu tovaru: "))
    pocet_kusov = int(input("Zadaj pocet kusov tovaru: "))
    produkty.append([nazov,cena,pocet_kusov])
    print("Tovar bol uspesne pridany.")

while True:

    print("-----MENU-----")
    print("1. Vypis skladu")
    print("2. Pridanie tovaru na sklad")
    print("0. Ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")
    if volba == '0':
        break
    elif volba == '1':
        for x in produkty:
            print(f"Produkt {x[0]}, cena {x[1]:.2f}€, pocet {x[2]}")
    elif volba == '2':
        pridanie_tovaru()