#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Analytika objednávok v pandas (ekvivalent SQL 1, 2, 3, 3a, 6).

Požiadavky:
    pip install pandas psycopg2-binary openpyxl

Výstup:
    report_pandas.xlsx   (viac listov)
"""

import pandas as pd
import psycopg2

# ---------------------------------------
# 1) Pripojenie k PostgreSQL (uprav)
# ---------------------------------------
DB_CFG = dict(
    host="localhost",
    port=5432,
    dbname="skolenie",
    user="admin",
    password="adminadmin",
)

SQL_OV = """
SELECT objednavka_id, datum, typ, nazov, mnozstvo, cena, kategoria
FROM objednavky_view;
"""

def load_data():
    conn = psycopg2.connect(**DB_CFG)
    try:
        df = pd.read_sql(SQL_OV, conn)
    finally:
        conn.close()
    # istota, že 'datum' je datetime
    df["datum"] = pd.to_datetime(df["datum"], utc=False)
    # prvý deň mesiaca (ekvivalent date_trunc('month'))
    df["mesiac"] = df["datum"].dt.to_period("M").dt.to_timestamp()
    # prepočítaná hodnota riadku
    df["hodnota"] = df["mnozstvo"] * df["cena"]
    return df

# ---------------------------------------
# 2) Reporty
# ---------------------------------------

def rpt_1_mesacne_pocty_a_obrat_podla_typu(df):
    """
    SQL 1:
      GROUP BY mesiac, typ
        COUNT(DISTINCT objednavka_id)
        SUM(mnozstvo)
        SUM(mnozstvo*cena)
    """
    out = (
        df.groupby(["mesiac", "typ"])
          .agg(
              pocet_objednavok=("objednavka_id", "nunique"),
              ks_spolu=("mnozstvo", "sum"),
              obrat=("hodnota", "sum"),
          )
          .reset_index()
          .sort_values(["mesiac", "typ"])
    )
    # voliteľné: zaokrúhlenie na 2 desatinné
    #out["obrat"] = out["obrat"].round(2)
    print(out)
    return out

def rpt_2_mesacne_saldo(df):
    """
    SQL 2:
      mesacne trzby (typ='odberatelska') a nakupy (typ='dodavatelska') + saldo
    """
    # agreguj obrat podľa mesiaca a typu do stĺpcov
    piv = (
        df.pivot_table(
            index="mesiac",
            columns="typ",
            values="hodnota",
            aggfunc="sum",
            fill_value=0.0,
        )
        .reset_index()
    )

    # očakávané stĺpce (ak neexistujú, doplň 0)
    #for col in ["odberatelska", "dodavatelska"]:
    #    if col not in piv.columns:
    #        piv[col] = 0.0
    piv.rename(columns={'mesiac': 'mesiac', 'odberatelska': 'trzby', 'dodavatelska': 'nakupy'}, inplace=True)
    #out= pd.DataFrame({
    #    "mesiac": piv["mesiac"],
    #    "trzby": piv["odberatelska"],
    #    "nakupy": piv["dodavatelska"],
    #})
    piv["saldo"] = (piv["trzby"] - piv["nakupy"]).round(2)
    piv = piv.sort_values("mesiac")
    #print(piv)
    return piv

def rpt_3_top_produkt_podla_mnozstva(df):
    """
    SQL 3: Najobjednávanejší produkt po mesiacoch (podľa množstva).
    - najprv suma po (mesiac, nazov)
    - potom pre každý mesiac vyber riadky s max ks (zvládne remízu)
    """
    sums = (
        df.groupby(["mesiac", "nazov"], as_index=False)["mnozstvo"]
          .sum()
          .rename(columns={"nazov": "produkt", "mnozstvo": "ks"})
    )
    # maximum v rámci mesiaca
    max_ks = sums.groupby("mesiac")["ks"].transform("max")
    out = sums[sums["ks"] == max_ks].copy()
    out = out.sort_values(["mesiac", "produkt"])
    return out

# jednoduchsie
#def rpt_3_top_produkt_podla_mnozstva(df):
#    sums = (
#        df.groupby(["mesiac", "nazov"], as_index=False)["mnozstvo"]
#          .sum()
#          .rename(columns={"nazov": "produkt", "mnozstvo": "ks"})
#    )
#    out = (
#        sums.sort_values(["mesiac", "ks"], ascending=[True, False])
#            .groupby("mesiac", as_index=False)
#            .first()
#    )
#    return out.sort_values(["mesiac", "produkt"])


def rpt_3a_top_produkt_podla_obratu(df):
    """
    Alternatíva 3a: Najvýnosnejší produkt po mesiacoch (podľa obratu).
    """
    sums = (
        df.groupby(["mesiac", "nazov"], as_index=False)["hodnota"]
          .sum()
          .rename(columns={"nazov": "produkt", "hodnota": "obrat"})
    )
    max_obrat = sums.groupby("mesiac")["obrat"].transform("max")
    out = sums[sums["obrat"] == max_obrat].copy()
    out["obrat"] = out["obrat"].round(2)
    out = out.sort_values(["mesiac", "produkt"])
    return out

def rpt_6_priemerna_jednotkova_cena(df):
    """
    SQL 6: Vážená priemerná cena produktu pre typ='odberatelska'.
      avg_price = SUM(mnozstvo*cena) / SUM(mnozstvo) per produkt
    """
    dfo = df[df["typ"] == "odberatelska"].copy()
    sums = dfo.groupby("nazov").agg(
        sum_hodnota=("hodnota", "sum"),
        sum_ks=("mnozstvo", "sum"),
    )
    # vyhnúť sa delením nulou
    sums = sums[sums["sum_ks"] != 0]
    out = (sums["sum_hodnota"] / sums["sum_ks"]).reset_index()
    out.columns = ["produkt", "priemerna_cena"]
    out["priemerna_cena"] = out["priemerna_cena"].round(2)
    out = out.sort_values("produkt")
    return out

# ---------------------------------------
# 3) Export do Excelu
# ---------------------------------------

def export_to_excel(dfs, path="report_pandas.xlsx"):
    """
    dfs = dict(nazov_listu -> DataFrame)
    """
    with pd.ExcelWriter(path, engine="openpyxl", datetime_format="yyyy-mm-dd") as xw:
        for sheet, frame in dfs.items():
            frame.to_excel(xw, index=False, sheet_name=sheet)

def main():
    df = load_data()

    r1  = rpt_1_mesacne_pocty_a_obrat_podla_typu(df)
    r2  = rpt_2_mesacne_saldo(df)
    r3  = rpt_3_top_produkt_podla_mnozstva(df)
    r3a = rpt_3a_top_produkt_podla_obratu(df)
    r6  = rpt_6_priemerna_jednotkova_cena(df)

    export_to_excel({
        "1_mesacne_typ": r1,
        "2_mesacne_saldo": r2,
        "3_top_ks": r3,
        "3a_top_obrat": r3a,
        "6_avg_cena": r6,
    })

    print("Hotovo -> report_pandas.xlsx")

if __name__ == "__main__":
    main()