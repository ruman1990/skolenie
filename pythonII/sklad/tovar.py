class Tovar:   
    def __init__(self,meno,cena, pocet):
        self.meno = meno
        self.cena = cena
        self.pocet = pocet

    def hodnota(self):
        return self.cena * self.pocet
    
    def export_format(self):
        return f'{self.meno};{self.cena};{self.pocet}'

    def __str__(self):
        return f'Produkt {self.meno:<20} Cena {self.cena:10.2f} Pocet {self.pocet:10d}'