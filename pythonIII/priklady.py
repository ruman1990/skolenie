# 1. List comprehension – vyber zo zoznamu slov tie, ktoré majú viac ako 3 znaky, a preved ich na veľké písmená.
# Vstup: ["ahoj", "svet", "AI", "Python", "ok"]

x = ["ahoj", "svet", "AI", "Python", "ok"]
upper = [i.upper() for i in x if len(i)>3]
print(upper)



# 2. Vnorený list comprehension – rozlož maticu (zoznam zoznamov) na jeden zoznam čísel.
# Vstup: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rozlozene = []
for x in matica:
    for i in x:
        rozlozene.append(i)

rozlozene = [i for x in matica for i in x]
print(rozlozene)

# 3. List comprehension s podmienkou vo vnútri – nahraď záporné čísla nulou, ostatné nechaj.
# Vstup: [-3, -1, 0, 2, 4]
cisla = [-3, -1, 0, 2, 4]
nulove = [x if x>=0 else 0 for x in cisla]
print(nulove)


# 4. List comprehension + lambda + map – zdvojnásob všetky čísla v matici pomocou lambda funkcie.
# Vstup: [[1, 2], [3, 4]]

v = [[1, 2], [3, 4]]



vystup = [list(map(lambda x: x*2,r)) for r in v]
print(vystup)

# 5. List comprehension – vyber mená ľudí starších ako 18 zo zoznamu slovníkov.
# Vstup:
# [
#     {"meno": "Eva", "vek": 17},
#     {"meno": "Jano", "vek": 22},
#     {"meno": "Mato", "vek": 15},
#     {"meno": "Ada", "vek": 31},
# ]
ludia = [
     {"meno": "Eva", "vek": 17},
     {"meno": "Jano", "vek": 22},
     {"meno": "Mato", "vek": 15},
     {"meno": "Ada", "vek": 31},
]
dospeli = [z['meno'] for z in ludia if z['vek']>=18]
print(dospeli)


# 6. Lambda vo funkcii sorted – zorad slová podľa dĺžky zostupne.
# Vstup: ["ahoj", "python", "je", "super"]

v =  ["ahoj", "python", "je", "super"]

print(sorted(v,key=lambda w: len(w),reverse=True))


# 7. List comprehension + lambda + zip – sčítaj po dvojiciach hodnoty z dvoch zoznamov.
# Vstup: [1, 2, 3] a [10, 20, 30]

a = [1, 2, 3]
b = [10, 20, 30]

sums = [(lambda x,y : x+y)(x,y) for x,y in zip(a,b)]
print(sums)

