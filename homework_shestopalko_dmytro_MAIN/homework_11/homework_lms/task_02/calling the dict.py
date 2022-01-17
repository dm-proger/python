import json

# Now we will extract the phonebook to console

with open("phonebook_list.json", "r") as phonebook_file:
    phonebook_list = json.load(phonebook_file)

# for k, v in phonebook_list.items():
#     print(k, ":", v)
print(*phonebook_list, sep = '\n')