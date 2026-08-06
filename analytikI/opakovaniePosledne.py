# letecka_preprava.py

#LH123	Viedeň	Berlín	150	"Airbus A320"
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737

import csv

# class Let:

#     def __init__(self,cislo,odlet,ciel,pocet_pasazierov,typ_lietadla):
#         self.cislo = cislo
#         self.odlet = odlet
#         self.ciel = ciel
#         self.pocet_pasazierov = pocet_pasazierov
#         self.typ_lietadla = typ_lietadla





# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple

Let = namedtuple("Let",["cislo","odlet","ciel","pocet_pasazierov","typ_lietadla"])

with open("lety.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    header = reader.__next__()
    data = [Let(*x) for x in reader]

print(data)



# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass

@dataclass
class LetDataClass:
    cislo : str
    odlet : str
    ciel : str
    pocet_pasazierov : int
    typ_lietadla : str

    def __post_init__(self):
        self.pocet_pasazierov = int(self.pocet_pasazierov)

    def to_list(self):
        return [self.cislo,self.odlet,self.ciel,self.pocet_pasazierov,self.typ_lietadla]

data_class = [LetDataClass(*x) for x in data]

print(data_class)

#print(zoznam)
# 3. Uloženie do Excelu (openpyxl)

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Lety"

ws.append(header)
for x in data_class:
    ws.append(x.to_list())
    #ws.append(x.cislo,x.odlet,x.ciel,int(x.pocet_pasazierov),x.typ_lietadla)

chart = BarChart()

dataset = Reference(ws,min_col=4,max_col=4,min_row=2,max_row=6)
kategorie = Reference(ws,min_col=1,max_col=1,min_row=2,max_row=6)

chart.add_data(dataset)
chart.set_categories(kategorie)

ws.add_chart(chart)

wb.save("lety.xlsx")

# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2

conn = psycopg2.connect(host="localhost",database="analytik",user="postgres",password="admin")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS lety (cislo TEXT PRIMARY KEY,odlet TEXT, ciel TEXT, pocet_pasazierov INTEGER, typ_lietadla TEXT)")
cur.execute("DELETE FROM lety")
cur.executemany("INSERT INTO lety VALUES (%s,%s,%s,%s,%s)",data)


conn.commit()

# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute("select sum(pocet_pasazierov) from lety")
result = cur.fetchone()
print(f"Celkovy pocet pasazierov je {result[0]}")

print(f"Celkovy pocet pasazierov je {sum([int(x.pocet_pasazierov) for x in data])}")




#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 

cur.execute("select * from lety where ciel='Paríž'")
result = cur.fetchall()

print(result)

cur.execute("select count(*) from lety where ciel='Paríž'")
result = cur.fetchone()
print(f"Pocet letov do Pariza je {result[0]}")

result = [x for x in data if x.ciel=='Paríž']
print(result)

print(f"Pocet letov do Pariza je {len(result)}")

