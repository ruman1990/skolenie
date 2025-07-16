def export_skladu(sklad):
    vystup = []
    for i in sklad.produkty:
        vystup.append(str(sklad.produkty[i]))
    retazec = ";".join(vystup)
    print(retazec)

def import_skladu(sklad):
    vstup = input("Zadaj data skladu: ")
    # voda,3,1;chlieb,4,3
    casti = vstup.split(';')
    for x in casti:
        item = x.split(',')
        sklad.produkty[item[0]] = item

#ww