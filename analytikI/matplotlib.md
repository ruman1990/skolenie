## Matplotlib Pyplot

Najväčšina utilít z Matplotlib sa nachádza v podmodule `pyplot`, a obyčajne sa importuje pod aliasom `plt`:

```python
import matplotlib.pyplot as plt
```

Teraz môžeme balík Pyplot odkazovať ako `plt`.

### Príklad

Nakreslite čiaru v grafe od pozície (0,0) až po (6,250):

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

🖼️ Výsledok: graf zobrazuje čiaru medzi bodmi (0,0) a (6,250) ([w3schools.com][1])

---

### 📚 Poznámka

V ďalších kapitolách sa naučíte viac o kreslení (plotovaní) pomocou Matplotlib. ([w3schools.com][1])

---

## 📊 Matplotlib – Kreslenie (`plot`)

Funkcia `plot()` slúži na zobrazenie bodov (značiek) v diagrame.
Štandardne funkcia `plot()` vykreslí čiaru spájajúcu body.

Parametre:

1. Pole s hodnotami na osi x
2. Pole s hodnotami na osi y

Ak chceme nakresliť čiaru od (1, 3) po (8, 10), odošleme dve polia `[1, 8]` a `[3, 10]` do funkcie `plot()`.

### Príklad

Nakreslite čiaru v diagrame od pozície (1, 3) po (8, 10):

```python
import matplotlib.pyplot as plt  
import numpy as np  

xpoints = np.array([1, 8])  
ypoints = np.array([3, 10])  

plt.plot(xpoints, ypoints)  
plt.show()
```

Osa x je horizontálna a osa y vertikálna. ([W3Schools][1])

---

### 🟢 Kreslenie bez čiary – len značky

Ak chceme zobraziť iba značky (bodky), použijeme parameter `'o'`:

```python
plt.plot(xpoints, ypoints, 'o')
plt.show()
```

Toto zobrazí dva body bez spojovacej čiary. ([W3Schools][1])

---

### ➕ Viacero bodov

Ak máme viac bodov, stačí poskytnúť viac hodnôt:

```python
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```

---

### 🔢 Predvolené hodnoty osi x

Ak špecifikujeme iba hodnoty pre os y, os x bude automaticky `[0, 1, 2, ...]`:

```python
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
```

Osi x v tomto prípade sú `[0, 1, 2, 3, 4, 5]`. ([W3Schools][1])

---

## 🎛️ Viacero grafov v jednom okne – `subplot()`

Funkcia `subplot()` umožňuje nakresliť viacero grafov v jedinom obrázku.

### Príklad – 2 grafy vedľa seba:

```python
import matplotlib.pyplot as plt
import numpy as np

# Graf 1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x, y)

# Graf 2
y2 = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x, y2)

plt.show()
```

Tu je rozloženie: 1 riadok, 2 stĺpce, aktuálny graf je 1. a potom 2. ([W3Schools][2])

---

### ↕️ 2 grafy nad sebou:

Ak chceme jeden nad druhým:

```python
plt.subplot(2, 1, 1)  # 2 riadky, 1 stĺpec, prvý graf
plt.plot(x, y)

plt.subplot(2, 1, 2)  # druhý graf
plt.plot(x, y2)

plt.show()
```

---

### 📐 Užitočná voľnosť:

Pomocou `subplot(m, n, i)` môžeme vytvoriť ľubovoľné rozloženie, napr. 6 grafov v mriežke 2×3.

---

### 📝 Zhrnutie

* `plot()` – kreslenie čiar alebo bodov
* `'o'` – parameter na zobrazenie iba bodov
* Viacero grafov – `subplot(rows, cols, index)`
* Automatické x‑hody ak špecifikujeme len y hodnoty

---

## 📍 Markers

Môžeš použiť kľúčový argument `marker`, aby si **zvýraznil každý bod** určeným markerom:

### Príklad

