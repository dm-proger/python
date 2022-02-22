import json


list_employee = ["All info is here"] # list of dicts with employees data
employee_data = {} # holds key and value of employees


def main_menu(list_employee: list):
    main_enter = int(input("If you are a user, please, enter 1.\nIf you are a manager, please, enter 0.\n"
                           "Exit - enter 9.\nSelect the option:  "))
    if main_enter == 1:
        print("Here is the main interface for you")
        main_interface()
    elif main_enter == 0:
        manager_function(list_employee)
    elif main_enter == 9:
        exit()
    else:
        print("Please, try again")
        main_menu()


def manager_function(list_employee: list):
    manager_input = int(input("Add employee - 1,\nRemove employee - 2,\nChange rate - 3,\n"
                              "Change position - 4,\nExit - 9\n"
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
        main_menu(list_employee)


def add_employee():
    input_full_name = input("Enter the full name: ")
    input_position = input("Enter the position of the employee: ")
    input_rate = int(input("Enter the rate: "))


    employee_data["name"] = input_full_name
    employee_data["position"] = input_position
    employee_data["rate"] = input_rate

    list_employee.append(employee_data)
    function_write(list_employee)
    print("The employee is successfully added")
    manager_function(list_employee)



def remove_employee():
    ...

def change_rate():
    ...

def change_position():
    ...

def main_interface():
    ...


def function_write(list_employee: list):
    with open("employee_info.json", "w") as file_object:
        json.dump(list_employee, file_object, indent=4)



def main():

    with open("employee_info.json", "r") as file_object:
        list_employee = json.load(file_object)

    main_menu(list_employee)



if __name__ == "__main__":
    main()