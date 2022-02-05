# Write a program that reads in a sequence of characters, and determines whether
# it's parentheses, braces, and curly brackets are "balanced."


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check_program(input_str):
    stack = []
    for i in input_str:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


# Driver code
string = "{[]{()}}"
print(string, "-", check_program(string))

string = "[{}{})(]"
print(string, "-", check_program(string))

string = "((()"
print(string, "-", check_program(string))
