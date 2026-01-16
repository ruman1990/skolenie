## Objekty a funkcie
###################################################################################
class Person:

    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname

class Student(Person):
    def __init__(self,name,lastname,rocnik):
        super().__init__(name,lastname)
        self.rocnik = rocnik

def sucet(a,b):
    return a + b

##################################################################################
## Logika programu

x = 10

y = Student("Jan","Novak",4)


x = Student("Jan","Novak",4)
print(x.lastname)