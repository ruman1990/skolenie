# Chceme spravit program pre manazment skladu
# budeme mat textove rozhranie - MENU
# vypis produktu, pridat_produkt, odstran_produkt
# naskladnit, vyskladnenie, nastavenie ceny
# zobrazit sumu, exportovat zo skladu, import do skladu
produkty = []
pocty = []
ceny = []

# Produkt: nazov X ks XX.XX €
def vypis_produktov():
    for x in range(0,len(produkty)):
        print(f'Produkt: {produkty[x]} {pocty[x]}ks {ceny[x]}€')
    print('')

def pridanie_produktu():
    nazov = input("Zadaj nazov produktu: ")
    if nazov in produkty:
        print("Produkt uz existuje.")
    else:
        produkty.append(nazov)
        pocty.append(0)
        ceny.append(0.0)
        print("Produkt bol pridany.")

def naskladnit():
    nazov = input("Zadaj nazov produktu: ")
    if nazov in produkty:
        kusy = int(input("Zadaj pocet kusov produktu: "))
        index = produkty.index(nazov)
        pocty[index] += kusy
        print("Produkt naskladneny")
    else:
        print("Produkt nie je na sklade")

def vyskladnit():
    nazov = input("Zadaj nazov produktu: ")
    if nazov in produkty:
        kusy = int(input("Zadaj pocet kusov produktu: "))
        index = produkty.index(nazov)

        if pocty[index] <= kusy:
            print("Nie je dost tovaru na vyskladnenie")
        else:
            pocty[index] -= kusy
            print("Produkt vyskladneny")
    else:
        print("Produkt nie je na sklade")

def nastav_cenu():
    nazov = input("Zadaj nazov produktu: ")
    if nazov in produkty:
        cena = float(input("Zadaj cenu za kus produktu: "))
        index = produkty.index(nazov)
        ceny[index] = cena
        print("Cena bola nastavena")
    else:
        print("Produkt nie je na sklade")

def celkova_suma():
    suma = 0
    for i in range(len(produkty)):
        suma += ceny[i] * pocty[i]
    print(f'Celkova hodnota skladu je: {suma:.2f}€')

def odstranit_produkt():
    nazov = input("Zadaj nazov produktu: ")
    if nazov in produkty:
        index = produkty.index(nazov)
        produkty.remove(nazov)
        del pocty[index]
        del ceny[index]
        print("Produkt bol odstraneny")
    else:
        print("Produkt nie je na sklavoda,0,0.0de")

def export_skladu():
    vystup = []
    for i in range(len(produkty)):
        vystup.append(f'{produkty[i]},{pocty[i]},{ceny[i]}')
    retazec = ";".join(vystup)
    print(retazec)

def import_skladu():
    vstup = input("Zadaj data skladu: ")
    # voda,3,1;chlieb,4,3
    casti = vstup.split(';')
    for x in casti:
        item = x.split(',')
        produkty.append(item[0])
        pocty.append(item[1])
        ceny.append(item[2])

print("------ SKLAD v1.0 ------")
while True:
    print("------- MENU ------")
    print("1. Vypis produktov")
    print("2. Pridat produkt")
    print("3. Naskladnit produkt")
    print("4. Vyskladnit produkt")
    print("5. Nastav cenu")
    print("6. Hodnota skladu")
    print("7. Odstranenie produktu")
    print("8. Export skladu")
    print("9. import skladu")
    print("0. Ukoncit program")
    volba = input("Zvol moznost: ")
    if volba == '1':
        vypis_produktov()
    elif volba == '2':
        pridanie_produktu()
    elif volba == '3':
        naskladnit()
    elif volba == '4':
        vyskladnit()
    elif volba == '5':
        nastav_cenu()
    elif volba == '6':
        celkova_suma()
    elif volba == '7':
        odstranit_produkt()
    elif volba == '8':
        export_skladu()
    elif volba == '9':
        import_skladu()
    elif volba == '0':
        print("Ukoncenie programu")
        break
    else:
        print("Neplatna volba, Skus znova.")