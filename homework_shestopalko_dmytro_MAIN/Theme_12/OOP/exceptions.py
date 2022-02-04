# An exception is an event, which occurs during the execution of a program
# that disrupts the normal flow of the program.


# When an exception occurs, the program stops executing.
# To handle exceptions, and to call code when an exception occurs, you can use a try/except statement.
# The try block contains code that might throw an exception.
# If that exception occurs, the code in the try block stops being executed, and the code in the except block is run.
# If no error occurs, the code in the except block doesn't run.

# try:
#     num1 = 7
#     num2 = 0
#     print(num1 / num2)
#     print("Done calculation")
# except ZeroDivisionError:
#     print("An error occurred")
#     print("due to zero division")


# A try statement can have multiple different except blocks to handle different exceptions.
# Multiple exceptions can also be put into a single except block using parentheses,
# to have the except block handle all of them.

# try:
#     variable = 10
#     print(variable + "hello")
#     print(variable / 2)
# except ZeroDivisionError:
#     print("Divided by zero")
# except(ValueError, TypeError):
#     print("Error occurred")


# An except statement without any exception specified will catch all errors.
# These should be used sparingly, as they can catch unexpected errors and hide programming mistakes.
#
# For example:

# try:
#     word = "spam"
#     print(word / 0)
# except:
#     print("An error occurred")




# After a try/except statement, a finally block can follow.
# It will execute after the try/except block, no matter if an exception occurred or not.

try:
    print("Hello")
    print( 1 / 0)
except ZeroDivisionError:
    print("Devided by zero")
finally:
    print("This code will run no matter what")

# The finally block is useful, for example, when working with files and resources:
# it can be used to make sure files or resources are closed or released regardless of whether an exception occurs.


# The else statement can also be used with try/except statements.
# In this case, the code within it is only executed if no error occurs in the try statement.

# try:
#     print(1)
# except ZeroDivisionError:
#     print(2)
# else:
#     print(3)
#
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print(4)
# else:
#     print(5)


# Raising Exceptions
#
#
# You can throw (or raise) exceptions when some condition occurs.
# For example, when you take user input that needs to be in a specific format,
# you can throw an exception when it does not meet the requirements.
# This is done using the raise statement.

# num = 102
# if num > 100:
#     raise ValueError

try:
    name = input()
    if len(name) > 4:
        print("Account created")
    elif len(name) < 4:
        raise TypeError