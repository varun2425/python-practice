#Variables (They are two types)
#1)Instance Variable                                   #Class(Static)variable
# mil = 10 , com =BMW


class Car:


    def __init__(self):
        self.mil=10
        self.com="BMW"



c1 = Car()
c2 = Car()

print(c1.com,c1.mil)
print(c2.com,c2.mil)