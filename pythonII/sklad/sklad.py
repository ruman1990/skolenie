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

# voda;1.5;20|muka;2;20|chlieb;2.5;50
from produkt import Produkt
from audit import Audit
import os
class Sklad:

    def __init__(self,name):
        self.audit = Audit()
        self.name = name
        self.file_db = name + '.txt'
        self.produkty = {}
        if os.path.exists(self.file_db):
            with open(self.file_db,'r',encoding='utf-8') as f:
                self._read_file_db(f.read())
        

    def vypis_skladu(self):
        for x in self.produkty.values():
            print(x)

    def pridanie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            self.audit.log_zapis("Tovar uz je na sklade")
        else:
            cena = input('Zadaj cenu: ')
            pocet_kusov = input('Zadaj pocet kusov: ')
            try:
                self.produkty[nazov]= Produkt(nazov,float(cena) if cena else 0,int(pocet_kusov) if pocet_kusov else 0)
                self.audit.log_zapis('Produkt bol pridany do skladu')
            except:
                self.audit.log_zapis("Zadal si neplatne hodnoty")

    def odobranie_tovaru(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            del self.produkty[nazov]
            self.audit.log_zapis(f"Tovar bol odstraneny {nazov}")
        else:
            self.audit.log_zapis(f'Tovar nie je na sklade {nazov}')

    def naskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            pocet_kusov = int(input('Kolko kusov: '))
            self.produkty[nazov].pocet_kusov += pocet_kusov
            self.audit.log_zapis(f'Naskladnene produkt {nazov}')
        else:
            self.audit.log_zapis(f'Tovar nie je na sklade {nazov}')

    def vyskladnenie(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            pocet_kusov = int(input('Kolko kusov: '))
            if pocet_kusov>self.produkty[nazov].pocet_kusov:
                self.audit.log_zapis('Nie je tolko tovaru na sklade')
            else:
                self.produkty[nazov].pocet_kusov -= pocet_kusov
                self.audit.log_zapis(f'Vyskladnenie produkt {nazov}')
        else:
            self.audit.log_zapis(f'Tovar nie je na sklade {nazov}')

    def nastav_cenu(self):
        nazov = input('Zadaj nazov tovaru: ')
        if nazov in self.produkty:
            cena = float(input('Zadaj cenu: '))
            self.produkty[nazov].cena = cena
            self.audit.log_zapis(f'Cena je nastavena {nazov}')
        else:
            self.audit.log_zapis(f'Tovar nie je na sklade {nazov}')

    def zobraz_sumu(self):
        suma = 0
        for x in self.produkty.values():
            suma = suma + x.hodnota()
        self.audit.log_zapis(f'Celkova cena tovarov je: {suma}')

    def export_skladu(self):
        print(self._priprava_exportu())
        self.audit.log_zapis(f'Export logu sa uspesne vykonal')

    def _priprava_exportu(self):
        vystup = []
        for x in self.produkty.values():
            vystup.append(x.export_string())
        return "|".join(vystup)

    def zapis_skladu(self):
        with open(self.file_db,'w',encoding='utf-8') as f:
            f.write(self._priprava_exportu())
        print(self.audit.log_zapis('Sklad sa zapisal do suboru'))

    def import_skladu(self):
        x = input("Zadaj string z exportu skladu: ")
        self._read_file_db(x)

    def _read_file_db(self,import_text):
        zoznam = import_text.split('|')
        produkty_temp = {}
        for y in zoznam:
            elementy = y.split(";")
            if len(elementy) != 3:
                self.audit.log_zapis('Zly import string')
                return
            produkty_temp[elementy[0]] = Produkt(elementy[0],float(elementy[1]),int(elementy[2]))
        self.produkty.clear()
        self.produkty.update(produkty_temp)
        self.audit.log_zapis('Import bol uspesne dokonceny')


    