# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)

print("hello there "*7,end=" ")

print()

for _ in range(7):
    print("hello there",end=" ")

print()

x = 0
while x < 7:
    print("hello there",end=" ")
    x += 1

print()

def reukrzivne_hello(n):
    print("hello there",end=" ")
    if n > 1:
        reukrzivne_hello(n-1)

reukrzivne_hello(7)

print()

print(*["hello there" for _ in range(7)])


# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]
vals = set(vals)
print(tuple(vals))

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

words = [
     'worD', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
     'sMall', 'terrific', 'alternative', 'book', 'dictionaRy', 'word'
 ]

result = [x.lower() for x in words if 'r' not in x.lower()]
print(result)

# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://jsonplaceholder.typicode.com/users

import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users")
vysledok = resp.json()

#print(vysledok)

print([x['email'] for x in vysledok])

y = []
for x in vysledok:
    y.append(x['email'])
print(y)



# 5. Práca so zoznamom miest:

cities = [
    {"id": 1, "name": "Bratislava", "population": 432000},
    {"id": 2, "name": "Budapest", "population": 1759000},
    {"id": 3, "name": "Prague", "population": 1280000},
    {"id": 4, "name": "Warsaw", "population": 1748000},
    {"id": 5, "name": "Los Angeles", "population": 3971000},
    {"id": 6, "name": "Edinburgh", "population": 464000},
    {"id": 7, "name": "Berlin", "population": 3671000},
    {"id": 8, "name": "Tokyo", "population": 14000000},
    {"id": 9, "name": "New York", "population": 8419600},
    {"id": 10, "name": "Sydney", "population": 5312163},
    {"id": 11, "name": "Mumbai", "population": 20411000},
    {"id": 12, "name": "Cairo", "population": 10220000},
    {"id": 13, "name": "Seoul", "population": 9733509},
    {"id": 14, "name": "London", "population": 8982000},
    {"id": 15, "name": "Moscow", "population": 11920000},
    {"id": 16, "name": "Bangkok", "population": 10539000},
    {"id": 17, "name": "Toronto", "population": 2930000}
]

# Úlohy:
# a) Vypíšte prvých 5 miest.

zosortovane = sorted(cities,key=lambda x : x['population'])
vyrezane = zosortovane[:5]
a = []
for x in vyrezane:
    a.append(x['name'])

print(a)

print([x['name'] for x in sorted(cities,key=lambda x : x['population'])[:5]])


# b) Vypíšte posledných 5 miest.
print([x['name'] for x in sorted(cities,key=lambda x : x['population'])[-5:]])

# c) Nájdite mesto s najväčším počtom obyvateľov.
print([x['name'] for x in sorted(cities,key=lambda x : x['population'])[-1:]])

print(max(cities,key=lambda x: x["population"]))

# d) Nájdite mesto s najmenším počtom obyvateľov.
print([x['name'] for x in sorted(cities,key=lambda x : x['population'])[:1]])

print(min(cities,key=lambda x: x["population"]))

# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.
print([x['name'] for x in cities if x['population']<1_000_000])