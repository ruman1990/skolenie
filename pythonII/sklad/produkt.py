class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return (f'Nazov {self.nazov}, Cena {self.cena:.2f}€, Pocet {self.pocet}ks')
    
    def export_tvar(self):
        return f'{self.nazov};{self.cena};{self.pocet}'