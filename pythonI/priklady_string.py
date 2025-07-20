# -- Základné reťazce --
print("Hello")
print('Hello')

# -- Úvodzovky v reťazci --
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# -- Priradenie reťazca do premennej --
a = "Hello"
print(a)

# -- Viacriadkový reťazec (""" alebo ''') --
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# -- Prístup k znaku cez index --
a = "Hello, World!"
print(a[1])

# -- Iterovanie cez reťazec --
for x in "banana":
    print(x)

# -- Dĺžka reťazca --
a = "Hello, World!"
print(len(a))

# -- Overenie, či reťazec obsahuje určitý text --
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("Yes, 'free' is present.")

# -- Overenie neprítomnosti reťazca --
print("expensive" not in txt)

if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# -- Slicing reťazca --
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

# -- Zmena veľkosti písmen --
a = "Hello, World!"
print(a.upper())
print(a.lower())

# -- Odstránenie medzier --
a = " Hello, World! "
print(a.strip())

# -- Nahradenie znakov --
a = "Hello, World!"
print(a.replace("H", "J"))

# -- Rozdelenie reťazca --
a = "Hello, World!"
print(a.split(","))

# -- Zreťazenie reťazcov --
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)

# -- F-string formátovanie --
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

# -- Formátovanie cez format() --
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)

# -- Vyhľadanie podreťazca cez find() --
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
x = txt.find("e")
print(x)
x = txt.find("e", 5, 10)
print(x)
print(txt.find("q"))  # -1 = nenájdené
# print(txt.index("q"))  # chyba, ak nenájdené

# -- Escape znaky --
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Poznámka: ďalšie escape znaky: \'  \\  \n  \r  \t  \b  \f  \ooo  \xhh


# Ukážka použitia slicing-u reťazcov

# 🔹 Základný slicing: znaky od indexu 2 po 4 (5 nie je zahrnuté)
b = "Hello, World!"
print("b[2:5] ->", b[2:5])  # od 'l' (index 2) po 'o' (index 4)

# 🔹 Slicing od začiatku po pozíciu 5 (5 nezahrnuté)
b = "Hello, World!"
print("b[:5] ->", b[:5])  # "Hello"

# 🔹 Slicing od pozície 2 až do konca
b = "Hello, World!"
print("b[2:] ->", b[2:])  # "llo, World!"

# 🔹 Slicing s negatívnymi indexmi: od -5 (písmeno 'W') po -2 (písmeno 'd', nezahrnuté)
b = "Hello, World!"
print("b[-5:-2] ->", b[-5:-2])  # "Wor"


# -- Zmena na veľké písmená --
a = "Hello, World!"
print(a.upper())  # => "HELLO, WORLD!"

# -- Zmena na malé písmená --
a = "Hello, World!"
print(a.lower())  # => "hello, world!"

# -- Odstránenie medzier na začiatku a konci --
a = " Hello, World! "
print(a.strip())  # => "Hello, World!"

# -- Nahradenie znakov/slov --
a = "Hello, World!"
print(a.replace("H", "J"))  # => "Jello, World!"

# -- Rozdelenie reťazca na zoznam podľa oddeľovača --
a = "Hello, World!"
print(a.split(","))  # => ['Hello', ' World!']

