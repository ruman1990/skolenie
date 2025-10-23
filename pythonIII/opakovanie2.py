# Načítaj údaje zo súboru auta.csv.
import csv
import sqlite3
with open('auta.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    cars = list(reader)

#with open('auta.csv','r',encoding='utf-8') as f:
#    reader = csv.DictReader(f)
#    cars = print(list(reader))
    

#print(cars)

conn = sqlite3.connect('auta.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS auta (
            id INTEGER PRIMARY KEY,
            znacka TEXT,
            model TEXT,
            rok_vyroby INTEGER,
            cena REAL
            )''')

#from decimal import Decimal
#for x in cars[1:]:
#    x[3] = int(Decimal(str(x[3])) * Decimal('100'))
#for x in cars[1:]:
#    cur.execute('INSERT INTO auta (znacka,model,rok_vyroby,cena) values (?,?,?,?)',x)   
#for x in cars:
#    cur.execute('INSERT INTO auta (znacka,model,rok_vyroby,cena) values (?,?,?,?)',(x['znacka'],x['model'],x['rok_vyroby'],x['cena']))
cur.execute('DELETE FROM auta')
cur.executemany('INSERT INTO auta (znacka,model,rok_vyroby,cena) values (?,?,?,?)',cars[1:])


conn.commit()


# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.

# Vlož všetky údaje z CSV do databázy.


# Po zápise:
from decimal import Decimal
#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
import datetime
rok = datetime.datetime.now().year
cur.execute('SELECT count(*) from auta where (? - rok_vyroby > 5)',(rok,))
pocet = cur.fetchone()[0]
print(pocet)
#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).
cur.execute('SELECT AVG(cena) from auta')
priemer = cur.fetchone()[0]
print(f'{Decimal(str(priemer)):.2f} €')
#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.

cur.execute('select * from auta where cena > 20000 order by cena desc')
result = cur.fetchall()

print(result)

conn.close()