# def input_function():
#     lst = []
#     n = int(input("Enter number of elements : "))
#     for i in range(0, n):
#         ele = int(input())
#
#         lst.append(ele)
#
#     print(lst)
#
#
# input_function()

# from typing import Optional
#
#
# def phonebook(phonebook_list: Optional[list] = None):
#     phonebook_list = [] if phonebook_list is None else phonebook_list
#
#     print(phonebook_list)

# def my_sum(a: int, b: int) -> int:
#     return a + b
#
#
# def main():
#     x = 2
#     y = 3
#     result = my_sum(a=x, b=y)
#     print(f'{result=}')
#
#
# if __name__ == '__main__':
#     main()

def my_sum(a: int, b: int) -> int:
    return a + b


def main():
    x = 2
    y = 3
    result = my_sum(a=x, b=y)
    print(f'{result=}')

    result_2 = my_sum(x, y)
    print(f'{result_2=}')


if __name__ == '__main__':
    main()
