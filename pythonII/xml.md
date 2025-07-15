# 📄 Úvod do XML (eXtensible Markup Language)

## Čo je XML?

**XML** (z anglického *eXtensible Markup Language*, teda „rozšíriteľný značkovací jazyk“) je univerzálny, textovo orientovaný formát na ukladanie a prenos štruktúrovaných dát. XML bol navrhnutý tak, aby bol **ľahko čitateľný pre človeka aj stroj**.

### Hlavné znaky XML:

* Je **nezávislý od platformy** – XML dokumenty fungujú rovnako na rôznych systémoch.
* **Striktne štruktúrovaný** – obsahuje pravidlá, ktoré zabezpečujú, že dáta sú organizované jasne a predvídateľne.
* **Nerozlišuje vzhľad** – XML je len o dátach, nie o prezentácii (na rozdiel od HTML).
* Dá sa **rozšíriť** – môžeš si vytvoriť vlastné značky podľa toho, aké údaje potrebuješ uložiť.

---

## Načo sa XML používa?

XML je všade tam, kde je potrebné bezpečne a jednoznačne uložiť alebo preniesť štruktúrované informácie.
Bežné použitie:

* **Prenos dát** medzi rôznymi aplikáciami (napríklad medzi serverom a klientom).
* **Konfiguračné súbory** (napr. v Java, .NET, niektoré hry a programy).
* **Ukladanie dát** (napríklad jednoduché databázy, export/import).
* **Výmena údajov** medzi systémami, ktoré používajú odlišné technológie.
* **Podklad pre ďalšie technológie**, ako je napr. SOAP, SVG, RSS, XSLT alebo Microsoft Office dokumenty.

---

## Príklad XML dokumentu

```xml
<zvierata>
    <pes>
        <meno>Azor</meno>
        <vek>5</vek>
    </pes>
    <pes>
        <meno>Bella</meno>
        <vek>3</vek>
    </pes>
</zvierata>
```

---

## Základné pojmy a syntax XML

* **Element (značka)**: Základná jednotka, obklopená `<znacka>` a `</znacka>`.
* **Atribút**: Doplnková informácia priamo v otváracej značke, napr. `<osoba vek="20">`.
* **Deklarácia**: Väčšina XML súborov začína riadkom `<?xml version="1.0" encoding="UTF-8"?>`.
* **Hierarchia (stromová štruktúra)**: Elementy môžu obsahovať iné elementy, vzniká „strom“.
* **Hodnota**: Text medzi značkami, napr. `<meno>Janko</meno>`.
* **Prázdne elementy**: Napr. `<kniha />` (rovnaké ako `<kniha></kniha>`).
* **Komentáre**: Začínajú `<!--` a končia `-->`.

### Príklad so všetkým:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<osoby>
    <!-- Zoznam osôb -->
    <osoba id="1">
        <meno>Janko</meno>
        <vek>30</vek>
    </osoba>
    <osoba id="2">
        <meno>Eva</meno>
        <vek>25</vek>
    </osoba>
