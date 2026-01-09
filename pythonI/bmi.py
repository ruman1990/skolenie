# Napíš krátky program, ktorý:

# * vypýta si dve čísla od používateľa,
# * vypočíta ich súčet, rozdiel, súčin a podiel,
# # * vypíše výsledky.
# x = int(input("Zadaj cislo: "))
# y = int(input("Zadaj druhe cislo: "))

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)

# Spravte program, ktory vypocita bmi index
# pouzivatel zada hmotnost a vysku a vy vypisete hodnotu bmi
# a interpretovanie vysledku (normal,nadvaha,obezita)
# vzorec =  hmotnost / ((vyska/100) ** 2)
# < 18.5 podvaha
# < 25 normal
# < 30 nadvaha
# >= 30 obezita
x = int(input("Zadaj hmotnost: "))
y = int(input("Zadaj vysku: "))

bmi = x / (y/100)**2

print(bmi)

if bmi < 18.5:
    print(f'Pri hmotnosti {x} a vyske {y} mas bmi {round(bmi,2)} a to je podvaha')
elif bmi < 25:
    print(f'Pri hmotnosti {x} a vyske {y} mas bmi {round(bmi,2)} a to je normal')
elif bmi < 30:
    print(f'Pri hmotnosti {x} a vyske {y} mas bmi {bmi:8.2f} a to je nadvaha')
else:
    print(f'Pri hmotnosti {x} a vyske {y} mas bmi {round(bmi,2)} a to je obezita')

