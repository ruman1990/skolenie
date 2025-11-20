from decimal import Decimal
class Produkt:
    def __init__(self,nazov,cena,pocet_kusov):
        self.nazov = nazov
        self.cena = cena
        self.pocet_kusov = pocet_kusov

    def hodnota(self):
        return Decimal(str(self.cena)) * self.pocet_kusov
    
    def export_string(self):
        return f'{self.nazov};{self.cena};{self.pocet_kusov}'

    def __str__(self):
        return f'Nazov produktu: {self.nazov}, jednotkova cena: {self.cena:.2f} €, pocet kusov: {self.pocet_kusov}'
