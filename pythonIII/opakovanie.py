import re
# Načítaj celý log súbor do zoznamu. (log.txt)

rows = []
with open('log.txt', 'r', encoding='utf-8') as file:
    for x in file:
        rows.append(x.strip())

#print(rows)


# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

vyskladnenia = {}



pattern = r'\[(.*?)\] Vyskladnenie (.+)$'

for x in rows:
    zhoda = re.match(pattern,x)
    #y = x.split('] ')
    #datum = y[0][1:]
    #produkt = y[1]
    #print(datum,produkt)
    if zhoda:
        datum = zhoda.group(1)
        produkt = zhoda.group(2).strip()
        if 'Chyba' not in produkt:
            if produkt in vyskladnenia:
                vyskladnenia[produkt]['datum'] = datum
                vyskladnenia[produkt]['pocet'] += 1
            else:
                vyskladnenia[produkt] = {'datum' : datum, 'pocet' : 1}

#    if 'Vyskladnenie' in x and 'Chyba' not in x:
#        vyskladnenia.append(x)

print(vyskladnenia)

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas

with open('vyskladnenie.log','w',encoding='utf-8') as f:
    f.write(f'produkt,pocet,datum\n')
    for x in vyskladnenia:
        f.write(f'{x},{vyskladnenia[x]['pocet']},"{vyskladnenia[x]['datum']}"\n')
