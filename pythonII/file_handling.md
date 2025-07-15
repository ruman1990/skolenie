---

# 🗂️ Python – Práca so súbormi (File Handling)

Práca so súbormi je dôležitou súčasťou mnohých aplikácií. Python poskytuje funkcie na **vytváranie**, **čítanie**, **aktualizáciu** aj **mazanie súborov**.

---

## Základ: funkcia `open()`

Kľúčovou funkciou je `open()`, ktorá otvára súbor.
Prijíma dva parametre: **nazov súboru** a **režim**.

### Režimy:

* `"r"` – čítanie (default). Vyvolá chybu, ak súbor neexistuje
* `"a"` – pridávanie. Vytvorí súbor, ak neexistuje
* `"w"` – zápis. Vymaže obsah alebo vytvorí nový súbor
* `"x"` – vytvorenie. Vyvolá chybu, ak súbor už existuje

Ďalej možno určiť režim textu alebo binárny:

* `"t"` – textový režim (predvolené)
* `"b"` – binárny režim (napr. pre obrázky) 

---

## Syntax

Na otvorenie súboru pre čítanie stačí:

```python
f = open("demofile.txt")
```

To je rovnaké ako:

```python
f = open("demofile.txt", "rt")
```

Keďže `"r"` a `"t"` sú predvolené, netreba ich explicitne uvádzať.

> Upozornenie: Súbor musí existovať, inak dostaneš chybu. 

---

## Ďalšie operácie so súbormi


* **Čítanie** – napr. `read()`, `readline()`, `readlines()`
* **Zápis** – `write()` a `writelines()`
* **Zatvorenie** súboru pomocou `close()`
* Použitie **`with open(...) as f`**, čo automaticky zatvorí súbor
* **Odstránenie súboru** pomocou modulu `os` (`os.remove()`)
