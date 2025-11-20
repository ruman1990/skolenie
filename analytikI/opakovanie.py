# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)

# # DOPLŇTE KÓD TU
# for _ in range(7):
#     print("hello there", end=' ')

# print()
# print('hello there ' * 7)

# print(*['hello there' for _ in range(7)],end=' ')
# print()
# def print_hello(n):
#     if n <= 0:
#         return
#     print("hello there", end=' ')
#     print_hello(n - 1)

# print_hello(7)
# print()
# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

# vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

# x = tuple(set(vals))
# print(x)

# import funcy
# print(tuple(funcy.distinct(vals)))


# # # DOPLŇTE KÓD TU

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

# words = [
#      'word', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
#      'small', 'terrific', 'alternative', 'book', 'dictionary', 'word'
#  ]

# for x in words:
#     if 'r' in x:
#         print(x)

# print()
# x = [ word for word in words if 'r' in word]
# print(*x)

# print()
# for x in filter(lambda x : 'r' in x,words):
#     print(x, end=' ')


# print()
# print()
# # DOPLŇTE KÓD TU

# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://webcode.me/users.json

# # DOPLŇTE KÓD TU
# import requests

# x = requests.get('https://webcode.me/users.json')
# data = x.json()

# for x in data['users']:
#     print(x['email'])

# print()
# print(*[x['email'] for x in data['users']])


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

for x in range(5):
    print(cities[x]['name'])

for x in cities[:5]:
    print(x['name'])

print(*[ x['name'] for x in cities[:5] ])

# b) Vypíšte posledných 5 miest.
for x in cities[-5:]:
    print(x['name'])

print()
# c) Nájdite mesto s najväčším počtom obyvateľov.

print(max(cities,key=lambda x : x['population'] ))


# d) Nájdite mesto s najmenším počtom obyvateľov.

print(min(cities,key=lambda x : x['population'] ))

# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.

# DOPLŇTE KÓD TU
print()
print(*[c['name'] for c in cities if c['population'] < 1_000_000])

print(list(filter(lambda x: x['population'] < 1_000_000,cities)))