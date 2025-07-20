# Modul `sqlite3` v Pythone

## Teória

**SQLite** je veľmi rozšírená, jednoduchá a rýchla databáza uložená v **jedinom súbore**.
Vhodná je na malé a stredne veľké aplikácie, učenie sa SQL, vývoj desktopových a mobilných aplikácií, prototypovanie, evidenciu dát a pod.

* **`sqlite3`** je vstavaný modul v Pythone (netreba nič inštalovať!)
* Umožňuje vytvárať, čítať, upravovať a mazať databázy cez SQL príkazy priamo zo skriptu.
* SQLite je **bez servera** – nepotrebujete žiadne špeciálne nastavenie databázového servera.
* Každá databáza je jeden obyčajný súbor (napr. `data.db`).

---

## Základné pojmy

* **Databáza** – súbor so všetkými tabuľkami, dátami, indexmi atď.
* **Tabuľka** – základná štruktúra na ukladanie údajov (riadky a stĺpce, ako v Exceli).
* **SQL** – jazyk na prácu s databázou (SELECT, INSERT, UPDATE, DELETE...).

---

## Základné použitie v Pythone

### 1. Pripojenie k databáze

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')  # Vytvorí (alebo otvorí) súbor mojadb.db
```

### 2. Vytvorenie tabuľky

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS osoby (
    id INTEGER PRIMARY KEY,
    meno TEXT,
    vek INTEGER
)
''')

conn.commit()  # Uloženie zmien
conn.close()
```

---

### 3. Vkladanie údajov

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.execute("INSERT INTO osoby (meno, vek) VALUES (?, ?)", ("Anna", 25))
c.execute("INSERT INTO osoby (meno, vek) VALUES (?, ?)", ("Peter", 31))
conn.commit()
conn.close()
```

> **Poznámka:** **Používajte zástupné znaky `?`** – chráni vás to pred SQL injection!

---

### 4. Výber (čítanie) údajov

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.execute("SELECT * FROM osoby")
vysledky = c.fetchall()

for riadok in vysledky:
    print(riadok)  # napr. (1, 'Anna', 25)

conn.close()
```

---

### 5. Aktualizácia údajov

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.execute("UPDATE osoby SET vek = ? WHERE meno = ?", (26, "Anna"))
conn.commit()
conn.close()
```

---

### 6. Vymazanie údajov

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.execute("DELETE FROM osoby WHERE meno = ?", ("Peter",))
conn.commit()
conn.close()
```

---

### 7. Vymazanie tabuľky alebo databázy

* Tabuľku zmažete SQL príkazom:

  ```python
  c.execute("DROP TABLE IF EXISTS osoby")
  ```
* Databázu (súbor) zmažete ako bežný súbor v Pythone cez modul `os` alebo `pathlib`.

---

### 8. Práca s viacerými záznamami naraz

```python
import sqlite3

osoby = [
    ("Jana", 22),
    ("Martin", 29),
    ("Eva", 24)
]

conn = sqlite3.connect('mojadb.db')
c = conn.cursor()

c.executemany("INSERT INTO osoby (meno, vek) VALUES (?, ?)", osoby)
conn.commit()
conn.close()
```

---

### 9. Práca so slovníkovými riadkami

Ak chcete priamo pracovať so slovníkmi namiesto tuple, nastavte **row\_factory**:

```python
import sqlite3

conn = sqlite3.connect('mojadb.db')
conn.row_factory = sqlite3.Row  # Teraz sa riadky správajú ako slovníky

c = conn.cursor()
c.execute("SELECT * FROM osoby")
for riadok in c.fetchall():
    print(riadok["meno"], riadok["vek"])

conn.close()
```

---

## Užitočné rady

* Vždy volajte `commit()`, keď meníte dáta (INSERT, UPDATE, DELETE).
* Po skončení prácu zatvorte databázu `close()`.
* Príkazy píšte vždy ako **reťazce s otáznikmi** a hodnoty ako tuple/list (kvôli bezpečnosti).
* **SQLite je skvelý na učenie a prototypovanie, ale nie je vhodný pre veľké webové aplikácie s mnohými užívateľmi.**

---

## Zhrnutie

* Modul `sqlite3` umožňuje prácu s SQL databázou bez inštalácie servera.
* Práca s databázou prebieha cez: pripojenie → kurzor → SQL príkaz → commit → zatvorenie.
* Všetko, čo platí pre SQL, platí aj pre SQLite (SELECT, WHERE, JOIN, GROUP BY...).
* V Pythone môžete pohodlne vkladať, čítať, meniť aj mazať dáta.

---

## 1. Práca s viacerými tabuľkami a vzťahom (cudzí kľúč, JOIN)

Predstavme si evidenciu zamestnancov a ich oddelení:

