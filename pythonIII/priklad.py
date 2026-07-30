# Načítaj údaje zo súboru auta.csv.
 
# Vlož všetky údaje z CSV do databázy.
 
#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
 
 
 
#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
 
import csv
import sqlite3
from datetime import datetime
 
conn = sqlite3.connect('auta.db')
cur = conn.cursor()
 
cur.execute('''
CREATE TABLE IF NOT EXISTS auta (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    znacka TEXT,
    model TEXT,
    rok_vyroby INTEGER,
    cena REAL
)''')
 
with open('auta.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute('''
        INSERT INTO auta (znacka, model, rok_vyroby, cena)
        VALUES (?, ?, ?, ?)
        ''', (row['znacka'], row['model'], int(row['rok_vyroby']), float(row['cena'])))
 
conn.commit()
 
# Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
current_year = datetime.now().year
cur.execute('SELECT COUNT(*) FROM auta WHERE ? - rok_vyroby > 5', (current_year,))
count_old_cars = cur.fetchone()[0]
print(f'Počet áut starších ako 5 rokov: {count_old_cars}')
 
# Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
cur.execute('SELECT * FROM auta WHERE cena > 20000 ORDER BY cena DESC')
expensive_cars = cur.fetchall()
print('Zoznam áut drahších ako 20 000 €:')
for car in expensive_cars:
    print(f'ID: {car[0]}, Značka: {car[1]}, Model: {car[2]}, Rok výroby: {car[3]}, Cena: {car[4]} €')
 
conn.close()