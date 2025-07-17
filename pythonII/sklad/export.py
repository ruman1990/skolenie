import xml.etree.ElementTree as ET
from produkt import Produkt

def export_skladu(sklad):
    vystup = []
    for i in sklad.produkty:
        vystup.append(sklad.produkty[i].export())
    retazec = ";".join(vystup)
    print(retazec)

def import_skladu(sklad):
    vstup = input("Zadaj data skladu: ")
    # voda,3,1;chlieb,4,3
    casti = vstup.split(';')
    for x in casti:
        item = x.split(',')
        sklad.produkty[item[0]] = item

def export_skladu_xml(sklad):
    root = ET.Element("sklad")
    for x in sklad.produkty.values():
        prod = ET.SubElement(root,'produkt')
        ET.SubElement(prod,'nazov').text = x.nazov
        ET.SubElement(prod,'pocet').text = str(x.pocet)
        ET.SubElement(prod,'cena').text = str(x.cena)
    strom = ET.ElementTree(root)
    strom.write('export.xml', encoding='utf-8' , xml_declaration=True)
    print("Export bol uspesne vykonany")

def import_skladu_xml(sklad):
    subor = ET.parse('export.xml')
    root = subor.getroot()
    sklad.produkty.clear()
    for x in root.findall('produkt'):
        nazov = x.find('nazov').text
        pocet = x.find('pocet').text
        cena = x.find('cena').text
        sklad.produkty[nazov] = Produkt(nazov,int(pocet),float(cena))
    print('Sklad bol uspesne importovany')

