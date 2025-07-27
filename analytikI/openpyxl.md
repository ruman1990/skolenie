### 🔍 Čo je `openpyxl`?

`openpyxl` je **knižnica na čítanie a zapisovanie súborov `.xlsx`** (Excel 2010 a novšie). Umožňuje manipulovať s **bunkami, hárkami, štýlmi, vzorcami, grafikou** a ďalšími funkciami Excelu.

---

## 🔧 Inštalácia

```bash
pip install openpyxl
```

---

## ✅ Základné použitie

### 1. 📂 Načítanie existujúceho Excel súboru

```python
from openpyxl import load_workbook

wb = load_workbook("subor.xlsx")
ws = wb.active  # alebo wb["Nazov_harka"]
print(ws["A1"].value)  # Výpis obsahu bunky A1
```

---

### 2. 📄 Vytvorenie nového Excel súboru

```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws["A1"] = "Meno"
ws["B1"] = "Vek"
ws.append(["Jana", 30])
ws.append(["Boris", 25])

wb.save("vystup.xlsx")
```

---

### 3. 🔄 Iterácia cez bunky

```python
for row in ws.iter_rows(min_row=2, values_only=True):
    meno, vek = row
    print(f"{meno} má {vek} rokov")
```

---

## 🎨 Štýlovanie buniek

```python
from openpyxl.styles import Font

ws["A1"].font = Font(bold=True, color="00FF00")
```

---

## ➕ Vzorce

```python
ws["C2"] = "=SUM(B2:B10)"
```

---

## 📑 Viacero hárkov

```python
ws2 = wb.create_sheet("NovyHark")
ws2["A1"] = "Dáta"
```

---

## 🧼 Praktické tipy

| Činnosť              | Ako na to                                   |
| -------------------- | ------------------------------------------- |
| Čítanie Excel súboru | `load_workbook("meno.xlsx")`                |
| Vytvorenie súboru    | `Workbook()` a `wb.save()`                  |
| Pridanie riadka      | `ws.append([hodnoty])`                      |
| Prístup k bunke      | `ws["B2"]` alebo `ws.cell(row=2, column=2)` |
| Iterácia cez dáta    | `iter_rows()`, `iter_cols()`                |
| Štýly, fonty         | `from openpyxl.styles import ...`           |

---

## 🚫 `openpyxl` NEpodporuje:

* staré `.xls` súbory (na to použi `xlrd` alebo `pandas`)
* pokročilú analýzu dát (na to použi `pandas`)
* prácu s veľkými Excel súbormi rýchlo (rieši `pandas` alebo `csv`)

---


**Excel report so štýlovanými dátami**:

1. Vytvárať nový Excel súbor
2. Zapisovať tabuľku údajov
3. Pridávať vzorec (súčet)
4. Používať štýly (tučný text, farebné bunky)
5. Ukladať súbor

---

## 🛠️ Scenár: „Report predaja“

Predstav si, že máš tieto dáta:

```python
data = [
    ["Produkt", "Cena", "Kusov"],
    ["Chleba", 1.50, 10],
    ["Mlieko", 0.90, 20],
    ["Maslo", 2.30, 5],
]
```

---

## 🧾 Kompletný kód:

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

# 1. Vytvorenie nového Excel súboru
wb = Workbook()
ws = wb.active
ws.title = "Report"

# 2. Dáta na zapísanie
data = [
    ["Produkt", "Cena", "Kusov"],
    ["Chleba", 1.50, 10],
    ["Mlieko", 0.90, 20],
    ["Maslo", 2.30, 5],
]

# 3. Zápis dát do hárku
for riadok in data:
    ws.append(riadok)

# 4. Výpočet celkovej sumy = cena * kusov
ws["D1"] = "Spolu (€)"
for row in range(2, ws.max_row + 1):
    ws[f"D{row}"] = f"=B{row}*C{row}"

# 5. Súčet všetkých hodnôt v stĺpci "Spolu"
last_row = ws.max_row + 1
ws[f"C{last_row}"] = "Suma spolu"
ws[f"D{last_row}"] = f"=SUM(D2:D{last_row-1})"

