# Načítaj údaje zo súboru auta.csv.
import csv

with open("auta.csv",'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data[1:]:
        print(row)

#print(auta)
# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
import sqlite3

conn = sqlite3.connect("auta.db")
c = conn.cursor()

c.execute('''
    create table if not exists auta (
            id INTEGER PRIMARY KEY,
            znacka TEXT,
            model TEXT,
            rok_vyroby INTEGER,
            cena REAL
          )
''')

c.execute('delete from auta')

c.executemany('insert into auta (znacka,model,rok_vyroby,cena) Values (?,?,?,?)',data[1:])

conn.commit()
# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
import datetime
year = datetime.datetime.now().year
c.execute('select count(*) from auta where rok_vyroby<?',(year-5,))
print(f'Pocet aut starsich ako 5 rokov je: {c.fetchone()[0]}')

#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).
c.execute('select avg(cena) from auta')
from decimal import Decimal, getcontext
getcontext().prec = 2
result = c.fetchone()[0]
d = Decimal(str(result))

print(f'Priemerna cena aut je: {d:.2f}')

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc

c.execute('select * from auta where cena > 20000 order by cena desc')
print(c.fetchall())