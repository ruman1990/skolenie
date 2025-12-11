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
import os
from datetime import datetime
from produkt import Produkt
import sqlite3

class Sklad:

    def __init__(self,nazov,data_path='sklad.db',log_path='log.txt'):
        self.nazov = nazov
        self.produkty = {}
        self.log_path = log_path
        self.data_path = data_path
        self._init_db()

    def _init_db(self):
        self.conn = sqlite3.connect(self.data_path)
        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS produkty 
                  (
                    id INTEGER PRIMARY KEY,
                    nazov TEXT UNIQUE NOT NULL,
                    cena REAL NOT NULL,
                    pocet INTEGER NOT NULL
                  )
                  ''')
        self.conn.commit()        
        self.c.execute('select nazov,cena,pocet from produkty')
        for x in self.c.fetchall():
            self.produkty[x[0]] = Produkt(x[0],float(x[1]),int(x[2]))

    def vypis_skladu(self):
        for x in self.produkty:
            print(self.produkty[x])
            
    def _write_to_log(self,message):
        with open(self.log_path,'a',encoding='utf-8') as f:
            f.write(f'{datetime.now()} - {message}\n')
            print(message)

    def pridanie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            self._write_to_log("Tovar uz je na sklade")
        else:
            cena = float(input('Zadaj cenu tovaru: '))
            pocet = int(input('Zadaj pocet kusov na sklade: '))
            self.produkty[nazov] = Produkt(nazov,cena,pocet) 
            self._write_to_log("Tovar bol uspesne pridany do skladu")
            self._export_skladu()
            


    def odstranenie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            self._write_to_log('Tovar neexistuje')
        else:
            del self.produkty[nazov]
            self._write_to_log('Tovar uspesne odstraneny')
            self._export_skladu()

    def naskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            self._write_to_log("Tovar neexistuje")
        else:
            pocet = int(input('Kolko kusov tovaru naskladnit: '))
            self.produkty[nazov].pripocitat(pocet)
            self._write_to_log(f"Naskladnenie bolo uspesne {nazov}")
            self._export_skladu()

    def vyskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            self._write_to_log("Tovar neexistuje")
        else:
            pocet = int(input('Kolko kusov tovaru vyskladnit: '))
            self.produkty[nazov].odpocitat(pocet)
            self._export_skladu()
            

    def nastav_cenu(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov not in self.produkty:
            self._write_to_log("Tovar neexistuje")
        else:
            cena = float(input('Zadaj cenu tovaru: '))
            self.produkty[nazov].nacen(cena)
            self._write_to_log('Cena bola uspesne nastavena')
            self._export_skladu()

    def hodnota_skladu(self):
        suma = 0
        for x in self.produkty.values():
            suma += x.vrat_celkovu_cenu()
        self._write_to_log(f"Celkova cena skladu je {suma}€")

    #"voda;2.5;20|chlieb;2;50"
    def export_skladu(self):
        for x in self.produkty.values():
            print(x.export_vypis(),end="|")
        print()
    
    def _export_skladu(self):
        self.c.execute('delete from produkty')
        for x in self.produkty:
            self.c.execute('insert into produkty (nazov,cena,pocet) VALUES (?,?,?)',
                           (x,self.produkty[x].cena,self.produkty[x].pocet))
        self.conn.commit()

        # records = []
        # for x in self.produkty.values():
        #     records.append(x.export_vypis())
        # data = "|".join(records)
        # with open(self.data_path,'w',encoding='utf-8') as f:
        #     f.write(data)

    def _import_skladu(self,data):
        x = data.split('|')
        #"voda;2.5;20"
        self.produkty.clear()
        for i in x:
            if i == '':
                continue
            result = i.split(';')
            # ["voda",2.5,20]
            self.produkty[result[0]] = Produkt(result[0],float(result[1]),int(result[2]))

    def import_skladu(self):
        import_string = input("Zadaj import string: ")
        self._import_skladu(import_string)





