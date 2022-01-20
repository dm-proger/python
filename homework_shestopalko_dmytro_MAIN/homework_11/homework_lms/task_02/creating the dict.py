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
from typing import Optional


def phonebook(phonebook_list: Optional[list] = None, filter_object=None):

    person_dict = {}
    person_dict["first_name"] = "Dmytro"
    person_dict["second_name"] = "Shestopalko"
    person_dict["tel_number"] = +380673291790
    person_dict["city"] = "IF"

    person_dict_02 = {}
    person_dict_02["first_name"] = "Maria"
    person_dict_02["second_name"] = "Kovaliuk"
    person_dict_02["tel_number"] = +380675643215
    person_dict_02["city"] = "IF2"

    person_dict_new_user = {}

    open_app = int(input(("Find a number = 1\nAdd a new number = 2\nEnter 9 to exit application\nPlease, make your choice: ")))

    if open_app == 1:
        def search(*args) -> int:
            search_input = input("Enter the key word: ")
            for key, value in person_dict.items():
                if search_input == value:
                    print(person_dict["tel_number"])
                    break
            for key, value in person_dict_02.items():
                if search_input == value:
                    print(person_dict_02["tel_number"])
                    break
            for key, value in person_dict_new_user.items():
                if search_input == value:
                    print(person_dict_new_user["tel_number"])
                    break
            for key, value in person_dict.items():
                if search_input != value:
                    print("Contact doesn`t exist")
                    break
        search()
    elif open_app == 2:
        def new_user(*args):
            first_name = input("Enter your first name: ")
            second_name = input("Enter second name: ")
            phone_number = int(input("Enter the phone number: "))
            city = input("Enter the city: ")

            person_dict_new_user["first_name"] = first_name
            person_dict_new_user["second_name"] = second_name
            person_dict_new_user["tel_number"] = phone_number
            person_dict_new_user["city"] = city

            phonebook_list = [person_dict, person_dict_02, person_dict_new_user]
            # phonebook_list = phonebook_list or []

            with open("phonebook_list.json", "w") as phonebook_file:
                json.dump(phonebook_list, phonebook_file)

        new_user()

    elif open_app == 9:
        print("Exit")
    else:
        print("Please, try again: ")
    return open_app

if __name__ == "__main__":
    phonebook()
