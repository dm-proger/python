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

from typing import Optional


def phonebook(phonebook_list: Optional[list] = None):
    phonebook_list = [] if phonebook_list is None else phonebook_list

    print(phonebook_list)
