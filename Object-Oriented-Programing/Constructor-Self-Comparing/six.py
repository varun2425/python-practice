#Here we will change age

class Computer:

    def __init__(self):
        self.name = "Varun"
        self.age = 23

   
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")  #Since the age is different we are getting //They are different


print(c1.name)
print(c2.name)
