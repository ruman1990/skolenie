# -- Vytvorenie slovníka a jeho výpis --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# -- Prístup k hodnote pomocou kľúča --
print(thisdict["brand"])  # => Ford

# -- Duplikát kľúča prepíše predchádzajúcu hodnotu --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)  # year bude 2020

# -- Zistenie počtu položiek --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(len(thisdict))  # => 3

# -- Hodnoty môžu byť rôzne typy (string, int, bool, list) --
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

# -- Overenie dátového typu slovníka --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))  # => <class 'dict'>

# -- Vytvorenie slovníka pomocou konštruktora dict() --
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)


# -- Prístup k hodnote cez kľúč pomocou [] --
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
x = thisdict["model"]
print(x)  # Mustang

# -- Prístup pomocou get() --
x = thisdict.get("model")
print(x)  # Mustang

# -- Získanie zoznamu všetkých kľúčov --
x = thisdict.keys()
print(x)  # dict_keys(['brand','model','year'])

# -- Zobrazenie reflexie zmien v keys() pohľade --
car = {"brand":"Ford","model":"Mustang","year":1964}
x = car.keys()
print("pred:", x)
car["color"] = "white"
print("po:", x)

# -- Získanie zoznamu všetkých hodnôt --
x = thisdict.values()
print(x)  # dict_values([...])

# -- Reflexia zmeny hodnoty vo values() pohľade --
car = {"brand":"Ford","model":"Mustang","year":1964}
x = car.values()
print("pred:", x)
car["year"] = 2020
print("po:", x)

# -- Reflexia pridania položky vo values() pohľade --
car = {"brand":"Ford","model":"Mustang","year":1964}
x = car.values()
print("pred:", x)
car["color"] = "red"
print("po:", x)

# -- Získanie zoznamu párov (kľúč, hodnota) --
x = thisdict.items()
print(x)  # dict_items([...])

# -- Reflexia zmeny hodnoty vo items() pohľade --
car = {"brand":"Ford","model":"Mustang","year":1964}
x = car.items()
print("pred:", x)
car["year"] = 2020
print("po:", x)

# -- Reflexia pridania položky vo items() pohľade --
car = {"brand":"Ford","model":"Mustang","year":1964}
x = car.items()
print("pred:", x)
car["color"] = "red"
print("po:", x)

# -- Overenie existencie kľúča pomocou in --
if "model" in thisdict:
    print("Áno, 'model' je v slovníku")



# -- Zmena hodnoty konkrétneho kľúča --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# zmena roka z 1964 na 2018
thisdict["year"] = 2018
print(thisdict)  # výstup: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# -- Použitie update(): aktualizácia jednej hodnoty --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# update pomocou iného slovníka
thisdict.update({"year": 2020})
print(thisdict)  # výstup: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# -- Pridanie novej položky pomocou priamej priradzovačky --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"  # pridáme kľúč "color" s hodnotou "red"
print(thisdict)
# Očakávaný výstup: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# -- Pridanie novej položky pomocou metódy update() --
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})  # pridáme (alebo aktualizujeme) položky zo slovníka
print(thisdict)
# Očakávaný výstup je rovnaký ako vyššie:
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# -- pop(): odstráni položku podľa kľúča a vráti jej hodnotu --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)  # očakávaný výstup: {'brand': 'Ford', 'year': 1964}

# -- popitem(): odstráni posledný vložený pár (Python ≥3.7) --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print(thisdict)  # očakávaný výstup: {'brand': 'Ford', 'model': 'Mustang'}

# -- del dict[key]: odstráni položku so zadaným kľúčom --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print(thisdict)  # očakávaný výstup: {'brand': 'Ford', 'year': 1964}

# -- del dict: zmaže celý slovník (premenná prestane existovať) --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict
# print(thisdict)  # táto línia by vyvolala chybu NameError

# -- clear(): vyprázdni slovník, ale nechá ho existovať --
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)  # očakávaný výstup: {}


# -- Loop cez samotné kľúče slovníka (predvolene prints key names) --
thisdict = {"brand":"Ford","model":"Mustang","year":1964}
for x in thisdict:
    print(x)

# -- Loop cez hodnoty slovníka pomocou prístupu cez kľúč --
for x in thisdict:
    print(thisdict[x])

# -- Loop pomocou values(): vypíše len hodnoty --
for x in thisdict.values():
    print(x)

# -- Loop pomocou keys(): vypíše len kľúče --
for x in thisdict.keys():
    print(x)

# -- Loop cez kľúč-hodnota pomocou items(): vypíše obe súčasne --
for key, value in thisdict.items():
    print(key, value)


# -- Definovanie vnoreného slovníka priamo --
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011
  }
}
print(myfamily)

# -- Definovanie vnoreného slovníka cez existujúce slovníky --
child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily2 = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily2)

# -- Prístup k prvkom vo vnorenom slovníku --
print(myfamily["child2"]["name"])  # očakávaný výstup: Tobias

# -- Prechádzanie vnoreného slovníka cez loop y items() --
for child_key, child_info in myfamily.items():
    print(child_key)  # vypíše "child1", "child2", "child3"
    for info_key in child_info:
        print(info_key + ":", child_info[info_key])
