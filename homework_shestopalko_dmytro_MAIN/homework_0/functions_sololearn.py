# You can call the same function with different arguments.
# def exclamation(word):
#     print(word + "!")
#
# exclamation("spam")
# exclamation("eggs")
# exclamation("python")

# Arguments are used to pass information to the function.
# This allows us to reuse the function logic for different values.

# Certain functions, such as int or str, return a value instead of outputting it.
# The returned value can be used later in the code, for example, by getting assigned to a variable.
# To do this for your defined functions, you can use the return statement. Like this:
# def sum(x, y):
#     return(x + y)


# Now we can use our function and assign the result to a variable:
# def sum(x, y):
#     return(x + y)
#
# res = sum(42, 7)
# print(res)

# Returning is useful when you don't need to print the result of the function, but need to use it in your code.
# For example, a bank account's withdraw() function could return the remaining balance of the account.

# Once you return a value from a function, it immediately stops being executed.
# Any code placed after the return statement won’t be executed.
# For example:

# def add_numbers(x, y):
#     total = x + y
#     return total
#     print("This won`t be printed")
#
# print(add_numbers(4, 5))

# A function can only return once, thus, if you need to return multiple values, you can use a list.
# For example:

# def double(a, b):
#     return [a*2, b*2]
#
# x = double(6, 9)
# print(x)

# def sum(x):
#     res = 0
#     for i in range(x):
#         res += i
#     return res
#
# print(sum(4))

# def print_nums(x):
#     for i in range(x):
#         print(i)
#         return
#
#
# print_nums(10)

# input is 10, without return it'd be 0,1,2,3,...9,
# but with return after first run, it only outputs the first position (position 0),
# which happens to also be 0

# def func(x):
#     res = 0
#     for i in range(x):
#         res += i
#
#     return res
#
# print(func(6))

text = input("Enter the text here: ")
text_list = text.split()
print(text_list)
word = input("Please, enter the word you are looking for: ")
word_list = word.split()
print(word_list)
text_list = list(text)


def search(text_list, word_list) -> str:
    if any in word_list == text_list:
    # print("The word is found")
        return True
    else:
    # print("The word is not found")
        return False


if __name__ == "__main__":
    print(search(text_list, word_list))
