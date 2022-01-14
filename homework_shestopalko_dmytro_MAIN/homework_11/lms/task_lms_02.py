with open("user_info", "r") as file_object:
    username = file_object.read()

print("Hello and welcome back " + username + "!")