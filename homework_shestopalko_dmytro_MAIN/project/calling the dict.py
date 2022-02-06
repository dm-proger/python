import json

with open("employee_info.json") as file_object:
    cj = json.load(file_object)

for k, v in cj.items():
    print(k, ":", v)