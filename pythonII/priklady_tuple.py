# -- Pridanie pomocou sčítania tuplov --
thistuple = ("apple", "banana", "cherry")
y = ("orange",)     # tuple s jedným prvkom (pozri čiarku!)
thistuple = thistuple + y      # spojí tuplu a y
print(thistuple)    # výstup: ('apple', 'banana', 'cherry', 'orange')

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

