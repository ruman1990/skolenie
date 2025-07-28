# Chceme spravit program pre manazment skladu
# budeme mat textove rozhranie - MENU
# vypis produktu, pridat_produkt, odstran_produkt
# naskladnit, vyskladnenie, nastavenie ceny
# zobrazit sumu, exportovat zo skladu, import do skladu
from produkt import Produkt
from audit import Audit
import re
#import psycopg2
#import psycopg2.extras
import sqlite3
from decimal import Decimal

class Sklad:
    def __init__(self):
        self.audit = Audit()
        self.produkty = {}
        #self.conn = psycopg2.connect(
        #    dbname="skolenie",
        #    user="admin",
        #    password="adminadmin",
         #   host="localhost",
        #    port=5432
        #)
        self.conn = sqlite3.connect("sklad.db")
        self.conn.row_factory = sqlite3.Row
        #self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cursor = self.conn.cursor()        

        self.cursor.execute('''
             CREATE TABLE IF NOT EXISTS produkty (
                 nazov TEXT PRIMARY KEY,
                 pocet INTEGER,
                 cena REAL
             )
         ''')
        self.conn.commit()

        self.cursor.execute("SELECT * from produkty")
        for row in self.cursor.fetchall():
            self.produkty[row['nazov']] = Produkt(row['nazov'],row['pocet'],Decimal(str(row['cena'])))

    def _uloz_zmenu(self,sql,params=()):
        self.cursor.execute(sql,params)
        self.conn.commit()

    # Produkt: nazov X ks XX.XX €
    def vypis_produktov(self):
        for x in self.produkty.values():
            print(x)
        self.audit.zapis(f"Boli vypisane produkty")
        print('')

    def pridanie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            print("Produkt uz existuje.")
            self.audit.zapis(f"Pridanie produktu {nazov} - Chyba: Produkt uz existuje")
        else:
            self.produkty[nazov] = Produkt(nazov)
            x = self.produkty[nazov]
            self._uloz_zmenu("INSERT INTO produkty (nazov,pocet,cena,kategoria) VALUES (?,?,?, ?)",(x.nazov,x.pocet,x.cena, x.kategoria))
            print("Produkt bol pridany.")
            self.audit.zapis(f"Pridanie produktu {nazov}")

    def naskladnit(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov produktu: "))
            self.produkty[nazov].pocet += kusy
            x = self.produkty[nazov]
            self._uloz_zmenu("UPDATE produkty SET pocet=? WHERE nazov=?",(x.pocet,x.nazov))
            print("Produkt naskladneny")
            self.audit.zapis(f"Naskladnenie {nazov}")
        else:
            print("Produkt nie je na sklade")
            self.audit.zapis(f"Naskladnenie {nazov} - Chyba: Produkt nie je na sklade")

    def vyskladnit(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov produktu: "))
            if self.produkty[nazov].pocet <= kusy:
                print("Nie je dost tovaru na vyskladnenie")
            else:
                self.produkty[nazov].pocet -= kusy
                x = self.produkty[nazov]
                self._uloz_zmenu("UPDATE produkty SET pocet=? WHERE nazov=?",(x.pocet,x.nazov))
                print("Produkt vyskladneny")
        else:
            print("Produkt nie je na sklade")

    def nastav_cenu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            cena = Decimal(input("Zadaj cenu za kus produktu: "))
            self.produkty[nazov].cena = cena
            x = self.produkty[nazov]
            self._uloz_zmenu("UPDATE produkty SET cena=? WHERE nazov=?",(x.cena,x.nazov))
            print("Cena bola nastavena")
        else:
            print("Produkt nie je na sklade")

    def celkova_suma(self):
        suma = Decimal('0.00')
        for x in self.produkty.values():
            suma += x.cena * x.pocet
        print(f'Celkova hodnota skladu je: {suma:.2f}€')

    def odstranit_produkt(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            self._uloz_zmenu("delete from produkty WHERE nazov=?",(self.produkty[nazov].nazov,))
            del self.produkty[nazov]
            print("Produkt bol odstraneny")
            self.audit.zapis(f"Odstranenie produktu {nazov}")
        else:
            print("Produkt nie je na sklade")
            self.audit.zapis(f"Odstranenie produktu {nazov} - Chyba: Produkt nie je na sklade")

    def vypisat_dennik(self):
        self.audit.vypis()

    def vyhladat_nazov(self):
        nazov = input("Zadaj cast nazvu produktu alebo regex: ")
        self.audit.zapis(f"Vyhladavanie v produktoch {nazov}")
        zhody = []
        for p in self.produkty:
            if re.search(nazov,p,re.IGNORECASE):
                zhody.append(p)

        if not zhody:
            print('Zaznam sa nenasiel')
            return
        
        for i in zhody:
            print(f'{i}')

    def zavri(self):
        self.conn.commit()
        self.conn.close()
