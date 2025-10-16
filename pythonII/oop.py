import xml.etree.ElementTree as ET

xml_data = """
<data>
    <person>
        <name>Janko</name>
        <age>30</age>
    </person>
</data>
"""

root = ET.fromstring(xml_data)
for person in root.findall('person'):
    print(person.find('name').text)