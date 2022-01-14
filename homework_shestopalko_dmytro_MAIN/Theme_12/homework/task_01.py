# A Person class
#
# Make a class called Person. Make the __init__() method take firstname,
# lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person():

    def __init__(self, firstname: str, lastname: str, age: int = 26):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk() -> str:
        person_01 = Person("Carl", "Johnson", 26)
        print(person_01.firstname)
        print(person_01.lastname)
        print(person_01.age)
        # print(f"Hello, my name is + {firstname} + {lastname}")
        # print(f"and I`m + {age} + years old")

    talk()


if __name__ == "__main__":
    main()