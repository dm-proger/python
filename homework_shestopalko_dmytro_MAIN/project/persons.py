

class Person:

    def __init__(self, second_name: str, first_name: str):
        self.second_name = second_name
        self.first_name = first_name


class Manager(Person):

    def __init__(self, second_name: str, first_name: str):
        super().__init__(second_name, first_name)

    def add_employee(self):
        ...

    def remove_employee(self):
        ...

    def set_rate(self):
        ...


class Admin(Person):

    def __init__(self, second_name: str, first_name: str):
        super(self).__init__(second_name, first_name)


class Employee(Person):

    def __init__(self, second_name: str, first_name: str, position: str, rate: int):
        super(self).__init__(second_name, first_name)
        self.position = position
        self.rate = rate





def main():
    pass

if __name__ == "__main__":
    main()


