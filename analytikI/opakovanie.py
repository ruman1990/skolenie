# OPAKOVANIE – Zadania

# # 1. Nájdite viaceré spôsoby, ako vypísať "hello there" 7-krát.
# #    (Použite aspoň for cyklus, while cyklus, rekurziu, list comprehension alebo iný spôsob.)
sprava = "hello there"
count = 6
 
while count >= 0:
    count -= 1
    print (sprava, end=" ")

print() 
 
for x in range (0,7):
    print(sprava, end=" ")

print()

def print_hello_there(n):
    print("hello there",end=" ")
    if n > 1:
        print_hello_there(n - 1)

print_hello_there(7)

print()

print("hello there "*7,end=" ")

print()

print(*["hello there" for _ in range(7)])

# # 2. Vytvorte z premennej vals n-ticu (tuple) unikátnych hodnôt.

vals = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 10]

unikatne = tuple(set(vals))
 
print("\nUnikátne hodnoty:")
print(unikatne)

# # 3. Vyfiltrujte slová, ktoré obsahujú písmeno 'r'.

words = [
     'worD', 'sky', 'tomorrow', 'cat', 'dog', 'apple', 'orange', 'banana',
     'sMall', 'terrific', 'alternative', 'book', 'dictionaRy', 'word'
]


vysledok = [x for x in words if 'r' in x.lower()]
print(vysledok)




# # 4. Stiahnite JSON zo stránky a vypíšte všetky emaily používateľov.
# #    URL: https://jsonplaceholder.typicode.com/users
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users")
data = resp.json()

#print(data)
# unpacking
print(*[x['email'] for x in data])





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
print([x['name'] for x in cities[:5]])

vysledok = []
for x in cities[:5]:
    vysledok.append(x['name'])
print(vysledok)


# b) Vypíšte posledných 5 miest.
print([x["name"] for x in cities[-5:]])

# c) Nájdite mesto s najväčším počtom obyvateľov.

print(max(cities,key=lambda x: x["population"]))


# d) Nájdite mesto s najmenším počtom obyvateľov.
print(min(cities,key=lambda x: x["population"]))

# e) Vyfiltrujte mestá, ktoré majú menej ako 1 milión obyvateľov.

vysledok = [x for x in cities if x["population"] < 1_000_000]
for x in vysledok:
    print(f"Mesto {x["name"]} ma pocet obyvatelov {x["population"]}")
#print(vysledok)