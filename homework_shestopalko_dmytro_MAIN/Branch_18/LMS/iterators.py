# class MySquareIterator:
#
#     def __init__(self, _from, _to, step=1):
#         self.ind = _from
#         self.to = _to
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.ind > self.to:
#             raise StopIteration
#         val = self.ind ** 2
#         self.ind += self.step
#         return val
#
# c = MySquareIterator(1, 10, 2)
#
# for i in c:
#     print(i)
#
# next(c)






# def my_squares_generator(_from, _to, step = 1):
#     for i in range(_from, _to+1, step):
#         yield i ** 2
#
# c = my_squares_generator(1, 10, 2)
# for i in c:
#     print(i)



# # Generator expressions
# squares = (it ** 2 for it in range(10))
# squares_1 = [it ** 2 for it in range(10)]
#
# print(squares)
# print(squares_1)
#
# for i in squares:
#     print(i)



# generator-iterator methods

def echo(value = None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don`t forget to clean up when 'close()' is called.")

gen = echo(1)
print(next(gen))
print(next(gen))
print(gen.send(2))

gen.close()