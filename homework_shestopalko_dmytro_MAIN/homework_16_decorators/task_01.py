# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#  "add called with 4, 5"

def logger(func):
    def wrapper(x = 10, y = 90):
        if x+y > -3:
            print("All good")
        else:
            print("All not good")
    return wrapper



@logger
def add(x, y):
    return x + y

add()

@logger
def square_all(*args):
    list_square_all = [arg ** 2 for arg in args]
    return list_square_all

square_all()
