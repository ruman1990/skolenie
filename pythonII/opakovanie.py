# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
x = 'python'

print(x[::-1])

c = len(x)
while c > 0:
    c -= 1
    print(x[c],end="")

print()

for a in reversed(x):
    print(a,end="")

# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
# range

print()

for x in range(2,51,2):
    print(x,end=" ")

for x in range(1,51):
    if x % 2 == 0:
        print(x,end=" ")

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
print()

rok = 1900

def je_priestupny(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Je priestupny")
    else:
        print("Nie je priestupny")

je_priestupny(rok)


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]

def maximum(zoznam):
    return max(zoznam)

# def maximum(zoznam):
#     maximalna_hodnota = y[0]
#     for x in y:
#         if maximalna_hodnota < x:
#             maximalna_hodnota = x
#     print(maximalna_hodnota)

print(maximum(y))

# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"

print(slovo[:5])
print(slovo[-3:])

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
zoznam = ["jablko","banan","hruska"]
zoznam.append("pomaranc")

zoznam.pop(0)

print(zoznam)

# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"
#          0123456789
print(retazec[1::2])


# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]
vysledok = []
def vyrezanie(zoznam):
    for x in zoznam:
        vysledok.append(x[0])

vyrezanie(mena)
print(vysledok)
# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]

vysledok = []

for x in cisla:
    if x >= 0:
        vysledok.append(x)

print(vysledok)

#print([x for x in cisla if x>=0])
# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
vetas_medzerami = "   Python je super!   "

print(vetas_medzerami.strip())

# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"

print(vstup.isnumeric())

# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"

print(cele_meno.title())
