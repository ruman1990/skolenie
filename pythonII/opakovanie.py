# # Opakovanie – Python, 2. kurz
# # Úlohy na precvičenie (bez riešení, ale s príkladovými vstupmi)

# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
# text = "python"

# def otoc_string(s):
#     return s[::-1]

# print(otoc_string(text))

# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)

# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# rok = 2024

# def priestupny(x):
#     if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
#         print("priestupny")
#     else:
#         print("nepriestupny")

# priestupny(rok)

# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
# zoznam_cisel = [3, 1, 9, 7, 5]

# def max_cislo(zoznam):
#     return max(zoznam)

# print(max(zoznam_cisel))

# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.
# meno = "Ján"
# vek = 21
# # Alebo: meno = "Eva", vek = 15
# if vek>17:
#     print("dospely")
# else:
#     print("mladistvy")

# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
# slovo = "programovanie"
# print(slovo[:5])
# print(slovo[-3:])

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
# ovocie = ["jablko", "banán", "hruška"]
# # Pridať: "pomaranč"
# # Odstrániť: "banán"
# ovocie.append("pomaranc")
# ovocie.remove("banán")
# print(ovocie)

# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
# retazec = "programovanie"
# # Výsledok by mal byť "rraoin"
# print(retazec[1::2])

# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
# 2. Vlož číslo 99 na tretie miesto.
# 3. Odstráň posledný prvok.
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.
# cisla = list(range(1, 11))
# cisla.insert(2,99)
# print(cisla)
# cisla.pop()
# if 5 in cisla:
#     print("je tam",cisla.index(5))

# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
# mena = ["Martin", "Eva", "Jozef"]
# # Výsledok: ["artin", "va", "ozef"]
# def vyrez(zoznam):
#     vysledok = []
#     for m in mena:
#         vysledok.append(m[1:])
#     return vysledok

# print(vyrez(mena))

# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]


# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
# vetas_medzerami = "   Python je super!   "

# print(vetas_medzerami.strip())

# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
# vstup = "12345"
# # alebo vstup = "12ab45"
# print(vstup.isnumeric())

# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
# cele_meno = "jan novak"
# # Výstup: "Jan Novak"
# print(cele_meno.swapcase())

# 15. Kombinovaný príklad (strip, title, isnumeric)
# Program prijme meno s medzerami a vek (ako reťazec), odstráni medzery, meno naformátuje správne a skontroluje, či vek je číslo.
input_meno = "  peter veliky  "
input_vek = " 25 "

meno = input_meno.strip().title()
vek = input_vek.strip().title()

if vek.isnumeric():
    print("spravne zadane")