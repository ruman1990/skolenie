import psycopg2
#conn = psycopg.connect("host=localhost dbname=mojadb user=moje_meno password=moje_heslo")
conn = psycopg2.connect(
    host="localhost",
    database="sklad",
    user="postgres",
    password="admin"
)

cur = conn.cursor()