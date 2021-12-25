# Task 3
# Words combination

import random
import string

original_str = input("Please, enter a word: ")
str_size = len(original_str)

def random_string(str_size, original_str, ):
    return ''.join(random.choice(original_str) for x in range(str_size))

print(original_str)
print("random str: ", random_string(str_size, original_str))
