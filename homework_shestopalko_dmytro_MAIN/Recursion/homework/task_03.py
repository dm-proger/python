def multiplication(a, n):
    if a < 0 or n < 0:
        raise ValueError("This function works only with positive integers")
    else:
        if a == 0:
            return 0
        elif a == 1:
            return n
        else:
            return n + multiplication(a - 1, n)


print(multiplication(3, 100))
