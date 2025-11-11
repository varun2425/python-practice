class Computer:

    def __init__(self):
        self.name = "Varun"
        self.age = 23

    def update(self):
        self.age=30


c1 = Computer()
c2 = Computer()

c1.name = "Renuka"
c1.age = 12

c1.update()


print(c1.name)
print(c2.name)