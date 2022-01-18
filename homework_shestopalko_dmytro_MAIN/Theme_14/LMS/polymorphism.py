def animals_say_hello(animal):
    print(animal.say_hi())  # say_hi - is a method

    class Animal:
        def say_hi():
            pass

    class Cat(Animal):
        def say_hi(self):
            print("meow")

    class Dog(Animal):
        def say_hi(self):
            print("bow")

    cat = Cat()
    dog = Dog()

    animals_say_hello(cat)
    animals_say_hello(dog)
