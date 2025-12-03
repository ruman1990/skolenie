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

class Sklad:

    def __init__(self,nazov):
        self.nazov = nazov

        self.produkty = { "voda" : Produkt("voda",2.5,25) , 
                         "chlieb" : Produkt("chlieb",2,50)}
    
    
    def vypis_skladu(self):
        for x in self.produkty:
            print(self.produkty[x])
            

    def pridanie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            print("Tovar uz je na sklade")
        else:
            cena = float(input('Zadaj cenu tovaru: '))
            pocet = int(input('Zadaj pocet kusov na sklade: '))
            self.produkty[nazov] = Produkt(nazov,cena,pocet) 
            print("Tovar bol uspesne pridany do skladu")

    def odstranenie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            print('Tovar neexistuje')
        else:
            del self.produkty[nazov]
            print('Tovar uspesne odstraneny')

    def naskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            print("Tovar neexistuje")
        else:
            pocet = int(input('Kolko kusov tovaru naskladnit: '))
            self.produkty[nazov].pripocitat(pocet)
            print("Naskladnenie bolo uspesne")

    def vyskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            print("Tovar neexistuje")
        else:
            pocet = int(input('Kolko kusov tovaru vyskladnit: '))
            self.produkty[nazov].odpocitat(pocet)
            

    def nastav_cenu(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            print("Tovar neexistuje")
        else:
            cena = float(input('Zadaj cenu tovaru: '))
            self.produkty[nazov].nacen(cena)
            print('Cena bola uspesne nastavena')

    def hodnota_skladu(self):
        suma = 0
        for x in self.produkty.values():
            suma += x.vrat_celkovu_cenu()
        print(f"Celkova cena skladu je {suma}€")

    #"voda;2.5;20|chlieb;2;50"
    def export_skladu(self):
        for x in self.produkty.values():
            print(x.export_vypis(),end="|")
        print()

    def import_skladu(self):
        import_string = input("Zadaj import string: ")
        x = import_string.split('|')
        #"voda;2.5;20"
        self.produkty.clear()
        for i in x:
            if i == '':
                continue
            result = i.split(';')
            # ["voda",2.5,20]
            self.produkty[result[0]] = Produkt(result[0],float(result[1]),int(result[2]))

class Produkt:

    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def export_vypis(self):
        return f'{self.nazov};{self.cena};{self.pocet}'
    
    def vrat_celkovu_cenu(self):
        return self.cena * self.pocet
    
    def pripocitat(self,pocet):
        self.pocet += pocet
    
    def dostatok_tovaru(self,pocet):
        return self.pocet >= pocet
    
    def odpocitat(self,pocet):
        if not self.dostatok_tovaru(pocet):
            print('Nedostatok tovaru')
        else:
            self.pocet -= pocet
            print("Vyskladnenie bolo uspesne")

    def nacen(self,cena):
        self.cena = cena

    def __str__(self):
        return f'Nazov produktu: {self.nazov:<15} Cena: {self.cena:8.2f}€ Pocet kusov {self.pocet:8}'



def display_menu():
    print('Skladovy softver 1.0')
    print(f'{'-'*10}MENU{'-'*10}')
    print('0. Ukoncit program')
    print('1. Vypis skladu')
    print('2. Pridanie tovaru na sklad')   
    print('3. Naskladnenie tovaru')
    print('4. Vyskladnenie tovaru')
    print('5. Nastavenie ceny tovaru')
    print('6. Sucet ceny tovarov na sklade')
    print('7. Odstranenie tovaru zo skladu')
    print('8. Exportovat sklad do suboru')
    print('9. Importovat sklad zo suboru')




sklad = Sklad('test')

while True:
    display_menu()
    volba = input('Zadaj svoju volbu: ')
    if volba == '0':
        break
    elif volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridanie_tovaru()
    elif volba == '3':
        sklad.naskladnenie()
    elif volba == '4':
        sklad.vyskladnenie()
    elif volba == '5':
        sklad.nastav_cenu()
    elif volba == '6':
        sklad.hodnota_skladu()
    elif volba == '7':
        sklad.odstranenie_tovaru()
    elif volba == '8':
        sklad.export_skladu()
    elif volba == '9':
        sklad.import_skladu()




