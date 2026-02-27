import xml.etree.ElementTree as ET


tree = ET.parse('people.xml')

root = tree.getroot()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_data(self):
        return f'{self.name};{self.age}'
persons = []

for x in root.findall('person'):
    persons.append(Person(x.find('name').text,x.find('age').text))

with open('vysledok.csv','w',encoding='UTF-8') as f:
    for x in persons:
        f.write(x.print_data()+ '\n')