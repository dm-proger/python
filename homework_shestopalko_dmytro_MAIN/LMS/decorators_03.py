# def div(a, b):
#     print(a/b)
#
# def smart_div(func):
#
#     def inner(a, b):
#         if a<b:
#             a,b = b,a
#         return func(a, b)
#     return inner
#
# div = smart_div(div)
#
# div(2,4)

def check(func):
    def inside(a, b):
        if b == 0:
            print("Can`t divide by 0")
            return
        func(a, b)
    return inside

@check
def div(a, b):
    print(a/b)

print(div(10, 20))