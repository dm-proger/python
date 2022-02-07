# # Map
x = [1, 2, 3, 4]
# res = []
# for it in x:
#     res.append(it**2)
# print(res)
# #
# # # The same result we could reach using list comprehension
# # res = [it**2 for it in x]
# # print(res)
# #
# # # let`s encapsulate this logic into a function:
# def sqr(item):
#     return item**2
#
# res = [sqr(it) for it in x]
# print(res)
# #
# # # MAP
# # map(sqr, x)
# # print(list(map(sqr, x)))
# #
# def my_pow(item, power):
#     return item**power
#
# powers = [2, 3, 4, 5]

# print(list(map(my_pow, x, powers)))

# print(list(map(my_pow, x, powers[:3])))
# #
# from timeit import timeit
# # # help(timeit)
# #
# # timeit("[my_pow(x[i], powers[i]) for i in range(len(powers))]",
# #        number = 1000,
# #        globals = {"x": x, "powers": powers, "my_pow":my_pow})
# #
# # timeit("list(map(my_pow, x, powers))",
# #        number = 1000,
# #        globals = {"x": x, "powers": powers, "my_pow": my_pow})
# #
# #
#
#
# # Filter
# # x = [1, 2, 0, 34, 5, 6, 7, 8, 2, 2, 1, 4, 6, 7]
# # res = []
# # for it in x:
# #     if it > 2:
# #         res.append(it)
# # print(res)
# #
# # res = [it for it in res if it > 2]
# # print(res)
# #
# # filter(lambda it: it > 2, x)
# # list(filter(lambda it:it > 2, x))
# # print(x)
# #
# # list(filter(None, x))
# #
# # timeit("list(filter(lambda it: it > 2, x))",
# #        number = 1000,
# #        globals = {"x": x}
# #        )
# # timeit("[it for it in x if it > 2]",
# #        number = 1000,
# #        globals = {"x":x}
# #         )
#
# # ZIP
#
# x = [1, 2, 3, 4]
# y = ["a", "b", "c", "d"]
# [(x[i], y[i]) for i in range(len(x))]
#
# print(list(zip(x, y)))
#
# from itertools import zip_longest
# print(list(zip_longest([1, 2, 3], [4, 5, 6, 7, 8, 9])))
#
# # Reduce
# from functools import reduce
#
# reduce(lambda x, y: x + y, x)
# reduce(lambda x, y: x + y, x, 2)
# reduce(lambda x, y: x + y, [], 2)

# def my_sum(a_list):
#     if not a_list:
#         return 0
#     res = 0
#     for it in a_list: #incrementation
#         res += it #iteration
#     return res



# def test_reduce(x):
#     res = 0
#     f = lambda x, y: x + y
#     for it in x:
#         res = f(res, it)
#     return res
# print(test_reduce(x))
#
# # Partial
# def my_pow(item, power):
#     return item ** power
#
# from functools import  partial
#
# sqrt = partial(my_pow, power = 0.5)
# cubic = partial(my_pow, power = 3)
#
# print(sqrt(12))
# print(cubic(3))
# print(my_pow(3, 3))

