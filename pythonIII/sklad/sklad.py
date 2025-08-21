# Chcem vytvori skladovy softver
# Bude mat textove menu s volbami
# ked klient vyberie volbu, zadane potrebne vstupne udaje, volba sa vykona
# Po vykonani zvolenej volby sa zobrazi znovu MENU s volbami
# Pre ukoncenie programu je potrebne mat vlastnu volbu.
# 1. Vypisat zoznam produktov na sklade
# 2. Pridat produkt do skladu
# 3. Odstranit produkt
# 4. Nastavenie ceny produktu
# 5. Naskladnenie produktu
# 6. Vyskladnenie produktu
# 7. Hodnota skladu
# 8. Export skladu
# 9. Import skladu
from produkt import Produkt
from audit import Audit
import sqlite3

class Sklad:
    def __init__(self,nazov):
        self.nazov = nazov
        self.produkty = {}
        self.log = Audit()

        self.conn = sqlite3.connect('sklad.db')
        self.c = self.conn.cursor()

        self.c.execute('''
                    CREATE TABLE IF NOT EXISTS produkty (
                       nazov TEXT PRIMARY KEY,
                       cena REAL NOT NULL DEFAULT 0.0,
                       pocet INTEGER NOT NULL DEFAULT 0
                       )
                    ''')
        
        self.conn.commit()

        self.c.execute('SELECT * FROM produkty')
        for row in self.c.fetchall():
            self.produkty[row[0]] = Produkt(row[0],row[1],row[2])


    def prikaz_db(self,sql,params):
        self.c.execute(sql,params)
        self.conn.commit()

    def vypis_produkty(self):
        print('')
        for p in self.produkty.values():
            print(p)
        print('')

    def pridaj_produkt(self):
        print('')
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            print('Produkt uz existuje')
        else:
            cena = float(input("Zadaj cenu produktu: "))
            pocet = int(input("Zadaj pocet kusov: "))
            self.produkty[nazov] = Produkt(nazov,cena,pocet)
            self.prikaz_db('INSERT INTO produkty (nazov,cena,pocet) VALUES (?,?,?)',(nazov,cena,pocet))
            self.log.zapis(f'Produkt {nazov} bol uspesne pridany do skladu')

    def odstran_produkt(self):
        nazov = input("Zadaj nazov produktu na odstranenie: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            self.prikaz_db('DELETE FROM produkty where nazov=?',(nazov,))
            self.log.zapis(f"Produkt {nazov} bol odstraneny.")
        else:
            print('Produkt sa nenasiel.')

    def zobraz_sumu(self):
        suma = 0.0
        for p in self.produkty.values():
            suma += (p.cena * p.pocet)
        print(f'Celkova hodnota skladu: {suma:.2f}€')

    def export_skladu(self):
        vystup = []
        for p in self.produkty.values():
            vystup.append(p.export_tvar())
        retazec = '|'.join(vystup)
        print('====EXPORT TEXT====')
        print(retazec)
        print('====Skopiruj a uloz====')

    def import_skladu(self):
        text = input("Vloz vstupny text: ")
        zoznam_produktov = text.split("|")
        self.produkty.clear()

        for i in zoznam_produktov:
            x = i.split(';')
            self.produkty[x[0]] = Produkt(x[0],float(x[1]),int(x[2]))
        self.prikaz_db('DELETE from produkty',())

        for x in self.produkty:
            self.prikaz_db('INSERT INTO produkty (nazov,cena,pocet) VALUES (?,?,?)',(self.produkty[x].nazov,self.produkty[x].cena,self.produkty[x].pocet))          
        self.log.zapis(f"Import bol uspesny. Pocet naimportovanych produktov {len(self.produkty)}")

    def naskladnit(self):
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov: "))
            self.produkty[nazov].pocet += kusy
            self.prikaz_db('UPDATE produkty SET pocet=? WHERE nazov=?',(self.produkty[nazov].pocet,nazov))
            self.log.zapis(f'Produkt {nazov} bol naskladneny {kusy}')
        else:
            print("Produkt nie je na sklade")
        

    def vyskladnit(self):
        nazov = input('Zadaj nazov produktu: ')
        if nazov in self.produkty:
            kusy = int(input("Zadaj pocet kusov: "))
            if kusy>self.produkty[nazov].pocet:
                print('Nedostatok kusov na sklade')
            else:
                self.produkty[nazov].pocet -= kusy
                self.prikaz_db('UPDATE produkty SET pocet=? WHERE nazov=?',(self.produkty[nazov].pocet,nazov))
                self.log.zapis(f"Produkt {nazov} bol vyskladneny")
        else:
            print("Produkt nie je na sklade")



