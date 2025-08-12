# mame tajne cislo, vyzveme pouzivatela hadat, ak uhadne , pochvalime ho
# ak neuhadne tak ho vyzveme hadat znovu
import random
tajne_cislo = random.randint(0,100)

pocitadlo_pokusov = 1
cislo = int(input('Hadaj cislo (0-100): '))

while cislo != tajne_cislo:
    pocitadlo_pokusov += 1
    if cislo < tajne_cislo:
        print('Hladane cislo je vacsie')
    else:
        print('Hladane cislo je mensie')
    cislo = int(input('Znova hadaj cislo: '))


print("Super, zvladol si to na " + str(pocitadlo_pokusov) + ' pokusov.')

