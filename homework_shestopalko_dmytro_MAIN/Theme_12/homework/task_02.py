# Doggy age
#
# Create a class Dog with class attribute `age_factor` equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog():
    class_attr = 7


def __init__(self, name: str, human_age: int = 29):
    self.human_age = 1 / class_attr
    self.name = name
    self.human_age = human_age


def calculate():
    age_dog_01 = Dog("Bars", 26)

    print(f"Hello, my name is {age_dog_01.name} and I am {age_dog_01.human_age} years old.")


if __name__ == "__main__":
    calculate()

