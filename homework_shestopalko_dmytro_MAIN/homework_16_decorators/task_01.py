# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!
# For example:
#  "add called with 4, 5"

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        args_as_string = [repr(a) for a in args]
        kwargs_as_string = [f"{k}={v}" for k, v in kwargs.items()]
        print(f"{func_name} called with {(', ').join(args_as_string + kwargs_as_string)}")
        return func(*args, **kwargs)
    return wrapper

# if there are arguments, the output is correct. Modify the f-n for the output without arguments.
@logger
def add(x, y):
    print(x + y)

add(10, 20)

@logger
def square_all(*args):
    list_square_all = [arg ** 2 for arg in args]
    print(list_square_all)

square_all(10, 20)
