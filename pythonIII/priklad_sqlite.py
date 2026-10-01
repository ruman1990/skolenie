import sqlite3
import csv

conn = sqlite3.connect("mojadb.db")

cur = conn.cursor()

cur.execute("""create table if not exists users (

    id INTEGER PRIMARY KEY,
    meno TEXT,
    vek INTEGER

) """)

cur.execute("alter table users add column email TEXT")

with open("users.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    reader.__next__()
    zoznam = []
    for x in reader:
        zoznam.append([int(x[0]),x[1]+x[2],x[3]])
    cur.executemany("insert into users (id,meno,email) values (?,?,?)",zoznam)
    #for x in reader:
    #    cur.execute("insert into users (id,meno,email) values (?,?,?)",(int(x[0]),x[1]+x[2],x[3]))

#cur.execute("drop table users")

conn.commit()
cur.close()
conn.close()

