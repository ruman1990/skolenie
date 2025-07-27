Samozrejme! Tu je **prehľadný učebný materiál o knižnici Tablib** (v slovenčine), vhodný pre rýchle samoštúdium aj do výučby:

---

# 📦 Tablib – jednoduchá práca s tabuľkovými dátami v Pythone

---

## Čo je **Tablib**?

**Tablib** je knižnica na jednoduchú prácu s tabuľkovými dátami (dáta vo formáte tabuliek, teda riadky a stĺpce).
Vieš s ňou:

* pracovať s dátami vo formáte CSV, XLS, XLSX, JSON, YAML,
* jednoducho importovať a exportovať tabuľky,
* filtrovať, meniť, triediť alebo transformovať dáta,
* vytvárať jednoduché dataset-y priamo v Pythone.

Použitie Tablib je veľmi jednoduché a intuitívne – **funguje podobne ako práca s tabuľkou v Exceli, ale v Pythone**.

---

## Inštalácia

```bash
pip install tablib
```

---

## Základné pojmy

* **Dataset**: hlavný objekt Tablibu, reprezentuje tabuľku.
* **Stĺpce** a **riadky**: do datasetu vkladáš hodnoty po riadkoch (ako list alebo tuple).
* **Headers**: hlavička stĺpcov (názvy stĺpcov).

---

## Základné použitie

### 1️⃣ Vytvorenie datasetu

```python
import tablib

data = tablib.Dataset()
data.headers = ["meno", "vek", "mesto"]

data.append(["Janko", 25, "Bratislava"])
data.append(["Katka", 22, "Košice"])
data.append(["Robo", 30, "Žilina"])
```

---

### 2️⃣ Prístup k dátam

```python
print(data)
# Vypíše tabuľku v textovej podobe

print(data[0])        # Prvý riadok: ('Janko', 25, 'Bratislava')
print(data[1][2])     # Mesto z druhého riadku: 'Košice'
print(data.headers)   # ['meno', 'vek', 'mesto']
```

---

### 3️⃣ Pridanie viac riadkov naraz

```python
data.extend([
    ["Lenka", 27, "Prešov"],
    ["Miro", 29, "Poprad"],
])
```

---

### 4️⃣ Export dát

Tablib podporuje jednoduchý export do viacerých formátov:

```python
csv_data = data.export("csv")
print(csv_data)

json_data = data.export("json")
print(json_data)

xls_data = data.export("xls")   # binárne dáta pre Excel (XLS)
xlsx_data = data.export("xlsx") # binárne dáta pre Excel (XLSX)
```

Pre zápis do súboru:

```python
with open("ludia.csv", "w", encoding="utf-8") as f:
    f.write(csv_data)
```

---

### 5️⃣ Import dát zo súboru

Príklad načítania CSV do Tablib Dataset:

```python
with open("ludia.csv", encoding="utf-8") as f:
    obsah = f.read()
    data = tablib.import_set(obsah, format="csv")
```

---

### 6️⃣ Filtrovanie a triedenie dát

Filtrovanie podľa hodnoty:

```python
vyber = [row for row in data if row[1] > 25]  # vyber všetkých starších ako 25
for osoba in vyber:
    print(osoba)
```

Triedenie:

```python
data.sort(1)  # zoradí podľa druhého stĺpca ("vek")
```

---

### 7️⃣ Pridávanie a odoberanie stĺpcov

Pridanie nového stĺpca:

```python
data.append_col(["M", "Ž", "M", "Ž", "M"], header="pohlavie")
```

Odstránenie stĺpca:

```python
data.remove_col(2)  # odstráni tretí stĺpec (indexuje sa od nuly)
```

---

## Zhrnutie

* **Tablib** je vhodný, ak potrebuješ rýchlo a jednoducho pracovať s tabuľkovými dátami bez zložitosti pandas.
* Je vhodný na export/import medzi rôznymi formátmi (CSV, Excel, JSON, YAML).
* Ovládanie je jednoduché, syntax intuitívna.

---

## Praktické cvičenie

1. Vytvor Dataset so študentmi (meno, vek, známka).
2. Pridaj zopár záznamov.
3. Exportuj výsledok do CSV.
4. Vyfiltruj len študentov s najlepšou známkou.
5. Zoraď dataset podľa veku.
6. Načítaj CSV naspäť do Datasetu.

---

```python
# PRAKTICKÉ CVIČENIA S TABLIB

import tablib

# 1. Vytvor Dataset so študentmi (meno, vek, známka)
data = tablib.Dataset()
data.headers = ["meno", "vek", "znamka"]

# 2. Pridaj zopár záznamov
data.append(["Janko", 17, 1])
data.append(["Katka", 18, 2])
data.append(["Robo", 19, 1])
data.append(["Lenka", 18, 3])
data.append(["Miro", 17, 2])

print("Všetci študenti:")
print(data)
print("-" * 40)

# 3. Exportuj výsledok do CSV
csv_vystup = data.export("csv")
with open("studenti.csv", "w", encoding="utf-8") as f:
    f.write(csv_vystup)
print("CSV súbor 'studenti.csv' bol uložený.")
print("-" * 40)

# 4. Vyfiltruj len študentov s najlepšou známkou (znamka == 1)
best_students = [row for row in data if row[2] == 1]
print("Študenti s najlepšou známkou (1):")
for st in best_students:
    print(st)
print("-" * 40)

# 5. Zoraď dataset podľa veku
data = data.sort("vek")  
print("Študenti zoradení podľa veku:")
print(data)
print("-" * 40)

# 6. Načítaj CSV naspäť do Datasetu
with open("studenti.csv", encoding="utf-8") as f:
    obsah = f.read()
    data2 = tablib.import_set(obsah, format="csv")
print("Načítaný Dataset z CSV súboru:")
print(data2)
```

---

### **Vysvetlenie jednotlivých krokov:**

1. **Vytvorenie datasetu** s hlavičkou.
2. **Pridanie viacerých riadkov** (študentov).
3. **Export do CSV** a uloženie na disk.
4. **Filtrovanie** podľa známky (len tí, čo majú známku 1).
5. **Triedenie** podľa veku.
6. **Načítanie CSV** naspäť do datasetu (overenie správnosti).

---

