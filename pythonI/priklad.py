notes = ['Jack','Robert']

def pridaj_meno():
    meno = input("Pridaj do adresara meno: ")
    notes.append(meno)


while True:
    pridaj_meno()
    print(notes)


