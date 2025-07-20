# Virtuálne prostredia v Pythone

## Prečo používať virtuálne prostredia?

### Výhody virtuálnych prostredí:

* **Oddelenie závislostí:** Každý projekt môže mať svoje vlastné knižnice a verzie (nie je konflikt s inými projektami).
* **Bezpečnosť:** Aktualizácia alebo odinštalovanie balíka v jednom projekte neovplyvní ostatné projekty ani systémový Python.
* **Jednoduchá správa projektov:** Viete presne, aké balíky váš projekt používa (cez `requirements.txt`).
* **Testovanie rôznych verzií knižníc:** Môžete skúšať nové verzie knižníc bez rizika, že rozbijete iné projekty.
* **Lepšia prenositeľnosť:** Projekt s vlastným zoznamom závislostí ľahko spustíte na inom počítači či serveri.

Virtuálne prostredie je teda **izolovaný „mini-Python“** s vlastnými knižnicami, oddelený od systémového Pythona.

---

## Modul `venv` – Tvorba virtuálneho prostredia

Python od verzie 3.3 obsahuje vstavaný modul **`venv`** na tvorbu virtuálnych prostredí.

### Ako vytvoriť nové virtuálne prostredie:

1. **Vytvorenie prostredia:**

   ```bash
   python -m venv myenv
   ```

   Toto vytvorí adresár `myenv` s vlastnou kópiou Pythona a prázdnou sadou knižníc.

2. **Aktivácia prostredia:**

   * **Windows:**

     ```bash
     myenv\Scripts\activate
     ```
   * **Linux/macOS:**

     ```bash
     source myenv/bin/activate
     ```

   Po aktivácii by ste mali vidieť v príkazovom riadku predponu `(myenv)`.

3. **Deaktivácia prostredia:**

   ```bash
   deactivate
   ```

---

## Manažér balíkov `pip`

**`pip`** je oficiálny správca balíkov pre Python.
Používa sa na **inštaláciu, odinštalovanie a aktualizáciu knižníc** z [PyPI](https://pypi.org).

### Základné príkazy:

* **Inštalácia balíka:**

  ```bash
  pip install numpy
  ```

* **Zoznam nainštalovaných balíkov:**

  ```bash
  pip list
  ```

* **Odinštalovanie balíka:**

  ```bash
  pip uninstall numpy
  ```

* **Vypísanie všetkých závislostí do súboru:**

  ```bash
  pip freeze > requirements.txt
  ```

* **Inštalácia podľa requirements.txt:**

  ```bash
  pip install -r requirements.txt
  ```

> **Pozor:** Vždy používajte pip až po aktivácii virtuálneho prostredia – inštalované knižnice budú len v tomto prostredí, nie v celom systéme!

---

## Typický workflow s virtuálnym prostredím

1. **Vytvoríš projekt a nové prostredie:**

   ```bash
   python -m venv venv
   ```
2. **Aktivuješ prostredie:**

   ```bash
   source venv/bin/activate  # Linux/mac
   # alebo
   venv\Scripts\activate     # Windows
   ```
3. **Inštaluješ knižnice cez pip:**

   ```bash
   pip install requests flask
   ```
4. **Vygeneruješ requirements.txt:**

   ```bash
   pip freeze > requirements.txt
   ```
5. **Deaktivuješ prostredie, keď už nepotrebuješ pracovať:**

   ```bash
   deactivate
   ```

---

## Zhrnutie

* **Virtuálne prostredie** je izolované prostredie pre každý projekt so samostatnými knižnicami.
* Vytvára sa cez modul **`venv`** (vstavaný v Pythone).
* **`pip`** slúži na správu balíkov (inštalácia, export, update...).
* Vďaka virtuálnym prostrediam sa vyhnete konfliktom medzi projektmi a zjednodušíte si vývoj aj prenositeľnosť kódu.
