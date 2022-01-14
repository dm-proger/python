def add_logging(f):
    def inner(*args, **kwargs):
        print("before")
        result = f(*args, **kwargs)
        print("after")
        return result

    return inner

@add_logging
def takes_int_str(x:int, y: str) -> int:
    print(y.upper())
    return x + 7


# def takes_int_str(x:int, y: str) -> int:
#     print(y.upper())
#     return x + 7


# takes_int_str = add_logging(takes_int_str)

def main():
    print("Hello world")
    takes_int_str(1, A)

    takes_int_str("B", 2)

if __name__ == "__main__":
    main()