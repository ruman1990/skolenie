globalna_premenna = 100

class Person:
    count = 0

    def __init__(self,id,name,surname,age=18):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        Person.count += 1

    def __eq__(self, value):
        return self.id == value.id

    def __str__(self):
        return f"{self.name} {self.surname} ma vek {self.age}"

    def je_dospely(self):
        if self.age >= 18:
            print("je dospely")
        else:
            print("je malolety")


class Student(Person):
    def __init__(self,id,name,surname,age=18,school=None):
        super().__init__(id,name,surname,age)
        self.school = school

    def __str__(self):
        return f"{self.name} {self.surname} ma vek {self.age} a chodi na {self.school}"

p = Person(1,"Vlado","Ruman")
p2 = Person(2,"Jan","Mrkvicka",85)
p3 = Person(3,"Jozef","Hrach",74)

s = Student(4,"Peter","Petrovic",22,"gamca")

print(s)
print(p3)