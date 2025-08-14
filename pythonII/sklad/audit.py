import datetime

class Audit:
    def __init__(self):
        self.log = []

    def zapis(self,s):
        print(s)
        self.log.append(f'[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {s}')

    def vypis(self):
        for i in self.log:
            print(i)
