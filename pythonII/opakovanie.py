# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
x = 'python'

def otoceny_string(s):
    return s[::-1]

print(otoceny_string(x))

# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
# range
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i,end=" ")
    i += 1

print()
for x in range(2,51,2):
    print(x,end=" ")

print()
# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
rok = 2026

def is_priestupny(r):
    if (r % 4 == 0 and r % 100 != 0) or (r % 400 == 0):
        return True
    else:
        return False
    
print(is_priestupny(rok))

#rok = int(input("Zadaj rok: "))


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]
print(max(y))

naj = 0
for x in y:
    if x > naj:
        naj = x

print(naj)


# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"
print(slovo[:5])
print(slovo[-3:])


# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
zoznam = ["jablko","banan","hruska"]

zoznam.append("pomaranc")

if "jablko" in zoznam:
    zoznam.remove("jablko")

print(zoznam)

# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"
print(retazec[1::2])


# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]

def funkcia_vyrezania(x):
    zoznam = []
    for x in mena:
        zoznam.append(x[1:])
    return zoznam

print(zoznam)
# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]

zoznam = []
for x in cisla:
    if x >= 0:
        zoznam.append(x)
[print(zoznam)]


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