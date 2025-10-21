# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.
znamky = {'Jana' : 2, 'Peter' : 1, 'Marek' : 3, 'Lucia' : 2}

znamky['Vlado'] = 1 
#znamky.update({'Vlado' : 1})

#[2,1,3,2]
priemer = sum(znamky.values()) / len(znamky)

suma = 0
for x in znamky.values():
    suma += x
priemer = suma / len(znamky)

print(f'Priemerna znamka triedy je {priemer}')


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

for x in knihy:
    if x['rok'] > 1960:
        print(f'{x['nazov']} {x['autor']}')


# ---------------------------------------------------------

# Priklad 3: Základná trieda Kniha (objekty)
# Zadanie:
# Vytvor triedu Kniha, ktorá má atribúty nazov, autor a rok.
# Vytvor objekt a vypíš o ňom informácie.


class Kniha:

    def __init__(self,nazov, autor, rok):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok

    def __str__(self):
        return f'{self.nazov} {self.autor} {self.rok}'
    
    def __repr__(self):
        return f'{self.nazov} {self.autor} {self.rok}'

knihyObjekty = []
for x in knihy:
    knihyObjekty.append(Kniha(x['nazov'],x['autor'],x['rok']))

print(knihyObjekty)

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

y = ['nazov knihy','autor knihy',2000,'56464654']

class EKniha(Kniha):

    def __init__(self,nazov,autor,rok,velkost_MB=10):
        super().__init__(nazov,autor,rok)
        self.velkost_MB = velkost_MB

    def __str__(self):
        return f'{super().__str__()} {self.velkost_MB}'
    
    def vypis_info(self):
        print(f'{super().__str__()} {self.velkost_MB}')

ekniha = EKniha('maly princ','Saint Exupery',1943,25)

ekniha.vypis_info()



# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.


class StaraKniha(Kniha):

    def je_historicka(self):
        return self.rok < 1950
    
    @classmethod
    def from_book(cls,book):
        return cls(book.nazov,book.autor,book.rok)

book = Kniha('1984','George Orwell',1948)
oldBook = StaraKniha('1984','George Orwell',1948)

print(oldBook.je_historicka())
book = StaraKniha.from_book(book)
print(book.je_historicka())
