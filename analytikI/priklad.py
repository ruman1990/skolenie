import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="test",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("select * from objednavky where typ='odberatelska' and datum <= '2024-03-31' and datum >= '2024-03-01'")



res = cur.fetchall()

v = [x for x in res if x[4]==23]

for x in v:
    print(v)
