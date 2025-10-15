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
    def __init__(self,nazov,cena,pocet_kusov):
        self.nazov = nazov
        self.cena = cena
        self.pocet_kusov = pocet_kusov

    def hodnota(self):
        return self.cena * self.pocet_kusov
    
    def export_string(self):
        return f'{self.nazov};{self.cena};{self.pocet_kusov}'

    def __str__(self):
        return f'Nazov produktu: {self.nazov}, jednotkova cena: {self.cena:.2f} €, pocet kusov: {self.pocet_kusov}'

produkty = {"voda" : Produkt("voda",1.5,20),
            "muka" : Produkt("muka",2,20),
            "chlieb" : Produkt("chlieb",2.5,50)}

def vypis_skladu():
    for x in produkty.values():
        print(x)

def pridanie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        print("Tovar uz je na sklade")
    else:
        cena = input('Zadaj cenu: ')
        pocet_kusov = input('Zadaj pocet kusov: ')
        try:
            produkty[nazov]= Produkt(nazov,float(cena) if cena else 0,int(pocet_kusov) if pocet_kusov else 0)
            print('Produkt bol pridany do skladu')
        except:
            print("Zadal si neplatne hodnoty")

def odobranie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        del produkty[nazov]
        print("Tovar bol odstraneny")
    else:
        print('Tovar nie je na sklade')

def naskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        pocet_kusov = int(input('Kolko kusov: '))
        produkty[nazov].pocet_kusov += pocet_kusov
        print('Naskladnene')
    else:
        print('Tovar nie je na sklade')

def vyskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        pocet_kusov = int(input('Kolko kusov: '))
        if pocet_kusov>produkty[nazov].pocet_kusov:
            print('Nie je tolko tovaru na sklade')
        else:
            produkty[nazov].pocet_kusov -= pocet_kusov
            print('Vyskladnenie')
    else:
        print('Tovar nie je na sklade')

def nastav_cenu():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        cena = float(input('Zadaj cenu: '))
        produkty[nazov].cena = cena
        print('Cena je nastavena')
    else:
        print('Tovar nie je na sklade')

def zobraz_sumu():
    suma = 0
    for x in produkty.values():
        suma = suma + x.hodnota()
    print(f'Celkova cena tovarov je: {suma}')

def export_skladu():
    vystup = []
    for x in produkty:
        vystup.append(x.export_string())
    v = "|".join(vystup)
    print(v)

def import_skladu():
    x = input("Zadaj string z exportu skladu: ")
    zoznam = x.split('|')
    produkty.clear()
    for y in zoznam:
        elementy = y.split(";")
        produkty.append(elementy[0])

def vypis_menu():
    print()
    print('-------------MENU-------------')
    print('0. Ukoncenie programu ')
    print('1. Vypis skladu')
    print('2. pridanie tovaru')
    print('3. odobranie tovaru')
    print('4. naskladnenie')
    print('5. vyskladnenie')
    print('6. nastavenie ceny')
    print('7. sucet cien tovarov')
    print('8. exportovat sklad')
    print('9. importovat sklad')
    print()

while True:
    vypis_menu()
    volba = input("Zvol moznost (napriklad 4): ")
    if volba == '0':
        print("Program sa ukoncuje")
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        odobranie_tovaru()
    elif volba == '4':
        naskladnenie()
    elif volba == '5':
        vyskladnenie()
    elif volba == '6':
        nastav_cenu()
    elif volba == '7':
        zobraz_sumu()
    elif volba == '8':
        export_skladu()
    elif volba == '9':
        import_skladu()
    else:
        print("Neplatna volba. Skus znova.")
    