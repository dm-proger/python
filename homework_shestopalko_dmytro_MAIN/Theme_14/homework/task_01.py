# Method overloading.
#
# Create a base class named Animal with a method called talk and then create two subclasses:
# Dog and Cat, and make their own implementation of the method talk be different.
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.
#
# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes
# and performs talk method on input parameter.

def animal_function():
    animal_input = input("Say something: ")


class Animal():
    def __init__(self, talk: str):
        self.talk = talk


class Dog(Animal):
    def talk(self):
        print("bow")


class Cat(Animal):
    def talk(self):
        print("meow")
        

print(animal_input.talk)

animal_function()
