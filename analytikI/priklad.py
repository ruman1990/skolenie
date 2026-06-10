import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="admin",
    port=5432
)

cur = conn.cursor()


cur.execute("select * from objednavky_view")

for x in cur.fetchall():
    print(x)
