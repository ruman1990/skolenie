import psycopg2
from openpyxl import Workbook

conn = psycopg2.connect(host="localhost",database="analytik",user="postgres",password="admin")
cur = conn.cursor()

cur.execute("""select * from objednavka_view""")


data = cur.fetchall()


#print(data)


wb = Workbook()

ws = wb.active
ws.title = "Objednavky"
ws.append(["ID objednavky","mnozstvo","cena","typ","datum","nazov","dodavatel","odberatel"])

for x in data:
    ws.append(x)

wb.save("objednavky.xlsx")