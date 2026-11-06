# Priklad 1: Slovník so študentmi
# Zadanie:
# Vytvor slovník, kde kľúčom bude meno študenta a hodnotou jeho známka
# (napr. { 'Jana': 2, 'Peter': 1, ... }).
# Pridaj do slovníka nového študenta a vypíš priemernú známku triedy.

studenti = { 'Jana' : 2 , 'Peter' : 1 , 'Zuzana' : 3 , 'Vlado' : 4}

studenti['Marek'] = 2
priemer = round(sum(studenti.values()) / len(studenti))

print(f"Priemerna znamka: {priemer:.2f}, pocet studentov je {len(studenti)}, najhorsia znamka {max(studenti.values())}")

round(2.5)  # 2
round(3.5) # 4

# ---------------------------------------------------------

# Priklad 2: Zoznam slovníkov
# Zadanie:
# Vytvor zoznam, kde každý prvok je slovník s informáciami o knihe (nazov, autor, rok).
# Pridaj 3 knihy a vypíš názvy všetkých kníh vydaných po roku 2010.

knihy = [
    {'nazov': 'Kubko sa uci rozpravat', 'autor': 'Marta Galewska-Kustra', 'rok': 2020},
    {'nazov': 'Rozprávky o psíkovi a mačičke', 'autor': 'Josef Capek', 'rok': 1940},
    {'nazov': 'Budkovo', 'autor': 'Zuzana Smatanova', 'rok': 2025}
]
 
for kniha in knihy:
    if kniha['rok'] > 2010:
        print(f"Nazov knihy vydanej po roku 2010 : {kniha['nazov']}")

print()
print()
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
        return f"Nazov: {self.nazov}, Autor: {self.autor}, Rok: {self.rok}"    

knihy_zoznam = []
for x in knihy:
    #knihy_zoznam.append(Kniha(x['nazov'],x['autor'],x['rok']))
    knihy_zoznam.append(Kniha(*x.values()))




# ---------------------------------------------------------

# Priklad 4: Dedičnosť (E-Kniha)
# Zadanie:
# Vytvor triedu EKniha, ktorá dedí z Kniha a má navyše atribut velkost_MB.
# Prepis metódu vypis_info tak, aby vypísala aj veľkosť súboru.
class EKniha(Kniha):

    def __init__(self, nazov, autor, rok, velkost_MB=10):
        super().__init__(nazov,autor,rok)
        self.velkost_MB = velkost_MB

    def __str__(self):
            return f"{super().__str__()}, Velkost v MB {self.velkost_MB}"    

knihy_zoznam.append(EKniha('Budkovo II','Zuzana Smatanova',2027,25))


# ---------------------------------------------------------

# Priklad 5: Dedičnosť a kontrola roku (Metóda)
# Zadanie:
# Vytvor triedu StaraKniha, ktorá dedí z Kniha a má metódu je_historicka(),
# ktorá vráti True ak bola vydaná pred rokom 1950.
class StaraKniha(Kniha):

    def je_historicka(self):
        return self.rok < 1950

    def __str__(self):
                return f"{super().__str__()}, historicka {self.je_historicka()}"    

s = StaraKniha("1984","George Orwell",1948)
knihy_zoznam.append(s)

print(s.je_historicka())


for x in knihy_zoznam:
    print(x)
            