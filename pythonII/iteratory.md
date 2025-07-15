# Python – Iterátory

Iterátor je objekt, cez ktorý sa dá prechádzať (iterovať), čiže umožňuje prejsť všetky jeho hodnoty. Technicky je iterátor objekt implementujúci protokol iterátora (`__iter__()` a `__next__()`) 

---

## Iterátor vs. Iterable

Objekty ako zoznamy (`list`), n-tice (`tuple`), slovníky (`dict`) a množiny (`set`) sú **iterables** – dá sa z nich získať iterátor.

### Príklad

```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
```

Rovnako sa dá iterovať aj reťazcami:

```python
mystr = "banana"
myit = iter(mystr)

print(next(myit))  # 'b'
print(next(myit))  # 'a'
# a tak ďalej...
```

Tieto príklady ukazujú, že reťazce sú tiež **iterable**, poskytujúci iterátor cez `iter()` .

---

## Použitie `for` cyklu

`for` cyklus automaticky vytvorí iterátor a opakovane volá `next()`:

```python
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

mystr = "banana"
for ch in mystr:
    print(ch)
```

Tento prístup využíva interný mechanizmus volania `__iter__()` a `__next__()` .

---

## Vytvorenie vlastného iterátora

Ak chceš, aby tvoja trieda fungovala ako iterátor, implementuj obe metódy `__iter__()` a `__next__()`.

### Príklad

Iterátor, ktorý postupne vracia čísla od 1 vyššie:

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3
# ...
```

Tu metóda `__iter__()` vracia samotný objekt (aj s inicializáciou), a `__next__()` vracia ďalšiu hodnotu .

---

## `StopIteration`

Ak nám dochádzajú hodnoty, mali by sme ukončiť iteráciu pomocou výnimky `StopIteration`.

### Príklad

Zastavenie po 20 iteráciách:

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)  # vytlačí čísla 1 až 20, potom skončí
```

Toto zabezpečí, že iterácia sa ukončí, keď `a` presiahne 20.


