## 🗃️ Čo je súbor a súborový systém?

### ✅ **Súbor (file):**

* Je to **jednotka ukladania dát** v počítači.
* Môže obsahovať text, obrázky, zvuk, video, dáta, programy atď.
* Vzniká ako **posloupnosť bajtov (bytes)**.
* Každý súbor má:

  * **názov**
  * **príponu** (napr. `.txt`, `.jpg`, `.py`, `.exe`)
  * **obsah** – ktorý môže byť **textový alebo binárny**

### 📂 **Súborový systém (file system):**

* Je to spôsob, **ako operačný systém organizuje súbory na disku** (HDD, SSD, USB atď.).
* Obsahuje:

  * Adresáre (zložky, priečinky)
  * Prístupové práva (kto môže čítať/písať)
  * Metadáta: čas vytvorenia, veľkosť, typ atď.
* Príklady súborových systémov: `NTFS` (Windows), `ext4` (Linux), `FAT32`, `APFS` (macOS)

---

## 📝 Textové vs. Binárne súbory

### 1. **Textové súbory:**

* Obsahujú **čitateľný text** (napr. v Unicode/UTF-8/ASCII).
* Typicky používajú `\n` pre nový riadok.
* Príklady: `.txt`, `.csv`, `.json`, `.py`

#### V Pythone:

```python
with open("subor.txt", "r", encoding="utf-8") as f:
    obsah = f.read()
```

### 2. **Binárne súbory:**

* Obsahujú **dáta v binárnej forme** – **nie sú čitateľné** bez dekódovania.
* Používajú sa pre obrázky, zvuk, PDF, EXE, atď.
* Príklady: `.jpg`, `.mp3`, `.zip`, `.exe`, `.pdf`

#### V Pythone:

```python
with open("obrazok.jpg", "rb") as f:  # "rb" = read binary
    data = f.read()
```

---

## 📌 Režimy otvárania súborov v Pythone

| Režim  | Popis                |
| ------ | -------------------- |
| `'r'`  | čítanie (text)       |
| `'w'`  | zápis (vymaže obsah) |
| `'a'`  | pridanie na koniec   |
| `'rb'` | čítanie (binárne)    |
| `'wb'` | zápis (binárne)      |
| `'r+'` | čítanie aj zápis     |

---

## 📎 Zaujímavosti

* **Textový súbor je vlastne tiež binárny súbor**, len má bajty, ktoré sú zmysluplné pre človeka (napr. UTF-8).
* **Binárne súbory sú často menšie** a rýchlejšie na spracovanie (napr. `pickle`, `protobuf`).
* V Pythone môžeš ukladať binárne serializované objekty napr. pomocou `pickle`.

---

## 🎯 Kedy použiť ktorý typ?

| Účel                    | Formát súboru             |
| ----------------------- | ------------------------- |
| Konfiguračný súbor      | textový (`.ini`, `.json`) |
| Uloženie obrázkov       | binárny (`.jpg`, `.png`)  |
| Export do Excelu        | binárny (`.xlsx`)         |
| Jednoduchý log/poznámky | textový (`.txt`)          |
| Uloženie modelu AI      | binárny (`.pkl`, `.pt`)   |

---

## 1. 📄 **Práca s textovým súborom**

### ✅ Zápis do textového súboru:

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Toto je riadok 1\n")
    f.write("Toto je riadok 2\n")
```

### ✅ Čítanie zo súboru:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for riadok in f:
        print(riadok.strip())  # .strip() odstráni \n
```

---

## 2. 💾 **Práca s binárnym súborom**

### ✅ Zápis binárnych dát (napr. bajty):

```python
data = bytes([65, 66, 67, 0, 255])  # A, B, C, null byte, max byte

with open("data.bin", "wb") as f:
    f.write(data)
```

### ✅ Čítanie binárnych dát:

```python
with open("data.bin", "rb") as f:
    obsah = f.read()
    print(list(obsah))  # výstup: [65, 66, 67, 0, 255]
```

---

## 3. ⚙️ (Extra) Štruktúra binárneho súboru (napr. vlastný formát)

