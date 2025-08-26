import psycopg2
import pandas as pd
conn = psycopg2.connect(
    host="localhost",
    dbname="sklad",
    user="postgres",
    password='admin')

cur = conn.cursor()

def fetch_data():
    df = pd.read_sql("SELECT * FROM objednavky_view", conn)
    print(df)
    df['datum'] = pd.to_datetime(df['datum'])
    df['mesiac'] = df['datum'].dt.to_period('M').dt.to_timestamp()
    df['hodnota'] = df['mnozstvo'] * df['cena']
    return df

import datetime
from decimal import Decimal

def report_mesacne_obraty(df):
    df = df.groupby(['mesiac','typ']).agg(
        pocet_objednavok = ('objednavka_id','nunique'),
        ks_spolu = ('mnozstvo','sum'),
        obrat = ('hodnota','sum')
    ).reset_index().sort_values(['mesiac','typ'])
    return df


data = fetch_data()
df = report_mesacne_obraty(data)
df['mesiac'] = df['mesiac'].dt.strftime('%Y-%m-%d')
df.to_excel("report_mesacne_obraty_pandas.xlsx", index=False)


import matplotlib.pyplot as plt

df.plot(x='mesiac', y='obrat', kind='bar')
plt.show()


