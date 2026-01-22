class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return f'Produkt {self.nazov} cena {self.cena}€ mnozstvo {self.pocet} ks'