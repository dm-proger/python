# class C:
#     def __init__(self):
#         self._x = "HELLO"
#
#     def getx(self): # we get X with the help of this method
#         return self._x
#
#     def setx(self, value): # setter assigns value to the variable
#         self._x = value
#
#     def delx(self): # deleter discards the attribute
#         del self._x
#
#     our_property = property(getx, setx, delx, "I`m the 'x' property")
#
# c = C()
#
# print(c.our_property)
#
# class Test:
#     def __init__(self, var):
#         self._var = var
#
#     def get_var(self):
#         return self._var
#
# t = Test(1)
# print(t.get_var())

# class Test:
#     def __init__(self, var):
#         self._var = var
#
#     @property
#     def get_var(self):
#         #return value of _var
#         return self._var
#
# t = Test(1)
# print(t.get_var)

class Test:
    def __init__(self, var):
        self._var = var

    @property
    def get_var(self):
        #return value of _var
        return self._var

    @get_var.setter
    def set_var(self, value):
        self._var = value

    @get_var.deleter
    def del_var(self):
        del self._var

t = Test(1)