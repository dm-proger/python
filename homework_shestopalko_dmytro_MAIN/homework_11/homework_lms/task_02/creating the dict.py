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
# Let`s create a simple phonebook as a dict
# I need to append dictionary to a dictionary. Dict made of dicts.
phonebook_dict = {}
person_dict = {}
person_dict["first_name"] = "Dmytro"
person_dict["second_name"] = "Shestopalko"
person_dict["tel_number"] = int("+380673291790")
person_dict["city"] = "IF"

with open("phonebook_dict.json", "w") as phonebook_file:
    json.dump(person_dict, phonebook_file)


