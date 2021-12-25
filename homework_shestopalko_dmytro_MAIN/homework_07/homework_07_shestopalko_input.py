import random

print("Let`s play rock, paper, scissors")
player = input("Choose rock, paper or scissors by typing r, p, s: ")

if player == 'r' or player == 'p' or player == 's':
    computer = random.randint(1, 3)
    # 1 == 'r'
    # 2 == 'p'
    # 3 == 's'
    if (computer == 1 and player == 'r' or computer == 2 and player == 'p' or computer == 3 and player == 's'):
        print("It is a draw")
    elif (computer == 1 and player == 'p' or computer == 2 and player == 's' or computer == 3 and player == 'r'):
        print("Good job! You win!")
    else:
        print("You lost")
else:
    print("Your input was in the wrong format, no game for you")
