import time

# The code withot decorator

def calc_square(numbers):
    start = time.time() #code duplication
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()                                              ##code duplication
    print("calc_square took " + str((end-start)*1000) + "mil sec") #code duplication
    return result

def calc_cube(numbers):
    start = time.time() #code duplication
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()#code duplication
    print("calc_cube took " + str((end-start)*1000) + "mil sec")#code duplication
    return result

array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)

# The first problem is that there is duplication code
# Second problem is that there is timing logic in the main logic. Two logics are combined. It makes the code less readable

# The result before the decorating
# calc_square took23.74434471130371mil sec
# calc_cube took32.06610679626465mil sec