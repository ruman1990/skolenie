# -- Definovanie funkcie bez parametrov --
def my_function():
    print("Hello from a function")

# Volanie funkcie
my_function()

# -- Funkcia s jedným parametrom (argument) --
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# -- Funkcia s dvoma parametrami --
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

# -- *args pre neznámy počet pozičných argumentov --
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# -- keyword arguments (argumenty označené mena = hodnota) --
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

# -- **kwargs pre neznámy počet pojmenovaných argumentov --
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")

# -- Predvolená hodnota parametra --
def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# -- Funkcia volaná s argumentom typu zoznam --
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# -- Funkcia vracajúca hodnotu --
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# -- Prázdna funkcia pomocou pass (bez chýb) --
def myfunction():
    pass

# -- Rekurzívna funkcia: výpočet sumy od k po 0 --
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)
