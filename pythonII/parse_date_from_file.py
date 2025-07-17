import datetime

with open("C:\\Users\\ruman\\skolenie\\pythonII\\demofile.txt","r", encoding="utf-8") as f:
    for line in f:
        s = line.split('" ')
        zaznam = s[0]
        dt = datetime.datetime.strptime(zaznam[1:], "%d.%m.%Y %H:%M")
        print(dt)
