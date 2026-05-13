class Person:
    counter = 0
    def __init__(self,name,age=18):
        Person.counter += 1
        self.name = name
        self.age = age
        self.clovek = True

    def __str__(self):
        return f"{self.name}, {self.age} rokov, je clovek {self.clovek}"
    
    def is_clovek(self):
        return self.clovek
    
    def is_dospely(self):
        if self.age>=18:
            return True
        else:
            return False
        
    def is_starsi(self,other):
        if self.age > other.age:
            print("Je starsi")
        else:
            print("Je mladsi")

    @staticmethod
    def is_senior(age):
        return age > 65

    @classmethod
    def pocet(cls):
        return cls.counter

class Student(Person):
    def __init__(self,name,age=18,is_vysokoskolak=False):
        super().__init__(name,age)
        self.is_vysokoskolak = is_vysokoskolak
        self.rocnik = None

    def nastav_rocnik(self,rocnik):
        self.rocnik = rocnik

    def is_dospely(self):
        super().is_dospely()
        return False
    

osoba = Person("Adam",25)
print(type(osoba))
Person.is_senior(10)

student = Student("Bohumil",22)
student.is_starsi(osoba)
print(student.is_dospely())
print(student.is_vysokoskolak)

print(Person.pocet())


osoba2 = Person("Eva",42)
osoba3 = Person("Bohumil")
osoba.age = 10

osoba.is_starsi(osoba2)


print(osoba)
print(osoba.clovek)
osoba.name = "Boris"
print(osoba.name)


