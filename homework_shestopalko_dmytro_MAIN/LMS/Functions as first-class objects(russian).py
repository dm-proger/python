# def test(word):
#     return f"Test {word}"
#
# x = test
# print(x)
#
# x.__name__
#
# x("this")
#
# del x

# Functions inside other data structures

# word = "Test"
# command = "up"
# if command == "up":
#     print(word.upper())
# elif command == "down":
#     print(word.lower())
# else:
#     print("Unknown command")

# The same logic is here, but with the help of the functions

# word = "Test"
# command = "down"
# def up(word):
#     print(word.upper())
#
# def down(word):
#     print(word.lower())
#
# def default():
#     print("Unknown command")
#
# command_dict = {
#     "up": up,
#     "down": down
# }
#
# if command in command_dict:
#     command_dict[command](word)
# else:
#     default()
#
# func = command_dict.get(command, default)
# func("HELLLO")


# Functions could be returned from another function

# word = "Test"
# command = "down"
#
# def up(word):
#     print(word.upper())
#
# def down(word):
#     print(word.lower())
#
# def default(*args, **kwargs):
#     print("Unknown command")
#
# def process(command):
#     command_dict = {
#         "up": up,
#         "down": down
#     }
#
#     if command in command_dict:
#         return command_dict[command]
#     else:
#         return default
#
# process("up")("Test1")
#
# func = process(command)
# func(word)

# Nested functions
# def test(word):
#     def low(it):
#         if it.isdigit():
#             return "N"
#         return it.lower()
#     res = " "
#     for i in word:
#         res += low(i)
#     return res
#
# test("Hello1")

# Function could be passed to another function

# def logger_func(func):
#     print("before execution")
#     func()
#     print("after execution")
#
# def test():
#     print("inside test func")
#
#     loger_func(test)

# Objects can behave like functions

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

    x = Adder(10)
x