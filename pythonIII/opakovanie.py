# variant 1

# Načítaj celý log súbor do zoznamu. (log.txt)
with open("pythonIII/log.txt", "r", encoding="utf-8") as f:
    riadky = f.readlines()
 
produkty = {}
 
for riadok in riadky:
    if "Vyskladnenie" in riadok and "Chyba" not in riadok:
 
        datum_cas = riadok[1:20]
        produkt = riadok.split("Vyskladnenie ")[1].strip()
 
        if produkt not in produkty:
            produkty[produkt] = []
 
        produkty[produkt].append(datum_cas)

with open("pythonIII/vysledky2.csv", "w", encoding="utf-8") as f:
    for produkt, udaje in produkty.items():
        f.write(f"{produkt}; {len(udaje)}; {udaje[-1]}\n")

# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.


# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas



#variant 2

# nacitanie logu
with open("pythonIII/log.txt", "r", encoding="utf-8") as subor:
    riadky = subor.readlines()
 
produkty = {}
 
# prejdem vsetky riadky a hladam vyskladnenie
for riadok in riadky:
    if "Vyskladnenie " in riadok and "Chyba" not in riadok:
        datum_cas = riadok[1:20]
        produkt = riadok.split("Vyskladnenie ")[1].strip()
 
        # ak tam produkt este neni, pridam ho
        if produkt not in produkty:
            produkty[produkt] = [0, datum_cas]
 
        # pripocitam jedno vyskladnenie
        produkty[produkt][0] += 1
 
        # ulozim posledny datum
        if datum_cas > produkty[produkt][1]:
            produkty[produkt][1] = datum_cas
 
# zapis vysledku do suboru
with open("vysledok.txt", "w", encoding="utf-8") as subor:
    subor.write("produkt,pocet_vyskladneni,posledny_datum_cas\\n")
 
    for produkt, udaje in produkty.items():
        subor.write(f"{produkt},{udaje[0]},{udaje[1]}\\n")
 
print("Hotovo, vysledok je v subore vysledok.txt")


# variant 3

import re
 
with open("pythonIII/log.txt", "r", encoding="utf-8") as f:
    riadky = f.readlines()
 
produkty = {}

for riadok in riadky:
    zhoda = re.match(r"\[(.*?)\] Vyskladnenie (.*)", riadok)
 
    if zhoda and "Chyba" not in riadok:
 
        datum_cas = zhoda.group(1)
        produkt = zhoda.group(2)
 
        if produkt not in produkty:
            produkty[produkt] = [0, datum_cas]
 
        produkty[produkt][0] += 1
        produkty[produkt][1] = datum_cas
 
 
with open("pythonIII/vysledky3.txt", "w", encoding="utf-8") as f:
    f.write("produkt, pocet_vyskladneni, posledny_datum_cas\n")
    for produkt, udaje in produkty.items():
        f.write(f"{produkt}, {udaje[0]}, {udaje[1]}\n")