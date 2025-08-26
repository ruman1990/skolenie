from decimal import Decimal

class Produkt:
    def __init__(self,nazov,cena,pocet,kategoria=1):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet
        self.kategoria = kategoria

    def __str__(self):
        return (f'Nazov {self.nazov}, Cena {self.cena:.2f}€ bez DPH, Cena {self.cena_s_dph():.2f}€ s DPH, Pocet {self.pocet}ks')
    
    def export_tvar(self):
        return f'{self.nazov};{self.cena};{self.pocet};{self.kategoria}'
    
    def cena_s_dph(self):
        if self.kategoria == 1:
            return self.cena * 1.23
        elif self.kategoria == 2:
            return self.cena * 1.19
        else:
            return self.cena * 1.05