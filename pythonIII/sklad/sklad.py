from produkt import Produkt
import sqlite3
from functools import reduce
import csv,json

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
        self._ulozenie_do_databazy()
        print("Produkt bol uspesne pridany")

    def odobratie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            self._ulozenie_do_databazy()
            print("Tovar bol uspesne odstraneny")
            return
        print("Zadany produkt sa nenasiel")

    def hodnota_skladu(self):
        hodnota = reduce(lambda x,y : x + y.get_value(),self.produkty.values(),initial=0)
        print(f"Hodnota skladu je {hodnota}")

    def export_skladu(self,format):
        if format == "csv":
            with open("export.csv","w",encoding="utf-8",newline="") as f:
                writer = csv.writer(f)
                for x in self.produkty.values():
                    writer.writerow(x.get_as_list())
                print("Export do CSV uspesne vytvoreny.")
        else:
            with open("export.json","w",encoding="utf-8") as f:
                json.dump([x.to_dict() for x in self.produkty.values()],f,ensure_ascii=False,indent=4)

    def _ulozenie_do_databazy(self):
        self.cur.execute("delete from produkty")
        data = [x.get_as_list() for x in self.produkty.values()]
        self.cur.executemany("insert into produkty (nazov,cena,pocet) values (?,?,?) ",data)
        self.conn.commit()

