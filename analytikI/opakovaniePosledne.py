# letecka_preprava.py

#LH123	Viedeň	Berlín	150	"Airbus A320"
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737

lety = []
with open("lety.txt","r",encoding="utf-8") as f:
    for x in f:
        lety.append(x.replace("#","").replace("\"","").replace("	",",").strip())

lety = [x.split(",") for x in lety]

# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple

Let = namedtuple("Let",["cislo","odlet","ciel","pocet_pasazierov"])

namedtuples = [Let(*x[:-1])  for x in lety]

print(namedtuples)

# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass

@dataclass
class LetDataclass:
    cislo : str
    odlet : str
    ciel : str
    pocet_pasazierov : int
    typ_lietadla : str

objekty = [LetDataclass(*x) for x in lety]

# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Lety"

ws.append(["cislo","odlet","ciel","pocet_pasazierov","typ lietadla"])
for x in objekty:
    ws.append([x.cislo,x.odlet,x.ciel,x.pocet_pasazierov,x.typ_lietadla])

wb.save("lety.xlsx")
# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2

conn = psycopg2.connect(dbname="test",host="localhost",user="postgres",password="admin")

cur = conn.cursor()

cur.execute("""create table if not exists lety 
            (cislo TEXT PRIMARY KEY, 
            odlet TEXT, 
            ciel TEXT, 
            pocet_pasazierov BIGINT, 
            typ_lietadla TEXT)
            """)

cur.execute("delete from lety")
cur.executemany("insert into lety (cislo,odlet,ciel,pocet_pasazierov,typ_lietadla) values (%s,%s,%s,%s,%s)",lety)

conn.commit()

# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute("SELECT sum(pocet_pasazierov) from lety")
result = cur.fetchone()
print(f"Pocet pasazierov bolo : {result[0]}")

print(f"Pocet pasazierov bolo : {sum([int(x.pocet_pasazierov) for x in namedtuples])}")

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 
cur.execute("SELECT * from lety where ciel=%s",("Paríž",))
result = cur.fetchall()

print(result)
print(f"Pocet letov do Pariza bolo : {len(result)}")

filter = [x for x in namedtuples if x.ciel == 'Paríž']
print(filter)
print(f"Pocet letov do Pariza bolo : {len(filter)}")