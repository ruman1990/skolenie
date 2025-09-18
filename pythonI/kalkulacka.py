# jednoducha kalkulacka
#ziskat od pouzivatela dve cisla a urobit zakladne aritmeticke vypocty


cislo1 = int(input('Zadaj prve cislo '))
cislo2 = int(input('Zadaj druhe cislo '))

print('sucet',cislo1 + cislo2)
print('rozdiel',cislo1 - cislo2)
print('nasobenie',cislo1 * cislo2)
print('delenie',cislo1 / cislo2)
print('celociselne delenie',cislo1 // cislo2)
print('mocnenie',cislo1 ** cislo2)
print('modulo',cislo1 % cislo2)
       
if cislo1 % 2 != 0:
    print('cislo',cislo1,' je neparne')
else:
    print('cislo',cislo1,' je parne')

if cislo2 % 2 == 0:
    print('cislo',cislo2,' je parne')
else:
    print('cislo',cislo2,' je neparne')
