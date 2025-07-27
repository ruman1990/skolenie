# Pandas – Začíname

## Čo je Pandas?

* **Pandas** je knižnica v Pythone na prácu s dátami vo forme tabuliek (DataFrame).
* Pandas poskytuje nástroje na čítanie, analýzu, manipuláciu a vizualizáciu dát.
* Je veľmi populárna v oblasti dátovej analytiky, vedy o dátach a strojového učenia.

## Prečo používať Pandas?

* Pracuje so štruktúrovanými dátami ako Excel tabuľky, CSV súbory, databázy, atď.
* Vie jednoducho filtrovať, triediť, upravovať, agregovať a vizualizovať dáta.
* Je veľmi rýchla a efektívna aj pri veľkých datasetoch.

## Inštalácia Pandas

Pandas nainštaluješ cez pip:

```bash
pip install pandas
```

## Importovanie Pandas

V Pythone sa zvyčajne importuje pod skratkou `pd`:

```python
import pandas as pd
```

## Kontrola verzie

Ak chceš zistiť, akú verziu Pandas máš nainštalovanú:

```python
import pandas as pd
print(pd.__version__)
```

## Prvé použitie

Najdôležitejšie objekty v Pandas sú:

* **Series** – jednorozmerné pole (napr. stĺpec čísel, reťazcov)
* **DataFrame** – tabuľka (viacero stĺpcov, každý so svojím názvom)

Príklad vytvorenia `Series`:

```python
import pandas as pd

moj_objekt = pd.Series([1, 7, 2])
print(moj_objekt)
```

**Výsledok:**

```
0    1
1    7
2    2
dtype: int64
```

---

# Pandas Series

## Čo je to Series?

* **Series** v Pandas je jednorozmerné pole dát podobné zoznamu (list) v Pythone.
* Každý prvok v Series má svoj **index** (poradie).
* Najčastejšie sa Series používa ako stĺpec v tabuľke (DataFrame), ale môže byť aj samostatne.

---

## Ako vytvoriť Series

### Vytvorenie Series zo zoznamu

```python
import pandas as pd

moj_zoznam = [1, 7, 2]
moj_series = pd.Series(moj_zoznam)
print(moj_series)
```

**Výstup:**

```
0    1
1    7
2    2
dtype: int64
```

* Čísla vľavo (0, 1, 2) sú **indexy**.

---

## Prístup k hodnotám v Series

* Vieš pristupovať k hodnotám pomocou indexu:

```python
print(moj_series[0])  # vypíše 1
```

---

## Vlastné indexy

* Môžeš nastaviť vlastné názvy indexov:

```python
import pandas as pd

moje_cisla = [4, 7, 8]
moj_series = pd.Series(moje_cisla, index=["a", "b", "c"])
print(moj_series)
```

**Výstup:**

```
a    4
b    7
c    8
dtype: int64
```

---

## Series zo slovníka

* Môžeš vytvoriť Series aj zo slovníka (kľúče budú indexy):

```python
import pandas as pd

moj_dict = {"jablko": 10, "hruska": 7, "banan": 5}
moj_series = pd.Series(moj_dict)
print(moj_series)
```

**Výstup:**

```
jablko    10
hruska     7
banan      5
dtype: int64
```

---

## Zhrnutie

* **Series** je základná dátová štruktúra v Pandas – podobá sa stĺpcu v tabuľke.
* Vieš si nastaviť vlastné indexy alebo vytvoriť Series zo zoznamu či slovníka.
* Ku každému prvku pristupuješ podľa indexu.

---

# Pandas DataFrame

## Čo je to DataFrame?

* **DataFrame** je dvojrozmerná tabuľka v Pandas.
* Má riadky a stĺpce, podobne ako Excel alebo databázová tabuľka.
* Každý stĺpec môže mať iný dátový typ (čísla, text, dátum, atď.).

---

## Vytvorenie DataFrame zo slovníka

Najčastejšie vytvárame DataFrame zo slovníka, kde kľúče sú názvy stĺpcov:

```python
import pandas as pd

data = {
    "meno": ["Janko", "Katka", "Robo"],
    "vek": [12, 15, 14]
}

df = pd.DataFrame(data)
print(df)
```

