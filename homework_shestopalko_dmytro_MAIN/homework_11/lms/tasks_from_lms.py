#
# with open("weekdays") as week_file:
#     weekdays = week_file.read()
#
# print(weekdays)

# with open("weekdays") as week_file:
#     weekdays = week_file.readlines()
#
# print(weekdays)

# with open("weekdays") as week_file:
#     weekdays = [day.rstrip() for day in week_file.readlines()]
#
# print(weekdays)

username = input("Hey, what`s your name?: ")

with open("user_info", "w") as file_object:
    file_object.write(username)