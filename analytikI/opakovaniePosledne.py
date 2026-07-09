# letecka_preprava.py

#LH123	Viedeň	Berlín	150	"Airbus A320"
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737
from collections import namedtuple

# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
Let = namedtuple("Let",["cislo_letu","odlet","ciel","pocet_pasazierov","typ_lietadla"])

import csv


with open("lety.csv","r",encoding="utf-8") as f:
    lety = [Let(*x) for x in csv.reader(f)]
    header = lety[0]
    lety = lety[1:]
    # data = csv.reader(f)
    # for x in data:
    #     lety.append(Let(x[0],x[1],x[2],x[3],x[4]))

#print(lety)

# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass

@dataclass
class LetDataclass:
    cislo_letu : str
    odlet : str
    ciel : str
    pocet_pasazierov : int
    typ_lietadla : str

zoznam = [LetDataclass(*x) for x in lety]

#print(zoznam)
# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Lety"

ws.append(header)
for x in lety:
    ws.append([x[0],x[1],x[2],int(x[3]),x[4]])

wb.save("lety.xlsx")


# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2
# import psycopg

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS lety (
                cislo TEXT PRIMARY KEY,
                odlet TEXT NOT NULL,
                ciel TEXT NOT NULL,
                pocet_pasazierov BIGINT NOT NULL,
                typ_lietadla TEXT NOT NULL
            )""")

cur.execute("DELETE FROM lety")

for x in lety:
    cur.execute("INSERT INTO lety values (%s,%s,%s,%s,%s)",x)

conn.commit()

# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute("select sum(pocet_pasazierov) from lety")

data = cur.fetchone()
print(f"Pocet prevezenych pasazierov je: {data[0]}")

print(f"Pocet prevezenych pasazierov je: {sum([int(x.pocet_pasazierov) for x in zoznam])}")


#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 
cur.execute("SELECT count(*) FROM public.lety where ciel='Paríž'")
data = cur.fetchone()

print(f"Pocet letov do pariza je {data[0]}")

data  = [ x for x in zoznam if x.ciel == 'Paríž']
print(f"Pocet letov do pariza je {len(data)}")


cur.execute("SELECT * FROM public.lety order by pocet_pasazierov desc limit 1")
data = cur.fetchone()

print(f"Let s najviac pasaziermi {data}")

print(f"Let s najviac pasaziermi {max(lety,key=lambda x : x.pocet_pasazierov)}")