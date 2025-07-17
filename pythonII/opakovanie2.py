# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

znamky = {
    "Jana": 2,
    "Peter" : 1,
    "Michal" : 1,
    "Bohumil" : 3
}

znamky["Adam"] = 4

priemer = sum(znamky.values()) / len(znamky)
print(f"Priemerna znamka je: {priemer}" ) 

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.

zoznam = [
    {"nazov" : "Roman pre zeny" , "autor" : "Autorka" , "rok" : 1989},
    {"nazov" : "Roman pre muzov" , "autor" : "Autor" , "rok" : 1995},
    {"nazov" : "Roman pre vsetkych" , "autor" : "Kolektiv" , "rok" : 2012 }
]

zoznam.append({"nazov" : "Roman pre nikoho" , "autor" : "Nikto" , "rok" : 2022 })

for z in zoznam:
    if z['rok'] > 2010:
        print(z['nazov'])

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

    def vypis_info(self):
        print(f'Nazov: {self.nazov}, Autor: {self.autor}, Rok: {self.rok}')
        
kniha = Kniha("Python pre zaciatocnikov","Expert na programovanie",2020)
kniha.vypis_info()

# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.

class Ekniha(Kniha):
    def __init__(self,nazov,autor,rok,velkost_mb=10):
        super().__init__(nazov,autor,rok)
        self.velkost_mb = velkost_mb

    def vypis_info(self):
        print(f'Nazov: {self.nazov}, Autor: {self.autor}, Rok: {self.rok} Velkost : {self.velkost_mb}' )

ekniha = Ekniha("Python pre zaciatocnikov","Expert na programovanie",2020,25)

ekniha.vypis_info()

# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.

class StaraKniha(Kniha):

    def je_historicka(self):
        return self.rok < 1950

stara = StaraKniha("Python pre zaciatocnikov","Expert na programovanie",1948)

stara.vypis_info()
print(stara.je_historicka())
