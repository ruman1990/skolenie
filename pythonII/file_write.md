

# 📝 Python – Zápis do súboru (File Write)

## Zápis do existujúceho súboru

Na zápis do existujúceho súboru potrebuješ zadať parameter do funkcie `open()`:

* `"a"` – append – pridá text na koniec súboru
* `"w"` – write – prepíše celý obsah súboru

### Príklad – príloha (append)

```python
# Pridaj text na koniec súboru demofile.txt
with open("demofile.txt", "a") as f:
    f.write("Now the file has more content!")

# Otvor a zobraz aktuálny obsah súboru
with open("demofile.txt") as f:
    print(f.read())
```

---

## Prepísanie celého obsahu súboru

Ak chceš prepísať celý obsah:

```python
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
    print(f.read())
```

> Parametr `"w"` **vymaže pôvodný obsah** a zapíše nový. 

---

## Vytvorenie nového súboru

Na vytvorenie nového súboru použi režimy:

* `"x"` – create – vytvorí nový súbor, ak už existuje, vyvolá chybu
* `"a"` – append – ak súbor neexistuje, vytvorí ho
* `"w"` – write – rovnako vytvorí súbor, ak neexistuje

### Príklad – vytvorenie súboru

```python
# Vytvorí nový, prázdny súbor myfile.txt; ak existuje, vyvolá chybu
f = open("myfile.txt", "x")
f.close()
```

> Režimy `"x"`, `"a"` a `"w"` môžu vytvoriť súbor, ak neexistuje. 

---

---

# 🗑️ Python – Odstraňovanie súborov

## Odstránenie súboru

Na odstránenie súboru treba importovať modul `os` a použiť jeho funkciu `os.remove()`.

### Príklad

```python
import os
os.remove("demofile.txt")
```

> Tento kód odstráni súbor `demofile.txt`. 

---

## Skontrolovanie existencie súboru

Ak si chceš byť istý, že súbor existuje pred jeho odstránením, použiješ `os.path.exists()`, aby si predišiel chybe.

### Príklad

```python
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("Súbor neexistuje.")
```

> Takto sa vyhneš chybe, ak súbor neexistuje.&#x20;

---

## Odstránenie priečinka

Na odstránenie **prázdneho priečinka** voľ `os.rmdir()`.

### Príklad

```python
import os
os.rmdir("myfolder")
```

> Odstráni prázdny priečinok `myfolder`.

> **Poznámka:** `os.rmdir()` zlyhá, ak je priečinok neprázdny.&#x20;

---
