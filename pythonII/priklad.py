child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}
print(myfamily)

# -- Prístup k prvkom vo vnorenom slovníku --
print(myfamily["child2"]["name"])  # očakávaný výstup: Tobias

# -- Prechádzanie vnoreného slovníka cez loop y items() --
for child_key, child_info in myfamily.items():
    print(child_key)  # vypíše "child1", "child2", "child3"
    for info_key in child_info:
        print(info_key + ":", child_info[info_key])