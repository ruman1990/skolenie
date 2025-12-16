# letecka_preprava.py

#LH123	Viedeň	Berlín	150	Airbus A320
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737


# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple

Let = namedtuple("Let",['cislo','odlet','ciel','pocet_pasazierov'])

l = Let('LH123','Viedeň','Berlín',150)
l2 = Let('BA456','Londýn','Paríž',200)
l3 = Let('AF789','Praha','Rím',180)
l4 = Let('KL101','Amsterdam','Madrid',220)
l5 = Let('LX202','Ženeva','Brusel',170)

lety = [l,l2,l3,l4,l5]


# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass, field

@dataclass
class LetDataClass:
    cislo : str
    odlet : str 
    ciel : str
    pocet_pasazierov : int
    typ_lietadla : str

import random

#zoznam = [LetDataClass(x.cislo,x.odlet,x.ciel,x.pocet_pasazierov,random.choice(['Airbus A320','Boeing 737'])) for x in lety]

zoznam = []
for x in lety:
    zoznam.append(LetDataClass(x.cislo,
                               x.odlet,
                               x.ciel,
                               x.pocet_pasazierov,
                               random.choice(['Airbus A320','Boeing 737'])))


print(zoznam)
# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabelList

wb = Workbook()
ws = wb.active
ws.title = 'Lety'
ws.append(['cislo','odlet','ciel','pocet_pasazierov','typ_lietadla'])
for x in zoznam:
    ws.append([x.cislo,x.odlet,x.ciel,x.pocet_pasazierov,x.typ_lietadla])


graf = BarChart()
graf.title = "Lety"
graf.y_axis.title = "Pocet pasazierov"
graf.x_axis.title = "Cislo letu"

# 4. Určenie dát pre graf (iba stĺpec „Spolu €“)
data = Reference(ws, min_col=4, max_col=4,min_row=2,max_row=ws.max_row)
kategorie = Reference(ws, min_col=1,max_col=1, min_row=2,max_row=ws.max_row)

graf.add_data(data, titles_from_data=True)
graf.set_categories(kategorie)

graf.dataLabels = DataLabelList()
graf.dataLabels.showVal = True

# 5. Vloženie grafu
ws.add_chart(graf, "G2")

wb.save('result_lety.xlsx')

# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2

conn = psycopg2.connect(
    dbname="sklad",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)

cur = conn.cursor()

cur.execute('''
    create table if not exists lety (
         	cislo TEXT PRIMARY KEY,
            odlet TEXT,
            ciel TEXT,
            pocet_pasazierov INTEGER,
            typ_lietadla TEXT   )
''')

cur.execute('delete from lety')

for x in zoznam:
    cur.execute('insert into lety (cislo,odlet,ciel,pocet_pasazierov,typ_lietadla) values' \
                '(%s,%s,%s,%s,%s)',(x.cislo,x.odlet,x.ciel,x.pocet_pasazierov,x.typ_lietadla))


conn.commit()
# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute('select sum(pocet_pasazierov) from lety')
x = cur.fetchone()
print(f'Celkovy pocet pasazierov je: {x[0]}')

pocet = sum([x.pocet_pasazierov for x in zoznam])
print(f'Celkovy pocet pasazierov je: {pocet}')

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 
cur.execute("select count(*) from lety where ciel='Paríž' ")
x = cur.fetchone()
print(f'Celkovy pocet letov do Pariza je: {x[0]}')

pocet = len([x for x in zoznam if x.ciel=='Paríž'])
print(f'Celkovy pocet letov do Pariza je: {pocet}')
#7. let s najvacsim poctom pasazierov v sql a python
cur.execute("select * from lety order by pocet_pasazierov desc limit 1 ")
x = cur.fetchone()
print(f'Let s najvyssim poctom pasazierov je: {x}')

naj_let = max(zoznam,key=lambda x: x.pocet_pasazierov)
print(f'Let s najvyssim poctom pasazierov je: {naj_let}')