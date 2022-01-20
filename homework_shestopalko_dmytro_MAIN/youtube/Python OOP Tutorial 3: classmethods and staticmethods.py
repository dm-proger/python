
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

import datetime
my_date = datetime.date(2022, 1, 20)

print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05) # we ran this method as a class method from the class
                                # that means we are working now with class, not with an instance
# we can run class method from an instance, but it doesn`t make any sens in general:
# emp_1.set_raise_amt(1.05) # it still changes the class amount, even if it is ran from the instance

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#Class methods as alternative constructors: (multiple way of creating objects)

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"
#
# new_emp_1 = Employee.from_string(emp_str_1) #alternative constructor
#
# # first, last, pay = emp_str_1.split("-")
#
# # new_emp_1 = Employee(first, last, pay)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

#Static method