Zvýraznenie každého bodu kruhom:

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker='o')
plt.show()
```

---

### 🌟 Príklad

Zvýraznenie každého bodu hviezdičkou:

```python
plt.plot(ypoints, marker='*')
plt.show()
```

---

## 📋 Referencia markerov

Môžeš si zvoliť niektorý z týchto markerov:

| Marker | Popis              |
| ------ | ------------------ |
| `o`    | Kruh               |
| `*`    | Hviezdička         |
| `.`    | Bodka              |
| `,`    | Pixel              |
| `x`    | Krížik             |
| `X`    | Vyplnený krížik    |
| `+`    | Plus               |
| `P`    | Vyplnený plus      |
| `s`    | Štvorec            |
| `D`    | Diamant            |
| `d`    | Tenký diamant      |
| `p`    | Pentagon           |
| `H`    | Hexagon            |
| `h`    | Hexagon            |
| `v`    | Trojuholník dolu   |
| `^`    | Trojuholník hore   |
| `<`    | Trojuholník vľavo  |
| `>`    | Trojuholník vpravo |
| `1`    | Tri dolu           |
| `2`    | Tri hore           |
| `3`    | Tri vľavo          |
| `4`    | Tri vpravo         |
| `\|`   | Vertikálna čiara   |
| `_`    | Horizontálna čiara |

---

## ✂️ Skrátený zápis (`fmt`)

Môžeš tiež použiť **skratkový formát** `marker|line|color`:

### Príklad

Zvýraznenie kruhmi, s bodkovanou čiarou, červenej farby:

```python
plt.plot(ypoints, 'o:r')
plt.show()
```

* `marker` – môže byť ktorýkoľvek z vyššie uvedených
* `line` – `-`, `:`, `--`, `-.`
* `color` – `r`, `g`, `b`, `c`, `m`, `y`, `k`, `w`

Poznámka: Ak vynecháš `line`, nebude zobrazená žiadna čiara.

---

## 🔧 Nastavenie veľkosti a farby markerov

* `markersize` alebo skrátene `ms` – veľkosť markera
* `markeredgecolor` alebo `mec` – farba okraja
* `markerfacecolor` alebo `mfc` – farba výplne

### Príklad – veľké kruhy:

```python
plt.plot(ypoints, marker='o', ms=20)
plt.show()
```

### Príklad – červený okraj:

```python
plt.plot(ypoints, marker='o', ms=20, mec='r')
plt.show()
```

### Príklad – červená výplň:

```python
plt.plot(ypoints, marker='o', ms=20, mfc='r')
plt.show()
```

### Príklad – celý marker červený:

```python
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
plt.show()
```

---

### 🎨 Použitie hex farieb alebo názvov

#### Príklad – zelený marker (#4CAF50):

```python
plt.plot(ypoints, marker='o', ms=20, mec='#4CAF50', mfc='#4CAF50')
plt.show()
```

#### Príklad – názov farby “hotpink”:

```python
plt.plot(ypoints, marker='o', ms=20, mec='hotpink', mfc='hotpink')
plt.show()
```
---

## 📉 Matplotlib – Štýl čiar (Line Styles)

Môžeš použiť kľúčový argument `linestyle`, alebo skrátene `ls`, na zmenu štýlu nakreslenej čiary:

### Príklad: bodkovaná čiara

```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle='dotted')
plt.show()
```

---

### Príklad: prerušovaná čiara

```python
plt.plot(ypoints, linestyle='dashed')
plt.show()
```

---

### 🔄 Skrátený zápis

Rovnaké výsledky dosiahneš kratšou syntaxou:

* `linestyle` → `ls`
* `'dotted'` → `':'`
* `'dashed'` → `'--'`

#### Príklad s krátkou syntaxou:

```python
plt.plot(ypoints, ls=':')
plt.show()
```

---

## 🎨 Dostupné štýly čiar

Môžeš zvoliť niektorý z týchto štýlov:

| Štýl                                 | Skratka          |
| ------------------------------------ | ---------------- |
| solid (štandardný)                   | `-`              |
| dotted (bodkovaná)                   | `:`              |
| dashed (prerušovaná)                 | `--`             |
| dashdot (čiara bod prerušovanie bod) | `-.`             |
| None (bez čiary)                     | `''` alebo `' '` |

---

## 🌈 Farba čiary

Na nastavenie farby čiary použij kľúčový argument `color`, alebo skrátene `c`:

```python
plt.plot(ypoints, color='r')
plt.show()
```

Môžeš tiež použiť hexadecimálne farby:

```python
plt.plot(ypoints, c='#4CAF50')
plt.show()
```

Alebo použiť jeden zo 140 podporovaných názvov farieb:

```python
plt.plot(ypoints, c='hotpink')
plt.show()
```

---

## 🔎 Šírka čiary

Na zmenu hrúbky čiary, použij `linewidth` (alebo skrátene `lw`), hodnota je desatinné číslo predstavujúce body:

```python
plt.plot(ypoints, linewidth=20.5)
plt.show()
```

---

## ➕ Viacero čiar v jednom grafe

Môžeš nakresliť viac čiar buď použitím viacerých `plt.plot()` volaní:

```python
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()
```

Alebo v jednom volaní buď poskytnutím viacerých polí:

```python
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
```

*(Ak zadáš len `y` hodnoty, os x bude automaticky `[0, 1, 2, ...]`)*

---

## 🏷️ Vytvorenie popiskov pre graf

Pomocou `xlabel()` a `ylabel()` z Pyplot môžeš nastaviť popisky pre os x a os y.

### Príklad

Pridaj popisky osi x a osi y:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Priemerný tep")
plt.ylabel("Spálené kalórie")

plt.show()
```

