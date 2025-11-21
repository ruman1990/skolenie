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
        self.tovary = {"voda" : Tovar("voda",1,100),"chlieb" : Tovar("chlieb",1.5,50)}

    def vypis_skladu(self):
        for t in self.tovary:
            print(self.tovary[t])

    def hodnota_skladu(self):
        suma = 0
        for t in self.tovary:
            suma += self.tovary[t].hodnota()
        print(suma)

    def pridat_tovar(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.tovary:
            print('Tovar uz existuje na sklade')
        else:
            try:
                ks = int(input('Zadaj pocet kusov: '))
            except Exception:
                print('Zadal si nespravny pocet kusov')
            cena = float(input("Zadaj jednotkovu cenu: "))
            self.tovary[nazov] = Tovar(nazov,cena,ks)
            print("Tovar bol uspesne pridany")

    def odobratie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            del self.tovary[nazov]

    def naskladnit(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            ks = int(input("Kolko kusov naskladnit: "))
            self.tovary[nazov].pocet += ks
            print("Tovar naskladneny")

    def vyskladnit(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            ks = int(input("Kolko kusov vyskladnit: "))
            if self.tovary[nazov].pocet<ks:
                print("Nedostatok kusov tovaru na sklade")
            else:
                self.tovary[nazov].pocet -= ks
                print("Tovar vyskladneny")

    # voda;1;100|chlieb;1.5;50|cola;2.5;25
    def export(self):
        e = []
        for t in self.tovary:
            e.append(self.tovary[t].export_format())
        print("|".join(e))

    def importovanie(self):
        self.tovary.clear()
        x = input('Zadaj import string: ')
        tov = x.split('|')
        # voda;2.5;20
        for y in tov:
            r = y.split(';')
            self.tovary[r[0]] = Tovar(r[0],float(r[1]),int(r[2]))
        print("sklad importovany")


class Tovar:   
    def __init__(self,meno,cena, pocet):
        self.meno = meno
        self.cena = cena
        self.pocet = pocet

    def hodnota(self):
        return self.cena * self.pocet
    
    def export_format(self):
        return f'{self.meno};{self.cena};{self.pocet}'

    def __str__(self):
        return f'Produkt {self.meno:<20} Cena {self.cena:10.2f} Pocet {self.pocet:10d}'

sklad =  Sklad('test')
while True:
    print(f'{'-'*10}MENU{'-'*10}')
    print('0. ukoncenie programu')
    print('1. vypis tovary')
    print('2. hodnota skladu')
    print('3. pridanie tovaru')
    print('4. odobranie tovaru')
    print('5. naskladnenie tovaru')
    print('6. vyskladnenie tovaru')
    print('7. exportovat sklad')
    print('8. import skladu')
    print()
    x = input("Zadaj volbu: ")
    if x == '0':
        break
    elif x == '1':
        sklad.vypis_skladu()
    elif x == '2':
        sklad.hodnota_skladu()
    elif x == '3':
        sklad.pridat_tovar()
    elif x == '4':
        sklad.odobratie_tovaru()
    elif x == '5':
        sklad.naskladnit()
    elif x == '6':
        sklad.vyskladnit()
    elif x == '7':
        sklad.export()
    elif x == '8':
        sklad.importovanie()
    else:
        print("Neplatna volba")
