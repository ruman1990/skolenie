import psycopg2
import pandas as pd


conn = psycopg2.connect(
    dbname='sklad',
    user='postgres',
    password='admin',
    host='localhost',
)

df = pd.read_sql("SELECT * FROM objednavka_view", conn)
print(df.info())

df['mesiac'] = df['datum'].dt.to_period('M').dt.to_timestamp()
df['hodnota'] = df['mnozstvo'] * df['cena']

df = df.groupby(['mesiac','nazov'])['hodnota'].sum().reset_index()

max_obrat = df.groupby('mesiac')['hodnota'].transform('max')
df = df[df['hodnota'] == max_obrat]

# df = df.groupby(['mesiac','typ']).agg(
#     pocet_objednavok=('objednavka_id','nunique'),
#     ks_spolu = ('mnozstvo','sum'),
#     obrat = ('hodnota','sum')
# ).reset_index().sort_values(['mesiac','typ'])

print(df)
