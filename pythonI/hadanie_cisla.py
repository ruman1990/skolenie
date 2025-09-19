# mame tajne cislo, vyzveme pouzivatela hadat, ak uhadne , pochvalime ho
# ak neuhadne tak ho vyzveme hadat znovu
import random

secret_value = random.randint(1,100)
counter = 0

while True:
    cislo = int(input('Hadaj cislo '))
    if cislo > secret_value:
        print('hladaj mensie')
    elif cislo < secret_value:
        print('hladaj vacsie')
    else:
        print('Uhadol si, super!')
        break
    counter += 1
    if counter == 7:
        print('Prehral si, minul si vsetkych 7 pokusov')
        break