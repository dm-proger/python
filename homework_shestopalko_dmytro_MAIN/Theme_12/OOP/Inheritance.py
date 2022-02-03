# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on.
# Although they may differ in some ways (only Dog might have the method bark),
# they are likely to be similar in others (all having the attributes color and name).
# This similarity can be expressed by making them all inherit from a superclass Animal,
# which contains the shared functionality.
# To inherit a class from another class, put the superclass name in parentheses after the class name.

# Example:
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

# A class that inherits from another class is called a subclass.
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them.


# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
# super().spam() calls the spam method of the superclass.