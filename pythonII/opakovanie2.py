# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.
slovnik = { 'Jana' : 2, 'Peter' : 1, 'Fero' : 3, 'Vlado' : 4 }

slovnik['Zuzka'] = 1

print(f'Priemerna znamka je {sum(slovnik.values()) / len(slovnik)}')

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
zoznam = [{'nazov' : 'Python pre zaciatocnikov','autor' : 'Python Guru', 'year': 2010}]

zoznam.append({'nazov' : 'Java pre zaciatocnikov','autor' : 'Java Guru', 'year': 2015})
zoznam.append({'nazov' : 'C++ pre zaciatocnikov','autor' : 'C++ Guru', 'year': 2005})

for kniha in zoznam:
    if kniha['year'] >= 2010:
        print(kniha['nazov'])


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
        return f'{self.nazov}, {self.autor}, {self.rok}'

kniha1 = Kniha('Python pre zaciatocnikov','Python Guru',2010)
kniha2 = Kniha('Java pre zaciatocnikov','Java Guru',2015)
print(kniha1)
print(kniha2)


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
        return f'{super().__str__()}, {self.velkost_MB}MB'

ekniha = EKniha('Java pre zaciatocnikov','Java Guru',2015,5)
print(ekniha)
# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.
class StaraKniha(Kniha):
    def je_historicka(self):
        return self.rok < 1950
    
kniha1 = StaraKniha('Python pre zaciatocnikov','Python Guru',2010)
stara = StaraKniha('1984','Orwell',1948)
print(kniha1.je_historicka())
print(stara.je_historicka())