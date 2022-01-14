import json


def telephone_function(data, filename="phonebook_dict.json"):
    with open(filename, "w") as f:
        json.dump(data, f)


with open("phonebook_dict.json", "r") as json_file:
    data = json.load(json_file)
    temp = data["first_name"]
    y = {"name": "Joe", "age": 40}
    temp.append(y)

telephone_function(data, filename="phonebook_dict.json")

if __name__ == "__main__":
    main()
