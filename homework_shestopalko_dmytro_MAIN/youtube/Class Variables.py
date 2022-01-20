
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last    #this is an instance variable. It contains field and the value that is stored in the field
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.num_of_emps)

# print(Employee.__dict__) # function __dict__ makes a dictionary from the object

# emp_1.raise_amount = 1.05
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.raise_amount
# Employee.raise_amount