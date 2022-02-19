import json

from project.main_file import list_employee

with open("employee_info.json") as file_object:
    cj = json.load(file_object)


print(list_employee, sep = '\n')



