# def test():
#     x = 1
#     print(x) # local namespace
# print("x") # built-in namespace
# test() # global namespace
#
# def test():
#     x = 1
#     print(x)
#
# def test2():
#     x = 2
#     print(x)
#
# test2()
# test()

# spam = 1
# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment: ", spam)
#     do_nonlocal()
#     print("After nonlocal assignment: ", spam)
#     do_global()
#     print("After global assignment: ", spam)
#
# # print(spam)
# scope_test()
# print("In global scope: ", spam)

class Test:
    x = 1
    def __init__(self, temp):
        self.temp = temp