# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

studenti = { 'Jana': 2, 'Peter': 1, 'Vlado' : 3 }

studenti['Bohumil'] = 3

priemer = sum(studenti.values()) / len(studenti)
print(f"Priemerna znamka celej triedy je: {priemer}")

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
zoznam = [{'nazov' : 'Python pre zaciatocnikov','autor' : 'Python Guru', 'year': 2011}]
zoznam.append({'nazov' : 'Python pre pokrocilych','autor' : 'Python Guru II', 'year': 2013})
zoznam.append({'nazov' : 'Java pre pokrocilych','autor' : 'Java Guru I', 'year': 2005})
zoznam.append({'nazov' : 'Java pre zaciatocnikov','autor' : 'Java Guru II', 'year': 2003})

for x in zoznam:
    if x['year'] > 2010:
        print(x['nazov'])


# ---------------------------------------------------------

# Priklad 3: Základná trieda Kniha (objekty)
# Zadanie:
# Vytvor triedu Kniha, ktorá má atribúty nazov, autor a rok.
# Vytvor objekt a vypíš o ňom informácie.
class Kniha:
    def __init__(self,nazov,autor,rok,vydavatel):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok
        self.vydavatel = vydavatel
    
    def vypis(self):
        print(f'Nazov {self.nazov}, autor {self.autor}, rok {self.rok}')

    def __str__(self):
        return f'Nazov {self.nazov}, autor {self.autor}, rok {self.rok}, vydavatel {self.vydavatel}'

book = Kniha('Python pre zaciatocnikov', 'Python Guru', 2011, "IKAR")

print(book)

book.vypis()


# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.
class EKniha(Kniha):
    def __init__(self,nazov,autor,rok,vydavatel,velkost_MB):
        super().__init__(nazov,autor,rok,vydavatel)
        self.velkost_MB = velkost_MB

    def __str__(self):
        return f'{super().__str__()}, velkost {self.velkost_MB}'

ebook = EKniha('Python pre pokrocilych', 'Python Guru II', 2015,"IKAR", 20)

print(ebook)

# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.
class StaraKniha(Kniha):

    def je_historicka(self):
        return self.rok < 1950
    
oldBook = StaraKniha('Fortran pre pokrocilych', 'Eniac Guru II', 1940,"IKAR")

print(oldBook.je_historicka())