# Úvod

## Python

Python je všeobecný, dynamický, objektovo orientovaný programovací jazyk.
Jeho dizajn kladie dôraz na produktivitu programátora a čitateľnosť kódu.

Python pôvodne vyvinul Guido van Rossum.
Prvá verzia bola vydaná v roku 1991.

Python bol inšpirovaný týmito jazykmi:

* ABC
* Haskell
* Java
* Lisp
* Icon
* Perl

Python je vysokoúrovňový, všeobecný, multiplatformový, interpretovaný jazyk.
Spravuje ho veľká komunita dobrovoľníkov po celom svete. Python je open source.

Python je minimalistický jazyk. Jednou z jeho najvýraznejších vlastností je, že nepoužíva bodkočiarky ani zátvorky; namiesto toho používa odsadenie.

Python podporuje viaceré štýly programovania a nevnucuje programátorovi jediný paradigmát. Podporuje procedurálne, objektovo orientované aj funkcionálne programovanie.

Oficiálna webstránka jazyka Python je [python.org](https://python.org)

![Python](images/python.jpg)

## Základné charakteristiky

1. **Vysoká úroveň a čitateľnosť**: Python je navrhnutý pre čitateľnosť kódu.
2. **Interpretovaný**: Python beží na interpreteri, čo umožňuje okamžité spustenie kódu hneď, ako ho napíšete.
3. **Dynamické typovanie**: Nemusíte explicitne deklarovať typy premenných; Python ich určí za vás za behu programu.
4. **Významné odsadenie**: Python používa odsadenie (biele znaky) na definovanie rozsahu, ako sú slučky, funkcie a triedy. Žiadne zátvorky nie sú potrebné.
5. **Univerzálne použitie**:

   * Webový vývoj (serverová časť)
   * Vývoj softvéru
   * Matematika a vedecké výpočty
   * Scripting systému
   * Spracovanie veľkých dát
6. **Multiplatformovosť**: Python funguje na rôznych platformách (Windows, Mac, Linux, Raspberry Pi a pod.).
7. **Menej riadkov kódu**: Python umožňuje písať programy s menším počtom riadkov oproti mnohým iným jazykom.

## Implementácie Pythonu

Formálne je Python špecifikácia jazyka. Existujú tri hlavné implementácie:

* **CPython**: napísaný v jazyku C, najrozšírenejšia implementácia. Keď sa povie "Python", zvyčajne sa myslí CPython.
* **IronPython**: napísaný v C#, súčasť .NET rámca.
* **Jython**: implementácia v Jave, prekladá Python do Java bytekódu a spúšťa ho JVM.

V tomto návode budeme pracovať s CPython.

## Popularita

Python patrí medzi najpopulárnejšie programovacie jazyky. Viaceré prieskumy ho radia do prvej desiatky. Medzi veľmi známe projekty v Pythone patria:

* distribuovaný nástroj na správu verzií **Mercurial**
* webový framework **Django**
* GUI knižnica **PyQt**
* správca balíčkov **Yum**

[Prieskum Stackoverflow](https://survey.stackoverflow.co/2023/#programming-scripting-and-markup-languages)
[Prieskum JetBrains](https://www.jetbrains.com/lp/devecosystem-2023/python/)

## Učebné materiály

**Knihy:**

* [Python Crash Course](https://www.amazon.co.uk/Python-Crash-Course-3Rd-Matthes/dp/1718502702)

**Videá:**

* [Python for Everyone: From Zero to Hero 6 Hours Complete Course](https://www.youtube.com/watch?v=JZDQKj9BOoc)
* [Python Full Course for Beginners](https://www.youtube.com/watch?v=H2EJuAcrZYU)

## Python skripty

Každý skript v Unixe začína tzv. **shebang** (prvé dva znaky `#!`), za ktorými nasleduje cesta k interpretovi. Shebangy na Windows nefungujú, no je dobrá prax ich pridať aj tam, ak očakávame spustenie na Unixe.

```python
# simple.py

print("The Python tutorial")
```

Tento skript vypíše na konzolu reťazec "The Python tutorial". Python skripty majú príponu `.py`.

```
$ which python
/usr/bin/python
```

Pomocou príkazu `which` zisťujeme cestu k Python interpretovi.

Python skripty môžeme spúšťať dvoma spôsobmi:

```
$ python simple.py
The Python tutorial
```

alebo

```
$ chmod +x simple.py
$ ./simple.py
The Python tutorial
```

Príkazom `chmod +x` súbor spravíme spustiteľným.

## Zoznamy (Lists)

Python zoznam je základná dátová štruktúra na ukladanie usporiadaných prvkov. Kľúčové vlastnosti:

* **Usporiadané**: poradie prvkov zostáva zachované.
* **Menniteľné**: prvky môžeme pridať, zmeniť alebo odstrániť.
* **Kombinované typy**: v jednom zozname môžu byť rôzne typy prvkov.

```python
vals = [1, 2, 3, 4, 5]
print(vals)

for val in vals:
    print(val)

words = ['sky', 'book', 'war', 'cup']
print(words)
```

## Čítanie vstupu

Funkcia `input` načíta riadok vstupu, odstráni koncový newline a vráti ho ako reťazec.

```python
# read_input.py

name = input("Enter your name:")
print("Hello", name)
```

Príklad vypíše prompt a prečíta meno od používateľa.

```
$ ./read_input.py
Enter your name:Peter
Hello Peter
```

## Argumenty z príkazového riadka

Argumenty sú dostupné v zozname `sys.argv`, kde `argv[0]` je názov skriptu.

```python
# command_line_arguments.py
import sys

print("Script name:", sys.argv[0])
print("Arguments:", end=" ")

for arg in sys.argv[1:]:
    print(arg, end=" ")

print()
```

```
$ ./command_line_arguments.py 1 2 3
Script name: ./command_line_arguments.py
Arguments: 1 2 3
```

## Náhodné hodnoty

Na prácu s náhodnosťou slúži modul `random`.

```python
import random

r1 = random.randint(0, 10)
print(r1)

r2 = random.randrange(500, 1000, 50)
print(r2)

vals = [11, 22, 33, 44, 55, 66, 77]
r3 = random.choice(vals)
print(r3)

words = ['sky', 'atom', 'war', 'cup', 'book', 'zebra', 'moon']
r4 = random.sample(words, 2)
print(r4)
```
