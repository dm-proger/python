# l = [1, 2, 3]
# iter_l = iter(l)
# print(next(iter_l))
# print(next(iter_l))
# print(next(iter_l))


# Using iterator
# class Reverse():
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#
#     def __iter__(self):
#         return self  # this object will be iterable, that`s why it returns self
#
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         else:
#             self.index -= 1
#             return self.data[self.index]
#
#
# my_str = "python"
# for elem in my_str:
#     print(elem, end="")
# print()
# for elem in Reverse(my_str):
#     print(elem, end="")
# print()


# Using generator

def Reverse(data):
    for i in range(len(data) -1, -1, -1):
        yield data[i]

my_str = "python"
for elem in my_str:
    print(elem, end="")
print()
for elem in Reverse(my_str):
    print(elem, end="")
print()