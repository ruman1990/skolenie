# Načítaj údaje zo súboru auta.csv.
import csv
import sqlite3
import datetime

with open("auta.csv",'r',encoding='utf-8') as f:
    reader = csv.reader(f)
    auta = list(reader)

print(auta[1:])

# Vytvor databázu auta.db a v nej tabuľku auta so zodpovedajúcimi stĺpcami.
conn = sqlite3.connect('auta.db')
cur = conn.cursor()
#znacka,model,rok_vyroby,cena
cur.execute("""
    create table if not exists auta (
                id INTEGER PRIMARY KEY,
                znacka TEXT NOT NULL,
                model TEXT NOT NULL,
                rok_vyroby INTEGER NOT NULL,
                cena REAL NOT NULL,
                popis_auta TEXT
            )
""")

cur.execute("DELETE from auta")
cur.executemany("INSERT INTO auta (znacka,model,rok_vyroby,cena) values (?,?,?,?) ",auta[1:])

cur.execute("update auta set popis_auta='Poskriabany pravy blatnik' where id=3")

conn.commit()

# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).

rok = datetime.datetime.now().year

cur.execute("select count(*) from auta where ? - rok_vyroby > 5",(rok,))

print(f'Pocet aut starsich 5 rokov je: {cur.fetchone()[0]}')

cur.execute("select * from auta")
result = cur.fetchall()
vysledok = []
for x in result:
    if rok - x[3] > 5:
        vysledok.append(x)
print(len(vysledok))

#     Zobraz priemernú cenu všetkých áut (s presnosťou na dve desatinné miesta).
cur.execute("select avg(cena) from auta")
print(f'Priemerna cena aut je: {cur.fetchone()[0]:.2f}€')

cur.execute("select cena from auta")
result = list(cur.fetchall())
suma = 0
for x in result:
    suma += x[0]
print(f'Priemerna cena aut je: {suma/len(result):.2f}€')

#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc

cur.execute('select * from auta where cena>20000 order by cena desc')
print(cur.fetchall())

cur.execute("select * from auta")
result = list(cur.fetchall())
result = [x for x in result if x[4]>20000]
print(sorted(result,key=lambda x : x[4],reverse=True))

conn.close()