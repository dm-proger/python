#Fibo

def fib_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fib_recursive(n):
    if n == 0 or n ==1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

print(fib_recursive(int(input("what fib do you want?: "))))

print(fib_iterative(int(input("what fib do you want?: "))))