**Výstup:**

```
    meno  vek
0  Janko   12
1  Katka   15
2   Robo   14
```

---

## Prístup k stĺpcom

Môžeš získať stĺpec ako Series:

```python
print(df["meno"])
```

**Výstup:**

```
0    Janko
1    Katka
2     Robo
Name: meno, dtype: object
```

---

## Prístup k riadkom

Použi metódu `.loc[]` (podľa názvu/indexu) alebo `.iloc[]` (podľa poradia):

```python
print(df.loc[1])    # Riadok s indexom 1
```

**Výstup:**

```
meno    Katka
vek        15
Name: 1, dtype: object
```

---

## Nastavenie vlastných indexov

Môžeš nastaviť vlastné mená riadkov:

```python
df2 = pd.DataFrame(data, index=["prvy", "druhy", "treti"])
print(df2)
```

**Výstup:**

```
        meno  vek
prvy   Janko   12
druhy  Katka   15
treti   Robo   14
```

---

## Zhrnutie

* **DataFrame** je hlavný typ tabuľky v Pandas – každý stĺpec má svoj názov a typ.
* Vieš vytvoriť DataFrame zo slovníka, listu, CSV súboru a pod.
* Prístup k dátam je jednoduchý podľa názvu stĺpca alebo indexu riadku.

---

# Pandas – Práca so CSV súbormi

## Čo je CSV?

* **CSV (Comma Separated Values)** je bežný formát na ukladanie tabuliek.
* Dáta sú oddelené čiarkou, každý riadok predstavuje jeden záznam.

---

## Načítanie CSV súboru do DataFrame

* Na načítanie CSV do Pandas slúži funkcia `read_csv()`.

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df)
```

* Takto načítaš celý súbor **data.csv** do objektu DataFrame.

---

## Základné použitie `read_csv()`

* Ak súbor nie je v aktuálnom adresári, zadaj celú cestu (napr. `"cesta/subor.csv"`).
* Prvý riadok v CSV je automaticky považovaný za hlavičku (názvy stĺpcov).

---

## Uloženie DataFrame do CSV

* Na zápis (uloženie) DataFrame do CSV súboru slúži funkcia `to_csv()`:

```python
import pandas as pd

df = pd.DataFrame({
    "meno": ["Janko", "Katka", "Robo"],
    "vek": [12, 15, 14]
})

df.to_csv("vystup.csv", index=False)
```

* Argument `index=False` zabezpečí, že do CSV sa nezapíše číselný index riadkov.

---

## Dôležité argumenty

* `sep=";"` – ak máš CSV oddelené bodkočiarkou (napr. v niektorých európskych krajinách), použi tento parameter.
* `header=None` – ak v CSV nie je hlavička, Pandas automaticky vytvorí číselné názvy stĺpcov.
* `encoding="utf-8"` – nastaví kódovanie (napr. pri slovenčine).

---

## Príklad – čítanie CSV bez hlavičky

```python
df = pd.read_csv("data.csv", header=None)
print(df)
```

---

## Zhrnutie

* CSV je najpoužívanejší formát na výmenu tabuliek.
* V Pandas vieš jednoducho načítať aj uložiť CSV pomocou `read_csv()` a `to_csv()`.
* Vieš nastaviť oddelovač, hlavičku aj kódovanie podľa potreby.

---

# Pandas – Práca s JSON súbormi

## Čo je JSON?

* **JSON (JavaScript Object Notation)** je populárny formát na výmenu a ukladanie dát.
* Dáta v JSON sú uložené ako páry kľúč\:hodnota, podobne ako slovník v Pythone.

---

## Načítanie JSON súboru do DataFrame

* Na načítanie JSON do Pandas slúži funkcia `read_json()`:

```python
import pandas as pd

df = pd.read_json("data.json")
print(df)
```

* Takto načítaš súbor **data.json** do objektu DataFrame.

---

## Ako má vyzerať JSON súbor?

Príklad obsahu súboru `data.json`:

```json
[
  {"meno": "Janko", "vek": 12},
  {"meno": "Katka", "vek": 15},
  {"meno": "Robo", "vek": 14}
]
```

---

## Uloženie DataFrame do JSON

* Na zápis DataFrame do JSON súboru slúži metóda `to_json()`:

```python
import pandas as pd

