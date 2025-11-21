class Person:
    people_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people_count += 1

    def __del__(self):
        Person.people_count -= 1

    def isAdult(self):
        return self.age >= 18

    def __eq__(self, other):
        return self.name == other.name

    @classmethod
    def how_many(cls):
        print(f"Počet ľudí: {cls.people_count}")

    @classmethod
    def del_person(cla):
        cla.people_count -= 1

x = Person("Anna", 50)
y = Person("Vlado", 25)
Person.how_many()  # Počet ľudí: 2

Person.how_many()  # Počet ľudí: 1


if x == y:
    print("Rovnakí ľudia")
else:
    print("Rôzni ľudia")