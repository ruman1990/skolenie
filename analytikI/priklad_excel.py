from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
import csv

with open("data.csv","r",encoding="utf-8") as f:
    data = csv.reader(f)

    wb = Workbook()
    ws = wb.active
    ws.title = "Zamestnanci"

    y = []
    for x in data:
        y.append(x)

    z = [[int(x[0]),x[1],x[2],int(float(x[3]))] for x in y[1:]]

    print(z)

    ws.append(y[0])
    for x in z:
        ws.append(x)

    ws.append(["priemer","=AVERAGE(D2:D6)"])

    graf = BarChart()
    graf.title = "Plat zamestnancov"

    graf.y_axis.title = "Plat"
    graf.x_axis.title = "Zamestnanec"

    data = Reference(ws,min_col=4,min_row=2, max_row=6)
    cat = Reference(ws,min_col=3,min_row=2,max_row=6)

    graf.add_data(data)
    graf.set_categories(cat)

    ws.add_chart(graf,"F2")
    wb.save("platy.xlsx")
