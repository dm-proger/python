# x = "hello"
#
# #if condition returns False, AssertionError is raised:
# assert x == "f", "x should be 'hello'"


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):  # this is a subclass
    raise_amt = 1.1  # here we change the method raise_amt, without disturbing it in the parent class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # instead of copy-paste these attributes from the Employee class, we can use this function -super()
        # Employee.__init__(self, first, last, pay) # alternative way of calling a parent
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))

# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
#
# mgr_1.print_emp()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
