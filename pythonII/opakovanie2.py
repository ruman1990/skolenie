# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

studenti = { 'Jana': 2, 'Peter': 1, 'Vlado' : 3 }

studenti['Zuzana'] = 1

print(studenti)

print(f'Priemerna znamka je: {sum(studenti.values())/len(studenti)}')

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
zoznam = [{'nazov' : 'Python pre zaciatocnikov','autor' : 'Python Guru', 'year': 2010}]
zoznam.append({'nazov' : 'Java pre zaciatocnikov','autor' : 'Java Guru', 'year': 2015})
zoznam.append({'nazov' : 'C++ pre zaciatocnikov','autor' : 'C++ Guru', 'year': 2020})
zoznam.append({'nazov' : 'JavaScript pre zaciatocnikov','autor' : 'JavaScript Guru', 'year': 2000})

for x in zoznam:
    if x['year'] > 2010:
        print(x)

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
        return f'Nazov knihy {self.nazov}, autor {self.autor}, rok {self.rok}'
    
k1 = Kniha('Python pre zaciatocnikov','Python Guru',2010)

print(k1)

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.
class EKniha(Kniha):
    def __init__(self,nazov,autor,rok,velkost_mb):
        super().__init__(nazov,autor,rok)
        self.velkost_mb = velkost_mb

    def vypis_info(self):
        print(f'{self.__str__()}, velkost {self.velkost_mb}MB')

ekniha = EKniha('Python pre zaciatocnikov','Python Guru',2010,10)
print(ekniha)
ekniha.vypis_info()
# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.
class StaraKniha(Kniha):
    def je_historicka(self):
        return self.rok < 1950
    
sk = StaraKniha('Python pre zaciatocnikov','Python Guru',1940)
print(sk.je_historicka())