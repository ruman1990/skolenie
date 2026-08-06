import pandas as pd
import psycopg2
import matplotlib.pyplot as plt


conn = psycopg2.connect(host="localhost",database="analytik",user="postgres",password="admin")
df = pd.read_sql("select * from objednavka_view",conn)

df["datum"] = pd.to_datetime(df["datum"])

df["mesiac"] = df["datum"].dt.to_period("M").dt.to_timestamp()

df["hodnota"] = df["mnozstvo"] * df["cena"]

df = df.groupby(["mesiac","typ"]).agg(
    pocet_objednavok = ("objednavka_id","nunique"),
    ks_spolu = ("mnozstvo","sum"),
    obrat= ("hodnota","sum")
).reset_index()


# for typ, typy in df.groupby("typ"):
#     plt.barh(
#         typy["mesiac"],
#         typy["obrat"]
#     )
# plt.title("Obrat po mesiacoch")
# plt.xlabel("mesiace")
# plt.ylabel("obrat v €")
# plt.show()

df.to_excel("priklad.xlsx",index=False)

