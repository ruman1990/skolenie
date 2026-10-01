class Produkt:
    def __init__(self,nazov,cena,pocet):
        self.nazov = nazov
        self.cena = cena
        self.pocet = pocet

    def __str__(self):
        return f"nazov produktu {self.nazov:10}, jednotkova cena {self.cena:10}€, pocet kusov {self.pocet:10}"

    def get_value(self):
        return self.cena * self.pocet