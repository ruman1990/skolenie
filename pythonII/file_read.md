

# 🗂️ Python – Otvorenie súboru

## Otvorenie súboru na serveri

Predpokladajme, že máš súbor **`demofile.txt`** v rovnakom adresári ako tvoj Python skript:

```
Hello! Welcome to demofile.txt  
This file is for testing purposes.  
Good Luck!
```

Na jeho otvorenie použiješ vstavanú funkciu `open()`, ktorá **vráti file objekt**, z ktorého potom môžeš čítať pomocou metódy `read()`:

### Príklad

```python
f = open("demofile.txt")
print(f.read())
```


Ak máš súbor v inom priečinku, musíš zadať cestu:

### Príklad

```python
f = open("D:\\myfiles\\welcome.txt")
print(f.read())
```



---

## Použitie `with`–bloku

Doporučuje sa použiť `with open(...) as f:`, ktorý **automaticky uzatvorí súbor**, keď ukončíš blok:

```python
with open("demofile.txt") as f:
    print(f.read())
```



---

## Uzavretie súboru (Close Files)

Ak nepoužiješ `with`, musíš súbor po použití zavrieť pomocou `close()`:

```python
f = open("demofile.txt")
print(f.readline())
f.close()
```

Je to dôležité pre uvoľnenie systémových prostriedkov a správne ukladanie dát, pretože zmeny sa pri buffrovaní nemusia prejaviť, kým súbor nezavrieš.


---

## Čítanie časti súboru

Metódu `read()` môžeš použiť aj s parametrom, ktorý určí, koľko **znakov** číta:

```python
with open("demofile.txt") as f:
    print(f.read(5))  # prečíta prvých 5 znakov
```



---

## Čítanie po riadkoch

### Jednotlivý riadok

```python
with open("demofile.txt") as f:
    print(f.readline())
```

Toto prečíta **iba prvý riadok**.


### Dva riadky

```python
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
```

Prečíta prvé dva riadky.


### Cez celý súbor

Najpohodlnejšie je použiť **cyklus**, ktorý prejde celý súbor riadok po riadku:

```python
with open("demofile.txt") as f:
    for line in f:
        print(line)
```



---

## ✅ Zhrnutie

* Na otvorenie súboru použiješ `open("cesta_k_súboru", "mód")`, kde mód býva napr. `r` pre čítanie (predvolené).
* `read()` prečíta celý obsah, `read(n)` len n znakov.
* `readline()` prečíta jeden riadok.
* Používaj `with open(...) as f:` pre automatické zatvorenie súboru.
* Ak nepoužiješ `with`, zavri súbor pomocou `f.close()`.

---
