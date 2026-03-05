
# Načítaj celý log súbor do zoznamu. (log.txt)

log_riadky = []
with open("log.txt",'r',encoding='utf-8') as f:
    for x in f:
        log_riadky.append(x)



# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).
vyskladnenia = {}

for x in log_riadky:
    if '- Chyba:' not in x and 'Vyskladnenie' in x:
        y = x.split('] ')
        datum = y[0]
        event = y[1].replace("Vyskladnenie ","").strip()
        if event not in vyskladnenia:
            vyskladnenia[event] = []
        vyskladnenia[event].append(datum[1:])

print(vyskladnenia)





# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.
for x in vyskladnenia:
    print(f'Produkt {x} sa vyskladnil {len(vyskladnenia[x])} krat')

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas

with open("vyskladnene_produkty.csv","w",encoding='utf-8') as f:
    f.write("produkt; pocet_vyskladneni; posledny_datum_cas\n")
    for produkt in vyskladnenia:
        datumy = vyskladnenia[produkt]
        f.write(f'{produkt};{len(datumy)};{datumy[-1]}\n')

