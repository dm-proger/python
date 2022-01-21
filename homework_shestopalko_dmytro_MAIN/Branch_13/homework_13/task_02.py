# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
#
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:
    pass

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

list_01 = [10, 20, 30, 40]
list_02 = [-12, -15, 60, 40, -98, -90, 67]
list_03 = [2000, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986]

#I need to apply methods of Mathematician() to objects list_01, list_02 and list_03




# super_list = [list_01, list_02, list_03]
# check_operation = Mathematician(super_list)




# class CheckOperation():
#     def __init__(self, list_01, list_02, list_03):
#         super().__init__()
#         self.list_01 = list_01
#         self.list_02 = list_02
#         self.list_03 = list_03





