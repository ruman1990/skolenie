# Načítaj údaje zo súboru auta.csv.
import os
import csv
import sqlite3
import datetime
from decimal import Decimal

os.chdir("pythonIII")

def make_connection():
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
    # len pre testovacie ucely
    cur.execute("delete from auta")
    return cur,conn

with open("auta.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    reader.__next__()
    cur,conn = make_connection()

    data = []
    for x in reader:
        data.append(x)
        
    cur.executemany("insert into auta (znacka,model,rok_vyroby,cena) values (?,?,?,?)",data)

    conn.commit()
# Vlož všetky údaje z CSV do databázy.

#     Zisti, koľko áut je starších ako 5 rokov (použi aktuálny rok).
    current_year = datetime.date.today().year
    cur.execute("select count(*) from auta where rok_vyroby<?",(current_year-5,))
    print(f"Pocet aut starsich ako 5 rokov je {cur.fetchone()[0]}")

    vysledok = []
    for x in data:
        if int(x[2]) < current_year-5:
            vysledok.append(x)

    print(f"Pocet aut starsich ako 5 rokov je {len(vysledok)}")



#     Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
# select * from auta where cena>20000 order by cena desc
    cur.execute("select * from auta where cena>20000 order by cena desc")
    res = cur.fetchall()
    for x in res:
        print(f"{x[1]}, {x[2]}, {x[4]}")

    print()

    vysledok = []
    for x in data:
        if Decimal(x[3]) > 20000:
            vysledok.append(x)

    vysledok.sort(reverse=True)
    for x in vysledok:
            print(f"{x[0]}, {x[1]}, {x[3]}")
#znacka,model,rok_vyroby,cena
 



 
# Zobraz zoznam všetkých áut drahších ako 20 000 €, zoradený zostupne podľa ceny.