df = pd.DataFrame({
    "meno": ["Janko", "Katka", "Robo"],
    "vek": [12, 15, 14]
})

df.to_json("vystup.json", orient="records", force_ascii=False)
```

* Argument `orient="records"` zabezpečí zápis do zoznamu slovníkov (čo je najbežnejšie).
* `force_ascii=False` zaistí, že znaky s diakritikou sa správne uložia.

---

## Príklad – čítanie JSON zo stringu

* Môžeš načítať JSON aj priamo zo stringu:

```python
import pandas as pd

json_data = '[{"meno": "Janko", "vek": 12}, {"meno": "Katka", "vek": 15}]'
df = pd.read_json(json_data)
print(df)
```

---

## Zhrnutie

* JSON je veľmi bežný formát na výmenu dát.
* V Pandas môžeš použiť `read_json()` na načítanie a `to_json()` na uloženie dát.
* Vieš čítať/ukladať zo súboru aj zo stringu.

---

# Pandas – Analyzovanie dát

## Základné funkcie na analýzu dát

Pandas obsahuje veľa vstavaných funkcií na rýchlu analýzu a sumarizáciu dát v tabuľkách (DataFrame).
Najdôležitejšie funkcie ti umožnia rýchlo zistiť základné informácie o tvojich dátach.

---

## Zobrazenie prvých/posledných riadkov

* **`head()`** – zobrazí prvých 5 riadkov (môžeš zadať aj vlastný počet):

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())       # Prvých 5 riadkov
print(df.head(10))     # Prvých 10 riadkov
```

* **`tail()`** – zobrazí posledných 5 riadkov:

```python
print(df.tail())       # Posledných 5 riadkov
print(df.tail(3))      # Posledné 3 riadky
```

---

## Informácie o dátach

* **`info()`** – vypíše základné informácie o DataFrame (počet riadkov, stĺpcov, typy dát, chýbajúce hodnoty):

```python
print(df.info())
```

* **`describe()`** – vypočíta základné štatistiky (priemer, minimum, maximum, počet hodnôt, kvartily, atď.) pre číselné stĺpce:

```python
print(df.describe())
```

---

## Počet riadkov a stĺpcov

* **`len(df)`** alebo **`df.shape`**:

```python
print(len(df))         # Počet riadkov
print(df.shape)        # (počet riadkov, počet stĺpcov)
```

---

## Zhrnutie

* `head()` a `tail()` – rýchly náhľad na začiatok/koniec dát
* `info()` – základné info o tabuľke
* `describe()` – štatistika pre číselné údaje
* `shape` a `len()` – veľkosť tabuľky

---


# Pandas – Čistenie dát

## Prečo čistiť dáta?

Pri práci s reálnymi dátami často narazíš na **chýbajúce, nesprávne alebo nekonzistentné hodnoty**. Pred analýzou alebo spracovaním dát je dobré ich očistiť a pripraviť.

---

## Hlavné úlohy pri čistení dát

* Odstrániť chýbajúce hodnoty (missing values)
* Vyplniť chýbajúce hodnoty vhodnou hodnotou
* Odstrániť duplikáty (duplicitné riadky)
* Upraviť nesprávne alebo nekonzistentné údaje (napr. formáty dátumov, čísiel)

---

## Odstraňovanie chýbajúcich hodnôt

* **`dropna()`** – odstráni riadky (alebo stĺpce) s chýbajúcimi hodnotami:

```python
import pandas as pd

df = pd.read_csv("data.csv")
df_bez_na = df.dropna()  # Odstráni riadky s NaN hodnotami
```

---

## Vyplňovanie chýbajúcich hodnôt

* **`fillna()`** – nahradí chýbajúce hodnoty určenou hodnotou:

```python
df_filled = df.fillna(0)  # Nahradí všetky NaN hodnoty nulou
```

* Môžeš nahradiť aj inou hodnotou, alebo použiť napríklad priemer stĺpca:

```python
df["vek"].fillna(df["vek"].mean(), inplace=True)
```

