class Animal():

    def __init__(self, name):
        self.name = name

    # Abstract method. It can not be called unless it is implemented by the subclass
    def talk(self):
        raise NotImplementedError("Must be implemented by a sub class")

class Cat(Animal):
    def talk(self):
        print("Meow!")

class Dog(Animal):
    def talk(self):
        print("Woof!")

animals = [Cat("Garfield"), Dog("Hans"), Cat("Maja")]

for animal in animals:
    animal.talk()