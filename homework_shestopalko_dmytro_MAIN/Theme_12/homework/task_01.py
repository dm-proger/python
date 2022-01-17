# A Person class
#
# Make a class called Person. Make the __init__() method take firstname,
# lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person():

    def __init__(self, firstname: str, lastname: str, first_job: str, experience: int = 14, age: int = 29):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.first_job = first_job
        self.experience = experience


def talk() -> str:
    person_01 = Person("Carl", "Johnson", 26)
    person_02 = Person("Dmytro", "Shestopalko", 30)
    print(f"Hello, my name is {person_01.firstname} {person_01.lastname} and I am {person_01.age} years old.")
    print(f"Hello, my name is {person_02.firstname} {person_02.lastname} and I am {person_02.age} years old.")


def work() -> str:
    person_01 = Person("teacher", "driver", 14)
    person_02 = Person("student", "waiter", 16)
    print(f"My first job was {person_01.first_job}. My total work experience is {person_01.experience}")
    print(f"My first job was {person_02.first_job}. My total work experience is {person_02.experience}")



if __name__ == "__main__":
    talk()
    work()
