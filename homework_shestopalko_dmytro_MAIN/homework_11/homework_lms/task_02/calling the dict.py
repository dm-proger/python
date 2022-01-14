import json

# Now we will extract the phonebook to console

with open("phonebook_dict.json", "r") as phonebook_file:
    phonebook_dict = json.load(phonebook_file)

for k, v in phonebook_dict.items():
    print(k, ":", v)