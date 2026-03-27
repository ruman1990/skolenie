# number1 = int(input("Zadaj cislo: "))
# number2 = int(input("Zadaj cislo: "))

# print(f'Sucet je {number1 + number2}')
# print(f'Rozdiel je {number1 - number2}')
# print(f'Sucin je {number1 * number2}')
# print(f'Podiel je {number1 / number2}')


# vzorec =  hmotnost / ((vyska/100) ** 2)
# < 18.5 podvaha
# < 25 normal
# < 30 nadvaha
# >= 30 obezita
# hmotnost = int(input("Zadaj hmotnost: "))
# vyska = float(input("Zadaj vysku v metroch: "))

# bmi = hmotnost / (vyska ** 2)

# print(f'Vase BMI je {bmi}')

# if bmi < 18.5:
#     print('podvaha')
# elif bmi < 25:
#     print('normal')
# elif bmi < 30:
#     print('nadvaha')
# else:
#     print('obezita')

#      *     
#     ***
#    *****
#   *******
#  ********* 

x = int(input('zadaj vysku pyramidy: '))

for i in range(1,x):
    print(' ' * (x - 1 - i) + '*' * (2 * i - 1))