# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.
znamky = {'Jana' : 2, 'Peter' : 1, 'Marek' : 3, 'Lucia' : 2}

znamky['Vlado'] = 4

priemer = sum(znamky.values()) / len(znamky)
print(f'Priemerna znamka je: {priemer}')

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.
knihy = [
    {'nazov': '1984', 'autor': 'George Orwell', 'rok': 1949},
    {'nazov': 'Sto rokov samoty', 'autor': 'Gabriel García Márquez', 'rok': 1967},
    {'nazov': 'Sila zvyku', 'autor': 'Charles Duhigg', 'rok': 2012}
]

for kniha in knihy:
    if kniha['rok'] > 2010:
        print(kniha['nazov'])

# ---------------------------------------------------------

# Priklad 3: Základná trieda Kniha (objekty)
# Zadanie:
# Vytvor triedu Kniha, ktorá má atribúty nazov, autor a rok.
# Vytvor objekt a vypíš o ňom informácie.

class Kniha:
    def __init__(self,nazov,autor,rok,isbn):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok
        self.isbn = isbn

    def __str__(self):
        return f'Nazov {self.nazov} Autor {self.autor} Rok {self.rok} ISBN {self.isbn}'
    
    def vypis_info(self):
        print(f'Nazov {self.nazov} Autor {self.autor} Rok {self.rok} ISBN {self.isbn}')

x = Kniha('Biblia','Kolektiv',0,'515615615')
print(x)
x.vypis_info()

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

y = ['nazov knihy','autor knihy',2000,'56464654']

class EKniha(Kniha):
    def __init__(self, *args, pocet_stran,velkost=10):
        super().__init__(*args)
        self.velkost = velkost
        self.pocet_stran = pocet_stran

    def __str__(self):
        return f'Nazov {self.nazov} Autor {self.autor} Rok {self.rok} Velkost {self.velkost}'

#x = Kniha(*y)
#print(x) 
kniha = EKniha(*y,pocet_stran=125)
print(kniha)

# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.

class StaraKniha(Kniha):
    
    def je_historicka(self):
        return self.rok < 1950


a = StaraKniha('Biblia','Kolektiv',0,'546456465')
print(a.je_historicka())