---

## Odstraňovanie duplicitných riadkov

* **`drop_duplicates()`** – odstráni duplicitné riadky:

```python
df_unique = df.drop_duplicates()
```

---

## Upravenie formátu údajov

* Vieš meniť typy stĺpcov napríklad:

```python
df["datum"] = pd.to_datetime(df["datum"])
df["vek"] = df["vek"].astype(int)
```

---

## Zhrnutie

* Pri čistení dát často používaš: `dropna()`, `fillna()`, `drop_duplicates()`, úpravu typov
* Správne vyčistené dáta sú základ kvalitnej analýzy!

---

# Pandas – Čistenie prázdnych buniek

## Prázdne bunky v dátach

* Pri importe dát sa môžu v tabuľke vyskytnúť **prázdne bunky** (chýbajúce hodnoty, tzv. `NaN` – Not a Number).
* Takéto hodnoty je potrebné upraviť pred ďalšou analýzou.

---

## Kontrola prázdnych hodnôt

* Zistíš, ktoré bunky sú prázdne (NaN):

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.isnull())
```

* Vráti tabuľku s hodnotami `True` (prázdne) a `False` (vyplnené).

---

## Odstránenie riadkov s prázdnymi hodnotami

* **`dropna()`** – odstráni riadky, ktoré majú aspoň jednu prázdnu hodnotu:

```python
df2 = df.dropna()
print(df2)
```

---

## Nahradenie prázdnych buniek hodnotou

* **`fillna()`** – nahradí všetky prázdne bunky zadanou hodnotou:

```python
df2 = df.fillna(0)  # Všetky prázdne bunky budú nahradené nulou
print(df2)
```

* Môžeš použiť aj iný text alebo číslo, napríklad:

```python
df2 = df.fillna("neznáme")
```

---

## Vyplnenie len vybraného stĺpca

* Vieš nahradiť prázdne hodnoty len v jednom stĺpci:

```python
df["vek"].fillna(99, inplace=True)
```

---

## Zhrnutie

* Na odstránenie prázdnych riadkov použi `dropna()`.
* Na nahradenie prázdnych hodnôt použi `fillna()`.
* Vieš nahrádzať prázdne bunky v celej tabuľke alebo v konkrétnom stĺpci.

---

# Pandas – Čistenie nesprávneho formátu

## Nesprávny formát v dátach

* V reálnych dátach môžeš mať hodnoty vo **vnestejnom alebo nesprávnom formáte** – napríklad dátumy uložené ako text, čísla uložené ako reťazce atď.
* Pred spracovaním a analýzou je dôležité previesť tieto hodnoty do správneho dátového typu.

---

## Konverzia typu dát

### Prevod stĺpca na číselný typ

* Ak máš stĺpec, ktorý by mal obsahovať čísla, ale je uložený ako text, použiješ:

```python
df["vek"] = pd.to_numeric(df["vek"], errors='coerce')
```

* Argument `errors='coerce'` nahradí všetky hodnoty, ktoré sa nedajú previesť, hodnotou `NaN`.

---

### Prevod stĺpca na dátumový typ

* Ak máš dátumy uložené ako text, môžeš ich previesť na dátum:

```python
df["datum"] = pd.to_datetime(df["datum"], errors='coerce')
```

* Opäť, všetky nesprávne hodnoty sa stanú `NaN`.

---

## Odstránenie riadkov s nesprávnym formátom

* Po konverzii typu môžu vzniknúť prázdne hodnoty (`NaN`) tam, kde bol nesprávny formát.
* Môžeš tieto riadky odstrániť:

```python
df = df.dropna(subset=["vek"])
```

* Odstráni všetky riadky, kde je v stĺpci `vek` prázdna hodnota.

---

## Príklad

```python
import pandas as pd

df = pd.DataFrame({
    "meno": ["Janko", "Katka", "Robo"],
    "vek": ["12", "pätnásť", "14"]
})

df["vek"] = pd.to_numeric(df["vek"], errors='coerce')
df = df.dropna(subset=["vek"])
print(df)
```

**Výstup:**

```
    meno   vek
