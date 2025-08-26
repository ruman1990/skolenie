# letecka_preprava.py

#LH123	Viedeň	Berlín	150	Airbus A320
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737


# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple
Let = namedtuple('Let', ['cislo', 'odlet', 'ciel', 'pocet_pasazierov'])
zoznam=[
Let('LH123', 'Viedeň', 'Berlín', 150),
Let('BA456', 'Londýn', 'Paríž', 200),
Let('AF789', 'Praha', 'Rím', 180),
Let('KL101', 'Amsterdam', 'Madrid', 220),
Let('LX202', 'Ženeva', 'Brusel', 170)
]

# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass

@dataclass
class LetDataclass:
    cislo: str
    odlet: str
    ciel: str
    pocet_pasazierov: int
    typ_lietadla: str

import random

#zoznam_dataclass = []
#for x in zoznam:
#    zoznam_dataclass.append(LetDataclass(x[0], x.odlet, x.ciel, x.pocet_pasazierov, random.choice(['Airbus', 'Boeing'])))


zoznam_dataclass = [LetDataclass(x.cislo, x.odlet, x.ciel, x.pocet_pasazierov,random.choice(['Airbus','Boeing'])) for x in zoznam]
print(zoznam_dataclass)
# 3. Uloženie do Excelu (openpyxl)

from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Lety"
ws.append(['Cislo', 'Odlet', 'Ciel', 'Pocet_pasazierov', 'Typ_lietadla'])
for let in zoznam_dataclass:
    ws.append([let.cislo, let.odlet, let.ciel, let.pocet_pasazierov, let.typ_lietadla])

wb.save("lety.xlsx")

# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvo tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="sklad",
    user="postgres",
    password='admin')

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS lety (
            cislo TEXT PRIMARY KEY,
            odlet TEXT,
            ciel TEXT,
            pocet_pasazierov INTEGER,
            typ_lietadla TEXT
              )""")

cur.execute("DELETE FROM lety")  # Vyčisti tabuľku pred vložením nových dát
for let in zoznam_dataclass:
    cur.execute("INSERT INTO lety (cislo, odlet, ciel, pocet_pasazierov, typ_lietadla) VALUES (%s, %s, %s, %s, %s)",
                (let.cislo, let.odlet, let.ciel, let.pocet_pasazierov, let.typ_lietadla))
    
conn.commit()

# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute("SELECT SUM(pocet_pasazierov) FROM lety")
y = cur.fetchone()
total_pasazierov_sql = y[0]
print(f"Celkový počet pasažierov (SQL): {total_pasazierov_sql}")

pocet = sum(let.pocet_pasazierov for let in zoznam_dataclass)
print(f"Celkový počet pasažierov (Python): {pocet}")

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python
cur.execute("SELECT count(*) FROM lety WHERE ciel = %s", ('Paríž',))
y = cur.fetchone()
pocet_pariz_sql = y[0]
print(f"Počet letov do Paríža (SQL): {pocet_pariz_sql}")

lety_do_pariza = [let for let in zoznam_dataclass if let.ciel == 'Paríž']
print(f"Počet letov do Paríža (Python): {len(lety_do_pariza)}")

#7. let s najvacsim poctom pasazierov v sql a python
cur.execute("SELECT * FROM lety ORDER BY pocet_pasazierov DESC LIMIT 1")
y = cur.fetchone()
print(f"Let s najväčším počtom pasažierov (SQL): {y}")

max_let = max(zoznam_dataclass, key=lambda let: let.pocet_pasazierov)
print(f"Let s najväčším počtom pasažierov (Python): {max_let}")
