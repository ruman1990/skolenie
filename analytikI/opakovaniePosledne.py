# letecka_preprava.py

# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple
Let = namedtuple('Let',['cislo','odlet','ciel','pocet_pasazierov'])

lety = [ Let('LH123', 'Viedeň', 'Berlín', 150),
         Let('BA456', 'Londýn', 'Paríž', 200),
         Let('AF789', 'Praha', 'Rím', 180) ,
         Let('KL101', 'Amsterdam', 'Madrid', 220) ,
         Let('LX202', 'Ženeva', 'Brusel', 170) ]

# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass
import random

@dataclass
class LetClass:
    cislo : str
    odlet : str
    ciel : str
    pocet_pasazierov : int
    typ_lietadla : str

data_lety = [LetClass(*let,random.choice(['Boeing 737','Airbus A320'])) for let in lety]

# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.append(['Cislo', 'Odlet', 'Ciel', 'Pocet pasazierov', 'Typ lietadla'])
for let in data_lety:
    ws.append([let.cislo, let.odlet, let.ciel, let.pocet_pasazierov, let.typ_lietadla])

wb.save('lety.xlsx')
# 4. Načítanie z Excelu
from openpyxl import load_workbook
wb = load_workbook('lety.xlsx')
ws = wb.active

# Prečítaj všetky riadky z Excelu a zapis do tablib Dataset a exportuj do CSV

import tablib

data = tablib.Dataset()
rows = list(ws.iter_rows(values_only=True))
data.headers = rows[0]
for row in rows[1:]:
    data.append(row)

with open('lety.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(data.export('csv'))

# 5. Sčítanie pasažierov z CSV cez tablib
q = sum([r['Pocet pasazierov'] for r in data.dict])
<<<<<<< Updated upstream
print(f'Pocet pasazierov na vsetkych linkach je {q}')
=======
print(f'Pocet pasazierov na vsetkych linkach je {q}')
>>>>>>> Stashed changes