([W3Schools][1])

---

## 🎖️ Vytvorenie nadpisu grafu

Pomocou `title()` môžeš nastaviť nadpis grafu.

### Príklad

Pridaj nadpis a popisky osi x a osi y:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Údaje z športových hodiniek")
plt.xlabel("Priemerný tep")
plt.ylabel("Spálené kalórie")

plt.show()
```

([W3Schools][1])

---

## 🖋️ Nastavenie vlastností písma označení a nadpisu

Pomocou parametra `fontdict` v `xlabel()`, `ylabel()` a `title()` môžeš nastaviť vlastnosti písma.

### Príklad

Nastav vlastnosti písma pre nadpis a popisky:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.title("Údaje z športových hodiniek", fontdict=font1)
plt.xlabel("Priemerný tep", fontdict=font2)
plt.ylabel("Spálené kalórie", fontdict=font2)

plt.plot(x, y)
plt.show()
```

([W3Schools][1])

---

## 📍 Pozícia nadpisu

Pomocou parametra `loc` v `title()` môžeš nastaviť zarovnanie nadpisu.
Možné hodnoty: `'left'`, `'right'`, `'center'` (štandardne `'center'`).

### Príklad

Zarovnaj nadpis doľava:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Údaje z športových hodiniek", loc='left')
plt.xlabel("Priemerný tep")
plt.ylabel("Spálené kalórie")

plt.plot(x, y)
plt.show()
```

---

## 📊 Pridanie čiar mriežky do grafu

Pomocou funkcie `grid()` z Pyplot môžeš **pridať čiary mriežky** do grafu.

### Príklad

Pridanie čiar mriežky do grafu:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Údaje zo športových hodiniek")
plt.xlabel("Priemerný tep")
plt.ylabel("Spálené kalórie")

plt.plot(x, y)

plt.grid()

plt.show()
```

---

## 🧭 Výber čiar mriežky podľa osi

Pomocou argumentu `axis` v `grid()` môžeš špecifikovať, ktoré čiary mriežky sa zobrazia.

Možné hodnoty: `'x'`, `'y'`, `'both'`. Predvolená hodnota je `'both'`.

### Príklad – len čiary mriežky pre os x:

```python
# ...
plt.grid(axis='x')
plt.show()
```

---

### Príklad – len čiary mriežky pre os y:

```python
# ...
plt.grid(axis='y')
plt.show()
```

---

## 🎨 Nastavenie vzhľadu čiar mriežky

Môžeš definovať vlastnosti čiar mriežky: `color`, `linestyle`, `linewidth`.

### Príklad

Štýl mriežky – zelená prerušovaná čiara s hrúbkou 0.5:

```python
# ...
plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
```
---

## 📋 Matplotlib – Zobrazenie viacerých grafov (`subplot()`)

Funkcia `subplot()` umožňuje vykresliť **viacero grafov v jednom okne**.

### Príklad – 2 grafy vedľa seba:

```python
import matplotlib.pyplot as plt
import numpy as np

# Graf 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x, y)

# Graf 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()
```

---

### 🔍 Funkcia `subplot()`

Funkcia `subplot()` prijíma tri argumenty popisujúce rozloženie obrázku:

* 🟦 Prvý argument = počet **riadkov**
* 🟦 Druhý argument = počet **stĺpcov**
* 🟦 Tretí argument = **index** aktuálneho grafu (1 = prvý, 2 = druhý, atď.) ([w3schools.com][1])

---

