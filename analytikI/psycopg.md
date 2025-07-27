# 🐘 Práca s PostgreSQL v Pythone pomocou knižnice **psycopg** (psycopg3)

## Čo je to psycopg?

**psycopg** (čítaj "saikopídži") je moderná knižnica na pripojenie Pythonu k databáze **PostgreSQL**.
Je to nasledovník populárnej knižnice psycopg2, ale je rýchlejší, modernejší a podporuje aj asynchrónne pripojenie.

---

## Inštalácia

Nainštaluješ cez pip (pozor, **balík sa volá `psycopg`**):

```
pip install psycopg
```

---

## Základné použitie

### Pripojenie k databáze

```python
import psycopg

# Pripojenie k databáze (zmeň si prihlasovacie údaje podľa seba)
conn = psycopg.connect("host=localhost dbname=mojadb user=moje_meno password=moje_heslo")
```

### Vykonanie SQL príkazu

```python
with conn.cursor() as cur:
    cur.execute("SELECT * FROM produkty;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
```

### Vkladanie údajov s parametrami

Používaj **%s** ako placeholdery pre hodnoty:

```python
nazov = "chlieb"
pocet = 10
cena = 2.99

with conn.cursor() as cur:
    cur.execute(
        "INSERT INTO produkty (nazov, pocet, cena) VALUES (%s, %s, %s);",
        (nazov, pocet, cena)
    )
    conn.commit()
```

> **Poznámka:** Vďaka `with` sa kurzor vždy korektne uzavrie.

---

## Context manager (správa spojenia)

Najčastejší spôsob použitia je cez **with** bloky – spojenie aj kurzor sa automaticky uzavrú:

```python
import psycopg

with psycopg.connect("dbname=mojadb user=moje_meno password=moje_heslo") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM produkty;")
        for row in cur.fetchall():
            print(row)
    # Tu sa kurzor uzavrie
# Tu sa spojenie uzavrie
```

---

## Čítanie údajov do slovníka

Ak chceš pristupovať k výsledkom cez názvy stĺpcov, môžeš použiť špeciálny kurzor:

```python
import psycopg

with psycopg.connect("dbname=mojadb user=moje_meno password=moje_heslo") as conn:
    with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
        cur.execute("SELECT * FROM produkty;")
        for row in cur.fetchall():
            print(row["nazov"], row["cena"])
```

---

## Príklad – INSERT, SELECT a UPDATE

```python
import psycopg

with psycopg.connect("dbname=mojadb user=moje_meno password=moje_heslo") as conn:
    with conn.cursor() as cur:
        # Pridanie nového produktu
        cur.execute(
            "INSERT INTO produkty (nazov, pocet, cena) VALUES (%s, %s, %s);",
            ("mlieko", 20, 1.59)
        )
        conn.commit()

        # Zmena počtu produktov
        cur.execute(
            "UPDATE produkty SET pocet = %s WHERE nazov = %s;",
            (25, "mlieko")
        )
        conn.commit()

        # Výber všetkých produktov
        cur.execute("SELECT * FROM produkty;")
        for row in cur.fetchall():
            print(row)
```

---

## Asynchrónne pripojenie (pokročilé)

psycopg podporuje aj async/await prístup – užitočné v moderných webových aplikáciách.

```python
import asyncio
import psycopg

async def main():
    async with await psycopg.AsyncConnection.connect("dbname=mojadb user=moje_meno password=moje_heslo") as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM produkty;")
            rows = await cur.fetchall()
            print(rows)

asyncio.run(main())
```

---

## Najčastejšie chyby

* **Zabudnutý commit:** Pri vkladaní, úpravách alebo mazaní treba zavolať `conn.commit()`.
* **Zabudnuté uzavretie spojenia:** Používaj `with` bloky, automaticky uzavrú kurzor aj spojenie.
* **Použitie zlých placeholderov:** Vždy používaj `%s`, nie `?` alebo `%d` (aj pre čísla!).

---

## Zhrnutie

* psycopg (psycopg3) je moderný spôsob prístupu na PostgreSQL v Pythone.
* Vieš jednoducho robiť výbery, vkladať, aktualizovať a mazať údaje.
* Oplatí sa používať context managery (`with`), ktoré sa postarajú o správu zdrojov.
* Placeholder na všetky hodnoty v SQL je vždy `%s`.

