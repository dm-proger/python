import timeit

def bla1():
    a1 = "123"
    def bla2():
        b1 = "321"
        g = globals()
        l = locals()

        print(f"{a1=} - {b1=}")
        print()
    return bla2


if __name__ == "__main__":
    c = bla1()
    d = c()
    print(f"{c=}")
    print(f"{d=}")

    code = """
def question5(n: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res
    
question5(n=1000)
"""
    g = globals()
    l = locals()
    print(timeit.timeit(code, globals=globals(), number=10000))