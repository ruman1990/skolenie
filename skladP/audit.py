import datetime

class Audit:

    def __init__(self,file="log.txt"):
        self.dennik = []
        self.file = file
        try:
            with open(self.file,"r",encoding="utf-8") as f:
                for line in f:
                    self.dennik.append(line)
        except FileNotFoundError:
            pass

    def zapis(self,akcia):
        cas = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.dennik.append(f'[{cas}] {akcia}')
        with open(self.file,"a",encoding="utf-8") as f:
            f.write(f'[{cas}] {akcia}\n')

    def vypis(self):
        for i in self.dennik:
            print(i,end="")
