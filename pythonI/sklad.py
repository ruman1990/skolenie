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

produkty = ["voda" , "chlieb"]
ceny = [2.5 , 2]
pocty = [25 , 50]

def vypis_skladu():
    for i, x in enumerate(produkty):
        print(f'Nazov produktu: {x:<15} Cena: {ceny[i]:8.2f}€ Pocet kusov {pocty[i]:8}')

def pridanie_tovaru():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov in produkty:
        print("Tovar uz je na sklade")
    else:
        cena = float(input('Zadaj cenu tovaru: '))
        pocet = int(input('Zadaj pocet kusov na sklade: '))
        produkty.append(nazov)
        ceny.append(cena)
        pocty.append(pocet)
        print("Tovar bol uspesne pridany do skladu")

def naskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov not in produkty:
        print("Tovar neexistuje")
    else:
        pocet = int(input('Kolko kusov tovaru naskladnit: '))
        index = produkty.index(nazov)
        pocty[index] = pocty[index] + pocet 

def vyskladnenie():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov not in produkty:
        print("Tovar neexistuje")
    else:
        pocet = int(input('Kolko kusov tovaru vyskladnit: '))
        index = produkty.index(nazov)
        if pocty[index]<pocet:
            print('Nedostatok tovaru')
        else:
            pocty[index] = pocty[index] - pocet
            print("Vyskladnenie bolo uspesne")

def nastav_cenu():
    nazov = input('Zadaj nazov tovaru: ')
    if nazov not in produkty:
        print("Tovar neexistuje")
    else:
        cena = float(input('Zadaj cenu tovaru: '))
        index = produkty.index(nazov)
        ceny[index] = cena

def hodnota_skladu():
    suma = 0
    for i,x in enumerate(produkty):
        suma += ceny[i]*pocty[i]
    print(f"Celkova cena skladu je {suma}€")

while True:
    display_menu()
    volba = input('Zadaj svoju volbu: ')
    if volba == '0':
        break
    elif volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridanie_tovaru()
    elif volba == '3':
        naskladnenie()
    elif volba == '4':
        vyskladnenie()
    elif volba == '5':
        nastav_cenu()
    elif volba == '6':
        hodnota_skladu()




