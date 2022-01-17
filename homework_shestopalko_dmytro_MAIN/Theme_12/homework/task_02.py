# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
from typing import ClassVar


class Dog():
    class_attr: ClassVar[int] = 7

    def __init__(self, name: str, initial_age: int = 3):

        self.dog_age = self.class_attr * initial_age
        self.name = name


def calculate():
    age_dog_01 = Dog("Bars", initial_age=3)

    print(f"Hello, my name is {age_dog_01.name} and I am {age_dog_01.dog_age} years old.")


if __name__ == "__main__":
    calculate()