</osoby>
```

---

## Dôležité pravidlá XML

1. **Všetky značky musia byť uzatvorené** (napr. `<vek>30</vek>`, nie `<vek>30`).
2. **Koreňový element** – celý dokument musí byť uzatvorený v jedinom hlavnom elemente.
3. **Elementy musia byť správne vnorené** – nie je možné otvoriť `<a>`, potom `<b>`, a zatvoriť `<a>`, až potom `<b>`.
4. **Veľkosť písmen záleží** – `<Osoba>` a `<osoba>` sú dva rôzne elementy.
5. **Atribúty v úvodzovkách** – `<osoba vek="30">` (nie `<osoba vek=30>`).

---

## Výhody a nevýhody XML

### Výhody

* **Jasná štruktúra** – umožňuje validáciu (kontrolu správnosti dokumentu).
* **Podpora v mnohých programovacích jazykoch** (vrátane Pythonu).
* **Ľahko rozšíriteľné a zrozumiteľné pre človeka**.

### Nevýhody

* **Rozsiahlejší zápis** v porovnaní s JSON.
* **Čítanie a zápis môže byť pomalšie** pri veľkých súboroch.
* **Viac „hluku“ v dátach** – veľa značiek okolo samotných hodnôt.

---

## Kedy použiť XML?

* Ak potrebuješ **prísnu štruktúru a validáciu** (napr. schémy, DTD).
* Ak komunikuješ so staršími systémami alebo technológiami, ktoré s XML počítajú.
* Ak potrebuješ **výmenný formát nezávislý od technológie**.

V moderných aplikáciách sa na prenos dát často používa **JSON**, ale XML je stále kľúčové vo veľkých podnikových riešeniach, bankovníctve, alebo na miestach, kde sa vyžaduje striktná kontrola nad štruktúrou a typom údajov.

---

## Ako súvisí XML s Pythonom?

Python obsahuje **vstavané knižnice na prácu s XML** (napr. `xml.etree.ElementTree`, `minidom`, `lxml`).
Vieš tak XML **čítať, upravovať, vytvárať aj validovať** priamo v Pythone.


---

## Základný modul: `xml.etree.ElementTree`

Python obsahuje vstavaný modul **`xml.etree.ElementTree`** na základnú prácu s XML.

---

## 1. Načítanie a čítanie XML

### Ukážka XML súboru (ulož ho ako `people.xml`):

```xml
<data>
    <person>
        <name>Janko</name>
        <age>30</age>
    </person>
    <person>
        <name>Eva</name>
        <age>25</age>
    </person>
</data>
```

### Kód na čítanie XML:

```python
import xml.etree.ElementTree as ET

tree = ET.parse('people.xml')      # načítaj XML súbor
root = tree.getroot()              # získaj koreňový element

for person in root.findall('person'):
    name = person.find('name').text
    age = person.find('age').text
    print(f"Meno: {name}, Vek: {age}")
```

**Vysvetlenie:**

* `ET.parse()` načíta XML súbor.
* `getroot()` získa hlavný uzol (root).
* Pomocou `findall()` a `find()` sa prechádzajú vnorené elementy.

---

## 2. Vytvorenie nového XML súboru

### Kód na vytvorenie XML a uloženie do súboru:

```python
import xml.etree.ElementTree as ET

data = ET.Element('data')

person1 = ET.SubElement(data, 'person')
ET.SubElement(person1, 'name').text = 'Janko'
ET.SubElement(person1, 'age').text = '30'

person2 = ET.SubElement(data, 'person')
ET.SubElement(person2, 'name').text = 'Eva'
ET.SubElement(person2, 'age').text = '25'

tree = ET.ElementTree(data)
tree.write('novi_ludia.xml', encoding='utf-8', xml_declaration=True)
```

---

## 3. Úprava existujúceho XML

Pridajme osobu do existujúceho XML:

```python
import xml.etree.ElementTree as ET

tree = ET.parse('people.xml')
root = tree.getroot()

# Pridanie novej osoby
new_person = ET.SubElement(root, 'person')
ET.SubElement(new_person, 'name').text = 'Peter'
ET.SubElement(new_person, 'age').text = '28'

tree.write('people.xml', encoding='utf-8', xml_declaration=True)
```

---

## 4. Vyhľadávanie a úprava údajov v XML

Nájdi osobu podľa mena a zmeň jej vek:

```python
import xml.etree.ElementTree as ET

tree = ET.parse('people.xml')
root = tree.getroot()

for person in root.findall('person'):
    name = person.find('name').text
    if name == 'Eva':
        person.find('age').text = '26'  # aktualizuj vek

tree.write('people.xml', encoding='utf-8', xml_declaration=True)
```

---

## 5. Odstránenie elementu z XML

Vymaž osobu podľa mena:

```python
import xml.etree.ElementTree as ET

tree = ET.parse('people.xml')
root = tree.getroot()

for person in root.findall('person'):
    name = person.find('name').text
    if name == 'Janko':
        root.remove(person)

tree.write('people.xml', encoding='utf-8', xml_declaration=True)
```

---

## 6. Čítanie XML z reťazca

Ak máš XML priamo v kóde ako reťazec:

```python
import xml.etree.ElementTree as ET

xml_data = """
<data>
    <person>
        <name>Janko</name>
        <age>30</age>
    </person>
</data>
"""

root = ET.fromstring(xml_data)
for person in root.findall('person'):
    print(person.find('name').text)
