import xml.etree.ElementTree as ET
from produkt import Produkt
import csv

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
    _prepis_db(sklad,sklad.produkty)

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
    _prepis_db(sklad,sklad.produkty)
    print('Sklad bol uspesne importovany')

def export_skladu_csv(sklad):
    with open("sklad.csv",'w',newline='',encoding='utf-8') as f:
        
        writer = csv.DictWriter(f,fieldnames=['nazov','pocet','cena'])
        writer.writeheader()
        for row in sklad.produkty.values():
            writer.writerow({'nazov' : row.nazov, 'pocet' : row.pocet, 'cena' : row.cena})
    print(f'Export skladu do csv bol uspesny')

def import_skladu_csv(sklad):
    nove_produkty = {}
    with open('sklad.csv','r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nove_produkty[row['nazov']] = Produkt(row['nazov'],row['pocet'],row['cena'])
    _prepis_db(sklad,nove_produkty)
    print(f'Import skladu z CSV bol uspesny')

def _prepis_db(sklad,nove_produkty):
    sklad.cursor.execute("DELETE FROM produkty")
    for prod in nove_produkty.values():
        #sklad.produkty[prod.nazov] = prod
        sklad.cursor.execute("INSERT INTO produkty (nazov,pocet,cena) VALUES (?,?,?)",(prod.nazov,prod.pocet,prod.cena))
    sklad.conn.commit()
