# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)

for x in range(7):
    print("hello there",end=" ")

print()
print("hello there "*7)

print(*["hello there" for _ in range(7)])
print("hello there","hello there","hello there","hello there","hello there","hello there","hello there")

def print_hello(n):
    print("hello there",end =" ")
    if n > 1:
        print_hello(n-1)

print_hello(7)
print()
# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

print(tuple(set(vals)))

result = []
for x in vals:
    if x not in result:
        result.append(x)

print(tuple(result))

# # # DOPLŇTE KÓD TU

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

words = [
     'worD', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
     'sMall', 'terrific', 'alternative', 'book', 'dictionaRy', 'word'
 ]

print([w.lower() for w in words if 'r' in w.lower()])

# # DOPLŇTE KÓD TU

# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://jsonplaceholder.typicode.com/users
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users")
if "json" in resp.headers["Content-type"]:
    print([x['email'] for x in resp.json()])

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
for y in [x['name'] for x in cities[:5]]:
    print(y)

print()
# b) Vypíšte posledných 5 miest.
for y in [x['name'] for x in cities[-5:]]:
    print(y)
# c) Nájdite mesto s najväčším počtom obyvateľov.
print(max(cities,key=lambda x:x['population']))

max_value = {}

for x in cities:
    if not max_value or max_value['population'] < x['population']:
        max_value = x

print(max_value)

# d) Nájdite mesto s najmenším počtom obyvateľov.
print(min(cities,key=lambda x:x['population']))

# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.
print([x['name'] for x in cities if x['population'] < 1_000_000])



# DOPLŇTE KÓD TU
