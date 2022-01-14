class Animal:
    CLASS_VARIABLE: ClassVar[int] = 2
    _members: list = []


    def __init__(self, name: str, age: int = 8):
        self.name = name
        self._age = age
        self.__color = "black"

    def talk(self) -> str:
        return "Wow"

    def __str__(self):
        # return self.name
        return f"{self.__class__.__name__} {self.name}"
    __repr__ = __str__

    @classmethod
    def from_string(cls, data:str):
        return cls(name=data)

    @staticmethod
    def something() -> str:
        return "Some info"

    # getter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value:  int):
         self._age = value

    @age.deleter
    def age(self):
        print("Delete")

    def _age_getter(self):
        return self._age

    def _age_setter(self, value: int):
        self._age = value

class Dog(Animal):
    ...

    def talk(self) -> str:
        # temp = super().talk()
        return f"{super().talk()} Such wow!"

def main():
    dog_tosha = Dog(name = "Tosha")

    print(dog_tosha)

    dog_2 = Dog.from_string(data="Toshandiy")
    print(dog_2)

    print(dog_tosha.talk())

    print(dog_tosha.name)
    print(dog_tosha._age) # Do not do this!
    print(dog_tosha._Animal__color) # Do not do this!

    dog_tosha.name = "Toshiba"
    print(dog_tosha.name)

    dog_tosha.age = 20
    print(dog_tosha._age)

    del dog_tosha.age

    print(dog_tosha.CLASS_VARIABLE)
    print(Animal.CLASS_VARIABLE)
    Animal.CLASS_VARIABLE = 5
    print(dog_tosha.CLASS_VARIABLE)
    print(Animal.CLASS_VARIABLE)

if __name__ == "__main__":
    main()
