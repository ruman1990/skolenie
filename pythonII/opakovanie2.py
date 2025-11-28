# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.
znamky = {'Jana' : 2, 'Peter' : 1, 'Marek' : 3, 'Lucia' : 2}

znamky['Zuzana'] = 1

priemer = sum(znamky.values()) / len(znamky)
print(f"Priemerná známka triedy je: {priemer}")

#[2,1,3,2]


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

import random

name = random.choice(["Zuzana","Jana","Peter","Marek","Lucia"])
surname = random.choice(["Novakova","Kovac","Hrasko","Mikulas","Biely"])
year = random.randint(1990,2024)

knihy.append({'nazov': 'Nová kniha', 'autor': f'{name} {surname}', 'rok': year})

for kniha in knihy:
    if kniha['rok'] > 2010:
        print(kniha['nazov'])


# ---------------------------------------------------------

# Priklad 3: Základná trieda Kniha (objekty)
# Zadanie:
# Vytvor triedu Kniha, ktorá má atribúty nazov, autor a rok.
# Vytvor objekt a vypíš o ňom informácie.
class Kniha:
    def __init__(self, nazov, autor, rok):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok

    def __str__(self):
        return f'Kniha: {self.nazov}, Autor: {self.autor}, Rok: {self.rok}'
    
    def vypis_info(self):
        print(f'Názov: {self.nazov}, Autor: {self.autor}, Rok: {self.rok}')

book = Kniha('1984', 'George Orwell', 1949)
print(book)
book.vypis_info()

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

y = ['nazov knihy','autor knihy',2000,'56464654']

class EKniha(Kniha):
    def __init__(self, nazov, autor, rok, velkost_MB):
        super().__init__(nazov, autor, rok)
        self.velkost_MB = velkost_MB

    def __str__(self):
        return f'{super().__str__()}, Veľkosť: {self.velkost_MB} MB'
    
    def vypis_info(self):
        super().vypis_info()
        print(f'Veľkosť súboru: {self.velkost_MB} MB')


ekniha = EKniha('Digitálna éra', 'Tech Autor', 2020, 5.6)
print(ekniha)
# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.

class StaraKniha(Kniha):

    def __init__(self, nazov, autor, rok,typ_vazby='pevna'):
        super().__init__(nazov, autor, rok)
        self.typ_vazby = typ_vazby

    def je_historicka(self):
        return self.rok < 1950


staraKniha = StaraKniha('Staroveké príbehy', 'Historický Autor', 1940)
print(staraKniha.je_historicka())