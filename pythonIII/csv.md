# CSV a modul `csv` v Pythone

## Čo je CSV?

**CSV (Comma Separated Values)** je veľmi populárny formát na import a export dát, ktorý sa využíva v tabuľkových procesoroch (napr. Excel) aj databázach.
Každý riadok v CSV súbore predstavuje jeden záznam (riadok tabuľky). Jednotlivé hodnoty (polia, stĺpce) sú od seba **oddelené čiarkou** alebo iným znakom (napríklad bodkočiarkou, tabulátorom alebo „|“).

#### Príklad CSV súboru:

```
Meno,Vek,Email
Anna,23,anna@email.com
Peter,30,peter@email.com
```

### Vlastnosti a využitie CSV

* **Prenos a výmena dát** medzi aplikáciami a programovacími jazykmi.
* Ukladanie jednoduchých databáz.
* Rýchly export alebo import údajov z Excelu, databáz či rôznych systémov.
* Jednoduchý formát, čitateľný aj v bežnom textovom editore.

#### Výhody:

* Jednoduchosť a široká podpora v programoch a knižniciach.
* Dá sa otvoriť v Exceli, Google Sheets aj v Poznámkovom bloku.

#### Nevýhody:

* Nevhodný pre zložité štruktúry (napr. vnorené objekty).
* Problémy môžu nastať, ak polia obsahujú čiarky, úvodzovky alebo špeciálne znaky.

---

## Práca s CSV v Pythone – modul `csv`

Python ponúka **štandardný modul `csv`**, ktorý poskytuje množstvo funkcií a tried na prácu s CSV súbormi.

### Základné metódy modulu `csv`

| Metóda                   | Popis                                                 |
| ------------------------ | ----------------------------------------------------- |
| `csv.reader`             | Vráti objekt na čítanie CSV po riadkoch               |
| `csv.writer`             | Vráti objekt na zápis CSV po riadkoch                 |
| `csv.register_dialect`   | Registruje vlastný „dialekt“ (nastavenie formátu CSV) |
| `csv.unregister_dialect` | Odregistruje zadaný dialekt                           |
| `csv.get_dialect`        | Získa informácie o dialekte podľa mena                |
| `csv.list_dialects`      | Zoznam všetkých registrovaných dialektov              |
| `csv.field_size_limit`   | Zistí/určí maximálnu povolenú veľkosť poľa v CSV      |

---

## Čítanie CSV súboru

### 1. Základné čítanie pomocou `csv.reader`

```python
import csv

with open('numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for e in row:
            print(e)
```

Tento príklad načíta súbor `numbers.csv` s obsahom:

```
16,6,4,12,81
11,12,11,13,12
4,3,2,1,5
```

Každý prvok v každom riadku sa vypíše zvlášť.

---

### 2. Použitie iného oddeľovača

Napríklad súbor:

```
pen|cup|bottle
chair|book|tablet
```

Čítame takto:

```python
import csv

with open('items.csv', 'r') as f:
    reader = csv.reader(f, delimiter="|")
    for row in reader:
        for e in row:
            print(e)
```

Teraz sú polia oddelené znakom `|`.

---

### 3. Čítanie ako slovník – `csv.DictReader`

Trieda `csv.DictReader` číta CSV a automaticky mapuje stĺpce na kľúče slovníka podľa hlavičky (prvého riadku):

```python
import csv

with open('values.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['min'], row['avg'], row['max'])
```

Pre súbor:

```
min,avg,max
1,5.5,10
2,3.5,5
```

Prvky sú dostupné podľa názvu stĺpca (kľúča).

---

## Zápis do CSV súboru

### 1. Zápis riadkov – `csv.writer`

```python
import csv

nms = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]

with open('numbers2.csv', 'w') as f:
    writer = csv.writer(f)
    for row in nms:
        writer.writerow(row)
```

Výsledok:

```
1,2,3,4,5,6
7,8,9,10,11,12
```

#### Zápis viacerých riadkov naraz:

```python
import csv

nms = [[1, 2, 3], [7, 8, 9], [10, 11, 12]]

with open('numbers3.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(nms)
```

---

### 2. Zápis slovníkov – `csv.DictWriter`

Táto trieda zapisuje dáta zo slovníkov, pričom názvy stĺpcov sú určené parametrom `fieldnames`:

```python
import csv

with open('names.csv', 'w') as f:
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    writer.writerow({'first_name' : 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name' : 'Robert', 'last_name': 'Brown'})
    writer.writerow({'first_name' : 'Julia', 'last_name': 'Griffin'})
```

Výsledok v súbore:

```
first_name,last_name
John,Smith
Robert,Brown
Julia,Griffin
```

---

### 3. Vlastné CSV dialekty

Ak potrebujete špeciálne nastavenie CSV (napr. iný oddeľovač alebo úvodzovky), môžete si vytvoriť vlastný dialekt.

```python
import csv

csv.register_dialect("hashes", delimiter="#")

with open('items3.csv', 'w') as f:
    writer = csv.writer(f, dialect="hashes")
    writer.writerow(("pens", 4))
    writer.writerow(("plates", 2))
    writer.writerow(("bottles", 4))
    writer.writerow(("cups", 1))
```

Výsledok:

```
pens#4
plates#2
bottles#4
cups#1
```

---

## Generovanie falošných CSV dát

Na generovanie testovacích dát môžeme použiť modul `faker`:

```python
from faker import Faker
import csv

faker = Faker()

with open('users.csv', 'w', newline='') as f:
    fieldnames = ['id', 'first_name', 'last_name', 'occupation']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 101):
        _id = i
        fname = faker.first_name()
        lname = faker.last_name()
        occupation = faker.job()
        writer.writerow({'id': _id, 'first_name': fname, 
                         'last_name': lname, 'occupation': occupation})
```

Tento príklad vytvorí CSV súbor so 100 vygenerovanými používateľmi.

---

## Užitočné rady a zhrnutie

* Pri zápise CSV v Pythone **vždy používajte parameter `newline=""`** (inak môžu vznikať prázdne riadky navyše).
* Pri práci so znakmi mimo ASCII použite **`encoding="utf-8"`**.
* **CSV** je ideálny pre jednoduché tabuľkové dáta a je podporovaný väčšinou nástrojov.
* V Pythone ponúka modul `csv` jednoduché a univerzálne možnosti na čítanie a zápis.
* Pri zložitejších dátach alebo veľkých súboroch zvážte použitie knižnice **pandas**.
