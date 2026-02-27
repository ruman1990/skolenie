import xml.etree.ElementTree as ET

data = ET.Element('data')

person1 = ET.SubElement(data, 'person')
ET.SubElement(person1, 'name').text = 'Janko'
ET.SubElement(person1, 'age').text = '30'
pet = ET.SubElement(person1, 'pet')
ET.SubElement(pet,'name').text = 'Azor'

person2 = ET.SubElement(data, 'person')
ET.SubElement(person2, 'name').text = 'Eva'
ET.SubElement(person2, 'age').text = '25'

tree = ET.ElementTree(data)
tree.write('novi_ludia.xml', encoding='utf-8', xml_declaration=True)