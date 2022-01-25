# def outer():
#     x = 3
#     def inner(): # it is a nested function
#         y = 3
#         result = x+y
#         return result
#     return inner # outer f-n returns the inner function
#                 # we are returning the reference of the inner function
#
# a = outer() # the result of execution of the outer f-n will be stored in a variable
# # print(a())
# print(a.__name__) # we are printing the reference to the inner function

# def function1():
#     print("function1")
#
# def function2(func):
#     print("function2 is calling function1")
#     func()
#
# function2(function1)#we are not calling this function. We pass is as an argument. It is only the refference

# def str_upper(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner
#
# def print_str():
#     return "hello"
#
# print(print_str())
#
# d = str_upper(print_str)
# print(d())

# def str_upper(func):
#     def inner():
#         str1 = func()
#         return str1.upper()
#     return inner
#
# @str_upper
# def print_str():
#     return "hello"
#
# print(print_str())

# How to decorate a function if it contains a parametr:

def div_decorator(func):
    def inner(x, y):
        if y == 0:
            return "give proper input"
        return func(x, y)
    return inner

@div_decorator
def div(a, b):
    return a/b

print(div(4,0))
