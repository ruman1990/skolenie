import sklad
from produkt import Produkt
import sqlite3
import os

os.chdir('C:\\Users\\ruman\\skolenie\\pythonIII\\sklad')

def print_menu():
    print(f'{"-"*10}MENU{"-"*10}')
    print('1. Vypis skladu')
    print('2. Pridanie produktu')
    print('3. odstranenie produktu')
    print('4. naskladnenie')
    print('5. vyskladnenie')
    print('0. ukoncenie programu')

def init_sklad():
    conn = sqlite3.connect('sklad.db')
    cur = conn.cursor()

    cur.execute('''
    create table if not exists produkty (
                    id INTEGER PRIMARY KEY,
                    nazov TEXT NOT NULL,
                    cena REAL NOT NULL,
                    pocet INTEGER NOT NULL
                )
    ''')

    cur.execute('select * from produkty')
    data = cur.fetchall()
    for zoznam in data:
        sklad.produkty.append(Produkt(zoznam[1],float(zoznam[2]),int(zoznam[3])))
    conn.close()

init_sklad()
# voda,2.5,20

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