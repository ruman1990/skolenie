# 🧩 Moduly `argparse` a `rich` v Pythone

---

## 📌 1. `argparse` – spracovanie argumentov z príkazového riadku

### 🔍 Čo je `argparse`?

`argparse` je **štandardný Python modul**, ktorý umožňuje:

* prijímať argumenty z príkazového riadku,
* overovať ich a spracovať,
* automaticky generovať pomocný text (`--help`).

---

### ✅ Príklad – jednoduché argumenty

```python
import argparse

parser = argparse.ArgumentParser(description="Ukážka s argparse")
parser.add_argument("--meno", help="Vaše meno")
parser.add_argument("--vek", type=int, help="Váš vek")

args = parser.parse_args()

print(f"Ahoj, {args.meno}. Máš {args.vek} rokov.")
```

#### Spustenie:

```bash
python skript.py --meno Jana --vek 25
```

---

### ⚙️ Typy argumentov

| Typ                   | Použitie                       |
| --------------------- | ------------------------------ |
| `required=True`       | Argument je povinný            |
| `type=int`            | Premení hodnotu na celé číslo  |
| `choices=[…]`         | Obmedzí výber na dané možnosti |
| `action='store_true'` | Prepínač (boolean flag)        |

---

### 🆘 Automatická nápoveda

Spustením:

```bash
python skript.py --help
```

Dostaneš automaticky vygenerovaný prehľad argumentov.

---

## 🎨 2. `rich` – farebný a pekný výstup do terminálu

### 🔍 Čo je `rich`?

`rich` je externá knižnica (inštaluje sa cez `pip install rich`), ktorá umožňuje:

* farebný text,
* štýlové logovanie,
* tabuľky, panely, markdown,
* progress bary, stromy a iné vizuálne prvky v termináli.

---

### ✅ Základný farebný výstup

```python
from rich import print

print("[bold green]Ahoj![/bold green] Toto je [blue]farebný[/blue] výstup.")
```

---

### 🧱 Použitie `Console` objektu

```python
from rich.console import Console

console = Console()
console.print("Toto je tučný červený text", style="bold red")
```

---

### 📊 Príklad: tabuľka

```python
from rich.table import Table
from rich.console import Console

table = Table(title="Zoznam študentov")
table.add_column("Meno", style="cyan")
table.add_column("Vek", justify="right")

table.add_row("Jana", "21")
table.add_row("Boris", "25")

Console().print(table)
```

---

### 📝 Príklad: progress bar

```python
from time import sleep
from rich.progress import track

for krok in track(range(10), description="Spracovávam..."):
    sleep(0.3)
```

---

## 🧪 BONUS: `argparse` + `rich` spolu

```python
import argparse
from rich import print

parser = argparse.ArgumentParser()
parser.add_argument("--meno")
args = parser.parse_args()

print(f"[bold cyan]Ahoj, {args.meno}![/bold cyan]")
```

---

## 🔚 Zhrnutie

| Modul      | Účel                         | Inštalácia         |
| ---------- | ---------------------------- | ------------------ |
| `argparse` | Spracovanie CLI argumentov   | Nie, v jadre       |
| `rich`     | Vizuálny výstup do terminálu | `pip install rich` |

