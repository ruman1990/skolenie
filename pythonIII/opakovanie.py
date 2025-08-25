
# Načítaj celý log súbor do zoznamu. (log.txt)

riadky = []

with open('log.txt','r',encoding='utf-8') as f:
    for line in f:
        riadky.append(line)

import re

vzor = r'^\[(.*)\] Vyskladnenie (.+)$'

vyskladnenia = {}

for x in riadky:
    if 'chyba:' not in x.lower():
        zhoda = re.match(vzor,x)
        if zhoda:
            datum = zhoda.group(1)
            produkt = zhoda.group(2)
            if produkt not in vyskladnenia:
                vyskladnenia[produkt] = []
            vyskladnenia[produkt].append(datum)

with open('vyskladnene_produkty.csv','w',encoding='utf-8') as f:
    f.write('produkt,pocet_vyskladneni,posledny_datum\n')
    for produkt in vyskladnenia:
        f.write(f'{produkt},{len(vyskladnenia[produkt])},{vyskladnenia[produkt][-1]}\n')

# Pre každý riadok zisti, či ide o vyskladnenie produktu.

# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas
