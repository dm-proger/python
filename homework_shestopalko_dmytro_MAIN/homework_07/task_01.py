# Task 1
# The Guessing Game.

import random

player = int(input("Choose between 1, 2, 3, 4, 5, 6, 7, 8, 9, 10: "))
computer = random.randint(1, 10)
if computer == player:
    print("Congratulations, you win!")
else:
    print("You lost!")
print(computer)