0  Janko  12.0
2   Robo  14.0
```

* Katka bola odstránená, lebo jej vek nebol číslo.

---

## Zhrnutie

* Ak sú dáta v nesprávnom formáte, použite `pd.to_numeric()` alebo `pd.to_datetime()` na konverziu.
* Pri neúspešnej konverzii vznikne `NaN`, ktorý môžeš následne vyčistiť pomocou `dropna()`.

---

# Pandas – Čistenie nesprávnych údajov

## Nesprávne údaje v dátach

* Reálne dáta často obsahujú **chybné alebo nezmyselné hodnoty** (napr. záporný vek, extrémne čísla, hodnoty mimo logického rozsahu).
* Pred analýzou je dobré tieto nesprávne dáta odhaliť a opraviť alebo odstrániť.

---

## Hľadanie nesprávnych hodnôt

* Vieš si vypísať riadky, kde je podozrivá hodnota:

```python
print(df[df["vek"] < 0])    # nájde všetky záporné veky
print(df[df["vek"] > 120])  # nájde extrémne vysoké veky
```

---

## Nahradenie nesprávnych hodnôt

* Nahradiť chybné hodnoty môžeš pomocou podmienok:

```python
df.loc[df["vek"] < 0, "vek"] = 0      # záporné veky nahradí nulou
df.loc[df["vek"] > 120, "vek"] = 120  # extrémne veky nahradí maximom
```

---

## Odstránenie riadkov s nesprávnymi údajmi

* Ak nechceš nahradzovať, môžeš riadky rovno odstrániť:

```python
df = df[df["vek"] >= 0]
df = df[df["vek"] <= 120]
```

---

## Automatické čistenie podľa viacerých podmienok

* Môžeš kombinovať podmienky do jedného filtra:

```python
df = df[(df["vek"] >= 0) & (df["vek"] <= 120)]
```

---

## Príklad

```python
import pandas as pd

df = pd.DataFrame({
    "meno": ["Janko", "Katka", "Robo"],
    "vek": [12, -7, 156]
})

# Odstránenie nesprávnych vekov
df = df[(df["vek"] >= 0) & (df["vek"] <= 120)]
print(df)
```

**Výstup:**

```
    meno  vek
0  Janko   12
```

---

## Zhrnutie

* Nesprávne hodnoty (napr. záporné čísla, nezmyselné dáta) je dobré opraviť alebo odstrániť.
* Používaj podmienené priradenia alebo filtrovanie riadkov podľa podmienky.


---

# Pandas – Čistenie duplicitných riadkov

## Duplicitné údaje v dátach

* Duplicitné riadky znamenajú, že v tabuľke sú dva alebo viac riadkov s úplne rovnakými hodnotami.
* Duplicitné dáta môžu skresliť analýzu alebo štatistiku.

---

## Zistenie duplicitných riadkov

* Pomocou `duplicated()` zistíš, ktoré riadky sú duplicitné:

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.duplicated())
```

* Výsledok je séria `True`/`False`, kde `True` znamená, že riadok je duplicitný (okrem prvého výskytu).

---

## Odstránenie duplicitných riadkov

* Funkcia `drop_duplicates()` odstráni všetky duplicitné riadky (ponechá len prvý výskyt):

```python
df_bez_dupl = df.drop_duplicates()
print(df_bez_dupl)
```

---

## Odstránenie duplicit podľa vybraných stĺpcov

* Vieš určiť, podľa ktorých stĺpcov sa kontroluje duplicita:

```python
df_bez_dupl = df.drop_duplicates(subset=["meno"])
```

* Týmto odstrániš riadky, kde sa meno opakuje (ponechá prvý výskyt).

---

## Zhrnutie

* Duplicity vieš rýchlo zistiť pomocou `duplicated()`.
* Odstrániš ich jednoducho cez `drop_duplicates()`, a môžeš si zvoliť aj konkrétne stĺpce.
* Odporúča sa vždy pred analýzou dáta očistiť od duplicitných riadkov.

---

# Pandas – Korelácie

## Čo je korelácia?

