
# Načítaj celý log súbor do zoznamu.

# Pre každý riadok zisti, či ide o vyskladnenie produktu (úspešné aj neúspešné pokusy).

# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval (úspešne alebo aj s chybou podľa zadania).

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas

import re

log_riadky = []
with open("sklad/audit.log", encoding="utf-8") as f:
    for line in f:
        riadok = line.strip()
        if riadok:
            log_riadky.append(riadok)

# Tento regex len vezme to, čo je v zátvorkách na začiatku a potom slovo za "Vyskladnenie "
vzor = r"\[(.*?)\] - Vyskladnenie (.+)$"

vyskladnenia = {}

for riadok in log_riadky:
    if "- Chyba:" not in riadok:
        zhoda = re.match(vzor, riadok)
        if zhoda:
            datum = zhoda.group(1)
            produkt = zhoda.group(2).strip()
            if produkt not in vyskladnenia:
                vyskladnenia[produkt] = []
            vyskladnenia[produkt].append(datum)

with open("vyskladnene_produkty.log", "w", encoding="utf-8") as fout:
    fout.write("produkt,pocet_vyskladneni,posledny_datum_cas\n")
    for produkt in vyskladnenia:
        datumy = vyskladnenia[produkt]
        fout.write(f"{produkt},{len(datumy)},{datumy[-1]}\n")

