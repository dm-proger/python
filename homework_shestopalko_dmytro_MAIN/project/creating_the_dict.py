import json


list_employee = [] # list of employees with all the data
dict_employee_value = {} # holds position as a value and rate as a key


def add_employee():
    input_full_name = input("Enter the full name: ")
    input_position_key = input("Enter the position of the employee: ")
    input_rate_value = int(input("Enter the rate: "))

    list_employee[input_full_name] = dict_employee_value
    dict_employee_value[input_position_key] = input_rate_value


    function_write(list_employee)

def function_write(list_employee: dict):
    with open("employee_info.json", "w") as file_object:
        json.dump(list_employee, file_object, indent=4)



def main():


    with open("employee_info.json", "r") as file_object:
        list_employee = json.load(file_object)


    add_employee()


if __name__ == "__main__":
    main()