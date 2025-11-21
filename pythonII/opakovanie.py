# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").

x = "Python"

x[2:]

print(x[::-1])


# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
i = 1

while i <= 50:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1

for x in range(1,51):
    if x % 2 == 0:
        print(x, end=' ')

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
rok = 2024

if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
    print(f'Rok {rok} je priestupny.')
else:
    print(f'Rok {rok} nie je priestupny.')


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
y = [9,1,5,3,7,25,2]

print(max(y))

# print(najvacsie_cislo(y))

# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.

random_number =5
x = 'ss'




# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"

print(slovo[:25])  # prvých 5 znakov
print(slovo[-3:])  # posledné 3 znaky

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
# ovocie = ["jablko", "banán", "hruška"]


# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"

retazec[1::2]


# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
# 2. Vlož číslo 99 na tretie miesto.
# 3. Odstráň posledný prvok.
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.

# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]

# # Výsledok: ["artin", "va", "ozef"]

# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]



# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
# vetas_medzerami = "   Python je super!   "
# print(vetas_medzerami)



# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"

vstup = "12ab45"


# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
# # Výstup: "Jan Novak"


