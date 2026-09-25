# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

studenti = { 'Jana' : 2 , 'Peter' : 1 , 'Zuzana' : 3 , 'Vlado' : 4}

studenti['Boris'] = 2

print(studenti)

# suma = 0
# for x in studenti:
#     suma += studenti[x]

# priemer = suma / len(studenti)

priemer = sum(studenti.values())/len(studenti)

print(priemer)


# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
zoznam = [{"nazov" : "Python Guru" , "autor" : "Guru" , "rok" : 2005},
          {"nazov" : "Python Guru II" , "autor" : "Guru" , "rok" : 2017},
          {"nazov" : "Python Guru III" , "autor" : "Guru" , "rok" : 2025}]

for x in zoznam:
    if x['rok'] > 2010:
        print(x['nazov'])

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
        return f"{self.nazov}, autor je {self.autor}, rok vydania {self.rok}"

    def vypis_info(self):
        print(f"{self.nazov}, autor je {self.autor}, rok vydania {self.rok}")

zoznam = [Kniha("Python Guru","Guru",2005),Kniha("Python Guru II","Guru",2015),Kniha("Python Guru","Guru",2025)]

for x in zoznam:
    if x.rok > 2010:
        print(x.vypis_info())

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

class EKniha(Kniha):
    def __init__(self,nazov,autor,rok,velkost_MB):
        super().__init__(nazov,autor,rok)
        self.velkost_MB = velkost_MB
     
    def __str__(self):
        return f"{super().__str__()}, velkost {self.velkost_MB}"

zoznam.append(EKniha("Java Guru","Guru",2002,10))



# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.

class StaraKniha(Kniha):
    def je_historicka(self):
        return self.rok < 1950

    def __str__(self):
        return f"{super().__str__()}, je historicka {k.je_historicka()}"

k = StaraKniha("1984","Orwell",1948)
zoznam.append(k)

print(f"Je historicka: {k.je_historicka()}")


for x in zoznam:
    print(x)
