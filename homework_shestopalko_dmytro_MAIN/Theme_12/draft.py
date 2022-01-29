# contacts = [
#     ('James', 42),
#     ('Amy', 24),
#     ('John', 31),
#     ('Amanda', 63),
#     ('Bob', 18)
# ]
#
#
# def get_contact(contacts):
#     input_var = input("Please, enter the name: ")
#     if input_var == contacts[0][0]:
#         print(f"{contacts[0][0]} is {contacts[0][1]}")
#     elif input_var == contacts[1][0]:
#         print(f"{contacts[1][0]} is {contacts[1][1]}")
#     elif input_var == contacts[2][0]:
#         print(f"{contacts[2][0]} is {contacts[2][1]}")
#     elif input_var == contacts[3][0]:
#         print(f"{contacts[3][0]} is {contacts[3][1]}")
#     elif input_var == contacts[4][0]:
#         print(f"{contacts[4][0]} is {contacts[4][1]}")
#     else:
#         print("Not found")
#
#
# get_contact(contacts)



def calc():
    side = int(input(" "))
    p = 4 * side
    a = side * side

    print("Perimeter: " + str(p))
    print("Area: " + str(a))

calc()
