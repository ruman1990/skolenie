import pandas as pd
import psycopg2

conn = psycopg2.connect(
    database = 'postgres',
    host = 'localhost',
    user = 'postgres',
    password = 'admin'
)

df = pd.read_csv('users3.csv')
df.loc[df["salary"] < 0,'salary'] = 0
print(df[df['salary'] < 0])
df.to_json('vystup3.json',orient="records",force_ascii=False,indent=4)