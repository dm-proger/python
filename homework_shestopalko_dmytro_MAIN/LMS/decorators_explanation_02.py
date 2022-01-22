import time

# Functions are the first class objects in python.
# What it means is that they can be treated just like any other
# variable and you can pass them as argument to another
# function or even return them as a return value

# The first we need to do is to define a function which will take FUNC as an argument
def time_it(func):
# we define wrapper function now. This is inner function
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + "took" + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

