# def first_decorator(func):
#     def wrap():
#         print("before")
#         func()
#         print("after")
#     return wrap
#
# def test():
#     """test function docs"""
#     print("inside test")
#
# test.__name__

from functools import wraps

def first_decorator(func):
    @wraps(func)
    def wrap():
        print("before")
        func()
        print("after")
    return wrap

@first_decorator
def test():
    """test function docs"""
    print("inside test")

test()

#Complicated decorator

def add_brake_log(size=2):
    def add_brake_log_dec(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            for _ in range(size):
                print("_" * 80)
            func(*args, **kwargs)
            for _ in range(size):
                print("_" * 80)
        return wrap
    return add_brake_log_dec


@add_brake_log(size = 1)
def test():
    """test function docs"""
    print("inside test")

test()