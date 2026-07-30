# Načítaj údaje zo súboru auta.csv.

# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).



#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
import csv
import sqlite3

data = []
with open('auta.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    #reader.__next__()
    first_time = True
    for row in reader:
        if first_time:
            first_time = False
            continue
        data.append(row)
        print(row)
 
 
conn = sqlite3.connect('new_db.db')
c = conn.cursor()
 
#znacka,model,rok_vyroby,cena
 
c.execute('''
CREATE TABLE IF NOT EXISTS auta (
    id INTEGER PRIMARY KEY,
    znacka TEXT,
    model INTEGER,
    rok_vyroby INTEGER,
    cena REAL
)
''')

c.execute("DELETE FROM auta")

c.executemany("INSERT INTO auta (znacka,model,rok_vyroby,cena) VALUES (?,?,?,?)",data)

from datetime import datetime
current_year = datetime.now().year
c.execute('SELECT COUNT(*) FROM auta WHERE ? - rok_vyroby > 5', (current_year,))
data = c.fetchone()
print(data)
count_old_cars = data[0]
print(f'Počet áut starších ako 5 rokov: {count_old_cars}')
 
# Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
c.execute('SELECT * FROM auta WHERE cena > 20000 ORDER BY cena DESC')
expensive_cars = c.fetchall()
print('Zoznam áut drahších ako 20 000 €:')
for car in expensive_cars:
    print(f'ID: {car[0]}, Značka: {car[1]}, Model: {car[2]}, Rok výroby: {car[3]}, Cena: {car[4]} €')

 
conn.commit()  
conn.close()