### 📈 Príklad – 2 grafy nad sebou:

```python
import matplotlib.pyplot as plt
import numpy as np

# Graf 1:
plt.subplot(2, 1, 1)
plt.plot(np.array([0,1,2,3]), np.array([3,8,1,10]))

# Graf 2:
plt.subplot(2, 1, 2)
plt.plot(np.array([0,1,2,3]), np.array([10,20,30,40]))

plt.show()
```

---

### ➕ Viacero grafov v mriežke 2×3:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
y2 = np.array([10,20,30,40])

plt.subplot(2, 3, 1); plt.plot(x, y1)
plt.subplot(2, 3, 2); plt.plot(x, y2)
plt.subplot(2, 3, 3); plt.plot(x, y1)
plt.subplot(2, 3, 4); plt.plot(x, y2)
plt.subplot(2, 3, 5); plt.plot(x, y1)
plt.subplot(2, 3, 6); plt.plot(x, y2)

plt.show()
```

---

## 🏷️ Titulky pre jednotlivé grafy a celé okno

### Pridanie názvu ku každému grafu pomocou `title()`:

```python
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("SALES")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("INCOME")

plt.show()
```

---

### Pridanie "super" nadpisu celého obrázka pomocou `suptitle()`:

```python
plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("SALES")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
```
---

# 📈 Matplotlib – Bodový graf (`scatter()`)

Funkcia `scatter()` slúži na vykreslenie **bodového grafu**, kde každý bod reprezentuje jednu dvojicu hodnôt – z osí **x** a **y**.

---

## ✅ Príklad – základný scatter:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x, y)
plt.show()
```

---

## 🔁 Porovnanie viacerých datasetov

Môžeš vykresliť viaceré dataset(y) v jednom grafe, každý s inou farbou.

```python
# Deň 1
x = np.array([...])
y = np.array([...])
plt.scatter(x, y)

# Deň 2
x2 = np.array([...])
y2 = np.array([...])
plt.scatter(x2, y2)

plt.show()
```

---

## 🎨 Nastavenie farby

```python
plt.scatter(x, y, color='hotpink')
plt.scatter(x2, y2, color='#88c999')
plt.show()
```

---

## 🧩 Farba každého bodu zvlášť

```python
colors = np.array(["red", "green", "blue", "orange", "purple"])
plt.scatter(x, y, c=colors)
plt.show()
```

---

## 🌈 Colormap (farebná škála)

```python
values = np.array([0, 10, 20, 30, 40, 50])
plt.scatter(x, y, c=values, cmap='viridis')
plt.colorbar()
plt.show()
```

---

## 🔢 Nastavenie veľkosti bodov

```python
sizes = np.array([20, 50, 100, 200, 500])
plt.scatter(x, y, s=sizes)
plt.show()
```

---

## 🌫️ Transparentnosť bodov

```python
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.show()
```

---

## 🎯 Komplexný príklad: farba, veľkosť, priehľadnosť

```python
x = np.random.randint(100, size=100)
y = np.random.randint(100, size=100)
colors = np.random.randint(100, size=100)
sizes = 10 * np.random.randint(100, size=100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()
```

---

## 📊 Matplotlib – Pridávanie stĺpcových grafov (`bar()`)

S `bar()` z Pyplot môžeš vytvárať **vertikálne stĺpcové grafy**.

### Príklad

Vyhotov 4 stĺpce:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y)
plt.show()
```

Funkcia `bar()` očakáva dva argumenty – polia kategórií (`x`) a ich hodnoty (`y`).

---

## 🟨 Horizontálne stĺpce (`barh()`)

Ak chceš stĺpce horizontálne namiesto vertikálne, použiješ `barh()`:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
```

---

## 🎨 Farba stĺpcov

Argument `color` v `bar()` alebo `barh()` umožňuje nastaviť farbu:

```python
plt.bar(x, y, color="red")
plt.show()
```

Podpora zahŕňa:

* Názvy farieb (napr. `"hotpink"`)
* Hexadresemické hodnoty (napr. `"#4CAF50"`)

Príklad so zelenou farbou:

```python
plt.bar(x, y, color="#4CAF50")
plt.show()
```

---

## 📏 Šírka stĺpcov (`width`) a výška (`height`)

V `bar()` môžeš pomocou `width` nastaviť šírku stĺpcov:

```python
plt.bar(x, y, width=0.1)
plt.show()
```

