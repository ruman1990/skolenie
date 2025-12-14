
# Načítaj celý log súbor do zoznamu. (log.txt)
log_riadky = []
with open('log.txt','r',encoding='utf-8') as f:
    for line in f:
        log_riadky.append(line.replace('\n',''))

#print(log_riadky)
#print(len(log_riadky))

import re

vzor = r'\[(.*)\] Vyskladnenie (.+)$'
for x in log_riadky:
    if 'Chyba' not in x:
        zhoda = re.match(vzor,x)
        if zhoda:
            print(zhoda.group(1),zhoda.group(2))

vyskladnenia = {}

for x in log_riadky:   
    if 'Vyskladnenie' in x and 'Chyba:' not in x:
        y = x.split('] ')
        datum = y[0][1:]
        produkt = y[1].replace('Vyskladnenie','').strip()
        print(datum,produkt)
        if produkt not in vyskladnenia:
            vyskladnenia[produkt] = []
        vyskladnenia[produkt].append(datum)
# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).
print(vyskladnenia)


# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas
with open('vyskladnene_produkty.log','w',encoding='utf-8') as f:
    f.write('produkt,pocet_vyskladneni,posledny_datum_cas\n')
    for x in vyskladnenia:
        f.write(f'{x},{len(vyskladnenia[x])},"{vyskladnenia[x][-1]}"\n')
