import datetime

class Audit:

    def __init__(self,filename='log.txt'):
        self.filename = filename
        self.log_zapis("Nacitanie logu")

    def log_vypis(self):
        with open(self.filename,'r',encoding='utf-8') as f:
            print(f.read())

    def log_zapis(self,text):
        with open(self.filename,'a',encoding='utf-8') as f:
            f.write(f'[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}\n')
        print(text)