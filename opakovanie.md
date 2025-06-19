# napis program ktory ziska z inputu cislo a zisti ci je parne alebo nepárne

```python
cislo = int(input("Zadaj cislo: "))
if cislo % 2 == 0:
    print(f"{cislo} je parne cislo.")
else:
    print(f"{cislo} je nepárne cislo.")
```

# napis program ktory ziska z inputu cislo a vypise jeho mocninu

```python
cislo = int(input("Zadaj cislo: "))
mocnina = int(input("Zadaj mocninu: "))

print(cislo ** mocnina)
```


# napis program ktory zisti ci je zadane slovo palindrom

```python
def je_palindrom(slovo):
    slovo = slovo.lower()  # Pre   jednoduchost ignorujeme velkost pismen
    return slovo == slovo[::-1]
slovo = input("Zadaj slovo: ")
if je_palindrom(slovo):
    print(f"{slovo} je palindrom.")
else:
    print(f"{slovo} nie je palindrom.")
```

# napis program ktory vypise hviezdicky obratenu pyramidu
