import json


list_employee = [] # list of employees with all the data
employee_cell = [] # list of dicts with employee data
employee_data = {} # holds key and value of employees


def main_menu():
    main_enter = int(input("If you are a user, please, enter 1. If you are a manager, please, enter 0. "
                           "Exit - enter 9: "))
    if main_enter == 1:
        print("Here is the main interface for you")
        main_interface()
    elif main_enter == 0:
        manager_function()
    elif main_enter == 9:
        exit()
    else:
        print("Please, try again")
        main_menu()


def add_employee():
    input_full_name = input("Enter the full name: ")
    input_position = input("Enter the position of the employee: ")
    input_rate = int(input("Enter the rate: "))


    employee_data["name"] = input_full_name
    employee_data["position"] = input_position
    employee_data["rate"] = input_rate

    employee_cell.append(employee_data)
    list_employee.append(employee_cell)


    function_write(list_employee)
    print("The employee is successfully added")
    manager_function()


def remove_employee():
    ...

def change_rate():
    ...

def change_position():
    ...

def main_interface():
    ...

def manager_function():
    manager_input = int(input("Add employee - 1, remove employee - 2, change rate - 3, "
                              "change position - 4, exit - 9 "
                              "Please, select from above: "))
    if manager_input == 1:
        add_employee()
    elif manager_input == 2:
        remove_employee()
    elif manager_input == 3:
        change_rate()
    elif manager_input == 4:
        change_position()
    elif manager_input == 9:
        exit()
    else:
        print("Please, try again")
        main_menu()



def function_write(list_employee: list):
    with open("employee_info.json", "w") as file_object:
        json.dump(list_employee, file_object, indent=4)



def main():

    with open("employee_info.json", "r") as file_object:
        list_employee = json.load(file_object)
    main_menu()

    main_menu()


if __name__ == "__main__":
    main()