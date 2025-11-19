
class Student:

    def __init__(self,name,rollno):
        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i5'
            self.ram = 8



s1 = Student('Varun',24,)
s2 = Student('Renuka',26)

s1.show()

lap1 =s1.lap
lap2 =s2.lap

print(id(lap1))
print(id(lap2))