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
from produkt import Produkt
import sqlite3
import datetime
produkty = []
# [nazov produktu, cena, pocet kusov]

def vypis_skladu():
    print()
    for x in produkty:
        print(x)
    print()

def zapis_do_db():
    conn = sqlite3.connect('sklad.db')
    cur = conn.cursor()
    cur.execute('delete from produkty')
    for x in produkty:
        cur.execute('insert into produkty (nazov,cena,pocet) values (?,?,?)',(x.nazov,x.cena,x.pocet))
    conn.commit()
    conn.close()

def zapis_do_logu(message):
    with(open(r'C:\Users\ruman\skolenie\pythonII\sklad\log.txt','a',encoding='utf-8',newline='')) as f:
        f.write(f'[{datetime.datetime.now()}] : {message}')
        f.write('\n')

def pridaj_produkt():
    name = input('Zadaj nazov produktu: ')
    price = float(input('Zadaj jednotkovu cena: '))
    count = int(input('Zadaj pocet kusov: '))
    if _is_product(name):
        print('Produkt uz existuje')
        return
    produkty.append(Produkt(name,price,count))
    zapis_do_db()
    print('Produkt uspesne pridany do skladu')
    zapis_do_logu(f'Pridany produkt {name} cena {price} pocet {count}')

def odstran_produkt():
    name = input('Zadaj nazov produktu: ')
    for x in produkty:
        if x.nazov == name:
            produkty.remove(x)
            print('Produkt bol uspesne odstraneny')
            zapis_do_db()

def _is_product(name):
    for x in produkty:
        if x.nazov == name:
            return True
    return False

def _get_product(name):
    for x in produkty:
        if x.nazov == name:
            return x

def naskladnenie():
    name = input('Zadaj nazov produktu: ')
    if _is_product(name):
        pocet = int(input("Zadaj pocet kusov: "))
        product = _get_product(name)
        product.pocet += pocet
        zapis_do_db()

def vyskladnenie():
    name = input('Zadaj nazov produktu: ')
    if _is_product(name):
        pocet = int(input("Zadaj pocet kusov: "))
        product = _get_product(name)
        if pocet > product.pocet:
            print('Nedostat0ok tovaru na sklade')
        else:
            product.pocet -= pocet
            zapis_do_db()




