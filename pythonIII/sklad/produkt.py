
from babel.numbers  import format_decimal

class Produkt:

    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def export_vypis(self):
        return f'{self.nazov};{self.cena};{self.pocet}'
    
    def vrat_celkovu_cenu(self):
        return self.cena * self.pocet
    
    def pripocitat(self,pocet):
        self.pocet += pocet
    
    def dostatok_tovaru(self,pocet):
        return self.pocet >= pocet
    
    def odpocitat(self,pocet):
        if not self.dostatok_tovaru(pocet):
            print('Nedostatok tovaru')
        else:
            self.pocet -= pocet
            print("Vyskladnenie bolo uspesne")

    def nacen(self,cena):
        self.cena = cena

    def __str__(self):
        return f'Nazov produktu: {self.nazov:<15} Cena: {format_decimal(self.cena,format="#,##0.00",locale='sk')}€ Pocet kusov {self.pocet:8}'
