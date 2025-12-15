"""
Zadanie: Práca s JSON a CSV v Pythone

Vstupné údaje:
- internetový JSON: https://jsonplaceholder.typicode.com/todos

Úlohy:
1. Načítaj JSON dáta zo zadanej URL.
2. Vypíš všetky položky (každý záznam na samostatnom riadku).
3. Vyfiltruj všetky úlohy, ktoré nie sú dokončené (kde "completed": false) pomocou filter a lambda. Výsledok vypíš.
4. Použi map a lambda na vytvorenie zoznamu názvov úloh (title). Výsledok vypíš.
5. Pomocou list comprehension vytvor nový zoznam slovníkov, kde bude iba id, title a completed. Výsledok vypíš.
6. Ulož všetky dokončené úlohy (kde "completed": true) do CSV súboru done_tasks.csv, prvý riadok má byť hlavička.
"""


import csv

# ============================= ÚLOHY ======================================

# 1. Načítaj JSON dáta zo zadanej URL alebo z lokálneho súboru priklad.json
# url = "https://jsonplaceholder.typicode.com/todos"
# Namiesto url môžeš použiť lokálny súbor priklad.json
# DOPLŇ KÓD TU
import requests

resp = requests.get('https://jsonplaceholder.typicode.com/todos')
data = resp.json()

# 2. Vypíš všetky položky (každý záznam na samostatnom riadku)
# DOPLŇ KÓD TU
# for x in data:
#     print(x)

# 3. Vyfiltruj všetky úlohy, ktoré nie sú dokončené (kde "completed": false) pomocou filter a lambda. Výsledok vypíš.
# DOPLŇ KÓD TU

d = list(filter(lambda x: not x['completed'],data))
for x in d:
    print(d)

# 4. Použi map a lambda na vytvorenie zoznamu názvov úloh (title). Výsledok vypíš.
# DOPLŇ KÓD TU
a = [x['title'] for x in data]
print(len(a))

# 5. Pomocou list comprehension vytvor nový zoznam slovníkov, kde bude iba id, title a completed. Výsledok vypíš.
# DOPLŇ KÓD TU
print([{"id": x['id'], "title": x['title'], "completed" : x['completed']} for x in data])

# 6. Ulož všetky dokončené úlohy (kde "completed": true) do CSV súboru done_tasks.csv, prvý riadok má byť hlavička.
# DOPLŇ KÓD TU
import csv
hotove = [x for x in data if x['completed']]

with open('hotovo.csv','w',encoding='utf-8',newline='') as f:
    fieldnames = ['id','userId','title','completed']
    writer = csv.DictWriter(f,fieldnames=fieldnames)
    writer.writeheader()
    for x in hotove:
        writer.writerow(x)

