# Zmena hodnoty konkrétneho prvku (meni sa druhý prvok)
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Zmena rozsahu (slice): nahradenie "banana", "cherry" novými hodnotami
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Nahradenie jedného prvku dvoma novými (rozšíri sa dĺžka)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Nahradenie dvoch prvkov jedným (zosunie sa zvyšok)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Vloženie bez nahradenia pomocou insert(): pridá na tretiu pozíciu
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# -- APPEND: pridanie prvku na koniec zoznamu --
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # výstup: ['apple', 'banana', 'cherry', 'orange']

# -- INSERT: vloženie prvku na konkrétnu pozíciu --
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # výstup: ['apple', 'orange', 'banana', 'cherry']

# -- EXTEND: pridanie prvkov z iného zoznamu --
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# výstup: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# -- EXTEND s iným iterovateľným objektom (tuple) --
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# výstup: ['apple', 'banana', 'cherry', 'kiwi', 'orange']


# -- REMOVE: odstráni prvý výskyt zadanej hodnoty --
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry']

# -- REMOVE: odstráni prvý výskyt "banana", ak sa vyskytuje viackrát --
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry', 'banana', 'kiwi']

# -- POP: odstráni prvok na danom indexe --
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # ['apple', 'cherry']

# -- POP bez indexu: odstráni posledný prvok --
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)  # ['apple', 'banana']

# -- DEL: odstráni prvok na zadanom indexe --
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  # ['banana', 'cherry']

# -- DEL: vymaže celý zoznam --
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)  # už neexistuje – spôsobí chybu NameError

# -- CLEAR: ponechá zoznam, ale vymaže jeho obsah --
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # []


# -- Sort: zoradenie zoznamu textov vzostupne --
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)  # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# -- Sort: zoradenie zoznamu čísel vzostupne --
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)  # [23, 50, 65, 82, 100]

# -- Sort v zostupnom poradí (opak) --
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# -- Sort čísel v zostupnom poradí --
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)  # [100, 82, 65, 50, 23]

# -- Customize sort podľa vzdialenosti od 50 --
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)  # [50, 65, 23, 82, 100]

# -- Case-sensitive sort (veľké písmená majú prednosť) --
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  # napr. ['Kiwi', 'Orange', 'banana', 'cherry']

# -- Case-insensitive zoradenie pomocou str.lower --
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)  # ['banana', 'cherry', 'Kiwi', 'Orange']

# -- Reversed: otočenie poradia prvkov (po sort alebo pôvodne) --
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)  # zoznam v opačnom poradí

# -- JOIN pomocou + operátora --
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Výstup: ['a', 'b', 'c', 1, 2, 3]

# -- JOIN pomocou loopu a append --
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)  # Výstup: ['a', 'b', 'c', 1, 2, 3]

# -- JOIN pomocou extend() --
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Výstup: ['a', 'b', 'c', 1, 2, 3]
