# letecka_preprava.py

#LH123	Viedeň	Berlín	150	Airbus A320
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737


# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple

Let = namedtuple('Let',['cislo','odlet','ciel','pocet_pasazierov'])

zoznam = [
    Let('LH123','Viedeň','Berlín',150),
    Let('BA456','Londýn','Paríž',200),
    Let('AF789','Praha','Rím',180),
    Let('KL101','Amsterdam','Madrid',220),
    Let('LX202','Ženeva','Brusel',170)
]

# 2. Prevod na dataclass, pridanie typu lietadla

from dataclasses import dataclass

@dataclass
class CLet:
    cislo: str
    odlet: str
    ciel: str
    pocet_pasazierov: int

    def __repr__(self):
        return f'{self.cislo},{self.odlet},{self.ciel},{self.pocet_pasazierov}'

# dataclass_zoznam = []
# for x in zoznam:
#     dataclass_zoznam.append(CLet(x.cislo,x.odlet,x.ciel,x.pocet_pasazierov))

dataclass_zoznam = [CLet(x.cislo,x.odlet,x.ciel,x.pocet_pasazierov) for x in zoznam]

print(dataclass_zoznam)

# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.append(['cislo', 'odlet', 'ciel', 'pocet_pasazierov'])

for x in dataclass_zoznam:
    ws.append([x.cislo,x.odlet,x.ciel,x.pocet_pasazierov])

wb.save('lety.xlsx')

# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvo tabulku letov
# 4. Uloženie do Postgre (psycopg2)

import psycopg2

with psycopg2.connect('dbname=skolenie user=postgres password=admin host=localhost') as conn:
    with conn.cursor() as cur:

        cur.execute('''
                CREATE TABLE IF NOT EXISTS lety (
                        id SERIAL PRIMARY KEY,
                        cislo TEXT,
                        odlet TEXT,
                        ciel TEXT,
                        pocet_pasazierov INTEGER
                    )
                    ''')
        
        cur.execute('DELETE FROM lety')

        for a in dataclass_zoznam:
            cur.execute('INSERT INTO lety (cislo,odlet,ciel,pocet_pasazierov) VALUES (%s,%s,%s,%s)',
                        (a.cislo,a.odlet,a.ciel,a.pocet_pasazierov))

        conn.commit()


# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python

        cur.execute('select sum(pocet_pasazierov) from lety')
        result = cur.fetchone()
        print(f'Celkovy pocet pasazierov je {result[0]}')

        result = sum([a.pocet_pasazierov for a in dataclass_zoznam])
        print(f'Celkovy pocet pasazierov je {result}')

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python
        cur.execute('select * from lety where ciel=%s',('Paríž',))

        result = cur.fetchall()
        print(f'Vsetky lety do Pariza {result}',f'Pocet {len(result)}')

        result = [a for a in dataclass_zoznam if a.ciel == 'Paríž']
        print(f'Vsetky lety do Pariza {result}',f'Pocet {len(result)}')

#7. let s najvacsim poctom pasazierov v sql a python
        cur.execute('select * from lety order by pocet_pasazierov desc limit 1')
        result = cur.fetchone()
        print(f'Najvacsi pocet pasazierov je {result}')

        result = max(dataclass_zoznam,key= lambda x : x.pocet_pasazierov)
        print(f'Najvacsi pocet pasazierov je {result}')