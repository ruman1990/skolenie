# Modul `random` v Pythone

## Teória

Modul **`random`** poskytuje nástroje na generovanie **(pseudo)náhodných čísel** a miešanie/losovanie zo sekvencií (napr. zoznamov).
Používa sa v hrách, simuláciách, náhodných výberoch, testovaní, ale aj pri generovaní dát.

> **Pseudo-náhodné čísla** znamená, že čísla sú generované podľa určitého algoritmu a nie sú skutočne náhodné – ale pre väčšinu aplikácií sú dostatočne náhodné.

---

## Základné funkcie modulu `random`

| Funkcia                    | Popis                                                  |
| -------------------------- | ------------------------------------------------------ |
| `random.random()`          | Náhodné desatinné číslo od 0.0 do 1.0                  |
| `random.randint(a, b)`     | Náhodné celé číslo od a po b (vrátane)                 |
| `random.uniform(a, b)`     | Náhodné desatinné číslo z intervalu \[a, b]            |
| `random.choice(seq)`       | Náhodný prvok zo sekvencie (zoznam, reťazec, tuple)    |
| `random.choices(seq, k=n)` | Zoznam n náhodných prvkov zo sekvencie (s opakovaním)  |
| `random.shuffle(seq)`      | Náhodne premieša prvky v zozname (mení pôvodný zoznam) |
| `random.sample(seq, k)`    | Náhodný výber k prvkov bez opakovania                  |

---

### Príklady

```python
import random

print(random.random())        # 0.123456... (medzi 0 a 1)
print(random.randint(1, 10))  # napr. 7 (medzi 1 a 10)
print(random.uniform(5, 10))  # napr. 7.58 (desatinné číslo)
print(random.choice(['a', 'b', 'c']))  # napr. 'b'
print(random.choices([1, 2, 3, 4], k=3))  # napr. [2, 4, 2]
```

#### Premiešanie zoznamu

```python
zoznam = [1, 2, 3, 4, 5]
random.shuffle(zoznam)
print(zoznam)  # napr. [3, 1, 5, 2, 4]
```

#### Náhodný výber viacerých prvkov bez opakovania

```python
vyber = random.sample(range(1, 50), 6)
print(vyber)  # napr. [7, 21, 44, 10, 13, 38]
```

---

## Seed – opakovateľná náhodnosť

Na účely testovania môžeme nastaviť tzv. **seed** (počiatočné číslo), aby boli výsledky stále rovnaké:

```python
random.seed(42)
print(random.randint(1, 10))  # Výstup bude vždy rovnaký pre toto seed číslo
```

---

# Modul `secrets` v Pythone

## Teória

Modul **`secrets`** je určený na **generovanie kryptograficky bezpečných náhodných čísel**.
Používa sa tam, kde potrebujeme skutočnú náhodnosť a bezpečnosť – napríklad pri generovaní hesiel, tokenov, bezpečnostných kľúčov, PIN kódov, apod.

> Na rozdiel od modulu `random`, výsledky z `secrets` sa nedajú predvídať – preto je vhodný pre bezpečnostné účely!

---

## Základné funkcie modulu `secrets`

| Funkcia                    | Popis                                                    |
| -------------------------- | -------------------------------------------------------- |
| `secrets.randbelow(n)`     | Náhodné celé číslo od 0 do n-1                           |
| `secrets.choice(seq)`      | Bezpečný náhodný prvok zo sekvencie                      |
| `secrets.token_hex(n)`     | Náhodný hexadecimálny reťazec s dĺžkou 2n znakov         |
| `secrets.token_urlsafe(n)` | Bezpečný token vhodný do URL s dĺžkou približne n znakov |
| `secrets.token_bytes(n)`   | Náhodné bajty (bytes) danej dĺžky                        |

---

### Príklady

```python
import secrets

print(secrets.randbelow(10))      # číslo od 0 po 9
print(secrets.choice('abcdef'))   # napr. 'c'
print(secrets.token_hex(8))       # napr. 'a9f32b0a42e142e3'
print(secrets.token_urlsafe(12))  # napr. 'Qf8Sd-Jk8H2f6wL3k'
```

#### Bezpečné generovanie hesla (napr. pre používateľa)

```python
import secrets
import string

abeceda = string.ascii_letters + string.digits + "!@#$%^&*"
heslo = ''.join(secrets.choice(abeceda) for _ in range(12))
print(heslo)  # napr. 'b7V$u19@GwLs'
```

---

## Kedy použiť `random` a kedy `secrets`?

* **`random`** – na hry, simulácie, bežný náhodný výber, kde nejde o bezpečnosť.
* **`secrets`** – na heslá, tokeny, šifrovacie kľúče, kde musí byť výber NEPREDVÍDATEĽNÝ a bezpečný.

---

## Zhrnutie

* **`random`**: jednoduchý modul na náhodné čísla, miešanie, losovanie v bežných úlohách.
* **`secrets`**: bezpečný modul na generovanie náhodných údajov tam, kde je dôležitá bezpečnosť (heslá, tokeny).
* Vždy používajte **`secrets`** pri generovaní čohokoľvek, čo súvisí so zabezpečením a ochranou dát.
