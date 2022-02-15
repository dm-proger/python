import json


list_employee = [] # list of employees with all the data
dict_employee = {} # holds position as a key and rate as value
dict_data = {} # holds name as a key and dict_employee as value


def main_menu():
#     describe the main menu. Select the option


def add_employee():
    input_full_name = input("Enter the full name: ")
    input_position_key = input("Enter the position of the employee: ")
    input_rate_value = int(input("Enter the rate: "))

    dict_data.update({input_position_key: input_rate_value})
    dict_employee.update({input_full_name: dict_data})
    list_employee.append(dict_employee)

    function_write(list_employee)


def function_write(list_employee: list):
    with open("employee_info.json", "w") as file_object:
        json.dump(list_employee, file_object, indent=4)



def main():


    with open("employee_info.json", "r") as file_object:
        list_employee = json.load(file_object)


    add_employee()


if __name__ == "__main__":
    main()