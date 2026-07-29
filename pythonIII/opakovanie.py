# Načítaj celý log súbor do zoznamu. (log.txt)


# Pre každý riadok zisti, či ide o vyskladnenie produktu.
# Vyfiltruj len tie riadky, kde bolo vyskladnenie úspešné (neobsahuje „Chyba“).

# Pre každý produkt zisti, kedy (dátum a čas) bol úspešne vyskladnený.

# Spočítaj, koľkokrát sa každý produkt vyskladňoval.


# Výsledok zapíš do nového súboru vo formáte:
# produkt, pocet_vyskladneni, posledny_datum_cas

with open('log.txt', 'r', encoding='utf-8') as log_file:
    log_lines = log_file.readlines()
    #log_lines = log_lines[::-1]
    produkty = {}
 
    for line in log_lines:
        if 'Vyskladnenie' in line and 'Chyba' not in line:
            parts = line.split("] ")
            datum_cas = parts[0]
            datum_cas = datum_cas[1:]
            produkt = parts[1].strip().replace("Vyskladnenie ","")
            if produkt not in produkty:
                produkty[produkt] = {'pocet': 0, 'posledny_datum_cas': datum_cas}
            
            produkty[produkt]['pocet'] += 1
            produkty[produkt]['posledny_datum_cas'] = datum_cas
 
with open('vysledky.txt', 'w', encoding="utf-8") as vysledky_file:
    for produkt, info in produkty.items():
        vysledky_file.write(f"{produkt}, {info['pocet']}, {info['posledny_datum_cas']}\n")