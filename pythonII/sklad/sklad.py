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

class Sklad:

    def __init__(self,nazov,data_path='sklad.txt',log_path='log.txt'):
        self.nazov = nazov
        self.produkty = {}
        self.log_path = log_path
        self.data_path = data_path

        if os.path.exists(data_path):
            with open(data_path,'r',encoding='utf-8') as f:
                self._import_skladu(f.read())
        else:
            with open(data_path,'w',encoding='utf-8') as f:
                pass
    
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
        records = []
        for x in self.produkty.values():
            records.append(x.export_vypis())
        data = "|".join(records)
        with open(self.data_path,'w',encoding='utf-8') as f:
            f.write(data)

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





