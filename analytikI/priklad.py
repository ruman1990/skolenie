import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="moja_databaza",
    user="postgres",
    password="tajneheslo"
)

cur = conn.cursor()
