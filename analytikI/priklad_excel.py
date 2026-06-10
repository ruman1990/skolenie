from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Zamestnanci"

import csv
with open("data.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    ws.append(["Priezvisko","Plat"])
    for x in list(reader)[1:]:
        ws.append([x[2],int(float(x[3]))])

graf = BarChart()

graf.title = "Platy zamestnancov v roku 2026"

graf.y_axis.title = "Plat"
graf.x_axis.title = "Zamestnanec"

data = Reference(ws,min_col=2,min_row=2,max_row=6)
kategories = Reference(ws,min_col=1,min_row=2,max_row=6)

graf.add_data(data)
graf.set_categories(kategories)
ws.add_chart(graf)
wb.save("platy.xlsx")



# # 1. Dáta
# ws.append(["Produkt", "Cena", "Kusov", "Spolu (€)"])
# produkty = [
#     ["Chleba", 1.5, 10],
#     ["Mlieko", 0.9, 20],
#     ["Maslo", 2.3, 5],
# ]

# # 2. Zápis dát a výpočet spolu
# for produkt in produkty:
#     cena, kusy = produkt[1], produkt[2]
#     produkt.append(cena * kusy)
#     ws.append(produkt)


# graf = BarChart()
# graf.title = "Tržby podľa produktu"
# graf.y_axis.title = "€"
# graf.x_axis.title = "Produkt"

# data = Reference(ws, min_col=4, min_row=1, max_row=4)
# kategorie = Reference(ws, min_col=1, min_row=2, max_row=4)

# graf.add_data(data, titles_from_data=True)
# graf.set_categories(kategorie)

# ws.add_chart(graf, "O2")

# wb.save("priklad.xlsx")