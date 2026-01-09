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

produkty = [["voda",2.5,20],["chlieb",1.5,30]]
# [nazov produktu, cena, pocet kusov]

def print_menu():
    print(f'{"-"*10}MENU{"-"*10}')
    print('1. Vypis skladu')
    print('2. Pridanie produktu')
    print('3. odstranenie produktu')
    print('0. ukoncenie programu')

def vypis_skladu():
    print()
    for x in produkty:
        print(f'Produkt {x[0]} cena {x[1]}€ mnozstvo {x[2]} ks')
    print()

def pridaj_produkt():
    name = input('Zadaj nazov produktu: ')
    price = float(input('Zadaj jednotkovu cena: '))
    count = int(input('Zadaj pocet kusov: '))
    for x in produkty:
        if name in x:
            print('Produkt uz existuje')
            return
    produkty.append([name,price,count])
    print('Produkt uspesne pridany do skladu')

while True:

    print_menu()
    volba = input("Zadaj svoju volbu: ")

    if volba == '1':
        vypis_skladu()
    elif volba == '2':
        pridaj_produkt()
    elif volba == '3':
        pass
    elif volba == '0':
        break





