class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return(self.pay*12) + self.bonus

class Employee: # Agregation represents HAS-A relation ship #Employee has a Salary
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def total__salary(self):
        return self.obj_salary.annual_salary()

#We have created the instance of the Salary Class and we pass this instance to the Employee constructor which can be used inside the Emp Class
salary = Salary(15000, 10000) # we are extensiating the salary class
emp = Employee("max", 25, salary) # now we pass the salary class to the constructor of Employee class
print(emp.total__salary())
#We can pass salary obj to the emp class, but not the opposite

#We have created two independent objects - salary(obj) and emp(obj)