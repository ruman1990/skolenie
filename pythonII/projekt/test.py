__all__ = ["x","PI","Kniha","sucet"]


x = 35

PI = 3.14

def sucet(a,b):
   return a + b


class Kniha:
    def __init__(self,nazov,autor,rok):
      self.nazov = nazov
      self.autor = autor
      self.rok = rok

    def __str__(self):
      return f"{self.nazov} {self.autor} {self.rok}"