# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
x = 'python'

def otoc_string(retazec):
    vysledok = ""
    for znak in retazec:
        vysledok = znak + vysledok
 
    return vysledok
 
x = 'string'
print(otoc_string(x))

def otoc_string(s):
    return s[::-1]

print(x[::-1])

# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
# range
for x in range(2,51,2):
    print(x,end=" ")

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
print()

rok = 2026

def priestupny_rok(r):
    if r % 4 == 0 and ( r % 100 != 0 or r % 400 == 0 ):
        print("Je priestupny")
    else:
        print("Nie je priestupny")

priestupny_rok(rok)

# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]

def najdi_max(zoznam):
    najvacsie = zoznam[0]
 
    for cislo in zoznam:
        if cislo > najvacsie:
            najvacsie = cislo
 
    return najvacsie
 
print(najdi_max(y))
max(y)

# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"
print(slovo[:5])
print(slovo[-3:])

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
zoznam = ["jablko","banan","hruska"]
zoznam.append("mandarinka")
zoznam.insert(0,"pomaranc")
zoznam.remove("jablko")
zoznam.pop(1)

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
for x in mena:
    vysledok.append(x[1:])
print(vysledok)

print([x[1:] for x in mena])

#print([x for x in cisla if x>=0])
# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
vetas_medzerami = "   Python je super!   "
print(vetas_medzerami.strip())
# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"
print(vstup.isdigit())
# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
print(cele_meno.title())
