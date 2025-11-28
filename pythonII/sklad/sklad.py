from tovar import Tovar
from datetime import datetime
import csv

class Sklad:
    
    def __init__(self,nazov):
        self.nazov = nazov
        with open('/home/vlado/devel/python/skolenie/pythonII/sklad/sklad.log','r',encoding='utf-8') as f:
            content_string = f.read()
            self.tovary = {}
            self._importovanie(content_string)


    def vypis_skladu(self):
        for t in self.tovary:
            print(self.tovary[t])
        self._update_log("Vypis skladu")

    def hodnota_skladu(self):
        suma = 0
        for t in self.tovary:
            suma += self.tovary[t].hodnota()
        self._update_log(f"Vypis hodnoty skladu. Hodnota skladu je {suma}€")

    def pridat_tovar(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov in self.tovary:
            print('Tovar uz existuje na sklade')
        else:
            try:
                ks = int(input('Zadaj pocet kusov: '))
            except Exception:
                print('Zadal si nespravny pocet kusov')
            cena = float(input("Zadaj jednotkovu cenu: "))
            self.tovary[nazov] = Tovar(nazov,cena,ks)
            self._update_memory()
            self._update_log(f"Uspesne pridanie tovaru {nazov}")

    def odobratie_tovaru(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            del self.tovary[nazov]
            self._update_memory()
            self._update_log(f"Uspesne odstranenie tovaru {nazov}")

    def naskladnit(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            ks = int(input("Kolko kusov naskladnit: "))
            self.tovary[nazov].pocet += ks
            self._update_log(f"Uspesne naskladnenie tovaru {nazov}")
            self._update_memory()

    def vyskladnit(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            ks = int(input("Kolko kusov vyskladnit: "))
            if self.tovary[nazov].pocet<ks:
                print("Nedostatok kusov tovaru na sklade")
            else:
                self.tovary[nazov].pocet -= ks
                self._update_log(f"Uspesne vyskladnenie tovaru {nazov}")
                self._update_memory()

    def export_csv(self):
        fieldnames = ['nazov','cena','pocet']
        with open('export.csv','w',encoding='utf-8') as f:
            wr = csv.DictWriter(f,fieldnames=fieldnames)
            wr.writeheader()
            for x in self.tovary:
                wr.writerow({"nazov" : self.tovary[x].meno, "cena" : self.tovary[x].cena, "pocet" : self.tovary[x].pocet})
        self._update_log("Export do csv bol uspesny")


    def export_print(self):
        print(self._export())

    def _export(self):
        e = []
        for t in self.tovary:
            e.append(self.tovary[t].export_format())
        self._update_log(f"Uspesne exportovanie skladu")
        return "|".join(e)

    def importovanie_from_user(self):
        self._importovanie(input('Zadaj import string: '))
        self._update_log(f"Uspesne importovanie skladu")


    def _importovanie(self,content_string):
        self.tovary.clear()
        tov = content_string.split('|')
        for y in tov:
            r = y.split(';')
            self.tovary[r[0]] = Tovar(r[0],float(r[1]),int(r[2]))

    def nastav_cenu(self):
        nazov = input("Zadaj nazov tovaru: ")
        if nazov not in self.tovary:
            print('Tovar neexistuje')
        else:
            cena = float(input("Zadaj cenu tovaru: "))
            self.tovary[nazov].cena = cena
            self._update_log(f"Uspesne nastavenie ceny tovaru {nazov}")
            self._update_memory()

    def _update_memory(self):
        with open('sklad.log','w',encoding='utf-8') as f:
            f.write(self._export())

    def _update_log(self,message):
        with open('log.txt','a',encoding='utf-8') as f:
            f.write(f"{datetime.now()} - {message}\n")
            print(message)

    def vypis_log(self):
        with open('log.txt','r',encoding='utf-8') as f:
            print(f.read())





