# def sum_of_squares(x, y):
#     return_value = x**2 + y**2
#     return return_value
# print(sum_of_squares(2, 3))

# def favorite_car(car, color = "black"):
#     print("My favorite car is " + color + " " + car)
#
#
# favorite_car(car = "Volvo")
# favorite_car("BMW", "black")

# def increment_values(l):
#     for i in range(len(l)):
#         l[i] += 1
#     print("List inside of the function: " + str(l))
#
# original = [1, 2, 3]
# increment_values(original)
# print("List outside of the function: " + str(original))

# length = len("Ukraine")
# print(length)

# def build_pet(species, name, ** pet_info):
#     pet = {}
#     pet['species'] = species
#     pet['name'] = name
#     for key, value in pet_info.items():
#         pet[key] = value
#         return pet
# my_pet = build_pet("Husky", "Doge", color = "white", age = 2)
# print(my_pet)

# """ A tree of size 3
#     *
#    ***
#   *****
# """
#
#
# def print_tree(n):
#     for i in range(n):
#         for j in range(n - i):
#             print(" ", end="")
#         for k in range(2 * i + 1):
#             print("*", end="")
#         print()
# print_tree(30)
