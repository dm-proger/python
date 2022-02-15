
import json
from typing import Optional


def search(phonebook_list: list):
    search_input = input("Enter the key word: ")
    search_result = []
    for contact in phonebook_list:
        for value in contact.values():
            if search_input == value:
                search_result.append(contact)
                break
    if search_result == []:
        print("This user doesn`t exist")
    else:
        for contact in search_result:
            print(contact["tel_number"])
    phonebook(phonebook_list)


def new_user(phonebook_list: list):
    first_name = input("Enter your first name: ")
    second_name = input("Enter second name: ")
    phone_number = int(input("Enter the phone number: "))
    city = input("Enter the city: ")

    new_user = {}
    new_user["first_name"] = first_name
    new_user["second_name"] = second_name
    new_user["tel_number"] = phone_number
    new_user["city"] = city

    phonebook_list.append(new_user)
    function_write(phonebook_list)
    phonebook(phonebook_list)

def delete_contact(phonebook_list:list):
    with open("phonebook_list.json", "r") as phonebook_file:
        phonebook_list = json.load(phonebook_file)
        print(*phonebook_list, sep='\n')
    select_user = input("Please, select the first_name of the user, you would like to delete: ")
    for contact in phonebook_list:
        for value in contact.values():
            if select_user == value:
                phonebook_list.remove(contact)
                print("The user is deleted")
                function_write(phonebook_list)
                break
    phonebook(phonebook_list)

def function_write(phonebook_list: list):
    with open("phonebook_list.json", "w") as phonebook_file:
        json.dump(phonebook_list, phonebook_file, indent=4)


def phonebook(phonebook_list: Optional[list] = None):

    open_app = int(input(("Find a number = 1\nAdd a new number = 2\nDelete a contact = 3\nEnter 9 to exit application\nPlease, make your choice: ")))

    if open_app == 1:
        search(phonebook_list)
    elif open_app == 2:
        new_user(phonebook_list)
    elif open_app == 3:
        delete_contact(phonebook_list)
    elif open_app == 9:
        function_write(phonebook_list)
        print("Exit")
    else:
        print("Please, try again: ")

def main():
    with open("phonebook_list.json", "r") as phonebook_file:
        phonebook_list = json.load(phonebook_file)
    phonebook(phonebook_list)


if __name__ == "__main__":
    main()
