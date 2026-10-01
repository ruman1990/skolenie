from produkt import Produkt
import sqlite3

class Sklad:
    def __init__(self,nazov):
        self.nazov = nazov
        self.produkty = {}
        self.conn = sqlite3.connect(f"{nazov}.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""create table if not exists produkty (
            id INTEGER PRIMARY KEY,
            nazov TEXT,
            cena REAL,
            pocet INTEGER
        )""")
        self.cur.execute("select * from produkty")
        data = self.cur.fetchall()
        for x in data:
            self.produkty[x[1]] = Produkt(*x[1:])
    
    def vypis_skladu(self):
        for x in self.produkty.values():
            print(x)

    def pridanie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty:
            print("Zadany tovar uz existuje")
            return
        cena = float(input("Zadaj cenu: "))
        pocet = int(input("Zadaj pocet kusov: "))
        self.produkty[nazov] = Produkt(nazov,cena,pocet)
        print("Produkt bol uspesne pridany")

    def odobratie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            print("Tovar bol uspesne odstraneny")
            return
        print("Zadany produkt sa nenasiel")

    def hodnota_skladu(self):
        hodnota = 0
        for x in self.produkty.values():
            hodnota += x.get_value()
        print(f"Hodnota skladu je {hodnota}")
