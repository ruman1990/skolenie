# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)

print('hello there '*7,end='')

print()
for _ in range(7):
    print('hello there',end=' ')

print()
x = 0
while x < 7:
    print('hello there',end=' ')
    x += 1

print()
print(*['hello there' for _ in range(7)],end=' ')

print()
def print_hello(n):
    print('hello there',end=' ')
    if n > 1:
        print_hello(n-1)
    
print_hello(7)

print()
# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

print(list(set(vals)))

y = []
for x in vals:
    if x not in y:
        y.append(x)
print(y)

print([x for i,x in enumerate(vals) if x not in vals[:i]])


# # # DOPLŇTE KÓD TU

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

words = [
     'word', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
     'small', 'terrific', 'alternative', 'book', 'dictionary', 'word'
 ]


print([ x for x in words if 'r' in x])

print(list(filter(lambda x: 'r' in x,words)))

y = []
for x in words:
    if 'r' in x:
        y.append(x)

print(y)

# # DOPLŇTE KÓD TU

# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://jsonplaceholder.typicode.com/users

import requests

resp = requests.get('https://jsonplaceholder.typicode.com/users')
data = resp.json()
print([x['email'] for x in data])

data2 = []
for x in data:
    data2.append(x['email'])
print(data2)

# # DOPLŇTE KÓD TU


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
print(cities[:5])
# b) Vypíšte posledných 5 miest.
print(cities[-5:])
# c) Nájdite mesto s najväčším počtom obyvateľov.
print(max(cities,key=lambda x : x['population']))

# d) Nájdite mesto s najmenším počtom obyvateľov.
print(min(cities,key=lambda x : x['population']))

# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.
print([x['name'] for x in cities if x['population']<1_000_000])



# DOPLŇTE KÓD TU
from functools import reduce

def sucet(**kwargs):
    kwargs['x']
    kwargs['y']

print(sucet(x=5,y=6,z=7))