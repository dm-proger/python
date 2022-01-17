person_dict_01 = {}
person_dict_01["first_name"] = "Dmytro"
person_dict_01["second_name"] = "Shestopalko"
person_dict_01["tel_number"] = int("+380673291790")
person_dict_01["city"] = "IF"

person_dict_02 = {}
person_dict_02["first_name"] = "Dmytro2"
person_dict_02["second_name"] = "Shestopalko2"
person_dict_02["tel_number"] = int("+38067329179022")
person_dict_02["city"] = "IF2"

phonebook_dict = zip(person_dict_01, person_dict_02)
print(phonebook_dict)















# class Car:
#     def __init__(self, driver_name: str, cab: str, engine: str, chassis: str):
#         self.driver = driver_name
#         self.cab = cab
#         self.engine = engine
#         self.chassis = chassis
#
#     def drive_forward(self) -> str:
#         return "forward"
#
#     def drive_back(self) -> str:
#         return "back"
#
#     def turn_left(self) -> str:
#         return "left"
#
#     def turn_right(self) -> str:
#         return "right"
#
#     def stop(self) -> str:
#         return "stop"

# class Animal:
#     CLASS_VARIABLE: CLassVar[int] = 2
#     _members: list = []


    # def __init__(self, name: str, age: int = 8):
    #     self.name = name
    #     self._age = age
    #     self.__color = "black"
    #
    # def talk(self) -> str:
    #     return "Wow"
    #
    # def __str__(self):
    #     # return self.name
    #     return f"{self.__class__.__name__} {self.name}"
    # __repr__ = __str__