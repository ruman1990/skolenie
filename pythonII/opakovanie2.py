# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.
znamky = {'Jana' : 2, 'Peter' : 1, 'Marek' : 3, 'Lucia' : 2}

znamky['Vlado'] = 4

priemer = sum(znamky.values())/len(znamky)

print(priemer)

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

knihy.append({'nazov': 'Kniha 1', 'autor': 'George Orwell st.', 'rok': 1752})
knihy.append({'nazov': 'Kniha 2', 'autor': 'George Orwell ml.', 'rok': 1995})
knihy.append({'nazov': 'Kniha 3', 'autor': 'George Orwell najml.', 'rok': 2025})

#print(knihy)

for x in knihy:
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
        return f'Nazov knihy {self.nazov} autor {self.autor} rok {self.rok}'
    
kniha = Kniha('1984','George Orwell',1949)

print(kniha)

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

y = ['nazov knihy','autor knihy',2000,'56464654']

class EKniha(Kniha):

    def __init__(self,n,a,r,velkost):
        super().__init__(n,a,r)
        self.velkost = velkost

    def vypis_info(self):
        print(f'{super().__str__()} velkost {self.velkost}')


ekniha = EKniha('1984','George Orwell',1949,10)

ekniha.vypis_info()
# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.

STARA_KNIHA = 1950

class StaraKniha(Kniha):
    def je_historicka(self):
        return self.rok < STARA_KNIHA

stara = StaraKniha('1984','George Orwell',1949)
print(stara.je_historicka())