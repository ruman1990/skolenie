import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute("""
    create table if not exists produkty (
                id integer PRIMARY KEY,
            nazov TEXT not null,
            cena real not null,
            pocet integer not null
            )
""")

conn.commit()
conn.close()