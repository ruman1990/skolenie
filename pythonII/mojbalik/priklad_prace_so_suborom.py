__all__ = ["Person","zoznam"]

class Person:
   def __init__(self,name,age):
      self.name = name.strip()
      self.age = str(age).strip()

   def __str__(self):
      return f"{self.name},{self.age}"

   def to_file(self,last=False):
      if last:
         return f"{self.name},{self.age}"
      else:
         return f"{self.name},{self.age}\n"

zoznam = []

# with open("vysledok.csv","r",encoding="utf-8") as f:
#    for x in f:
#       z = x.split(";")
#       if z[0] != 'Vlado':
#          zoznam.append([z[0].strip(),z[1].strip()])

# print(zoznam)

# with open("vysledok2.csv","w",encoding="utf-8") as f:
#    for x in zoznam[:-1]:
#       f.write(",".join(x)+"\n")
#    f.write(",".join(zoznam[-1]))
#       #f.write(f"{",".join(x)}\n")

def main():
    with open("vysledok.csv","r",encoding="utf-8") as f:
        for x in f:
            z = x.split(";")
            if z[0] != 'Vlado':
                zoznam.append(Person(*z))
    
    for x in zoznam:
        print(x)

    with open("vysledok2.csv","a",encoding="utf-8") as f:
        for x in zoznam[:-1]:
            f.write(x.to_file())
        f.write(zoznam[-1].to_file(True))
    
    # riesenie cez CSV modul
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


if __name__ == "__main__":
    main()
    