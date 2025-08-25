# Načítaj údaje zo súboru auta.csv.
import csv

with open('auta.csv','r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    auta = list(reader)

print(auta)
# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
import sqlite3
conn = sqlite3.connect('auta.db')
c = conn.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS auta 
          (
            id INTEGER PRIMARY KEY,
            znacka TEXT,
            model TEXT,
            rok_vyroby INTEGER,
            cena REAL
          )
          ''')

conn.commit()

c.execute('DELETE FROM auta')

# Vlož všetky údaje z CSV do databázy.
c.executemany('INSERT INTO auta (znacka,model,rok_vyroby,cena) VALUES (:znacka,:model,:rok_vyroby,:cena)',auta)

conn.commit()

# Po zápise:

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
import datetime
rok = datetime.datetime.now().year
c.execute('SELECT COUNT(*) from auta where rok_vyroby < ?',(rok-5,))
pocet = c.fetchone()[0]
print(f'Pocet starsich aut je: {pocet}')
#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).

c.execute('SELECT AVG(cena) FROM auta')
priemerna_cena = c.fetchone()[0]
print(f'Priemerna cena aut je: {priemerna_cena:.2f} €')


#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
c.execute('SELECT * FROM auta WHERE cena > ? ORDER BY cena DESC',(20000,))
drahsi_auta = c.fetchall()

print('Auta drahsie ako 20 000 €:')
for auto in drahsi_auta:
    print(auto)
conn.close()
