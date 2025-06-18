```
vek = input('Kolko mas rokov? ')
match vek:
    case "18" | '20' if int(vek)>10:
        print("Ma 18")
    case "19":
        print("Ma 19")
    case _:
        print("Iná hodnota")

print('hotovo')
```
