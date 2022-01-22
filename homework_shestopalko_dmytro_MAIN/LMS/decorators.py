import time


def time_function(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f.__name__ + "took" + str((end - start) * 1000) + "ms")
        return result
    return wrapper

# @time_function is a syntatic sugar for this:
# decorated_fun = time_function(square_numbers)


@time_function
def square_numbers(num_list):
    new_list = []
    for num in num_list:
        new_list.append(num ** 2)
    return new_list

@time_function
def cube_numbers(num_list):
    new_list = []
    for num in num_list:
        new_list.append(num ** 3)
    return new_list


my_list = [1, 2, 3, 4, 5, 6]
my_list_squared = square_numbers(my_list)
my_list_cubed = cube_numbers(my_list)
print(my_list_squared)
print(my_list_cubed)
