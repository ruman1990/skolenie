# Pre studijne ucely, nepracujeme s decimalom pri cenach
produkty = []
pocty = []
ceny = []

def export_skladu():
    if len(pocty) == 0:
        print('Sklad je prazdny')
        return
    for x in range(len(produkty)):
        print(f'{produkty[x]};{pocty[x]};{ceny[x]}|',end='')
    print('')
    print('Uspesne vyexportovane')

def import_skladu(data):
    global produkty, pocty, ceny
    nove_produkty = []
    nove_pocty = []
    nove_ceny = []

    polozky = data.strip().split("|")
    for polozka in polozky:
        casti = polozka.split(";")
        if len(casti) != 3:
            print("Chybný formát položky:", polozka)
            continue
        nazov = casti[0]
        try:
            pocet = int(casti[1])
            cena = float(casti[2])
        except ValueError:
            print("Chybný počet alebo cena pri položke:", polozka)
            continue

        nove_produkty.append(nazov)
        nove_pocty.append(pocet)
        nove_ceny.append(cena)

    # Nahradenie existujúceho skladu novými údajmi
    produkty = nove_produkty
    pocty = nove_pocty
    ceny = nove_ceny
    print("Sklad bol úspešne importovaný.")

def nastav_cenu(pnazov):
    if pnazov not in produkty:
        nie_je_na_sklade(pnazov)
    else:
        cena = float(input('Zadaj cenu za kus: '))
        index = produkty.index(pnazov)
        ceny[index] = cena
        print(f'Cena {cena} EUR uspesne nastavena pre produkt {pnazov}')

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
        print(f'{produkty[x]} {pocty[x]}ks {ceny[x]} EUR')

def zobraz_menu():
    print('\n========= MENU SKLADU =========')
    print('0. Ukonci program')
    print('1. Zobraz polozky skladu')
    print('2. Pridat produkt')
    print('3. Odstranit produkt')
    print('4. Naskladnit produkt')
    print('5. Vyskladnit produkt')
    print('6. Nastavit cenu')
    print('7. Import skladu')
    print('8. Export skladu')
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
    elif volba == '6':
        nazov = input('Zadaj nazov produktu na nastavenie ceny ')
        nastav_cenu(nazov)
    elif volba == '7':
        data = input('Zadaj data skladu: ')
        import_skladu(data)
    elif volba == '8':
        export_skladu()
        


