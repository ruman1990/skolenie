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

class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return f"{self.nazov} cena: {self.cena:.2f}€ pocet kusov: {self.pocet}"

class Sklad:
    def __init__(self):
        self.produkty = {"muka" : Produkt(nazov="muka",cena=1.5,pocet=20),
            "chlieb" : Produkt(nazov="chlieb",cena=2.5,pocet=50),
            "voda" : Produkt(nazov="voda",cena=1,pocet=40)
            }


    def vypis_skladu(self):
        for x in self.produkty.values():
            print(x)

    def pridanie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            print("Produkt sa uz na sklade nachadza!")
            return

        cena = float(input("Zadaj cenu produktu: "))
        pocet_kusov = int(input("Zadaj pocet kusov produktu: "))
        self.produkty["nazov"] = Produkt(nazov,cena,pocet_kusov)
        print("Produkt bol uspesne pridany")

    def odstranenie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            print("Produkt bol uspesne odstraneny")
        else:
            print("Produkt neexistuje!")

sklad = Sklad()

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
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_produktu()
    elif volba == '3':
        sklad.odstranenie_produktu()
    else:
        print("Nespravna volba")