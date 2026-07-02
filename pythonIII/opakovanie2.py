# Načítaj údaje zo súboru auta.csv.
import csv

data = []

with open("auta.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for x in reader:
        data.append(x)

data = data[1:]
#print(data)

# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
import sqlite3

conn = sqlite3.connect("auta.db")
cur = conn.cursor()

cur.execute("""
    create table if not exists auta (
                id INTEGER PRIMARY KEY,
                znacka TEXT,
                model TEXT,
                rok_vyroby INTEGER,
                cena REAL
            )
""")

cur.execute("DELETE FROM auta")

cur.executemany("INSERT INTO auta (znacka,model,rok_vyroby,cena) VALUES (?,?,?,?)",data)

conn.commit()

import datetime

today = datetime.date.today()

cur.execute("SELECT count(*) from auta where rok_vyroby<?",(today.year-5,))

pocet = cur.fetchone()
print(f"Pocet aut starsich ako 5 rokov je {pocet[0]}")

cur.execute("select * from auta where cena>20000 order by cena desc")

res = cur.fetchall()

cur.execute("select avg(cena) from auta")

priemer = cur.fetchone()

print(f"Priemerna cena aut je {priemer[0]}")

for x in res:
    print(x)

conn.close()

# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).



#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
