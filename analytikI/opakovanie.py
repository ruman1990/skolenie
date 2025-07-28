# OPAKOVANIE – Zadania

# 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
#    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)

# DOPLŇTE KÓD TU
# for _ in range(7):
#     print("hello there",end=' ')

# print('hello there'*7,end=' ')

# 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

# vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

# # DOPLŇTE KÓD TU
# print(tuple(set(vals)))

# import funcy
# print(tuple(funcy.distinct(vals)))

# 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

# words = [
#     'word', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
#     'small', 'terrific', 'alternative', 'book', 'dictionary', 'word'
# ]

# w = []
# for word in words:
#     if 'r' in word and 'o' in word:
#         w.append(word.lower())

# print(w)

# words_vysledok = [word.lower() for word in words if 'r' in word and 'o' in word]
# print(words_vysledok)
# DOPLŇTE KÓD TU


# 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
#    URL: https://webcode.me/users.json

# DOPLŇTE KÓD TU
import requests

resp = requests.get('https://webcode.me/users.json')
data = resp.json()


# {
#   "users": [
#     {
#       "id": 1,
#       "first_name": "Robert",
#       "last_name": "Schwartz",
#       "email": "rob23@gmail.com"
#     }
#   ]
# }


# for x in data["users"]:
#     print(x['email'])


# print([u['email'] for u in data["users"]])


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
# b) Vypíšte posledných 5 miest.
# c) Nájdite mesto s najväčším počtom obyvateľov.
# d) Nájdite mesto s najmenším počtom obyvateľov.
# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.

# DOPLŇTE KÓD TU
# prvych_5 = cities[:5]
# for x in prvych_5:
#     print(f'{x['name']} {x['population']}')

# print('------------------------')

# poslednych_5 = cities[-5:]  
# for x in poslednych_5:
#     print(f'{x['name']} {x['population']}')


# print(max(cities, key=lambda x: x['population']))

# print(min(cities, key=lambda x: x['population']))

# print([city for city in cities if city["population"] < 1000000])
