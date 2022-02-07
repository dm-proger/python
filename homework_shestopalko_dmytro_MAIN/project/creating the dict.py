import json

dict_employee = {} # holds names as keys; dict_employee_value as value
dict_employee_value = {} # holds position as a value and rate as a key


def add_employee():
    input_full_name = input("Enter the full name: ")
    input_position_key = input("Enter the position of the employee: ")
    input_rate_value = int(input("Enter the rate: "))

    dict_employee.update({input_full_name: dict_employee_value})
    dict_employee_value.update({input_position_key: input_rate_value})


    print(dict_employee)

def function_write(dict_employee: dict):
    with open("employee_info.json", "w") as file_object:
        json.dump(dict_employee, file_object, indent=4)



def main():
    add_employee()
    function_write(dict_employee)

if __name__ == "__main__":
    main()