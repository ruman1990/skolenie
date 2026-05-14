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
from produkt import Produkt
from datetime import datetime

class Sklad:
    def __init__(self):
        self.produkty = {}
        with open("data.txt",'r',encoding='utf-8') as f:
            for x in f:
                values = x.split(',')  # ['voda',2,100]
                self.produkty[values[0]] = Produkt(values[0],values[1],values[2])

    def pridanie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty:
            print("Tovar uz existuje")
            return
        cena = Decimal(input("Zadaj cenu tovaru: "))
        pocet_kusov = int(input("Zadaj pocet kusov tovaru: "))
        self.produkty[nazov] = (Produkt(nazov,cena,pocet_kusov))
        print("Tovar bol uspesne pridany.")
        self.ulozit_sklad()
        self.log(f'Tovar bol uspesne pridany. {nazov}')

    def ulozit_sklad(self):
        with open("data.txt",'w',encoding='utf-8') as f:
            for x in self.produkty:
                f.write(self.produkty[x].export_format())
                f.write("\n")

    def log(self,message):
        with open("log.txt",'a',encoding="utf-8") as f:            
            f.write(f"[{datetime.now()}] {message}")
            f.write("\n")


    def vypis_skladu(self):
        for x in self.produkty:
            print(self.produkty[x])


