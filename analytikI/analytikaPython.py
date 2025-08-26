import psycopg2
import tablib
conn = psycopg2.connect(
    host="localhost",
    dbname="sklad",
    user="postgres",
    password='admin')

cur = conn.cursor()


def fetch_data():
    cur.execute("SELECT * FROM objednavky_view")
    rows = cur.fetchall()
    return rows

import datetime
from decimal import Decimal

agg = {}
uniq = {}

def report_mesacne_obraty(rows):
    for x in rows:
        mesiac = datetime.datetime(x[1].year, x[1].month, 1)
        typ = x[2]

        key = (mesiac, typ)
        if key not in agg:
            agg[key] = {
                #"pocet_objednavok": x[4],
                "ks_spolu": Decimal('0'),
                "obrat": Decimal('0.0')
            }
        if key not in uniq:
            uniq[key] = set()

        uniq[key].add(x[0])
        agg[key]["ks_spolu"] += x[4]
        agg[key]["obrat"] += x[4]*x[5]
        
    ds = tablib.Dataset(headers = ["mesiac","typ","pocet_objednavok","ks_spolu","obrat"])
    for (mesiac,typ),vals in sorted(agg.items()):
        ds.append([str(mesiac), typ, len(uniq[(mesiac,typ)]),vals["ks_spolu"], vals["obrat"]])
    return ds

data = fetch_data()
dataset = report_mesacne_obraty(data)

print(dataset.sort('mesiac'))

with open("report_mesacne_obraty.xlsx", "wb") as f:
    f.write(dataset.export('xlsx'))