# 6. Štýlovanie hlavičky
for cell in ws[1]:
    cell.font = Font(bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")

# 7. Uloženie súboru
wb.save("report_predaja.xlsx")
```

---

## 📂 Výsledok:

* Vytvorený Excel súbor `report_predaja.xlsx`
* Hlavička má modré pozadie a biele písmo
* Vzorec v stĺpci „Spolu (€)“ počíta cenu × kusy
* Na konci je riadok so súčtom

---

## 📘 1. Čítanie a aktualizácia existujúceho Excel súboru

Predstav si, že máš súbor `produkty.xlsx` so stĺpcami:
`| Produkt | Cena | Kusov |`

### ✅ Cieľ:

* Otvoriť súbor
* Zmeniť cenu konkrétneho produktu
* Uložiť naspäť

### 🧾 Kód:

```python
from openpyxl import load_workbook

# Načítaj existujúci Excel
wb = load_workbook("produkty.xlsx")
ws = wb.active

# Nájdeme produkt a zmeníme cenu
for row in ws.iter_rows(min_row=2, values_only=False):
    if row[0].value == "Maslo":
        row[1].value = 2.99  # nová cena

# Uložíme späť
wb.save("produkty_aktualizovane.xlsx")
```

---

## 📋 2. Validácia dát – napr. záporný počet kusov

### ✅ Cieľ:

* Nájsť riadky s chybnými hodnotami (záporné kusy)
* Zvýrazniť ich červenou farbou

### 🧾 Kód:

```python
from openpyxl.styles import PatternFill

cervena = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
wb = load_workbook("produkty.xlsx")
ws = wb.active

for row in ws.iter_rows(min_row=2):
    kusov_cell = row[2]
    if isinstance(kusov_cell.value, int) and kusov_cell.value < 0:
        kusov_cell.fill = cervena  # farebné označenie chyby

wb.save("produkty_chybne.xlsx")
```

---

## 📆 3. Export reportu s názvom podľa dátumu

### ✅ Cieľ:

* Automaticky pomenovať Excel report podľa dnešného dátumu (napr. `report_2025-07-24.xlsx`)

### 🧾 Kód:

```python
from openpyxl import Workbook
from datetime import date

# Vytvorenie dát
wb = Workbook()
ws = wb.active
ws.append(["Dátum", "Hodnota"])
ws.append([str(date.today()), 123])

# Dynamický názov súboru
nazov = f"report_{date.today()}.xlsx"
wb.save(nazov)
```

---

# 📈 Príklad 1: Pridanie grafu do Excelu

### 🎯 Cieľ:

* Získať dáta o predaji
* Vypočítať hodnotu predaja (cena × kusy)
* Pridať **stĺpcový graf (bar chart)**

---

### 🧾 Kód:

```python
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

wb = Workbook()
ws = wb.active
ws.title = "Predaj"

# 1. Dáta
ws.append(["Produkt", "Cena", "Kusov", "Spolu (€)"])
produkty = [
    ["Chleba", 1.5, 10],
    ["Mlieko", 0.9, 20],
    ["Maslo", 2.3, 5],
]

# 2. Zápis dát a výpočet spolu
for produkt in produkty:
    cena, kusy = produkt[1], produkt[2]
    produkt.append(cena * kusy)
    ws.append(produkt)

# 3. Vytvorenie grafu
graf = BarChart()
graf.title = "Tržby podľa produktu"
graf.y_axis.title = "€"
graf.x_axis.title = "Produkt"

# 4. Určenie dát pre graf (iba stĺpec „Spolu €“)
data = Reference(ws, min_col=4, min_row=1, max_row=4)
kategorie = Reference(ws, min_col=1, min_row=2, max_row=4)

graf.add_data(data, titles_from_data=True)
graf.set_categories(kategorie)

# 5. Vloženie grafu
ws.add_chart(graf, "F2")

# 6. Uloženie súboru
wb.save("predaj_s_grafom.xlsx")
```

✅ Otvor súbor `predaj_s_grafom.xlsx` a nájdeš v ňom stĺpcový graf.

---

# 📂 Príklad 2: Načítanie CSV a export do Excelu

### 🎯 Cieľ:

* Načítať súbor `data.csv`
* Zapísať jeho obsah do Excelu
* Uložiť ako `data.xlsx`

---

### 🧾 CSV vstup (napr. `data.csv`):

```
Meno,Vek,Mesto
Jana,30,Bratislava
Boris,25,Košice
Eva,28,Zvolen
```

---

### 🧾 Kód:

```python
import csv
from openpyxl import Workbook

# 1. Načítanie CSV
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

# 2. Zápis do Excelu
wb = Workbook()
ws = wb.active
ws.title = "CSV dáta"

for row in rows:
    ws.append(row)

# 3. Uloženie
wb.save("data.xlsx")
```

✅ Výsledkom je súbor `data.xlsx` so všetkými údajmi z CSV.

---