Predstav si, že chceš uložiť štruktúru:
**meno (10 znakov) + vek (1 bajt)**

```python
# Zápis: meno + vek
meno = "Peter".ljust(10, '\x00')  # doplníme null znaky do 10 znakov
vek = 27

with open("osoba.bin", "wb") as f:
    f.write(meno.encode('utf-8'))
    f.write(bytes([vek]))
```

### Čítanie:

```python
with open("osoba.bin", "rb") as f:
    meno_bajty = f.read(10)
    vek = int.from_bytes(f.read(1), byteorder='big')

meno = meno_bajty.decode('utf-8').rstrip('\x00')
print(f"Meno: {meno}, Vek: {vek}")
```

---


**encoding** (kódovanie) je kľúčový pojem pri práci s textom a súbormi v Pythone aj všeobecne v počítačoch.

---

## 🧠 Čo je **encoding**?

**Encoding** (kódovanie) je spôsob, **ako premeniť znaky (text)** na **bajty (čísla)**, ktoré si počítač ukladá alebo prenáša.
Každý znak (napr. `A`, `č`, `🙂`) sa musí premeniť na konkrétnu postupnosť bajtov.

Bez správneho kódovania a dekódovania by počítač nevedel, **ako čítať a zapisovať text**.

---

## 📦 Bežné typy kódovaní:

| Kódovanie                | Popis                                                                     |
| ------------------------ | ------------------------------------------------------------------------- |
| **ASCII**                | Základné anglické znaky, 1 bajt (7 bitov), max 128 znakov                 |
| **UTF-8**                | Najbežnejšie dnes – podpora všetkých znakov, variabilná dĺžka (1–4 bajty) |
| **UTF-16**               | Alternatíva k UTF-8, bežne 2 alebo 4 bajty na znak                        |
| **Latin-1 (ISO-8859-1)** | Staršie európske znaky, 1 bajt, bez diakritiky pre slovenčinu             |

---

## 💡 Príklad: Rozdiel medzi textom a bajtami

```python
text = "čau"
bajty = text.encode("utf-8")
print(bajty)  # b'\xc4\x8dau'
```

Toto znamená:

* Znak `č` sa zakóduje do dvoch bajtov: `\xc4\x8d`
* Znak `a` a `u` sú v ASCII, takže zostávajú ako jeden bajt

---

## 🔁 Encode vs Decode

| Operácia   | Funkcia v Pythone | Príklad                                   |
| ---------- | ----------------- | ----------------------------------------- |
| **encode** | `str.encode()`    | `'čau'.encode('utf-8')` → bajty           |
| **decode** | `bytes.decode()`  | `b'\xc4\x8dau'.decode('utf-8')` → `'čau'` |

---

## ⚠️ Čo sa stane, keď použiješ zlé kódovanie?

```python
b = 'čau'.encode('utf-8')

# Skúsme dekódovať nesprávne
print(b.decode('ascii'))  # UnicodeDecodeError!
```

Ak použiješ nesprávne kódovanie, Python (alebo iný program) **nevie, ako správne "preložiť" bajty späť na znaky** → vznikne chyba alebo nezmyselný text.

---

## 📝 V textových súboroch

Keď zapisuješ text do súboru, **vždy si zvoľ encoding**, napr.:

```python
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("Dobrý deň, svet! čľž")
```

Ak ten súbor potom otvoríš bez správneho encodingu, môžu sa zobraziť „čudné znaky“ (`Ã¨`, `Å¾`, `Âľ`, atď.).

---

## 📌 Tipy:

* Vždy použi `encoding="utf-8"` — je to štandard pre moderný text (aj slovenčina, emoji, čokoľvek).
* Vyhýbaj sa `"ascii"` (príliš obmedzené) a `"latin-1"` (nevie slovenčinu úplne správne).
* Keď vidíš v konzole alebo súbore čudné znaky → je to takmer vždy problém s encodingom.

---

