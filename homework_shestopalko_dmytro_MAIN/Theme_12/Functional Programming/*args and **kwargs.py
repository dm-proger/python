# *args
#
#
# Python allows you to have functions with varying numbers of arguments.
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
# The arguments are then accessible as the tuple args in the body of the function.
#
# Example:

# def function(named_arg, *args):
#     print(named_arg)
#     print(args)
#
# function(1, 2, 3, 4, 5)

# The parameter *args must come after the named parameters to a function.
# The name args is just a convention; you can choose to use another.

# **kwargs
#
#
# **kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
# The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.
#
# Example:

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# a and b are the names of the arguments that we passed to the function call.
# The arguments returned by **kwargs are not included in *args.


# Python program to reverse a string using recursion

# Function to print reverse of the passed string
def reverse(string):
    if len(string) == 0:
        return

    temp = string[0]
    reverse(string[1:])
    print(temp, end='')


# Driver program to test above function
string = "Geeks for Geeks"
reverse(string)

# A single line statement to reverse string in python
# string[::-1]

# This code is contributed by Bhavya Jain
