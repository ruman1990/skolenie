class Produkt:
    def __init__(self,nazov,cena,pocet_kusov):
        self.nazov = nazov
        self.cena = cena
        self.pocet_kusov = pocet_kusov

    def celkova_cena(self):
        return self.cena * self.pocet_kusov