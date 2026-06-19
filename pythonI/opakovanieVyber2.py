# 1. priklad
# Napíš krátky program, ktorý:

# vypýta si dve čísla od používateľa,
# vypočíta ich súčet, rozdiel, súčin a podiel,
# vypíše výsledky.
# number1 = int(input("Zadaj prve cislo: "))
# number2 = int(input("Zadaj druhe cislo: "))

# print(f"Sucet je: {number1+number2}")
# print(f"Rozdiel je: {number1-number2}")
# print(f"Sucin je: {number1*number2}")
# print(f"Podiel je: {number1/number2}")

# 2. priklad
#Vytvor jednoduchý program na výpočet BMI (Body Mass Index):
#Vzorec:         BMI = váha / (výška v metroch)²
# interpretacia
# < 18 podvaha
# >= 18 < 25 normalna vaha
# >= 25 nadvaha
# >= 30 obezita
# vaha = int(input("Zadaj vahu: "))
# vyska = int(input("Zadaj vysku v centimetroch: "))

# #bmi = vaha / vyska**2
# bmi = vaha / (vyska/100)**2
# print(f"Hodnota bmi je : {bmi:10.2f}")
# if bmi < 18:
#     print("podvaha")
# elif bmi >=18 and bmi < 25:
#     print("normalna vaha")
# elif bmi >= 25 and bmi < 30:
#     print("nadvaha")
# else:
#     print("obezita")


# 6. napis horizontalnu pyramidu
# ```
#     *
#    ***
#   *****
#  *******
# *********
# ```
vyska = int(input("Zadaj vysku pyramidy: "))

for i in range(1,vyska+1):
    print(f"{' '*(vyska-i)}{"*"*(2*i-1)}")