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

class Sklad:
    def __init__(self):
        self.produkty = {"voda" : Produkt('voda',1.5,10),"chlieb" : Produkt('chlieb',2,20),"jogurt" : Produkt('jogurt',0.5,10)}

    def pridanie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty:
            print("Tovar uz existuje")
            return
        cena = Decimal(input("Zadaj cenu tovaru: "))
        pocet_kusov = int(input("Zadaj pocet kusov tovaru: "))
        self.produkty[nazov] = (Produkt(nazov,cena,pocet_kusov))
        print("Tovar bol uspesne pridany.")

    def vypis_skladu(self):
        for x in self.produkty:
            print(self.produkty[x])


class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet
    def __str__(self):
        return f"Produkt {self.nazov}, cena {self.cena:.2f}€, pocet {self.pocet}"



sklad = Sklad()

while True:

    print("-----MENU-----")
    print("1. Vypis skladu")
    print("2. Pridanie tovaru na sklad")
    print("0. Ukoncenie programu")

    volba = input("Zadaj svoju volbu: ")
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()