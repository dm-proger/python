#
# # The function apply_twice takes another function as its argument, and calls it twice inside its body.
#
# def apply_twice(func, arg):
#     return func(func(arg))
#
# def add_five(x):
#     return x + 5
#
# print(apply_twice(add_five, 100))
#
# # why the result is 20, not 15?
#
# def test(func, arg):
#   return func(func(arg))
#
# def mult(x):
#   return x * x
#
# print(test(mult, 2))

# Functional programing seeks to use pure functions.
# PF have no side effects, and return a value that depends only
# on there arguments. This is how f-ns in math work: f. e.,
# the cos(x) will, for the same value of x, always return
# the same result.
# Below ae examples of pure and impure f-ns:

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# impure:
some_list = []
def impure(arg):
    some_list.append(arg)

# The f-n above is not pure, because it changed the state of
# some_list