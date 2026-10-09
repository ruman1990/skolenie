# letecka_preprava.py

#LH123	Viedeň	Berlín	150	"Airbus A320"
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737

# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple
import csv

Let = namedtuple("Let",["cislo","odlet","ciel","pocet_pasazierov"])

with open("lety.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    reader.__next__()
    data = [Let(*x[:-1]) for x in reader]

print(data)

print()
print()
# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass

@dataclass
class Let:
    cislo: str
    odlet: str
    ciel: str
    pocet_pasazierov : int
    typ_lietadla: str

    def __post_init__(self):
        self.pocet_pasazierov = int(self.pocet_pasazierov)

    def to_list(self):
        return [self.cislo,self.odlet,self.ciel,self.pocet_pasazierov,self.typ_lietadla]

with open("lety.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    header = reader.__next__()
    data = [Let(*x) for x in reader]

print(data)
#print(zoznam)
# 3. Uloženie do Excelu (openpyxl)

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Lety"

ws.append(header)
for x in data:
    ws.append(x.to_list())

wb.save('opakovanieResult.xlsx')
# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2
conn = psycopg2.connect(
    host="aws-0-eu-west-2.pooler.supabase.com",
    database="postgres",
    user="postgres.mianvtfnpgfqnzdaendq",
    password="SilneHeslo.987"
)
cur = conn.cursor()

cur.execute("""create table if not exists vlado.lety
    (
        id SERIAL PRIMARY KEY,
        cislo VARCHAR(100),
        odlet VARCHAR(100),
        ciel VARCHAR(100),
        pocet_pasazierov INTEGER,
        typ_lietadla VARCHAR(100)
    )
""")
conn.commit()

data_DB = [x.to_list() for x in data]
cur.execute("delete from vlado.lety")
cur.executemany("insert into vlado.lety (cislo,odlet,ciel,pocet_pasazierov,typ_lietadla) values (%s,%s,%s,%s,%s)",data_DB)

conn.commit()


# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute("select sum(pocet_pasazierov) from vlado.lety")
result = cur.fetchone()
print(f"Pocet vsetkych pasazierov je {result[0]}")

print(f"Pocet vsetkych pasazierov je {sum([x.pocet_pasazierov for x in data])}")

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 

cur.execute("select cislo,odlet,ciel,pocet_pasazierov,typ_lietadla from vlado.lety where ciel='Paríž'")
result = cur.fetchall()
print(result)

print([tuple(x.to_list()) for x in data if x.ciel =='Paríž'])
