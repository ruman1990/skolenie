# Načítaj údaje zo súboru auta.csv.

# Spracuj hodnotu cena pomocou typu decimal.Decimal kvôli presnosti.

# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.

# Vlož všetky údaje z CSV do databázy.

# Po zápise:

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).

#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.


# Načítaj údaje zo súboru auta.csv.

# Spracuj hodnotu cena pomocou typu decimal.Decimal kvôli presnosti.

# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.

# Vlož všetky údaje z CSV do databázy.

# Po zápise:

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).

#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
import csv
import sqlite3

with open('auta.csv',encoding='utf-8',newline='') as f:
    reader = csv.DictReader(f)
    auta = list(reader)

conn = sqlite3.connect('auta.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS auta (
          id INTEGER PRIMARY KEY,
          znacka TEXT,
          model TEXT,
          datum INTEGTER,
          cena REAL)
          """)

c.execute("DELETE FROM auta")

for a in auta:
    #print(a)
    c.execute("INSERT INTO auta (znacka, model, datum,cena) VALUES (?,?,?,?)",(a['znacka'],a['model'],a['rok_vyroby'],a['cena']))


conn.commit()
import datetime

rok = datetime.datetime.now().year
c.execute("select count(*) from auta where ? - datum > 5 ",(rok,))

pocet = c.fetchone()[0]
print(f'Pocet aut starsich 5 rokov: {pocet}')


c.execute("select AVG(cena) from auta")

priemer = c.fetchone()[0]

print(f'Priemerna cena auta: {priemer}')


c.execute("select * from auta where cena > 20000")
zoznam = c.fetchall()
print(zoznam)

