postgre server - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads


pgadmin - https://www.postgresql.org/ftp/pgadmin/pgadmin4/v9.6/windows/




# 🐘 `psycopg2` – Práca s PostgreSQL v Pythone

---

## 🔍 Čo je `psycopg2`?

`psycopg2` je **najpoužívanejšia knižnica** pre komunikáciu medzi Python aplikáciou a databázou **PostgreSQL**.

Umožňuje:

* pripojiť sa k databáze,
* vykonávať SQL dotazy,
* čítať a zapisovať dáta,
* spravovať transakcie.

---

## 🧰 Inštalácia

```bash
pip install psycopg2-binary
```

> 🛠️ Odporúča sa používať `psycopg2-binary`, najmä pre jednoduché použitie a menšie projekty.

---

## 🔗 Pripojenie k databáze

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="moja_databaza",
    user="postgres",
    password="tajneheslo"
)

cur = conn.cursor()
```

---

## ✅ Vykonanie SQL dotazu

### Vytvorenie tabuľky:

```python
cur.execute("""
    CREATE TABLE IF NOT EXISTS studenti (
        id SERIAL PRIMARY KEY,
        meno TEXT,
        vek INTEGER
    )
""")
conn.commit()
```

---

### Vloženie dát:

```python
cur.execute("INSERT INTO studenti (meno, vek) VALUES (%s, %s)", ("Jana", 22))
conn.commit()
```

---

### Načítanie dát:

```python
cur.execute("SELECT * FROM studenti")
rows = cur.fetchall()

for row in rows:
    print(row)
```

---

## 🧪 Bezpečné parametre

Používaj **`%s` + tuplové hodnoty**, aby si zabránil SQL injekcii:

```python
meno = "Boris"
cur.execute("SELECT * FROM studenti WHERE meno = %s", (meno,))
```

---

## 🔁 Iterovanie cez výsledky

```python
for row in cur:
    print(f"{row[1]} má {row[2]} rokov")
```

---

## 🧼 Ukončenie spojenia

Na konci nezabudni zavrieť spojenie:

```python
cur.close()
conn.close()
```

---

## 🔄 Transakcie a rollback

Ak dôjde k chybe, môžeš zrušiť operáciu:

```python
try:
    cur.execute("NEEXISTUJUCIA SQL")
    conn.commit()
except Exception as e:
    print("Chyba:", e)
    conn.rollback()
```

---

## 🗂️ Príklady použitia

| Úloha                      | Príkaz                              |
| -------------------------- | ----------------------------------- |
| Pripojenie k DB            | `psycopg2.connect(...)`             |
| Vykonanie dotazu           | `cur.execute(sql, params)`          |
| Načítanie všetkých riadkov | `cur.fetchall()`                    |
| Pridanie riadka            | `INSERT INTO ...` a `conn.commit()` |
| Zatvorenie spojenia        | `cur.close()`, `conn.close()`       |

---

## 🛡️ Tipy na bezpečnosť

* **Nikdy nespájaj SQL reťazce manuálne** – použi parametre!
* **Zachytávaj výnimky** (`try-except`)
* **Používaj `with` bloky** (viď nižšie)

---

## 🔁 Moderný zápis pomocou `with`

```python
import psycopg2

with psycopg2.connect(...) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM studenti")
        print(cur.fetchall())
```

---

## 📚 Zhrnutie

`psycopg2` ti umožní jednoducho prepojiť Python aplikáciu s PostgreSQL databázou. Vieš cez ňu:

* pripojiť sa k databáze,
* spúšťať SQL príkazy,
* manipulovať s údajmi,
* bezpečne pracovať s transakciami.

---
