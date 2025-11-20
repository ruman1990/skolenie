import random
import pandas as pd
import psycopg2
from datetime import datetime, timedelta

# Pripojenie do DB (uprav podľa svojej konfigurácie)
conn = psycopg2.connect(
    dbname="skolenie",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)

# Načítaj produkty do DataFrame
produkty = pd.read_sql("SELECT id, nazov, cena FROM produkty", conn)

# Generuj 30 dodávateľov a 30 odberateľov
dod_ids = list(range(1, 31))
odb_ids = list(range(1, 31))
prod_ids = produkty['id'].tolist()

# Pre každého dodávateľa si môžeš uložiť vlastný diskont
diskont_dod = {dod: random.uniform(0.3, 0.6) for dod in dod_ids}  # Zľava = 40–70% (zostane 30–60%)

insert_objednavky = []
insert_objednavky_produkty = []
id_obj = 1

for _ in range(200):
    typ = random.choice(['dodavatelska', 'odberatelska'])
    datum = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 200))
    if typ == 'dodavatelska':
        dodavatel_id = random.choice(dod_ids)
        odberatel_id = None
    else:
        dodavatel_id = None
        odberatel_id = random.choice(odb_ids)
    # Priprav objednávku
    insert_objednavky.append(
        (id_obj, typ, datum, dodavatel_id, odberatel_id)
    )
    # Vyber 1–10 produktov
    produkty_v_obj = random.sample(prod_ids, random.randint(1, 10))
    for pid in produkty_v_obj:
        mnozstvo = random.randint(10, 100)
        # Cena podľa typu objednávky:
        zakladna_cena = produkty.loc[produkty['id'] == pid, 'cena'].iloc[0]
        if typ == 'dodavatelska':
            # Nakupná cena znížená o 40–70% (podľa diskontu dodávateľa)
            diskont = diskont_dod[dodavatel_id]
            cena = round(zakladna_cena * diskont, 2)
        else:
            # Odberateľská cena = cena z tab. produkty
            cena = round(zakladna_cena, 2)
        insert_objednavky_produkty.append(
            (id_obj, pid, mnozstvo, cena)
        )
    id_obj += 1

#conn.autocommit = True
cur = conn.cursor()

# INSERT objednávok
for row in insert_objednavky:
    id_obj, typ, datum, dod, odb = row
    cur.execute(
        "INSERT INTO objednavky (id, typ, datum, dodavatel_id, odberatel_id) VALUES (%s, %s, %s, %s, %s);",
        (id_obj, typ, datum, dod, odb)
    )

# INSERT produkty v objednávkach
for row in insert_objednavky_produkty:
    obj_id, prod_id, mnozstvo, cena = row
    cur.execute(
        "INSERT INTO objednavky_produkty (objednavka_id, produkt_id, mnozstvo, cena) VALUES (%s, %s, %s, %s);",
        (int(obj_id), int(prod_id), int(mnozstvo), float(cena))
    )

conn.commit()
cur.close()
conn.close()
print("Hotovo, všetky objednávky sú uložené v databáze!")
