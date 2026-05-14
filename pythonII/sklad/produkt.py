class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = float(cena)
        self.pocet = int(pocet)
    def __str__(self):
        return f"Produkt {self.nazov}, cena {self.cena:.2f}€, pocet {self.pocet}"
    def export_format(self):
        return f'{self.nazov},{self.cena},{self.pocet}'
