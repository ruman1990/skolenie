# vyrobime skladovy softver
# textove menu s volbami
    # ukoncenie programu
    # vypis skladu
    # pridanie tovaru na sklad
    # naskladnenie
    # vyskladnenie
    # nastavenie ceny tovaru
    # sucet ceny tovarov
    # odstranenie tovaru zo skladu
    # exportovat sklad
    # importovat sklad
from produkt import Produkt
import xml.etree.ElementTree as ET

class Sklad:
    def __init__(self):
        self.produkty = {}
        try:
            with open("data.txt","r",encoding="utf-8") as f:
                for x in f:
                    item = x.strip().split(",")
                    self.produkty[item[0]] = Produkt(*item)
        except Exception:
            print("Nemas inicialny data.txt")
        finally:
            if not self.produkty:
                with open("data.txt","w",encoding="utf-8") as f:
                    print("Inicialny subor data.txt bol vytvoreny!")
    def vypis_skladu(self):
        for x in self.produkty.values():
            print(x)

    def pridanie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            print("Produkt sa uz na sklade nachadza!")
            return
        try:
            cena = float(input("Zadaj cenu produktu: "))
            pocet_kusov = int(input("Zadaj pocet kusov produktu: "))
        except Exception:
            print("zadal si zle hodnoty!")
            return
        self.produkty["nazov"] = Produkt(nazov,cena,pocet_kusov)
        self._ulozenie_skladu()
        print("Produkt bol uspesne pridany")

    def odstranenie_produktu(self):
        nazov = input("Zadaj nazov produktu: ")
        if nazov in self.produkty:
            del self.produkty[nazov]
            self._ulozenie_skladu()
            print("Produkt bol uspesne odstraneny")
        else:
            print("Produkt neexistuje!")

    def _ulozenie_skladu(self):
        with open("data.txt","w",encoding="utf-8") as f:
            for x in self.produkty.values():
                f.write(x.formatovany_vypis())

    def cena_tovarov(self):
        suma = 0
        for x in self.produkty.values():
            suma += x.celkova_cena()
        print(f"Celkova cena tovarov je {suma:.2f}€")

    def export_skladu(self):
        data = ET.Element('sklad')
        for x in self.produkty.values():
            product = ET.SubElement(data, 'produkt')
            ET.SubElement(product, 'nazov').text = x.nazov
            ET.SubElement(product, 'cena').text = str(x.cena)
            ET.SubElement(product, 'pocet').text = str(x.pocet)
        tree = ET.ElementTree(data)
        tree.write("export.xml",encoding="utf-8",xml_declaration=True)
        print("Export bol uspesny!")

    def import_skladu(self):
        tree = ET.parse("export.xml")
        root = tree.getroot()

        self.produkty.clear()
        for x in root.findall("produkt"):
            self.produkty[x.find("nazov").text] = Produkt(x.find("nazov").text,x.find("cena").text,x.find("pocet").text)
        print("Import bol uspesny!")

