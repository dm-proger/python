# Extend Phonebook application
# Functionality of Phonebook application:

# Add new entries
# Search by first name
# Search by last name
# Search by full name
# Search by telephone number
# Search by city or state
# Delete a record for a given telephone number
# Update a record for a given telephone number
# An option to exit the program

# The first argument to the application should be the name of the phonebook.
# Application should load JSON data, if it is present in the folder with application,
# else raise an error. After the user exits, all data should be saved to loaded JSON.

import json


# Choose the option:
# 1) Find a number
# 2) Add a new number

def phonebook(*args):
    person_dict = {}
    person_dict["first_name"] = "Dmytro"
    person_dict["second_name"] = "Shestopalko"
    person_dict["tel_number"] = int("+380673291790")
    person_dict["city"] = "IF"

    person_dict_02 = {}
    person_dict_02["first_name"] = "Dmytro2"
    person_dict_02["second_name"] = "Shestopalko2"
    person_dict_02["tel_number"] = int("+38067329179022")
    person_dict_02["city"] = "IF2"

    phonebook_list = [person_dict, person_dict_02]

    with open("phonebook_list.json", "w") as phonebook_file:
        json.dump(phonebook_list, phonebook_file)

    open_app = int(input(("Find a number = 1\nAdd a new number = 2\nEnter 9 to exit application\nPlease, make your choice: ")))

    if open_app == 1:
        print("This is a search function")
    elif open_app == 2:
        print("You will add a new number now")
    elif open_app == 9:
        print("Exit")
    else:
        print("Please, try again: ")
    return open_app


if __name__ == "__main__":
    phonebook()
