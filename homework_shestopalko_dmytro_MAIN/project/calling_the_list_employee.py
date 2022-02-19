import json

with open("employee_info.json") as file_object:
    cj = json.load(file_object)

for k, v in cj.items():
    print(k, ":", v)


with open("phonebook_list.json", "r") as phonebook_file:
    phonebook_list = json.load(phonebook_file)

# for k, v in phonebook_list.items():
#     print(k, ":", v)
print(*employee_info, sep = '\n')



