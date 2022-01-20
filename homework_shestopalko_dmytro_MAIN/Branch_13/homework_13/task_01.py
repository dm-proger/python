# School
#
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person():
    def __init__(self, first_name: str, second_name: str, age: int):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age


# person_01 = Person("Dmytro", "Shestopalko", 29)
# print(f"My name is {person_01.first_name}, my second name is {person_01.second_name}. I am {person_01.age} years old.")

class Teacher(Person):
    def __init__(self, first_name: str, second_name: str, salary: str, subject: str, work_hrs: int, age: int):
        super().__init__(first_name, second_name, age)
        self.salary = salary
        self.subject = subject
        self.work_hrs = work_hrs

teacher_01 = Teacher("Maria", "Kovaliuk", 18000, "medicine", 8, 23,)
print(f"My name is {teacher_01.first_name} {teacher_01.second_name}. I am {teacher_01.age}. "
      f"I work for salary {teacher_01.salary} grn {teacher_01.work_hrs} per week")


class Student(Person):
    def __init__(self, first_name: str, second_name:str, age: int, form: str, favorite_subject: str, hobby: str):
        super().__init__(first_name, second_name, age)
        self.form = form
        self.favorite_subject = favorite_subject
        self.hobby = hobby


student_01 = Student("Volodymyr", "Vynar", 14, "7A", "math", "swimming")
print(f"My name is {student_01.first_name}, my second name is {student_01.second_name}. I am {student_01.age} years old"
      f". I am a pupil of {student_01.form}. My favorite subject is {student_01.favorite_subject}."
      f"My hobby is {student_01.hobby} ")
