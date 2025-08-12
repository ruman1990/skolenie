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

produkty = []
ceny = []
pocty = []

def menu():
    print('Skladovy softver v. 1.0')
    print('-' * 10,'MENU','-' * 10)
    for x in volby:
        print(x)

def vypis_produkty():
    print('')
    for idx,nazov in enumerate(produkty):
        print(f'Nazov {nazov}, Cena {ceny[idx]:.2f}€, Pocet {pocty[idx]}ks')
    print('')

def pridaj_produkt():
    print('')
    nazov = input('Zadaj nazov produktu: ')
    if nazov in produkty:
        print('Produkt uz existuje')
    else:
        cena = float(input("Zadaj cenu produktu: "))
        pocet = int(input("Zadaj pocet kusov: "))
        produkty.append(nazov)
        ceny.append(cena)
        pocty.append(pocet)
        print('Produkt bol uspesne pridany do skladu')

def odstran_produkt():
    nazov = input("Zadaj nazov produktu na odstranenie: ")
    if nazov in produkty:
        index = produkty.index(nazov)
        produkty.pop(index)
        ceny.pop(index)
        pocty.pop(index)
        print("Produkt bol odstraneny.")
    else:
        print('Produkt sa nenasiel.')

def zobraz_sumu():
    suma = 0.0
    for idx,i in enumerate(produkty):
        suma = suma + (ceny[idx] * pocty[idx])
    print(f'Celkova hodnota skladu: {suma:.2f}€')

def export_skladu():
    vystup = []
    for idx,i in enumerate(produkty):
        vystup.append(f'{produkty[idx]};{ceny[idx]};{pocty[idx]}')
    retazec = '|'.join(vystup)
    print('====EXPORT TEXT====')
    print(retazec)
    print('====Skopiruj a uloz====')

def import_skladu():
    text = input("Vloz vstupny text: ")
    zoznam_produktov = text.split("|")

    produkty.clear()
    ceny.clear()
    pocty.clear()

    for i in zoznam_produktov:
        x = i.split(';')
        produkty.append(x[0])
        ceny.append(float(x[1]))
        pocty.append(int(x[2]))
    print("Import bol uspesny")


while True:
    menu()
    try:
        volba = int(input("Zadaj cislo volby: "))
        if volba == 1:
            vypis_produkty()
        elif volba == 2:
            pridaj_produkt()
        elif volba == 3:
            odstran_produkt()
        elif volba == 4:
            pass
        elif volba == 5:
            pass
        elif volba == 6:
            pass
        elif volba == 7:
            zobraz_sumu()
        elif volba == 8:
            export_skladu()
        elif volba == 9:
            import_skladu()
        elif volba == 0:
            print("Program sa ukoncuje.")
            break
        else:
            print("Zadal si neexistujucu volbu !!!")
    except ValueError:
        print("Zadal si zlu volbu!")


