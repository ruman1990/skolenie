import psycopg2

conn = psycopg2.connect(
    host="aws-0-eu-west-2.pooler.supabase.com",
    database="postgres",
    user="postgres.mianvtfnpgfqnzdaendq",
    password="SilneHeslo123"
)

cur = conn.cursor()


cur.execute("select * from vlado.objednavky where datum > '2024-03-01'")

data = cur.fetchall()
import datetime


print(data)

conn.commit()