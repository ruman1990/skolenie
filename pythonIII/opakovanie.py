# Načítaj celý log súbor do zoznamu. (log.txt)
import os
zoznam = []

os.chdir("pythonIII")

with open("log.txt","r",encoding="utf-8") as f:
    for x in f:
        zoznam.append(x)

#print(zoznam)

vyfiltrovany_zoznam = []

for x in zoznam:
    if "Vyskladnenie" in x and "Chyba" not in x:
        vyfiltrovany_zoznam.append(x)
        print(x,end='')


# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

vyskladnenia = {}

for x in vyfiltrovany_zoznam:
    result = x.split("] ")
    date = result[0][1:]
    key = result[1].replace("Vyskladnenie ","").strip()
    if key in vyskladnenia:
        vyskladnenia[key].append(date)
    else:
        vyskladnenia[key] = [date]
# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.
print(vyskladnenia)
# Spočítaj, koľkokrát sa každý produkt vyskladňoval.


# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas
with open("vysledok.txt","w",encoding='utf-8') as f:
    for x in vyskladnenia:
        f.write(f"{x},{len(vyskladnenia[x])},{vyskladnenia[x][-1]}\n")



