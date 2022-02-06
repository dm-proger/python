import json

dict_employee = {} # the whole dictionary. Holds all the info
dict_employee_key_name = {} # holds names as keys and credentials as position and rate
dict_employee_value = {} # holds position and rate


def add_employee():
    manager_input_full_name = input("Enter the full name: ")
    manager_input_position_key = input("Enter the position of the employee: ")
    manager_input_rate_value = int(input("Enter the rate: "))
    dict_employee_value.update({manager_input_position_key: manager_input_rate_value})
    dict_employee_key_name.update({manager_input_full_name: dict_employee_value})

    print(dict_employee_key_name)

def function_write(dict_employee: dict):
    with open("employee_info.json", "w") as file_object:
        json.dump(dict_employee, file_object,  indent=4)



def main():
    add_employee()
    function_write(dict_employee)

if __name__ == "__main__":
    main()