```python
import sqlite3

conn = sqlite3.connect('firma.db')
c = conn.cursor()

# Vytvorenie tabuliek s väzbou cez foreign key
c.execute('PRAGMA foreign_keys = ON')
c.execute('''
CREATE TABLE IF NOT EXISTS oddelenie (
    id INTEGER PRIMARY KEY,
    nazov TEXT
)
''')
c.execute('''
CREATE TABLE IF NOT EXISTS zamestnanec (
    id INTEGER PRIMARY KEY,
    meno TEXT,
    oddelenie_id INTEGER,
    plat INTEGER,
    FOREIGN KEY(oddelenie_id) REFERENCES oddelenie(id)
)
''')

# Vloženie oddelení
c.executemany('INSERT INTO oddelenie (nazov) VALUES (?)', [
    ('IT',), ('Personalistika',), ('Marketing',)
])

# Vloženie zamestnancov
c.executemany('INSERT INTO zamestnanec (meno, oddelenie_id, plat) VALUES (?, ?, ?)', [
    ('Anna', 1, 1200),
    ('Peter', 1, 1500),
    ('Jana', 2, 1100),
    ('Eva', 3, 1050),
    ('Martin', 2, 2000)
])

conn.commit()
```

**Výber zamestnancov spolu s názvom oddelenia:**

```python
c.execute('''
SELECT zamestnanec.meno, oddelenie.nazov, zamestnanec.plat
FROM zamestnanec
JOIN oddelenie ON zamestnanec.oddelenie_id = oddelenie.id
''')

for r in c.fetchall():
    print(r)
# napr.: ('Anna', 'IT', 1200)
```

---

## 2. Agregácia a zoskupovanie (GROUP BY, AVG, MAX)

**Priemerný plat podľa oddelení:**

```python
c.execute('''
SELECT oddelenie.nazov, AVG(zamestnanec.plat) as priemerny_plat
FROM zamestnanec
JOIN oddelenie ON zamestnanec.oddelenie_id = oddelenie.id
GROUP BY oddelenie.nazov
''')

for r in c.fetchall():
    print(r)
# napr.: ('IT', 1350.0)
```

**Najvyšší plat v oddelení:**

```python
c.execute('''
SELECT oddelenie.nazov, MAX(zamestnanec.plat)
FROM zamestnanec
JOIN oddelenie ON zamestnanec.oddelenie_id = oddelenie.id
GROUP BY oddelenie.nazov
''')

for r in c.fetchall():
    print(r)
```

---

## 3. Vyhľadávanie s podmienkami (LIKE, BETWEEN)

**Vyhľadaj zamestnancov, ktorí majú meno začínajúce na 'A':**

```python
c.execute("SELECT meno FROM zamestnanec WHERE meno LIKE 'A%'")
for r in c.fetchall():
    print(r)
```

**Zamestnanci s platom medzi 1100 a 1600:**

```python
c.execute("SELECT meno, plat FROM zamestnanec WHERE plat BETWEEN 1100 AND 1600")
for r in c.fetchall():
    print(r)
```

---

## 4. Transakcie a spracovanie chýb (ROLLBACK)

**Použitie transakcie a rollback pri chybe:**

```python
try:
    conn = sqlite3.connect('firma.db')
    c = conn.cursor()
    conn.execute('BEGIN')  # začiatok transakcie

    # Nejaký hromadný update
    c.execute("UPDATE zamestnanec SET plat = plat + 100 WHERE oddelenie_id = 1")
    # Chybný SQL príkaz (napr. pre ukážku)
    c.execute("UPDATE zamestnanec SET plat = plat + 'test' WHERE id = 1")

    conn.commit()
except Exception as e:
    print("Chyba:", e)
    conn.rollback()
finally:
    conn.close()
```

---

## 5. Poddotazy (subquery)

**Zamestnanci s platom väčším ako priemerný plat vo svojom oddelení:**

```python
c.execute('''
SELECT z.meno, z.plat, o.nazov
FROM zamestnanec z
JOIN oddelenie o ON z.oddelenie_id = o.id
WHERE z.plat > (
    SELECT AVG(plat)
    FROM zamestnanec
    WHERE oddelenie_id = z.oddelenie_id
)
''')
for r in c.fetchall():
    print(r)
```

---

## 7. Pridanie unikátneho obmedzenia (UNIQUE)

**Tabuľka, kde každé meno je jedinečné:**

```python
c.execute('''
CREATE TABLE IF NOT EXISTS uzivatel (
    id INTEGER PRIMARY KEY,
    meno TEXT UNIQUE,
    heslo TEXT
)
''')
```

Ak sa pokúsite vložiť meno, ktoré už v tabuľke je, vyhodí sa výnimka.



---

```python

import sqlite3

# 1. Otvor spojenie
conn = sqlite3.connect(":memory:")  # alebo 'mojabaza.db'

# 2. Definuj Python funkciu
def moj_pocet_znakov(text):
    if text is None:
        return 0
    return len(text)

# 3. Registruj ju do SQLite
conn.create_function("MOJLEN", 1, moj_pocet_znakov)

# 4. Príklad použitia v SQL dotaze
c = conn.cursor()
c.execute("SELECT MOJLEN('ahoj svet')")
print(c.fetchone()[0])  # Výstup: 9

# 5. Vieš ju používať aj na tabuľkách:
c.execute("CREATE TABLE test(text TEXT)")
c.execute("INSERT INTO test VALUES ('abcde')")
c.execute("SELECT text, MOJLEN(text) FROM test")
print(c.fetchall())  # Výstup: [('abcde', 5)]

conn.close()
```
