class Produkt:
    def __init__(self, nazov, pocet=0, cena=0.0):
        self.nazov = nazov
        self.pocet = pocet
        self.cena = cena

    def __str__(self):
        return f'{self.nazov} {self.pocet}ks {self.cena:.2f}€'
    
    def export(self):
        return f'{self.nazov},{self.pocet},{self.cena}'