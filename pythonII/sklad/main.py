import sklad
from produkt import Produkt

def print_menu():
    print(f'{"-"*10}MENU{"-"*10}')
    print('1. Vypis skladu')
    print('2. Pridanie produktu')
    print('3. odstranenie produktu')
    print('4. naskladnenie')
    print('5. vyskladnenie')
    print('0. ukoncenie programu')

# voda,2.5,20
with(open(r'C:\Users\ruman\skolenie\pythonII\sklad\sklad.txt','r',encoding='utf-8')) as f:
    for x in f:
        nazov,cena,pocet = x.split(',')
        sklad.produkty.append(Produkt(nazov,float(cena),int(pocet.strip())))

while True:

    print_menu()
    volba = input("Zadaj svoju volbu: ")

    if volba == '1':
        sklad.vypis_skladu()
    elif volba == '2':
        sklad.pridaj_produkt()
    elif volba == '3':
        sklad.odstran_produkt()
    elif volba == '4':
        sklad.naskladnenie()
    elif volba == '5':
        sklad.vyskladnenie()
    elif volba == '0':
        break