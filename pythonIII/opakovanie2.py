# Načítaj údaje zo súboru auta.csv.
import csv
import sqlite3
from datetime import datetime
from decimal import Decimal
data = []
with open("auta.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    reader.__next__()
    for x in reader:
        data.append(x)
        print(x)
# Vlož všetky údaje z CSV do databázy.
conn = sqlite3.connect("auta.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS auta (
    id INTEGER PRIMARY KEY,
    znacka TEXT,
    model TEXT,
    rok_vyroby INTEGER,
    cena REAL
)
""")
cur.execute("delete from auta")
cur.executemany("insert into auta (znacka,model,rok_vyroby,cena) values (?,?,?,?)",data)

conn.commit()
#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
aktualny_rok = datetime.now().year
 
cur.execute("""
    SELECT COUNT(*) FROM auta
    WHERE rok_vyroby < ?
""", (aktualny_rok - 5,))
 
pocet = cur.fetchone()
print(f"Pocet aut starsich ako 5 rokov je: {pocet[0]}")

stare = []
for x in data:
    if int(x[2]) < (aktualny_rok - 5):
        stare.append(x)

print(f"Pocet aut starsich ako 5 rokov je: {len(stare)}")

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
cur.execute("""SELECT * FROM auta WHERE cena > 20000 ORDER BY cena DESC""")
 
auta = cur.fetchall()
 
for auto in auta:
    print(auto)

drahe = []
for x in data:
    if Decimal(x[3]) > 20000:
        drahe.append(x)

for x in drahe:
    print(x) 
 
# Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
cur.close()
conn.close()