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
from produkt import Produkt
class Sklad:

    def __init__(self,nazov='test'):
        self.nazov = nazov
        self.produkty = {}
        with open(nazov + '.csv','r',encoding='UTF-8') as f:
             for x in f:
                res = x.split(',')
                self.produkty[res[0]] = Produkt(res[0],res[1],res[2])     

    def vypis_skladu(self):
        print()
        for x in self.produkty:
            print(self.produkty[x])
        print()

    def pridanie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty.keys():
                print("Produkt uz existuje")
                return
        cena = float(input("Zadaj cenu tovaru: "))
        pocet = int(input("Zadaj pocet kusov: "))
        self.produkty[nazov] = Produkt(nazov,cena,pocet)
        print("Produkt bol uspesne pridany")

    def odstranenie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty.keys():
                del self.produkty[nazov]
                print("Tovar bol uspesne odstraneny")
                return
        print("Tovar sa nenasiel")

    def sucet_ceny(self):
        suma = 0
        for x in self.produkty.values():
            suma = suma + (x.cena*x.pocet)
        print(suma)

    


