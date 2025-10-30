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
for x in data:
    print(x)

# 3. Vyfiltruj všetky úlohy, ktoré nie sú dokončené (kde "completed": false) pomocou filter a lambda. Výsledok vypíš.
# DOPLŇ KÓD TU

print(len(list(filter(lambda x: not x['completed'],data))))
data_completed = list(filter(lambda x: not x['completed'],data))

# 4. Použi map a lambda na vytvorenie zoznamu názvov úloh (title). Výsledok vypíš.
# DOPLŇ KÓD TU
x = list(map(lambda x: x['title'],data_completed))
for y in x:
    print(y)

# 5. Pomocou list comprehension vytvor nový zoznam slovníkov, kde bude iba id, title a completed. Výsledok vypíš.
# DOPLŇ KÓD TU
data_csv = [{'poradie' : i['id'], 'uloha' : i['title'], 'status' : i['completed']} for i in data_completed]
print(data_csv)

# 6. Ulož všetky dokončené úlohy (kde "completed": true) do CSV súboru done_tasks.csv, prvý riadok má byť hlavička.
# DOPLŇ KÓD TU
import csv

with open('opakovanie.csv','w',encoding='utf-8',newline='') as f:
    names = ['poradie','uloha','status']
    writer = csv.DictWriter(f,fieldnames=names)
    writer.writeheader()
    for x in data_csv:
        writer.writerow(x)
