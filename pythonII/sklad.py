# Chcem vytvori skladovy softver
# Bude mat textove menu s volbami
# ked klient vyberie volbu, zadane potrebne vstupne udaje, volba sa vykona
# Po vykonani zvolenej volby sa zobrazi znovu MENU s volbami
# Pre ukoncenie programu je potrebne mat vlastnu volbu.
# 1. Vypisat zoznam produktov na sklade
# 2. Pridat produkt do skladu
# 3. Odstranit produkt
# 4. Nastavenie ceny produktu
# 5. Naskladnenie produktu
# 6. Vyskladnenie produktu
# 7. Hodnota skladu
# 8. Export skladu
# 9. Import skladu

class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return (f'Nazov {self.nazov}, Cena {self.cena:.2f}€, Pocet {self.pocet}ks')
    
    def export_tvar(self):
        return f'{self.nazov};{self.cena};{self.pocet}'

class Sklad:
    def __init__(self,nazov):
        self.nazov = nazov
        self.produkty = { 'voda' : Produkt('voda',2.5,20), 
                         'chlieb' : Produkt('chlieb',1.5,50), 
                         'muka' : Produkt('muka',0.80,30) }

    def vypis_produkty(self):
        print('')
        for p in self.produkty.values():
            print(p)
        print('')

    def pridaj_produkt(self):
        print('')
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            print('Produkt uz existuje')
        else:
            cena = float(input("Zadaj cenu produktu: "))
            pocet = int(input("Zadaj pocet kusov: "))
            self.produkty[nazov] = Produkt(nazov,cena,pocet)
            print('Produkt bol uspesne pridany do skladu')

    def odstran_produkt(self):
        nazov = input("Zadaj nazov produktu na odstranenie: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            print("Produkt bol odstraneny.")
        else:
            print('Produkt sa nenasiel.')

    def zobraz_sumu(self):
        suma = 0.0
        for p in self.produkty.values():
            suma += (p.cena * p.pocet)
        print(f'Celkova hodnota skladu: {suma:.2f}€')

    def export_skladu(self):
        vystup = []
        for p in self.produkty.values():
            vystup.append(p.export_tvar())
        retazec = '|'.join(vystup)
        print('====EXPORT TEXT====')
        print(retazec)
        print('====Skopiruj a uloz====')

    def import_skladu(self):
        text = input("Vloz vstupny text: ")
        zoznam_produktov = text.split("|")
        self.produkty.clear()

        for i in zoznam_produktov:
            x = i.split(';')
            self.produkty[x[0]] = Produkt(x[0],float(x[1]),int(x[2]))
            
        print("Import bol uspesny")

    def naskladnit(self):
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov: "))
            self.produkty[nazov].pocet += kusy
        else:
            print("Produkt nie je na sklade")

    def vyskladnit(self):
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov: "))
            if kusy>self.produkty[nazov].pocet:
                print('Nedostatok kusov na sklade')
            else:
                self.produkty[nazov].pocet -= kusy
                print("Produkt bol vyskladneny")
        else:
            print("Produkt nie je na sklade")


volby = [
    "1. Vypísať zoznam produktov na sklade",
    "2. Pridať produkt do skladu",
    "3. Odstrániť produkt",
    "4. Nastavenie ceny produktu",
    "5. Naskladnenie produktu",
    "6. Vyskladnenie produktu",
    "7. Hodnota skladu",
    "8. Export skladu",
    "9. Import skladu",
    "0. Ukoncit program"
]


def menu():
    print('Skladovy softver v. 1.0')
    print('-' * 10,'MENU','-' * 10)
    for x in volby:
        print(x)

sklad = Sklad('Firemny')

while True:
    menu()
    try:
        volba = int(input("Zadaj cislo volby: "))
        if volba == 1:
            sklad.vypis_produkty()
        elif volba == 2:
            sklad.pridaj_produkt()
        elif volba == 3:
            sklad.odstran_produkt()
        elif volba == 4:
            pass
        elif volba == 5:
            sklad.naskladnit()
        elif volba == 6:
            sklad.vyskladnit()
        elif volba == 7:
            sklad.zobraz_sumu()
        elif volba == 8:
            sklad.export_skladu()
        elif volba == 9:
            sklad.import_skladu()
        elif volba == 0:
            print("Program sa ukoncuje.")
            break
        else:
            print("Zadal si neexistujucu volbu !!!")
    except ValueError:
        print("Zadal si zlu volbu!")


