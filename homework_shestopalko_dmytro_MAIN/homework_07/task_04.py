# Task 4
#
# The math quiz program
import random

operators = ['+', '-', '*', '/']
number_01 = random.randint(0, 20)
number_02 = random.randint(0, 20)
operation = random.choice(operators)

# action = number_01, operation, number_02

action = input(f"Enter the correct answer {number_01} {operation} {number_02}: ")
check_answer = (f"{number_01} {operation} {number_02}")
    if check_answer == action:
        print("Good job!"),
    else:
        print("Try again")

#         I have to finish this task




