# def is_palindrome(looking_str: str) -> bool:
#     return looking_str == looking_str[::-1]
#     print(id(reversed_str)) == id(looking_str)
#
# # find palindrome fast
#
#
# if __name__ == "__main__":
#     print(is_palindrome("radar"))


# def check_if_palindrome(input_string: str) -> bool:
#     input_string = input_string.lower()
#     return input_string == input_string[::-1]
#
#
# def main():
#     input_string = "olololo"
#
#     print(check_if_palindrome(input_string))
#
#
# if __name__ == "__main__":
#     main()

def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if index == len(looking_str) // 2:
        return True
    if looking_str[index] != looking_str[index * -1 - 1]:
        return False
    return is_palindrome(looking_str, index + 1)

def main():
    print(is_palindrome("radar"))