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
import csv
import sqlite3
import json

class Sklad:

    def __init__(self,nazov='test'):
        self.nazov = nazov
        self.produkty = {}
        self.load_database()
        # with open(nazov + '.csv','r',encoding='UTF-8') as f:
        #      for x in f:
        #         res = x.split(',')
        #         self.produkty[res[0]] = Produkt(res[0],res[1],res[2])     

    def load_database(self):
        conn = sqlite3.connect(self.nazov + '.db')
        cur = conn.cursor()
        cur.execute("select * from produkty")
        for x in cur.fetchall():
             self.produkty[x[1]] = Produkt(x[1],x[2],x[3])
        conn.close()

    def save_database(self):
        conn = sqlite3.connect(self.nazov + '.db')
        cur = conn.cursor()
        cur.execute("delete from produkty")
        v = [self.produkty[x].get_as_tuple() for x in self.produkty]
        cur.executemany("insert into produkty (nazov,cena,pocet) values (?,?,?)",v)
        conn.commit()
        conn.close()


    def vypis_skladu(self):
        print()
        for x in self.produkty:
            print(self.produkty[x])
        print()

    def pridanie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty.keys():
                print("Produkt uz existuje")
                return
        cena = float(input("Zadaj cenu tovaru: "))
        pocet = int(input("Zadaj pocet kusov: "))
        self.produkty[nazov] = Produkt(nazov,cena,pocet)
        self.save_database()
        print("Produkt bol uspesne pridany")

    def odstranenie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.produkty.keys():
                del self.produkty[nazov]
                print("Tovar bol uspesne odstraneny")
                self.save_database()
                return
        print("Tovar sa nenasiel")

    def sucet_ceny(self):
        suma = 0
        for x in self.produkty.values():
            suma = suma + (x.cena*x.pocet)
        print(suma)

    def export_skladu(self,format):
        if format=='csv':
            with open("export.csv",'w',encoding='utf-8',newline='') as f:
                writer = csv.writer(f,delimiter=';')
                writer.writerow(['nazov','cena','pocet kusov'])
                writer.writerows([self.produkty[x].get_as_tuple() for x in self.produkty])
            print('Sklad bol uspesne exportovany')
        else:
            with open("export.json","w",encoding='utf-8') as f:
                json.dump([self.produkty[x].__dict__ for x in self.produkty],f,ensure_ascii=False,indent=4)
    


