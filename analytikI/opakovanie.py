# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)
# for _ in range(7):
#     print("hello there", end=' ')

# print("hello there " * 7)

# count = 0
# while count < 7:
#     print("hello there", end=' ')
#     count += 1

#[print("hello there", end=' ') for _ in range(7)]

# def repeat_hello(n):
#     if n <= 0:
#         return
#     repeat_hello(n - 1)
#     print("hello there", end=' ')

# repeat_hello(7)


# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

print(tuple(set(vals)))

x = []
for y in vals:
    if y not in x:
        x.append(y)

print(tuple(x))

import funcy
print(tuple(funcy.distinct(vals)))


# # # DOPLŇTE KÓD TU

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

words = [
     'word', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
     'small', 'terrific', 'alternative', 'book', 'dictionary', 'word'
 ]

w = []
for x in words:
    if 'r' in x:
        w.append(x)

print(w)

result = [x for x in words if 'r' in x]
print(result)

print(list(filter(lambda x: 'r' in x,words)))



# # DOPLŇTE KÓD TU

# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://webcode.me/users.json

# # DOPLŇTE KÓD TU
import json

with open("vystup.json",'r',encoding='utf-8') as f:
    data = json.load(f)
    result = [x['meno'] for x in data if 'm' in x['meno'].lower()]

    result2 = []
    for x in data:
        if 'm' in x['meno'].lower():
            result2.append(x['meno'])


    print(result)
    print(result2)

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
prvych_5 = cities[:5]
for x in prvych_5:
    print(x['name'])

# b) Vypíšte posledných 5 miest.
prvych_5 = cities[-5:]
for x in prvych_5:
    print(x['name'])

# c) Nájdite mesto s najväčším počtom obyvateľov.
print(max(cities,key=lambda x:x['population'] ))

# d) Nájdite mesto s najmenším počtom obyvateľov.
print(min(cities,key=lambda x:x['population'] ))
# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.

print([city for city in cities if city['population'] < 1_000_000])

# DOPLŇTE KÓD TU
