# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
x = 'python'

def reverse_string(x):
    return x[::-1]

print(reverse_string(x))


# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
# range

for x in range(2,51,2):
    print(x,end=' ')


print()
# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
rok = 2000

def is_priestupny(x):
    if (x % 4 == 0 and x % 100 !=0) or (x % 400 == 0):
        return True
    else:
        return False

print(is_priestupny(rok))

#rok = int(input("Zadaj rok: "))


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]

naj_cislo = 0
for x in y:
    if naj_cislo < x:
        naj_cislo = x

print(naj_cislo)

print(max(y))


# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"

print(slovo[:5])
print(slovo[-3:])


# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.

zoznam = ["jablko","hruska","ceresna"]

zoznam.append("slivka")
zoznam.insert(0,"broskyna")

zoznam.pop()
zoznam.remove("hruska")
print(zoznam)

# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"
print(retazec[::2])


# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]

vysledok = []
for x in mena:
    vysledok.append(x[1:])
print(vysledok)


# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]
v = []
for x in cisla:
    if x >= 0:
        v.append(x)

print(v)


# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
vetas_medzerami = "   Python je super!   "
print(vetas_medzerami.strip())


# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"
print(vstup.isnumeric())
d = int(vstup)
# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"

print(cele_meno.title())

