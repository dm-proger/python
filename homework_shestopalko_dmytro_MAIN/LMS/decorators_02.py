# def first_decorator(func):
#     def wrap():
#         print("before")
#         func()
#         print("after")
#     return wrap
#
# def test():
#     # test function docs
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
    # test func doc
    print("inside test")