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



# n! = n*(n-1)*(n-2)*(n-3)*...(1)
#5! = 5*4*3*2*1 = 120
def factorial(n):
    if n ==1:
        return 1
    print(n)
    return n * factorial(n-1)

print(factorial(int(input("what fib do you want?: "))))

# def recursor():
#     recursor()
# recursor()
