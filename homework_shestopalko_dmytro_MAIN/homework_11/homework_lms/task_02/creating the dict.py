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

def phonebook(phonebook_list = list, filter_object=None):
    person_dict = {}
    person_dict["first_name"] = "Dmytro"
    person_dict["second_name"] = "Shestopalko"
    person_dict["tel_number"] = int("+380673291790")
    person_dict["city"] = "IF"

    person_dict_02 = {}
    person_dict_02["first_name"] = "Maria"
    person_dict_02["second_name"] = "Kovaliuk"
    person_dict_02["tel_number"] = int("+380675643215")
    person_dict_02["city"] = "IF2"

    person_dict_new_entry = {}

    open_app = int(input(("Find a number = 1\nAdd a new number = 2\nEnter 9 to exit application\nPlease, make your choice: ")))

    if open_app == 1:
        search_input = input("Enter the key word: ")
        filter_object = filter(lambda a: search_input in phonebook_list, phonebook_list)
        print(filter_object)

    elif open_app == 2:

        new_entry_01 = input("Enter your first name: ")
        new_entry_02 = input("Enter second name: ")
        new_entry_03 = int(input("Enter the phone number: "))
        new_entry_04 = input("Enter the city: ")

        person_dict_new_entry["first_name"] = new_entry_01
        person_dict_new_entry["second_name"] = new_entry_02
        person_dict_new_entry["tel_number"] = new_entry_03
        person_dict_new_entry["city"] = new_entry_04

        phonebook_list = [person_dict, person_dict_02, person_dict_new_entry]

        with open("phonebook_list.json", "w") as phonebook_file:
            json.dump(phonebook_list, phonebook_file)

    elif open_app == 9:
        print("Exit")
    else:
        print("Please, try again: ")
    return open_app


if __name__ == "__main__":
    phonebook()
