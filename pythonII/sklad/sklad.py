# Chceme spravit program pre manazment skladu
# budeme mat textove rozhranie - MENU
# vypis produktu, pridat_produkt, odstran_produkt
# naskladnit, vyskladnenie, nastavenie ceny
# zobrazit sumu, exportovat zo skladu, import do skladu
from produkt import Produkt
from audit import Audit
import re

class Sklad:
    def __init__(self):
        self.audit = Audit()
        self.produkty = { "voda" : Produkt("voda",5,1.5), "chlieb": Produkt("chlieb",10,2.5) }

    # Produkt: nazov X ks XX.XX €
    def vypis_produktov(self):
        for x in self.produkty.values():
            print(x)
        self.audit.zapis(f"Boli vypisane produkty")
        print('')

    def pridanie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            print("Produkt uz existuje.")
            self.audit.zapis(f"Pridanie produktu {nazov} - Chyba: Produkt uz existuje")
        else:
            self.produkty[nazov] = Produkt(nazov)
            print("Produkt bol pridany.")
            self.audit.zapis(f"Pridanie produktu {nazov}")

    def naskladnit(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov produktu: "))
            self.produkty[nazov].pocet += kusy
            print("Produkt naskladneny")
            self.audit.zapis(f"Naskladnenie {nazov}")
        else:
            print("Produkt nie je na sklade")
            self.audit.zapis(f"Naskladnenie {nazov} - Chyba: Produkt nie je na sklade")

    def vyskladnit(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov produktu: "))
            if self.produkty[nazov].pocet <= kusy:
                print("Nie je dost tovaru na vyskladnenie")
            else:
                self.produkty[nazov].pocet -= kusy
                print("Produkt vyskladneny")
        else:
            print("Produkt nie je na sklade")

    def nastav_cenu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            cena = float(input("Zadaj cenu za kus produktu: "))
            self.produkty[nazov].cena = cena
            print("Cena bola nastavena")
        else:
            print("Produkt nie je na sklade")

    def celkova_suma(self):
        suma = 0
        for x in self.produkty.values():
            suma += x.cena * x.pocet
        print(f'Celkova hodnota skladu je: {suma:.2f}€')

    def odstranit_produkt(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            print("Produkt bol odstraneny")
            self.audit.zapis(f"Odstranenie produktu {nazov}")
        else:
            print("Produkt nie je na sklade")
            self.audit.zapis(f"Odstranenie produktu {nazov} - Chyba: Produkt nie je na sklade")

    def vypisat_dennik(self):
        self.audit.vypis()

    def vyhladat_nazov(self):
        nazov = input("Zadaj cast nazvu produktu alebo regex: ")
        self.audit.zapis(f"Vyhladavanie v produktoch {nazov}")
        zhody = []
        for p in self.produkty:
            if re.search(nazov,p,re.IGNORECASE):
                zhody.append(p)

        if not zhody:
            print('Zaznam sa nenasiel')
            return
        
        for i in zhody:
            print(f'{i}')

