# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").

#x = "Python"
# x = input("Zadaj string: ")

# def otoc_string(vstup):
#     return vstup[::-1]

# print(otoc_string(x))



# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)

# for x in range(2,51,2):
#     print(x,end=" ")

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# # priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
# rok = 2024

# def je_priestupny(r):
#     if r % 4 == 0 and (r % 100 != 0 or r % 400 == 0):
#         return True
#     else:
#         return False
    
# print(je_priestupny(rok))

# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
# y = [9,1,5,3,7,25,2]

# def najvacsie_cislo(zoznam):
#     naj = zoznam[0]
#     for x in zoznam:
#         if x > naj:
#             naj = x
#     return naj

# print(najvacsie_cislo(y))

# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.



# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
# slovo = "programovanie"

# prve = slovo[:5]
# posledne = slovo[-3:]

# print(f'{prve} {posledne}')

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
# ovocie = ["jablko", "banán", "hruška"]
# print(ovocie)
# ovocie.append("broskyna")
# print(ovocie)

# ovocie.remove("jablko")
# print(ovocie)
# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
# retazec = "programovanie"

# print(retazec[1::2])

# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
# 2. Vlož číslo 99 na tretie miesto.
# 3. Odstráň posledný prvok.
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.

# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]
print(mena[0][1:])
# # Výsledok: ["artin", "va", "ozef"]

# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]



# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
# vetas_medzerami = "   Python je super!   "
# print(vetas_medzerami)
# print(vetas_medzerami.strip())


# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"
print(vstup.isnumeric())
vstup = "12ab45"
print(vstup.isnumeric())

# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
# # Výstup: "Jan Novak"
print(cele_meno.title())

