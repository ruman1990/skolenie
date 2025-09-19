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

produkty = ['voda','mlieko']
kusy = [5,10]
ceny = [0.5,1.5]

def vypis_skladu():
    print()
    for i,x in enumerate(produkty):  
        print(f'Nazov: {x} Pocet kusov: {kusy[i]} Cena: {ceny[i]}')
    print()

def pridanie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        print('Produkt uz je na sklade')
    else:
        pocet_kusov = input('Zadaj pocet kusov tovaru (nepovinne): ')
        jedn_cena = input('Zadaj jednotkovu cenu tovaru (nepovinne): ')
        produkty.append(nazov)
        kusy.append(int(pocet_kusov) if pocet_kusov else 0)
        ceny.append(float(jedn_cena) if jedn_cena else 0.0)
        print('Produkt bol pridany')
        vypis_skladu()

def existuje(nazov):
    if nazov not in produkty:
        print('Produkt neexistuje')
        return False
    else:
        return True
    
def odstran_produkt():
    nazov = input('Zadaj nazov tovaru pre odstranenie: ')
    if existuje(nazov):
        index = produkty.index(nazov)
        produkty.pop(index)
        kusy.pop(index)
        ceny.pop(index)
        print('Produkt bol odstraneni')
        vypis_skladu()

def naskladnit():
    nazov = input('Zadaj nazov tovaru pre naskladnenie: ')
    if existuje(nazov):
        index = produkty.index(nazov)
        pocet = int(input("Zadaj mnozstvo: "))
        kusy[index] += pocet
        print("Produkt bol uspesne naskladneny")

def vyskladnenie():
    nazov = input('Zadaj nazov tovaru pre vyskladnenie: ')
    if existuje(nazov):
        index = produkty.index(nazov)
        pocet = int(input("Zadaj mnozstvo: "))
        kusy[index] -= pocet
        print("Produkt bol uspesne vyskladneny")

def nastav_cenu():
    nazov = input('Zadaj nazov tovaru pre vyskladnenie: ')
    if existuje(nazov):
        index = produkty.index(nazov)
        cena = float(input("Zadaj cenu: "))
        ceny[index] = cena
        print("Produkt bol uspesne naceneny")

def sucet():
    suma = 0.0
    for i,x in enumerate(produkty):
        suma += kusy[i] * ceny[i]
    print(f'Celkova cena produktov je {suma:.2f} €')

# voda;10;2.45|mlieko;50;1.5|...
#['voda;10;2.45','mlieko;50;1.5']

# voda;5;0.5|mlieko;10;1.5|cola;25;2.0

def export_skladu():
    vystup = []
    for i,x in enumerate(produkty):
        vystup.append(f'{produkty[i]};{kusy[i]};{ceny[i]}')
    print("|".join(vystup))

def import_skladu():
    retazec = input('Zadaj vstupny string: ')
    produkty.clear()
    kusy.clear()
    ceny.clear()

    vstup = retazec.split("|")
    # ['voda;10;2.45','mlieko;50;1.5']
    for x in vstup:
        #'voda;10;2.45'  
        nazov,kus,cena = x.split(";")
        produkty.append(nazov)
        kusy.append(kus)
        ceny.append(cena)
    print("Sklad bol importovany")

def menu():
    print('------------- MENU ------------')
    print('1. Vypis skladu')
    print('2. Pridanie tovaru na sklad')
    print('3. Odstranenie tovaru zo skladu')
    print('4. Naskladnenie')
    print('5. Vyskladnenie')
    print('6. Nastavenie ceny tovaru')
    print('7. Sucet ceny tovarov')
    print('8. Export skladu')
    print('9. Import skladu')
    print('0. Ukoncit program')

while True:
    menu()
    volba = input('Zvol moznost: ')
    if volba == '0':
        print('Dovidenia')
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        odstran_produkt()
    elif volba == '4':
        naskladnit()
    elif volba == '5':
        vyskladnenie()
    elif volba == '6':
        nastav_cenu()
    elif volba == '7':
        sucet()
    elif volba == '8':
        export_skladu()
    elif volba == '9':
        import_skladu()
    else:
        print('Zadal si neplatnu volbu.')