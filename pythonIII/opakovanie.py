# Načítaj celý log súbor do zoznamu. (log.txt)
import datetime

vyskladnenia = {}

with open("log.txt","r",encoding="utf-8") as f:
    for x in f:
        if "Vyskladnenie" in x and "Chyba" not in x:
            s = x.split("] Vyskladnenie")
            key = s[1].strip()
            datum = s[0][1:].strip()
            if key not in vyskladnenia:
                vyskladnenia[key] = [datum]
            else:
                vyskladnenia[key].append(datum)


print(vyskladnenia)

with open("vyskladnenia.csv","w",encoding="utf-8") as f:
    for x in vyskladnenia:
        last_date = datetime.datetime.strptime(vyskladnenia[x][-1],"%Y-%m-%d %H:%M:%S")
        f.write(f"{x},{len(vyskladnenia[x])},{last_date.strftime("%d.%m.%Y %H:%M:%S")}\n")

# { "muka" : ["2025-07-21 08:18:55","2025-07-21 09:18:55"],
#   "cukor" : [2025-07-21 08:07:56]}

# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.


# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas
