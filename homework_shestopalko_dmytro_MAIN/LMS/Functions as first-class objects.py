# def add_five(x):
#     return x+5
#
# def do_twice(f):
#     def resulting_func(x):
#         return f(f(x)) #nested function. The inner function has access to the outer function scope
#     return resulting_func
#
# result = do_twice(add_five)
# print(result(5))

import math

def make_cylinder_volume_function(r):
    def volume(h):
        return math.pi * r ** 2 * h
    return volume

volume_of_r10 = make_cylinder_volume_function(10)  # variable is holding a function
print(volume_of_r10(30)/(30*100))
