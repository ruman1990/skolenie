# 1. napis program ktory zisti ci je zadane slovo palindrom

# x = 'anna'
# x = 'level'
# x = 'oko'
# x = '12321'
# x = input('Zadaj slovo: ')
# y = x[::-1]

# if y == x:
#     print('je to palindrom')
# else:
#     print('nie je to palindrom')
# 2. napis program ktory vypise hviezdicky obratenu pyramidu
# ziskaj od pouzivatela vstup kolko hviezdiciek
# ```
# *****
# ****

# ***
# **

# *
# ```

# pocet = int(input("Zadaj pocet hviezdiciek: "))
# line = 1
# for x in reversed(range(1,pocet+1)):
#     print('*'*x)
#     if line % 2 == 0:
#         print('')
#     line+=1

# print()
# print()

# while pocet > 0:
#     if line % 3 == 0:
#         print('')
#     else:
#         print('*'*pocet)
#         pocet -= 1
#     line += 1

# 3. Súčet čísel od 1 do N
# Napíš program, ktorý si vypýta číslo N a spočíta súčet čísel od 1 po N pomocou for:
# ```
# # Vstup: N = 5
# # Výstup: Súčet je 15
# ```
# n = int(input('Zadaj cislo: '))

# suma = 0
# for i in range(n+1):
#     suma += i

# print(suma)

# 4. Fibonacciho postupnosť
#    ziskaj od pouzivatela info, aku dlhu postupnost chce a potom ju vypis
# ```
#    # Vstup: n = 7
# # Výstup: 0 1 1 2 3 5 8
# ```
# n = int(input('Zadaj dlzku postupnosti: '))

# a = 0
# b = 1
# for _ in range(n):
#     print(a, end=' ')
#     temp = a + b
#     a = b
#     b = temp

    

# 5. Vytvor jednoduchý program na výpočet BMI (Body Mass Index):
# ```
# Vzorec:         BMI = váha / (výška v metroch)²
# ```

# vyska = int(input("Zadaj vysku"))
# vaha = int(input('Zadaj vahu'))

# bmi = vaha / (vyska/100) ** 2

# print(f'BMI index je {bmi:.2f}')

# 6. napis horizontalnu pyramidu
# ```
#     *
#    ***
#   *****
#  *******
# *********
# ```

n = int(input("zadaj vysku: "))

for i in range(1,n+1):
    medzery = ' ' * (n-i)
    hviezdy = '*' * (2 * i -1)
    print(medzery + hviezdy)
