produkty = ['voda','chlieb']
pocty = [5,10]
ceny = [2.20,3.50]

def nie_je_na_sklade(pnazov):
    print(f'Produkt {pnazov} nie je vedeny na sklade')
    v = input('Chcete tento produkt pridat? (y/n) ')
    if v == 'y':
        pridat_produkt(pnazov)

def vyskladnit_produkt(pnazov):
    if pnazov not in produkty:
        nie_je_na_sklade(pnazov)
    else:
        kusy = int(input('Zadaj pocet kusov: '))
        index = produkty.index(pnazov)
        if pocty[index] < kusy:
            print('Nie je dostatok tovaru na sklade')
        else:
            pocty[index] -= kusy
            print(f'Produkt {pnazov} bol uspesne vyskladneny v pocte kusov {kusy}')

def naskladnit_produkt(pnazov):
    if pnazov not in produkty:
        nie_je_na_sklade(pnazov)
    else:
        kusy = int(input('Zadaj pocet kusov: '))
        index = produkty.index(pnazov)
        pocty[index] += kusy
        print(f'Produkt {pnazov} bol uspesne naskladneny v pocte kusov {kusy}')
        
def odstranit_produkt(pnazov):
    if pnazov in produkty:
        index = produkty.index(pnazov)
        produkty.pop(index)
        pocty.pop(index)
        ceny.pop(index)
        print('Produkt bol uspesne odstraneny')
    else:
        print('Produkt v sklade nie je vedeny')

def pridat_produkt(pnazov):
    if pnazov in produkty:
        print('Produkt uz existuje')
    else:
        produkty.append(pnazov)
        pocty.append(0)
        ceny.append(None)
        print('Produkt bol uspesne pridany')

def vypisat_produkty():
    for x in range(len(produkty)):
        print(f'{produkty[x]} {pocty[x]}ks {ceny[x]}eur')

def zobraz_menu():
    print('\n========= MENU SKLADU =========')
    print('0. Ukonci program')
    print('1. Zobraz polozky skladu')
    print('2. Pridat produkt')
    print('3. Odstranit produkt')
    print('4. Naskladnit produkt')
    print('5. Vyskladnit produkt')
    print('')


while True:
    zobraz_menu()
    volba = input("Zvol volbu: ")

    if volba == '0':
        break
    elif volba== '1':
        vypisat_produkty()
    elif volba == '2':
        nazov = input('Zadaj nazov produktu ')
        pridat_produkt(nazov)
    elif volba == '3':
        nazov = input('Zadaj nazov produktu na odstranenie ')
        odstranit_produkt(nazov)
    elif volba == '4':
        nazov = input('Zadaj nazov produktu na naskladnenie ')
        naskladnit_produkt(nazov)
    elif volba == '5':
        nazov = input('Zadaj nazov produktu na vyskladnenie ')
        vyskladnit_produkt(nazov)


