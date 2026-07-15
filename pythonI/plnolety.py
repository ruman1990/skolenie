# chceme zistit aky ma pouzivatel vek a podla toho vypiseme ci je alebo nie je plnolety
import datetime

now = datetime.datetime.now()
AKTUALNY_ROK = now.year

rok_narodenia = int(input("Zadaj rok narodenia: "))

vek = AKTUALNY_ROK-rok_narodenia

if rok_narodenia < 1900 or rok_narodenia > AKTUALNY_ROK:
    print("Zadal si nespravny rok")
else:
    if vek > 65:
        print(f"Si dochodza a mas {vek} rokov")
    elif vek >= 50:
        print(f"Si senior a mas {vek} rokov")
    elif vek >= 18:
        print(f"Si plnolety a mas {vek} rokov")
    else:
        print(f"Nie si plnolety a mas {vek} rokov")