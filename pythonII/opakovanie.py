# # Opakovanie – Python, 2. kurz


# # 1. Otočenie stringu
# # Napíš funkciu, ktorá prijme reťazec a vráti ho v opačnom poradí (napr. "python" → "nohtyp").
text = "python"
def otoc_string(s):
    return s[::-1]

print(otoc_string(text))

# # 2. Cykly – párne čísla
# # Napíš program, ktorý vypíše všetky párne čísla od 1 do 50 na jeden riadok, oddelené medzerou.
# # (Príklad: výstup: 2 4 6 ... 50)
for i in range(1,51):
    if i % 2 == 0:
        print(i,end=' ')

print('')
# 3. Podmienený príkaz – priestupný rok
# Napíš funkciu, ktorá zistí, či je zadaný rok priestupný.
# priestupny je ked: delitelny 4 a zaroven nedelitelny 100, vynimka je delitelnost 400
rok = 2024

def je_priestupny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        print('je priestupny')
    else:
        print('nie je priestupny')

je_priestupny(rok)


# 4. Funkcia – najväčšie číslo zo zoznamu
# Napíš funkciu, ktorá prijme zoznam čísel a vráti najväčšie číslo v zozname.
zoznam_cisel = [3, 1, 9, 7, 5]

def naj(z):
    return max(z)

print(naj(zoznam_cisel))

# 5. Funkcia – veková skupina
# Napíš program, ktorý prijme meno a vek, vypíše, či je dospelý alebo mladistvý.
meno = 'Bohumil'
vek = 25

#meno = input('Zadaj meno')
#vek = int(input("Zadaj vek"))

if vek < 18:
    print('je mladistvy')
else:
    print('je dospely')



# 6. Vyrezávanie (slicing) stringu
# Z reťazca vypíš len prvých 5 znakov a posledné 3 znaky.
slovo = "programovanie"

print(slovo[:5])
print(slovo[-3:])

# 7. Pridávanie a odoberanie prvkov zo zoznamu
# Vytvor zoznam s tromi ovocnými názvami. Pridaj do zoznamu ďalšie ovocie, potom jedno ovocie zo zoznamu vymaž a vypíš výsledný zoznam.
ovocie = ["jablko", "banán", "hruška"]

ovocie.append('pomaranc')
#ovocie.pop(0)
ovocie.remove('banán')
print(ovocie)


# 8. Zložitejšie vyrezávanie stringov
# Funkcia, ktorá vráti reťazec s vynechanými znakmi na párnych indexoch.
retazec = "programovanie"

def vynechaj_parne(text):
    return text[1::2]

print(vynechaj_parne(retazec))


# 9. Práca so zoznamom – vkladanie, odoberanie a vyhľadávanie
# 1. Vytvor zoznam čísel od 1 do 10.
# 2. Vlož číslo 99 na tretie miesto.
# 3. Odstráň posledný prvok.
# 4. Zisti, či je v zozname číslo 5 a ak áno, vypíš jeho index.
zoznam = list(range(1,11))
zoznam.insert(2,99)
zoznam.pop()
# 1 ,2 ,3 ,4,5
if 5 in zoznam:
    print(zoznam.index(5))

# vysledok je 5

# 10. Funkcia – práca so zoznamom mien
# Funkcia, ktorá zo zoznamu mien vyreže z každého mena prvé písmeno.
mena = ["Martin", "Eva", "Jozef"]
# # Výsledok: ["artin", "va", "ozef"]
def vyrez(zoznam):
    vysledok = []
    for meno in zoznam:
        vysledok.append(meno[1:])
    return vysledok

x = vyrez(mena)
print(x)

# 11. Odstránenie záporných čísel zo zoznamu
# Zo zoznamu čísel odstráň všetky záporné čísla.
cisla = [5, -3, 8, -1, 0, 2, -7, 6]

cisla_bez = []
for x in cisla:
    if x>=0:
        cisla_bez.append(x)

print(cisla_bez)


# 12. Použitie strip()
# Odstráň medzery na začiatku a na konci reťazca.
vetas_medzerami = "   Python je super!   "

print(vetas_medzerami.strip())


# 13. Použitie isnumeric()
# Skontroluj, či reťazec obsahuje iba číslice.
vstup = "12345"
vstup = "12ab45"
if vstup.isnumeric():
    print("je numeric")
else:
    print('nie je numeric')

# 14. Použitie title()
# Zmena mena a priezviska na formát s veľkými začiatočnými písmenami.
cele_meno = "jan novak"
# # Výstup: "Jan Novak"
print(cele_meno.title())

# 15. Kombinovaný príklad (strip, title, isnumeric)
# Program prijme meno s medzerami a vek (ako reťazec), odstráni medzery, meno naformátuje správne a skontroluje, či vek je číslo.

meno = ' Jan '
vek = 25

x = input("Zadaj meno a vek s medzerami: ")
udaje = x.strip().split(' ')

if udaje[1].strip().isnumeric():
    print(f'Meno {udaje[0].title()} a vek {udaje[1]}')


