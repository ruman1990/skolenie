# letecka_preprava.py

#LH123	Viedeň	Berlín	150	Airbus A320
#BA456	Londýn	Paríž	200	Airbus A320
# AF789	Praha	Rím	180	Boeing 737
# KL101	Amsterdam	Madrid	220	Boeing 737
# LX202	Ženeva	Brusel	170	Boeing 737


# 1. Vytvorenie letov pomocou namedtuple nazov Let a atributy cislo, odlet, ciel, pocet_pasazierov
from collections import namedtuple
Let = namedtuple('Let',['cislo','odlet','ciel','pocet_pasazierov'])

zoznam_letov = [Let('LH123','Viedeň','Berlín',150),
                Let('BA456','Londýn','Paríž',200),
                Let('AF789','Praha','Rím',180),
                Let('KL101','Amsterdam','Madrid',220),
                Let('LX202','Ženeva','Brusel',170)
                ]




# 2. Prevod na dataclass, pridanie typu lietadla
from dataclasses import dataclass
@dataclass
class Let:
    cislo: str
    odlet: str
    ciel: str
    pocet_pasazierov: int
    typ_lietadla: str

    def get_atributes(self):
        return [x.cislo,x.odlet,x.ciel,x.pocet_pasazierov,x.typ_lietadla]

zoznam_letov = [Let('LH123','Viedeň','Berlín',150,'Airbus A320'),
                Let('BA456','Londýn','Paríž',200,'Airbus A320'),
                Let('AF789','Praha','Rím',180,'Boeing 737'),
                Let('KL101','Amsterdam','Madrid',220,'Boeing 737'),
                Let('LX202','Ženeva','Brusel',170,'Boeing 737')
                ]

print(zoznam_letov)

# 3. Uloženie do Excelu (openpyxl)
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.append(['cislo','odlet','ciel','pocet_pasazierov','typ_lietadla'])
for x in zoznam_letov:
    ws.append(x.get_atributes())

wb.save('lety.xlsx')


# precitaj vsetky riadky a zapis ich do postgre databazy, predtym vytvor tabulku letov
# 4. Uloženie do Postgre (psycopg2)
import psycopg2

conn = psycopg2.connect(
    database = 'postgres',
    user = 'postgres',
    password = 'admin',
    host = 'localhost'
)
cur = conn.cursor()

cur.execute('''create table if not exists lety (
            id serial primary key, 
            cislo text, 
            odlet text, 
            ciel text,
            pocet_pasazierov integer,
            typ_lietadla text
            )''')

cur.execute('delete from lety')

for x in zoznam_letov:
    cur.execute('''insert into lety (cislo,odlet,ciel,pocet_pasazierov,typ_lietadla) values
            (%s,%s,%s,%s,%s)''',x.get_atributes())
conn.commit()


# 5. spocitaj pocet pasazierov celkovo pomocou sql a cez python
cur.execute('select sum(pocet_pasazierov) from lety')
result = cur.fetchone()
print(f'Pocet vsetkych pasazierov je: {result[0]}')

result = sum([x.pocet_pasazierov for x in zoznam_letov])
print(f'Pocet vsetkych pasazierov je: {result}')

#6. vypis vsetky lety do Pariza a kolko ich je cez sql a python 
cur.execute("select * from lety where ciel='Paríž'")
result = cur.fetchall()
for x in result:
    print(x)
print(f'pocet letov je: {len(result)}')

result = [x for x in zoznam_letov if x.ciel=='Paríž']
print(result)
print(f'pocet letov je: {len(result)}')
conn.close()