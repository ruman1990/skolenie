import sqlite3

conn = sqlite3.connect('firma.db')
c = conn.cursor()

#c.execute("insert into zamestnanec (meno,plat,oddelenie_id) values" \
#"('Vlado',2000,8)")

c.execute("insert into oddelenie (nazov) values ('Accounting')")

conn.commit()
conn.close()