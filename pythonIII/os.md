# Modul `os` v Pythone

## Teória

Modul **`os`** je štandardnou súčasťou jazyka Python a poskytuje rozhranie na komunikáciu s **operačným systémom**. Pomocou tohto modulu môžeme pracovať so súbormi a adresármi (zložkami), zisťovať informácie o systéme, meniť práva súborov, nastavovať premenné prostredia a podobne.

**`os`** nám umožňuje robiť tieto činnosti:

* Zisťovať a meniť aktuálny pracovný adresár
* Vytvárať, premenovávať, mazať súbory a adresáre
* Pracovať s cestami k súborom (v spolupráci s modulom `os.path`)
* Získavať informácie o súboroch a adresároch
* Spúšťať iné programy a príkazy operačného systému

Modul je multiplatformný – funguje na Windows, Linuxe aj macOS.

---

## Základné funkcie modulu `os`

| Funkcia                        | Popis                                                 |
| ------------------------------ | ----------------------------------------------------- |
| `os.getcwd()`                  | Zistí aktuálny pracovný adresár                       |
| `os.chdir(cesta)`              | Zmení aktuálny pracovný adresár                       |
| `os.listdir(cesta)`            | Vráti zoznam súborov a adresárov v zadanom adresári   |
| `os.mkdir(cesta)`              | Vytvorí nový adresár                                  |
| `os.makedirs(cesta)`           | Vytvorí všetky potrebné adresáre v ceste (aj vnorené) |
| `os.remove(súbor)`             | Zmaže súbor                                           |
| `os.rmdir(adresár)`            | Zmaže prázdny adresár                                 |
| `os.rename(starý, nový)`       | Premenuje súbor alebo adresár                         |
| `os.path.join(cesta1, cesta2)` | Spojí časti cesty správne podľa systému               |
| `os.path.exists(cesta)`        | Skontroluje, či cesta existuje                        |
| `os.path.isfile(cesta)`        | Skontroluje, či ide o súbor                           |
| `os.path.isdir(cesta)`         | Skontroluje, či ide o adresár                         |

---

## Praktické príklady

### 1. Zistenie aktuálneho adresára

```python
import os

print(os.getcwd())
```

**Výstup:**
Zobrazí aktuálny adresár, v ktorom sa program nachádza.

---

### 2. Zmena pracovného adresára

```python
import os

os.chdir('C:/Users/Student/Documents')
print(os.getcwd())
```

---

### 3. Zoznam súborov v adresári

```python
import os

soubory = os.listdir('.')
for s in soubory:
    print(s)
```

Zobrazí všetky súbory a priečinky v aktuálnom adresári.

---

### 4. Vytvorenie nového adresára

```python
import os

os.mkdir('novy_adresar')
```

---

### 5. Vymazanie súboru a adresára

```python
import os

os.remove('test.txt')      # vymaže súbor
os.rmdir('novy_adresar')   # vymaže prázdny adresár
```

Pozor: Ak adresár nie je prázdny, použite `os.removedirs` alebo knižnicu `shutil`.

---

### 6. Práca s cestami

Používajte `os.path.join` pre správne vytváranie ciest (funguje na všetkých operačných systémoch):

```python
import os

cesta = os.path.join('data', 'subor.txt')
print(cesta)  # napr. 'data/subor.txt'
```

---

### 7. Kontrola existencie súboru alebo adresára

```python
import os

print(os.path.exists('data'))      # True/False
print(os.path.isfile('data.txt'))  # True/False
print(os.path.isdir('data'))       # True/False
```

---

### 8. Premenovanie súboru alebo adresára

```python
import os

os.rename('stary.txt', 'novy.txt')
```

---

### 9. Získanie veľkosti súboru (v bajtoch)

```python
import os

velkost = os.path.getsize('data.txt')
print(velkost)
```

---

## Dôležité poznámky

* Pri práci so súbormi odporúčame overovať existenciu súboru/adresára (`os.path.exists`).
* Na mazaie neprázdnych adresárov použite knižnicu **`shutil`** a funkciu `shutil.rmtree`.
* Pri tvorbe a manipulácii s cestami vždy používajte **`os.path.join`** pre multiplatformnosť.
* Modul `os` obsahuje aj funkcie na prácu s procesmi, premennými prostredia a iné (viac v dokumentácii).

---

## Zhrnutie

* Modul **`os`** je základný nástroj pre komunikáciu Pythona s operačným systémom.
* Pomáha spravovať súbory, adresáre a pracovať s cestami multiplatformne.
* Pri práci s cestami používajte vždy `os.path.join`, aby bol váš kód funkčný na Windowse aj Linuxe.
* Väčšina funkcií z modulu `os` je jednoduchá na použitie a veľmi užitočná pre automatizáciu, skripty a správu dát.
