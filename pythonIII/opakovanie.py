# Načítaj celý log súbor do zoznamu. (log.txt)


zaznamy = []

with open("log.txt","r",encoding="utf-8") as f:
    for x in f:
        if "Vyskladnenie" in x and "Chyba" not in x:
            zaznamy.append(x)

# { "kava" : ["2025-07-21 08:14:40"], "muka" : ["2025-07-21 08:18:55","2025-07-21 09:18:55"]}

data = {}
for x in zaznamy:
    datum,nazov = x.split("] ")
    datum = datum[1:].strip()
    nazov = nazov.replace("Vyskladnenie ","").strip()

    #print(datum[1:].strip(), nazov.replace("Vyskladnenie ",""))

    if nazov in data:
        data[nazov].append(datum)
    else:
        data[nazov] = [datum]

print(data)

for x in data:
    print(x,len(data[x]))

with open("vysledok.txt","w",encoding="utf-8") as f:
    f.write("produkt,pocet_vyskladneni,posledny_datum\n")
    for x in data:
        f.write(f"{x},{len(data[x])},{data[x][-1]}\n")

# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.


# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas


