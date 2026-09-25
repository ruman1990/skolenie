import csv

zoznam = []

with open("vysledok.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f,delimiter=";")
    for x in reader:
        print(x)
        if x[0] != "Vlado":
         zoznam.append(x)


with open("vysledok2.csv","w",encoding="utf-8",newline="") as f:
   writer = csv.writer(f,delimiter=",")
   writer.writerows(zoznam)