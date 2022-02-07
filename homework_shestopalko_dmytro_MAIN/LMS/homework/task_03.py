# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list
# and return the result of it. Otherwise, return the result of the second one


def choose_func(nums: list, square_nums, remove_negatives):
    result = all(num >= 0 for num in nums)
    if result:
        return square_nums(nums)
    else:
        return remove_negatives(nums)


def square_nums(nums):
    print([num ** 2 for num in nums])


def remove_negatives(nums):
    print([num for num in nums if num > 0])


def main():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

if __name__ == "__main__":
    main()
