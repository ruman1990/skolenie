import xml.etree.ElementTree as ET

ludia = [["Janko",30],["Eva",25]]

data = ET.Element('data')

for x in ludia:
    person1 = ET.SubElement(data, 'person')
    ET.SubElement(person1, 'name').text = x[0]
    ET.SubElement(person1, 'age').text = str(x[1])

tree = ET.ElementTree(data)
tree.write('novi_ludia.xml', encoding='utf-8', xml_declaration=True)