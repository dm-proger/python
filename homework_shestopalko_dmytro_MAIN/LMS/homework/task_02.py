# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)


def main(x):
    square = x ** x
    print(f"The cube square is {square}")

    def cube_perimeter(x):
        perimeter = x * 4
        print(f"The cube perimeter is {perimeter}")

    cube_perimeter(x)


def outher_function(a, b):
    def inner_function(a, b):
        return a + b
    return inner_function(a, b)


if __name__ == "__main__":
    main(10)
    print(outher_function(1, 3))
