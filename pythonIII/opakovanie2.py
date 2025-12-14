# Načítaj údaje zo súboru auta.csv.
import csv

with open('auta.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    auta = list(reader)

#print(auta)
# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
import sqlite3

conn = sqlite3.connect('auta.db')
cur = conn.cursor()

cur.execute('''create table if not exists auta 
            (
                id INTEGER PRIMARY KEY,
                znacka TEXT,
                model TEXT,
                rok_vyroby INTEGER,
                cena REAL
            )
            ''')

cur.execute("delete from auta")

for x in auta:
    cur.execute('insert into auta (znacka,model,rok_vyroby,cena) VALUES (?,?,?,?)',
                (x['znacka'],x['model'],x['rok_vyroby'],x['cena']))
    
conn.commit()


# Vlož všetky údaje z CSV do databázy.
from datetime import datetime
rok = datetime.now().strftime('%Y')
#print(rok)
treshold = 5
#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
cur.execute('select count(1) from auta where ? - rok_vyroby > ?',(rok,treshold))
res = cur.fetchone()
print(f'pocet aut starsich ako 5 rokov: {res[0]}')
#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).
cur.execute('select avg(cena) from auta')
res = cur.fetchone()
print(f'priemerna cena aut: {res[0]}')

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
cur.execute('select * from auta where cena>20000')
res = cur.fetchall()

print(res)