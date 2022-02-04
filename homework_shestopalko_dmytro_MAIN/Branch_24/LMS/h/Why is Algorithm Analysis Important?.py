# To understand why algorithm analysis is important, we will take help of a simple example.
#
# Suppose a manager gives a task to two of his employees to design an algorithm in Python that
# calculates the factorial of a number entered by the user.
#
# The algorithm developed by the first employee looks like this:

def fact(n):
    product = 1
    for i in range(n):
        product = product * (i +1)
    return product

print(fact(5))


# Notice that the algorithm simply takes an integer as an argument.
# Inside the fact function a variable named product is initialized to 1.
# A loop executes from 1 to N and during each iteration,
# the value in the product is multiplied by the number being iterated by the loop
# and the result is stored in the product variable again. After the loop executes,
# the product variable will contain the factorial.
#
# Similarly, the second employee also developed an algorithm that calculates factorial of a number.
# The second employee used a recursive function to calculate the factorial of a program as shown below:

def fact2(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact2(5))

# The manager has to decide which algorithm to use. To do so, he has to find the complexity of the algorithm.
# One way to do so is by finding the time required to execute the algorithms.

# However, execution time is not a good metric to measure the complexity of an algorithm since it depends upon the hardware.
# A more objective complexity analysis metrics for the algorithms is needed.
# This is where Big O notation comes to play.

# Big-O notation is a metrics used to find algorithm complexity.
# Basically, Big-O notation signifies the relationship between the input to the algorithm and the steps required to execute the algorithm.
# It is denoted by a big "O" followed by opening and closing parenthesis.
# Inside the parenthesis, the relationship between the input and the steps taken by the algorithm is presented using "n".

# Constant Complexity (O(C))
# The complexity of an algorithm is said to be constant if the steps required to complete the execution of an algorithm remain constant,
# irrespective of the number of inputs. The constant complexity is denoted by O(c) where c can be any constant number.
#
# Let's write a simple algorithm in Python that finds the square of the first item in the list and then prints it on the screen.

def constant_algo(items):
    result = items[0] * items[0]
    print(result)

constant_algo([4, 5, 6, 8])