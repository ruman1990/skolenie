from produkt import Produkt

class Sklad:
    def __init__(self):
        self.produkty = {}
        with open("data.txt","r",encoding="utf-8") as f:
            for x in f:
                z = x.split(",")
                self.produkty[z[0]] = Produkt(z[0],float(z[1]),int(z[2]))

    def vypis_produktov(self):
        for x in self.produkty.values():
            print(f"{x.nazov:20} cena je {x.cena:6.2f}€, pocet kusov {x.pocet_kusov:6}, celkova cena {x.celkova_cena():6.2f}€")

    def pridanie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
                print("Zadany produkt uz existuje")
                return
        cena = float(input("zadaj cenu: "))
        pocet = int(input("pocet kusov: "))
        self.produkty[nazov] = Produkt(nazov,cena,pocet)
        self.ulozit_data()
        print("Pridanie produktu bolo uspesne")

    def odobranie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
                del self.produkty[nazov]
                self.ulozit_data()
                print("Odobranie produktu bolo uspesne")
                return
        print("Produkt sa nenasiel!")

    def celkova_cena(self):
        spolu = 0
        for x in self.produkty.values():
            spolu += x.celkova_cena()
        print(f"Celkova cena je {spolu}€")

    def naskladnenie(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Kolko kusov naskladnit: "))
            self.produkty[nazov].pocet_kusov += kusy
            self.ulozit_data()
            print("Naskladnenie bolo uspesne")
        else:
            print("Zadany produkt neexistuje")

    def vyskladnenie(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            kusy = int(input("Kolko kusov vyskladnit: "))
            if self.produkty[nazov].pocet_kusov < kusy:
                print("Nedostatok tovaru na sklade")
            else:
                self.produkty[nazov].pocet_kusov -= kusy
                self.ulozit_data()
                print("Vyskladnenie bolo uspesne")
        else:
            print("Zadany produkt neexistuje")

    def ulozit_data(self):
        with open("data.txt","w",encoding='utf-8') as f:
            for x in self.produkty.values():
                f.write(f"{x.nazov},{x.cena},{x.pocet_kusov}\n")

    def export_skladu(self):
        import xml.etree.ElementTree as ET
        produkty = ET.Element("produkty")
        for x in self.produkty.values():
            produkt = ET.SubElement(produkty,"produkt")
            ET.SubElement(produkt,"nazov").text = x.nazov
            ET.SubElement(produkt,"cena").text = str(x.cena)
            ET.SubElement(produkt,"pocet").text = str(x.pocet_kusov)
            tree = ET.ElementTree(produkty)
            tree.write("export.xml",encoding="utf-8",xml_declaration=True)



