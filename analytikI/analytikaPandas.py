import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname='skolenie',
    user='postgres',
    password='postgres',
    host='localhost',
    port=5432
)

data = pd.read_sql('select * from objednavka_view',conn)

#print(data)

najdrahsi = data.loc[data['cena'].idxmax()]

najlacnejsi = data.loc[data['cena'].idxmin()]

#print(najdrahsi)

#print(najlacnejsi)

#print(data['cena'],data['mnozstvo'])

data['trzba'] = data['cena'] * data['mnozstvo']

print(data['trzba'])

obrat_podla_produktov = data.groupby('nazov')['trzba'].sum().reset_index()

print(obrat_podla_produktov.head(20))

import matplotlib.pyplot as plt


plt.pie(obrat_podla_produktov['trzba'].head(10),labels=obrat_podla_produktov['nazov'].head(10),autopct='%1.1f%%')
plt.show()



#najdrahsi_obrat = obrat_podla_produktov.loc[obrat_podla_produktov['trzba'].idxmax()]
#print(najdrahsi_obrat)