Predvolená hodnota šírky je `0.8`.

Pre horizontálne stĺpcové grafy (`barh()`) sa namiesto `width` používa `height`:

```python
plt.barh(x, y, height=0.1)
plt.show()
```

Predvolená hodnota výšky je `0.8`.

---

## 📊 Matplotlib – Histogramy (`hist()`)

Histogram zobrazuje **rozloženie údajov** – ukazuje, koľko hodnôt spadá do jednotlivých intervalov (tzv. „binov“).

---

### ✅ Príklad – vytvorenie základného histogramu:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)

plt.hist(x)
plt.show()
```

Tento kód vytvorí histogram 1 000 náhodných hodnôt, tmavší stĺpec znamená viac dát v danom intervale.

---

### 🎯 Počet binov (`bins`)

Môžeš zmeniť počet binov pomocou argumentu `bins` (predvolene je 10):

```python
plt.hist(x, bins=20)
plt.show()
```

---

### 🎨 Farba histogramu

Pomocou `color` môžeš nastaviť farbu:

```python
plt.hist(x, bins=20, color='green')
plt.show()
```

Podporované sú názvy farieb aj hex hodnoty.

---

### ➕ Viacero dát v jednom histograme

Môžeš porovnať dve sady údajov naraz:

```python
x1 = np.random.randn(1000)
x2 = np.random.randn(1000)

plt.hist([x1, x2], bins=20, color=['red', 'blue'])
plt.show()
```

---

### 🔍 Priehľadnosť (`alpha`)

Nastav `alpha` (transparentnosť) ak chceš lepšie vidieť prekrytie:

```python
plt.hist([x1, x2], bins=20, color=['red', 'blue'], alpha=0.7)
plt.show()
```

---

### 📝 Súhrn

* `hist()` – vykreslí histogram
* `bins` – počet intervalov
* `color` – farba stĺpcov
* `alpha` – priehľadnosť
* Viacero datasetov – zobrazenie vedľa seba s rôznymi farbami

---

## 🥧 Matplotlib – Pie grafy (`pie()`)

### Vytvorenie pie grafu

Funkcia `pie()` z Pyplotu slúži na vykreslenie koláčového (pie) grafu. Každý výsek ("wedge") predstavuje pomer hodnoty v poli k celkovej sume.

#### Príklad:

```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()
```

Štandardne sa prvý výsek začína na ose x a pokračuje proti smeru hodinových ručičiek.

---

### Pridanie popiskov

Parameter `labels` umožňuje pridať názvy k výsekom. Pole názvov musí mať rovnaký počet prvkov ako pole hodnôt.

#### Príklad:

```python
y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels=labels)
plt.show()
```

---

### Zmena počiatočného uhla

Parameter `startangle` určuje, kde sa graf začne (v stupňoch). Predvolenou hodnotou je 0° (osa x).

#### Príklad:

```python
plt.pie(y, labels=labels, startangle=90)
plt.show()
```

---

### „Explode“ – oddialenie výsekov

Parameter `explode` umožňuje oddialiť niektorý výsek od stredu. Pole musí mať hodnotu pre každý výsek – napr. `0.2` znamená 20 % vychýlenie.

#### Príklad:

```python
explode = [0.2, 0, 0, 0]  # oddiali "Apples"

plt.pie(y, labels=labels, explode=explode)
plt.show()
```

---

### Stín (`shadow`)

Nastavením `shadow=True` pridáš výseku tieň.

#### Príklad:

```python
plt.pie(y, labels=labels, explode=explode, shadow=True)
plt.show()
```

---

### Farby výsekov

Parameter `colors` prijíma pole farieb pre každý výsek: môžeš použiť názvy farieb, hex hodnoty alebo skratky `'r'`, `'g'`, `'b'`, `'c'`, `'m'`, `'y'`, `'k'`, `'w'`.

#### Príklad:

```python
colors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=labels, colors=colors)
plt.show()
```

---

### Legenda

Funkcia `legend()` pridá vysvetlenie k výsekom. Môžeš jej pridať aj parameter `title` na nadpis legendy.

#### Príklad bez nadpisu:

```python
plt.pie(y, labels=labels)
plt.legend()
plt.show()
```

#### S nadpisom legendy:

```python
plt.pie(y, labels=labels)
plt.legend(title="Four Fruits:")
plt.show()
```

---
