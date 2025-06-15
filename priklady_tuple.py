# -- Zmena hodnoty v tupli pomocou konverzie na list a späť --
x = ("apple", "banana", "cherry")
y = list(x)        # prevedie tuple na list
y[1] = "kiwi"      # zmení druhý prvok
x = tuple(y)       # prevedie späť na tuple
print(x)           # výstup: ('apple', 'kiwi', 'cherry')

# -- Pridanie prvku do tupli (workaround) --
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")  # pridá nový prvok
thistuple = tuple(y)
print(thistuple)    # výstup: ('apple', 'banana', 'cherry', 'orange')

# -- Pridanie pomocou sčítania tuplov --
thistuple = ("apple", "banana", "cherry")
y = ("orange",)     # tuple s jedným prvkom (pozri čiarku!)
thistuple += y      # spojí tuplu a y
print(thistuple)    # výstup: ('apple', 'banana', 'cherry', 'orange')

# -- Odstránenie prvku (workaround) --
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")   # vymaže 'apple'
thistuple = tuple(y)
print(thistuple)    # výstup: ('banana', 'cherry')

# -- Vymazanie celej tupli pomocou del --
thistuple = ("apple", "banana", "cherry")
del thistuple       # tuple už neexistuje
# print(thistuple)  # toto by vyvolalo chybu NameError


# -- Packing: vytvorenie n-tice --
fruits = ("apple", "banana", "cherry")
print("Packed tuple:", fruits)

# -- Unpacking: rozbalenie n-tice do premenných --
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)   # apple
print(yellow)  # banana
print(red)     # cherry

# -- Unpacking so zvyškom pomocou * (všetko, čo zostane, sa dostane ako zoznam) --
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)   # apple
print(yellow)  # banana
print(red)     # ['cherry', 'strawberry', 'raspberry']

# -- Unpacking s * uprostred (napr. predposledný zostane vo variabilnej časti) --
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)   # apple
print(tropic)  # ['mango', 'papaya', 'pineapple']
print(red)     # cherry


# -- JOIN: spojenie dvoch n-tíc pomocou operátora + --
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("tuple1 + tuple2 =>", tuple3)  # ("a", "b", "c", 1, 2, 3)

# -- MULTIPLY: opakovanie n-tice pomocou operátora * --
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print("fruits * 2 =>", mytuple)
# Výstup: ("apple", "banana", "cherry", "apple", "banana", "cherry")