```python
text = "čau 👋"  # obsahuje aj diakritiku aj emoji

# UTF-8 (odporúčaný štandard)
utf8_bytes = text.encode("utf-8")
print("UTF-8 bajty:", utf8_bytes)

decoded_utf8 = utf8_bytes.decode("utf-8")
print("UTF-8 dekódované:", decoded_utf8)

# Latin-1 (ISO-8859-1) – nepodporuje č, 👋 (emoji)
try:
    latin1_bytes = text.encode("latin-1")
except UnicodeEncodeError as e:
    print("Latin-1 encoding error:", e)

# ASCII – nepodporuje nič okrem základných znakov
try:
    ascii_bytes = text.encode("ascii")
except UnicodeEncodeError as e:
    print("ASCII encoding error:", e)

# Ak skúsime dekódovať UTF-8 bajty iným spôsobom – bude zle
try:
    broken = utf8_bytes.decode("latin-1")
    print("Zle dekódované (UTF-8 ako Latin-1):", broken)
except UnicodeDecodeError as e:
    print("Decode error:", e)
```

---

## 🌐 Čo je **Unicode**?

**Unicode** je **medzinárodný štandard**, ktorý definuje:

1. ✅ **Číselné kódy pre všetky znaky** – každému znaku (napr. `A`, `č`, `中`, `🙂`) priradí jedinečné **číslo** = **kódový bod**.
2. ✅ Kódové body zapisujeme ako `U+XXXX` (napr. `č` je `U+010D`, `🙂` je `U+1F642`).
3. ❌ Unicode **neurčuje, ako sa tieto čísla uložia do bajtov** – to robia **encodings (UTF-8, UTF-16,...)**

---

## 📦 Unicode vs Encoding

| Pojem    | Čo to je                              | Príklad                         |
| -------- | ------------------------------------- | ------------------------------- |
| Unicode  | Zoznam znakov + ich číselné hodnoty   | `č` = `U+010D`                  |
| Encoding | Ako sa tie čísla uložia do **bajtov** | `U+010D` → `\xc4\x8d` (v UTF-8) |

Takže:

> Unicode je **abeceda**, encoding je **spôsob zápisu do súboru/pamäte**.

---

## 🐍 Unicode v Pythone

Python 3 má **všetky reťazce (`str`) ako Unicode**.

```python
text = "čau 👋"
print(text)              # normálny výstup
print(ord("č"))          # kódový bod Unicode → 269 (0x10D)
print(hex(ord("👋")))    # → 0x1f44b
```

### Funkcie:

* `ord(znak)` → získa Unicode číslo znaku
* `chr(kod)` → opačne: z čísla na znak

```python
print(chr(0x1F44B))  # 👋
```

---

## 🔧 Ako sa to ukladá?

**Príklad pre znak 👋 (U+1F44B):**

| Encoding | Bajty                        | Dĺžka   |
| -------- | ---------------------------- | ------- |
| UTF-8    | `F0 9F 91 8B`                | 4 bajty |
| UTF-16   | `D83D DC4B` (surrogate pair) | 4 bajty |
| UTF-32   | `00 01 F4 4B`                | 4 bajty |

UTF-8 je **kompaktné pre anglický text**, ale podporuje aj všetky znaky cez viac bajtov.

---

## 🔥 Unicode znaky priamo v kóde

```python
print("Unicode 👋 = \U0001F44B")
print("č = \u010D")  # krátka verzia pre U+010D
```

---

## 🧪 Unicode escape:

```python
s = "čau 👋"
for c in s:
    print(f"{c} → U+{ord(c):04X}")
```

Výstup:

```
č → U+010D
a → U+0061
u → U+0075
  → U+0020
👋 → U+1F44B
```

---

## 💡 Zhrnutie:

* **Unicode** je univerzálna mapa všetkých znakov → číselné kódy.
* **Encoding (napr. UTF-8)** je spôsob, ako tie čísla zakódovať do bajtov.
* **Python 3 nativne pracuje s Unicode**, čo znamená, že reťazce môžu obsahovať znaky z celého sveta.

---


```python
import locale
print(locale.getpreferredencoding())
```
