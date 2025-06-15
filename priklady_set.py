# -- ADD: pridanie jedného prvku pomocou add() --
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # pridá "orange" do množiny

# -- ADD: pokus o pridanie existujúceho prvku (nezmení množinu) --
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)  # množina ostáva nezmenená

# -- UPDATE: pridanie prvkov z inej množiny --
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # pridá všetky ovocie z tropical

# -- UPDATE: pridanie položiek z iného iterovateľného objektu (napr. list) --
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)  # pridá prvky z listu


# -- REMOVE: odstráni prvok, vyhodí chybu, ak neexistuje --
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # napr. {'apple', 'cherry'}

# -- DISCARD: odstráni prvok, ale žiadna chyba, ak neexistuje --
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # napr. {'apple', 'cherry'}

thisset.discard("pineapple")  # pokojne, nikdy nevydá chybu
print(thisset)  # zostáva {'apple', 'cherry'}

# -- POP: odstráni náhodný prvok a vráti ho --
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("Odstránený prvok:", x)
print("Zostávajúca množina:", thisset)

# -- CLEAR: vyprázdni množinu --
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # výstup: set()

# -- DEL: zmaže celú množinu --
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset)  # ← táto línia by vyvolala NameError


# -- union(): vráti novú množinu so všetkými prvkami z oboch množín --
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("union:", set3)

# -- union s operátorom "|" (rôzne množiny) --
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print("union via |:", set3)

# -- union viacerých množín naraz --
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print("union viacerých:", myset)

# -- union set + tuple (iné iterable) --
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print("union so tuple:", z)

# -- update(): pridá prvky inej množiny priamo do existujúcej množiny --
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print("update:", set1)

# -- update s operátorom "|=" --
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x |= y
print("update via |= :", x)

# -- intersection(): vráti novú množinu, ktorá obsahuje len spoločné prvky --
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("intersection:", z)

# -- intersection pomocou "&" operátora --
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
zz = x & y
print("intersection via &:", zz)

# -- intersection_update(): ponechá spoločné prvky v pôvodnej množine --
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print("intersection_update:", x)

# -- difference(): vráti novú množinu s prvkami, ktoré sú len v prvej množine --
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
diff = set1.difference(set2)
print("difference:", diff)

# -- difference pomocou "-" operátora --
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
diff2 = set1 - set2
print("difference via - :", diff2)

# -- symmetric_difference(): vráti novú množinu, ktorá obsahuje len jedinečné prvky z oboch množín --
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
sym = set1.symmetric_difference(set2)
print("symmetric_difference:", sym)

# -- symmetric_difference pomocou "^" operátora --
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
sym2 = set1 ^ set2
print("symmetric_difference via ^:", sym2)

# -- symmetric_difference_update(): ponechá jedinečné prvky v pôvodnej množine --
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("symmetric_difference_update:", x)
