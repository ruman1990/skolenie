# Opakovanie – Python, 2. kurz
# Úlohy na precvičenie (bez riešení, ale s príkladovými vstupmi)

# 1. Otočenie stringu
# Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
text = "python"


# 2. Cykly – párne čísla
# Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# (Príklad: výstup: 2 4 6 ... 50)


# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
rok = 2024


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
zoznam_cisel = [3, 1, 9, 7, 5]


# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.
meno = "Ján"
vek = 21
# Alebo: meno = "Eva", vek = 15


# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"


# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
ovocie = ["jablko", "banán", "hruška"]
# Pridať: "pomaranč"
# Odstrániť: "banán"


# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"
# Výsledok by mal byť "rraoin"


# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
# 2. Vlož číslo 99 na tretie miesto.
# 3. Odstráň posledný prvok.
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.
cisla = list(range(1, 11))


# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]
# Výsledok: ["artin", "va", "ozef"]


# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]


# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
vetas_medzerami = "   Python je super!   "


# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"
# alebo vstup = "12ab45"


# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
# Výstup: "Jan Novak"


# 15. Kombinovaný príklad (strip, title, isnumeric)
# Program prijme meno s medzerami a vek (ako reťazec), odstráni medzery, meno naformátuje správne a skontroluje, či vek je číslo.
input_meno = "  peter veliky  "
input_vek = " 25 "

