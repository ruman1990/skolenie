# mame tajne cislo, vyzveme pouzivatela hadat, ak uhadne , pochvalime ho
# ak neuhadne tak ho vyzveme hadat znovu

# spravme hru, kde hadame tajne cislo
# od pouzivatela si vypytame cislo a ked sa nerovna tajnemu cislu, vyzveme ho aby pokracoval v hadani
# ked uhadne, vypiseme, ze vyhral
import random

tajne_cislo = random.randint(1,100)
pocet_pokusov = 0

while True:
    cislo = int(input("Hadaj cislo od 1 do 100: "))

    if cislo == tajne_cislo:
        print("Super, uhadol si!")
        break
    else:
        pocet_pokusov += 1
        ostavajuce = 7-pocet_pokusov
        
        if ostavajuce == 0 or ostavajuce > 4:
            tvar_slova = 'pokusov'
        elif ostavajuce == 1:
            tvar_slova = 'pokus'
        else:
            tvar_slova = 'pokusy'

        if pocet_pokusov >= 7:
            print('Prehral si, koniec hry!')
            break
        else:
            if cislo < tajne_cislo:
                print("Tajne cislo je vacsie. Ostava este ",ostavajuce,tvar_slova)
            else:
                print("Tajne cislo je mensie. Ostava este ",ostavajuce,tvar_slova)


        