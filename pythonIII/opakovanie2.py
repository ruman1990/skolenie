# Načítaj údaje zo súboru auta.csv.
import csv
import sqlite3
import datetime

with open("auta.csv","r",encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
conn = sqlite3.connect("auta.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS auta (
            id INTEGER PRIMARY KEY,
            znacka TEXT,
          model TEXT,
          rok_vyroby INTEGER,
          cena REAL
          )""")

c.execute("DELETE FROM auta")
c.executemany("INSERT INTO auta (znacka, model, rok_vyroby, cena) values (?,?,?,?)",data[1:])

# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).

rok = datetime.datetime.now()
c.execute("SELECT count(*) FROM auta WHERE ? - rok_vyroby > 5",(rok.year,))
#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).
result = c.fetchone()


print(f"Pocet aut starsich ako 5 rokov je: {result[0]}")

c.execute("SELECT AVG(cena) FROM auta")
result = c.fetchone()
print(f"Priemerna cena aut je: {result[0]:.2f}")

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
c.execute("SELECT * FROM auta WHERE cena>20000 order by cena desc")
result = c.fetchall()
for x in result:
    print(x)

conn.commit()
conn.close()
