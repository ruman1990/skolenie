# Modul `pathlib` v Pythone

## Teória

**`pathlib`** je moderný modul v Pythone (od verzie 3.4), ktorý poskytuje objektovo orientovaný spôsob práce so súbormi a cestami k súborom a adresárom.
Je to alternatíva ku klasickým modulom ako `os`, `os.path` alebo `glob`, ale s oveľa jednoduchším, prehľadnejším a intuitívnejším rozhraním.

Hlavná výhoda `pathlib`:

* Namiesto prác s cestami ako so „stringmi“ (reťazcami) používate špeciálne **objekty typu `Path`**, ktoré majú mnoho metód na prácu so súbormi, adresármi, cestami, hľadaním a manipuláciou s nimi.
* `pathlib` automaticky rieši rozdiely medzi Windows a Linux cestami.

---

## Základná práca s `Path`

### Importovanie a vytvorenie cesty

```python
from pathlib import Path

cesta = Path('subor.txt')  # relatívna cesta
absolutna = Path('/home/student/dokumenty')  # absolútna cesta (Linux)
```

Na Windows sa absolutná cesta zapíše napr. `Path("C:/Users/Meno/Desktop")`.

---

### Najdôležitejšie metódy a vlastnosti

| Metóda/vlastnosť     | Popis                                                 |
| -------------------- | ----------------------------------------------------- |
| `Path.cwd()`         | Aktuálny pracovný adresár                             |
| `Path.home()`        | Domovský adresár používateľa                          |
| `Path.iterdir()`     | Iteruje cez obsah adresára                            |
| `Path.exists()`      | Skontroluje existenciu cesty                          |
| `Path.is_file()`     | Je to súbor?                                          |
| `Path.is_dir()`      | Je to adresár?                                        |
| `Path.mkdir()`       | Vytvorenie adresára                                   |
| `Path.unlink()`      | Vymazanie súboru                                      |
| `Path.rmdir()`       | Vymazanie adresára                                    |
| `Path.rename()`      | Premenovanie súboru alebo adresára                    |
| `Path.read_text()`   | Prečíta textový súbor                                 |
| `Path.write_text()`  | Zapíše text do súboru                                 |
| `Path.read_bytes()`  | Prečíta binárny súbor                                 |
| `Path.write_bytes()` | Zapíše binárny súbor                                  |
| `Path.glob('*.txt')` | Vyhľadá súbory podľa masky (napr. všetky .txt súbory) |
| `Path.parent`        | Nadradený adresár                                     |
| `Path.name`          | Názov súboru/adresára                                 |
| `Path.suffix`        | Prípona (napr. .txt)                                  |
| `Path.stem`          | Meno súboru bez prípony                               |

---

## Praktické príklady

### 1. Zistenie aktuálneho adresára

```python
from pathlib import Path

print(Path.cwd())
```

---

### 2. Zoznam všetkých súborov v adresári

```python
from pathlib import Path

adresar = Path('.')
for subor in adresar.iterdir():
    print(subor)
```

---

### 3. Vyhľadanie všetkých .txt súborov

```python
from pathlib import Path

for txt_subor in Path('.').glob('*.txt'):
    print(txt_subor)
```

---

### 4. Čítanie a zápis textového súboru

```python
from pathlib import Path

cesta = Path('test.txt')

# Zápis
cesta.write_text('Ahoj svet!', encoding='utf-8')

# Čítanie
obsah = cesta.read_text(encoding='utf-8')
print(obsah)
```

---

### 5. Kontrola, či súbor alebo adresár existuje

```python
from pathlib import Path

cesta = Path('data.txt')
if cesta.exists():
    print('Súbor existuje')
else:
    print('Súbor neexistuje')
```

---

### 6. Vytvorenie a mazanie adresára

```python
from pathlib import Path

novy_adresar = Path('moj_adresar')
novy_adresar.mkdir(exist_ok=True)  # exist_ok=True nespôsobí chybu, ak už existuje

# Mazanie
novy_adresar.rmdir()  # pozor, musí byť prázdny
```

---

### 7. Premenovanie súboru

```python
from pathlib import Path

p = Path('stary.txt')
p.rename('novy.txt')
```

---

### 8. Získanie mena, prípony a nadradeného adresára

```python
from pathlib import Path

cesta = Path('cesta/do/suboru.txt')
print(cesta.name)     # suboru.txt
print(cesta.suffix)   # .txt
print(cesta.stem)     # suboru
print(cesta.parent)   # cesta/do
```

---

### 9. Zreťazovanie ciest

S `Path` sa cesty jednoducho „spájajú“ cez `/`:

```python
from pathlib import Path

cesta = Path('data') / 'subory' / 'info.txt'
print(cesta)  # data/subory/info.txt
```

---

## Prečo používať pathlib?

* Jednoduchšie, bezpečnejšie a prehľadnejšie príkazy než s `os`/`os.path`.
* Kód je multiplatformný – nemusíte riešiť, či používate / alebo \ v ceste.
* Podpora moderných Python verzií.
* Lepšia čitateľnosť a menej chýb pri práci so súbormi.

---

## Zhrnutie

* **`pathlib`** je moderný modul na prácu s cestami, súbormi a adresármi v Pythone.
* Všetko sa robí cez objekt `Path` a jeho metódy/vlastnosti.
* Vďaka `pathlib` je kód čistejší a univerzálny pre všetky operačné systémy.