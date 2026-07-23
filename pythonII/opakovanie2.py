# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

studenti = { 'Jana' : 2 , 'Peter' : 1 , 'Zuzana' : 3 , 'Vlado' : 4}
studenti['Adam'] = 1
print(f"Priemerna znamka triedy je {sum(studenti.values())/len(studenti)}")



# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
x = [{"nazov" : "python guru I", "autor" : "Guru" , "rok" : 2008},
     {"nazov" : "python guru II", "autor" : "Guru" , "rok" : 2015},
     {"nazov" : "python guru III", "autor" : "Guru" , "rok" : 2017}]


x.append({"nazov" : "python guru IV", "autor" : "Guru" , "rok" : 2020})

result = []
for i in x:
    if i['rok'] > 2010:
        result.append(i)

print(result)

# ---------------------------------------------------------

# Priklad 3: Základná trieda Kniha (objekty)
# Zadanie:
# Vytvor triedu Kniha, ktorá má atribúty nazov, autor a rok.
# Vytvor objekt a vypíš o ňom informácie.

class Kniha:
     def __init__(self,nazov,autor,rok):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok

     def __str__(self):
        return f"{self.nazov}, {self.autor}, {self.rok}"

k = Kniha("Python I","Guru",1995)

print(k)



# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

class EKniha(Kniha):
     def __init__(self,nazov,autor,rok,velkost_MB=0):
          super().__init__(nazov,autor,rok)
          self.velkost_MB = velkost_MB

     def __str__(self):
         return f"{super().__str__()}, {self.velkost_MB}MB"

     def vypis_info(self):
         return f"{self.nazov}, {self.autor}, {self.rok}, {self.velkost_MB}MB"

ekniha = EKniha("Java I", "Java Guru",2008,25)

print(ekniha)
print(ekniha.vypis_info())
     


# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.


class StaraKniha(Kniha):

    def je_historicka(self):
        return self.rok < 1950

sk = StaraKniha("1984","Orwell",1948)

print(sk)
print(sk.je_historicka())
