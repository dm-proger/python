# Mathematician
# Implement a class Mathematician which is a helper class for doing math operations on lists
# The class doesn't take any attributes and only has methods:
#
# square_nums (takes a list of integers and returns the list of squares)
# remove_positives (takes a list of integers and returns it without positive numbers
# filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'

class Mathematician:


    def square_nums(self, nums:list):
        return [i*i for i in nums]

    def remove_positives(self, positives:list):
        return[i for i in positives if i < 0]

    def filter_leaps(self, leaps:list):
        return [i for i in leaps if i % 4 == 0]

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

def main():
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
    print(m.square_nums([12, 13, 14, 15]))
    print(m.remove_positives([-12, 44, 33, -90]))

if __name__ == "__main__":
    main()