```

---

## Užitočné tipy

* **ElementTree** je vhodné na jednoduché XML.
* Pre zložité alebo validované XML môžeš použiť knižnice ako `lxml` alebo `xml.dom.minidom`.
* Pri veľkých XML zváž použitie iterátorov (`ET.iterparse()`).

---

## Zhrnutie

* Na prácu s XML použi modul `xml.etree.ElementTree`
* Vieš XML čítať, vytvárať, upravovať aj mazať elementy
* Ukladať XML do súborov cez `tree.write()`
* Pracovať môžeš aj priamo s reťazcami obsahujúcimi XML

---

## 🏷️ Čo je XML schéma (schema)?

**XML schéma** (XML Schema Definition, XSD) je dokument, ktorý presne popisuje, akú štruktúru a typy údajov má mať platný XML súbor.
Pomocou schémy vieš **vynútiť pravidlá**: ktoré elementy sú povinné, aký typ dát môžu obsahovať, poradie elementov, atribúty a podobne.

### Príklad: časť jednoduchej XSD schémy

```xml
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="person">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="name" type="xs:string"/>
        <xs:element name="age" type="xs:integer"/>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

> **Takýto XSD súbor opisuje napríklad, že každá osoba musí mať meno (string) a vek (celé číslo).**

---

## ✅ Validácia XML

**Validácia XML** znamená overenie, či je konkrétny XML dokument v súlade so zadanou schémou (XSD, DTD).
Validácia ti dáva istotu, že:

* chýbajúce, nesprávne alebo neznáme elementy sa odhalia už pri načítaní súboru,
* XML je vhodné na automatizované spracovanie a znižuje riziko chýb.

### Typy validácie:

* **DTD** (Document Type Definition) – starší, jednoduchší spôsob validácie.
* **XSD** (XML Schema Definition) – modernejšie, typovo presnejšie, podporuje dátové typy, podmienky, rozsahy hodnôt.

#### Príklad validácie v Pythone (s knižnicou `lxml`):

```python
from lxml import etree

# Načítaj schému
with open("schema.xsd") as xsd_file:
    schema_root = etree.parse(xsd_file)
schema = etree.XMLSchema(schema_root)

# Načítaj XML
with open("osoby.xml") as xml_file:
    xml_doc = etree.parse(xml_file)

# Overenie validity
if schema.validate(xml_doc):
    print("XML je platné podľa schémy!")
else:
    print("Chyba: XML nespĺňa schému!")
```

> *Na validáciu podľa XSD v Pythone najčastejšie používaš knižnicu `lxml`.*

---

## 🔄 XSLT – Transformácia XML

**XSLT** (eXtensible Stylesheet Language Transformations) je špeciálny jazyk, pomocou ktorého môžeš **prevádzať XML dokumenty na iné XML, HTML, alebo textové formáty**.
Napríklad vieš z XML vytvoriť pekne naformátovanú webstránku, alebo zmeniť štruktúru údajov pre iný program.

### Príklad: Jednoduchá XSLT šablóna

```xml
<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

   <xsl:template match="/">
      <html>
      <body>
         <h2>Zoznam osôb</h2>
         <ul>
            <xsl:for-each select="osoby/osoba">
               <li><xsl:value-of select="meno"/> (<xsl:value-of select="vek"/>)</li>
            </xsl:for-each>
         </ul>
      </body>
      </html>
   </xsl:template>
</xsl:stylesheet>
```

### Transformácia XML cez XSLT v Pythone (pomocou `lxml`):

```python
from lxml import etree

dom = etree.parse("osoby.xml")
xslt = etree.parse("template.xslt")
transform = etree.XSLT(xslt)
novy_dokument = transform(dom)
print(str(novy_dokument))
```

> **Takto si vieš v Pythone automatizovane „preklopiť“ XML do ľubovoľného formátu – napríklad na HTML stránku.**

---

## Zhrnutie

* **Schéma (XSD, DTD)** opisuje, *ako má vyzerať* platné XML.
* **Validácia** overí, *či konkrétny XML dokument* naozaj zodpovedá svojej schéme.
* **XSLT** ti umožňuje *automaticky meniť štruktúru alebo formát* XML, napríklad pre export, prezentáciu alebo výmenu dát medzi rôznymi systémami.

---

