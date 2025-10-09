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

produkty = ["voda","muka","chlieb"]
ceny = [1,1.5,2.5]
kusy = [20,40,50]

def vypis_skladu():
    for i,x in enumerate(produkty):
        print(f'Nazov produktu: {x}, jednotkova cena: {ceny[i]:.2f} €, pocet kusov: {kusy[i]}')

def pridanie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        print("Tovar uz je na sklade")
    else:
        cena = input('Zadaj cenu: ')
        pocet_kusov = input('Zadaj pocet kusov: ')
        produkty.append(nazov)
        try:
            ceny.append(float(cena) if cena else 0)
            kusy.append(int(pocet_kusov) if pocet_kusov else 0)
            print('Produkt bol pridany do skladu')
        except:
            print("Zadal si neplatne hodnoty")

def odobranie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        i = produkty.index(nazov)
        produkty.pop(i)
        ceny.pop(i)
        kusy.pop(i)
        print("Tovar bol odstraneny")
    else:
        print('Tovar nie je na sklade')

def naskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        i = produkty.index(nazov)
        pocet_kusov = int(input('Kolko kusov: '))
        kusy[i] += pocet_kusov
        print('Naskladnene')
    else:
        print('Tovar nie je na sklade')

def vyskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        i = produkty.index(nazov)
        pocet_kusov = int(input('Kolko kusov: '))
        if pocet_kusov>kusy[i]:
            print('Nie je tolko tovaru na sklade')
        else:
            kusy[i] -= pocet_kusov
            print('Vyskladnenie')
    else:
        print('Tovar nie je na sklade')

def nastav_cenu():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        i = produkty.index(nazov)
        cena = float(input('Zadaj cenu: '))
        ceny[i] = cena
        print('Cena je nastavena')
    else:
        print('Tovar nie je na sklade')

def zobraz_sumu():
    suma = 0
    for i,x in enumerate(ceny):
        suma = suma + kusy[i] * x
    print(f'Celkova cena tovarov je: {suma}')

def export_skladu():
    vystup = []
    for i,x in enumerate(produkty):
        vystup.append(f'{produkty[i]};{ceny[i]};{kusy[i]}')
    v = "|".join(vystup)
    print(v)

def import_skladu():
    x = input("Zadaj string z exportu skladu: ")
    zoznam = x.split('|')
    produkty.clear()
    ceny.clear()
    kusy.clear()
    for y in zoznam:
        elementy = y.split(";")
        produkty.append(elementy[0])
        ceny.append(float(elementy[1]))
        kusy.append(int(elementy[2]))

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
    