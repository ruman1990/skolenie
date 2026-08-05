class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = float(cena)
        self.pocet = int(pocet)

    def __str__(self):
        return f"{self.nazov} cena: {self.cena:.2f}€ pocet kusov: {self.pocet}"

    def formatovany_vypis(self):
        return f"{self.nazov},{self.cena},{self.pocet}\n"

    def celkova_cena(self):
        return self.cena * self.pocet

    def as_list(self):
        return [self.nazov,self.cena,self.pocet]


# from dataclasses import dataclass
# from decimal import Decimal


# @dataclass
# class Produkt:
#     nazov : str
#     cena : Decimal
#     pocet : int

#     def formatovany_vypis(self):
#         return f"{self.nazov},{self.cena},{self.pocet}\n"

#     def celkova_cena(self):
#         return self.cena * self.pocet

#     def as_list(self):
#         return [self.nazov,self.cena,self.pocet]
