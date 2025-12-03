# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").

x = "Python"

print(x[::-1])



# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
rok = 2000

def priestupny_rok(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    else:
        return False

print()
print(priestupny_rok(rok))

# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]

def najvacsie_cislo(zoznam):
    najvacsie = zoznam[0]
    for cislo in zoznam:
        if cislo > najvacsie:
            najvacsie = cislo
    return najvacsie

print(max(y))

print(najvacsie_cislo(y))

# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.

def vekova_skupina(meno, vek):
    if vek >= 18:
        return f"{meno} je dospelý."
    else:
        return f"{meno} je mladistvý."

print(vekova_skupina("Anna", 20))

# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"

print(slovo[:5])
print(slovo[-3:])


# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
ovocie = ["jablko", "banán", "hruška"]

ovocie.append("pomaranč")

ovocie.remove("banán")
ovocie.pop(0)

print(ovocie)

# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"
def vynechaj_parne_znaky(retazec):
    return retazec[1::2]

print(vynechaj_parne_znaky(retazec))


# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
cisla = list(range(1, 11))
# 2. Vlož číslo 99 na tretie miesto.
cisla.insert(2, 99)
# 3. Odstráň posledný prvok.
cisla.pop()
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.
if 5 in cisla:
    print(cisla.index(5))

# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]
for i, x in enumerate(mena): 
    mena[i] = x[1:]
# # Výsledok: ["artin", "va", "ozef"]
print(mena)
# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]

x = []
for i in cisla:
    if i >= 0:
        x.append(i)

# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
# vetas_medzerami = "   Python je super!   "
# print(vetas_medzerami)

vetas_medzerami = "   Python je super!   "
print(vetas_medzerami.strip())


# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"

print(vstup.isnumeric())  # Výstup: True

vstup = "12ab45"

print(vstup.isnumeric())  # Výstup: False

# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
# # Výstup: "Jan Novak"
print(cele_meno.title())