* **Korelácia** je štatistická miera, ktorá ukazuje, **ako spolu súvisia dve alebo viac číselných premenných**.
* Korelačný koeficient je číslo medzi -1 a 1:

  * **1** = silná pozitívna závislosť (ak stúpa jedna premenná, stúpa aj druhá)
  * **0** = žiadna závislosť
  * **-1** = silná negatívna závislosť (ak stúpa jedna premenná, druhá klesá)

---

## Vypočítanie korelácie v Pandas

* Na výpočet korelácie medzi všetkými číselnými stĺpcami v tabuľke slúži metóda `corr()`:

```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.corr())
```

* Výsledok je korelačná matica – tabuľka, kde vidíš vzájomné korelácie medzi stĺpcami.

---

## Príklad

```python
import pandas as pd

data = {
    "vek": [20, 22, 23, 24, 25],
    "vyska": [160, 165, 167, 170, 175],
    "vaha": [55, 60, 61, 65, 70]
}
df = pd.DataFrame(data)
print(df.corr())
```

**Výstup:**

```
             vek     vyska      vaha
vek     1.000000  0.991241  0.990277
vyska   0.991241  1.000000  0.988385
vaha    0.990277  0.988385  1.000000
```

---

## Interpretácia výsledku

* Čísla blízke 1 alebo -1 znamenajú silnú (pozitívnu alebo negatívnu) koreláciu.
* Čísla blízke 0 znamenajú, že stĺpce spolu nesúvisia.

---

## Korelácia len medzi dvoma stĺpcami

* Vieš vypočítať aj priamo medzi dvoma stĺpcami:

```python
print(df["vek"].corr(df["vaha"]))
```

---

## Zhrnutie

* Korelácia pomáha zistiť, ktoré číselné stĺpce spolu súvisia.
* Použi `df.corr()` pre celú tabuľku alebo `df["stlpec1"].corr(df["stlpec2"])` pre konkrétnu dvojicu.

---

# Pandas – Vizualizácia dát (grafy)

## Základy vykresľovania grafov v Pandas

* Pandas má zabudovanú podporu pre jednoduché vytváranie grafov pomocou knižnice **Matplotlib**.
* Vieš rýchlo zobraziť svoje dáta v rôznych typoch grafov (čiarové, stĺpcové, bodové, koláčové atď.).

---

## Inštalácia Matplotlib

* Ak ešte nemáš, nainštaluj si knižnicu **matplotlib**:

```bash
pip install matplotlib
```

---

## Prvý jednoduchý graf

* Stačí použiť metódu **`plot()`** na Series alebo DataFrame:

```python
import pandas as pd
import matplotlib.pyplot as plt

data = [1, 7, 2, 6, 8]
s = pd.Series(data)
s.plot()
plt.show()
```

* `plt.show()` otvorí okno s grafom.

---

## Grafy pre DataFrame

* Ak máš tabuľku (DataFrame), môžeš vykresliť všetky číselné stĺpce naraz:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "A": [1, 7, 2, 6, 8],
    "B": [5, 3, 8, 4, 2]
})
df.plot()
plt.show()
```

---

## Výber typu grafu

* Typ grafu určíš parametrom `kind`:

| kind      | Typ grafu          |
| --------- | ------------------ |
| 'line'    | čiarový (default)  |
| 'bar'     | stĺpcový           |
| 'barh'    | vodorovný stĺpcový |
| 'hist'    | histogram          |
| 'box'     | boxplot            |
| 'kde'     | hustotný graf      |
| 'area'    | plošný graf        |
| 'pie'     | koláčový graf      |
| 'scatter' | bodový graf        |

* Príklad stĺpcového grafu:

```python
df.plot(kind="bar")
plt.show()
```

---

## Základné prispôsobenie grafu

* Môžeš pridať názov grafu a osi:

```python
ax = df.plot(kind="line", title="Môj graf")
ax.set_xlabel("Index")
ax.set_ylabel("Hodnota")
plt.show()
```

---

## Zhrnutie

* Pandas vie rýchlo vykresliť rôzne typy grafov priamo zo Series alebo DataFrame.
* Využíva na to knižnicu Matplotlib, ktorú treba mať nainštalovanú.
* Typ grafu vyberáš parametrom `kind` v metóde `plot()`.

---
