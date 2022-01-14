import json


def telephone_function(data, filename="phonebook_dict.json"):
    with open(filename, "w") as f:
        json.dump(data, f)


with open("phonebook_dict.json", "r") as json_file:
    data = json.load(json_file)
    # temp = person_dict{}
    # new_entry = {"first_name": "Oleg", "second_name": "Slon", "tel_number": int("+380969669798"), "city": "Rome"}
    temp.append(new_entry)

telephone_function(data, filename="phonebook_dict.json")

if __name__ == "__main__":
    main()
