
# Načítaj celý log súbor do zoznamu. (log.txt)
data = []
with(open("C:\\Users\\ruman\\skolenie\\pythonIII\\log.txt",'r',encoding='utf-8')) as f:
    for x in f:
        data.append(x)


#with(open("log.txt",'r',encoding='utf-8')) as f:
#    data = f.read()
#    x=data.split('\n')
#    print(x)

# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

vyskladnenie = {}
for x in data:
    if 'Vyskladnenie' in x and 'Chyba:' not in x:
        key = x.split('] Vyskladnenie ')[1].strip()
        datum = x.split('] Vyskladnenie ')[0]
        if key not in vyskladnenie:
            vyskladnenie[key] = []
        vyskladnenie[key].append(datum[1:])


print(vyskladnenie)
# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.

# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas
with open('vyskladnene_produkty.csv','w',encoding='utf-8') as f:
    f.write('produkt, pocet_vyskladneni, posledny_datum_cas\n')
    for x in vyskladnenie:
        f.write(f'{x},{len(vyskladnenie[x])},{vyskladnenie[x][-1]}\n')
