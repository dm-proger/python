class Test:
    _x = 1
    __x = 2

x = Test()

x._x

print(x._x)

    x.__x
    x._Test__x